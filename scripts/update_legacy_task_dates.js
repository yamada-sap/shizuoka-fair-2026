const https = require('https');

const token = process.env.GITHUB_TOKEN;
if (!token) {
  console.error("❌ エラー: GITHUB_TOKEN が設定されていません。");
  process.exit(1);
}

const OWNER = 'yamada-sap';
const PROJECT_NUMBER = 1;

function graphql(query, variables = {}) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ query, variables });
    const req = https.request({
      hostname: 'api.github.com',
      path: '/graphql',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'User-Agent': 'Antigravity-IDE-Update-Script',
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode !== 200) {
          reject(new Error(`GitHub API returned status ${res.statusCode}: ${data}`));
          return;
        }
        try {
          const json = JSON.parse(data);
          if (json.errors) reject(new Error(JSON.stringify(json.errors, null, 2)));
          else resolve(json.data);
        } catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

const getProjectQuery = `
query($owner: String!, $number: Int!, $after: String) {
  user(login: $owner) {
    projectV2(number: $number) {
      id
      fields(first: 50) {
        nodes {
          ... on ProjectV2FieldCommon { id name }
        }
      }
      items(first: 100, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          fieldValues(first: 10) {
            nodes {
              ... on ProjectV2ItemFieldTextValue {
                text
                field { ... on ProjectV2FieldCommon { name } }
              }
              ... on ProjectV2ItemFieldDateValue {
                date
                field { ... on ProjectV2FieldCommon { name } }
              }
            }
          }
        }
      }
    }
  }
}
`;

const updateFieldMutation = `
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: ProjectV2FieldValue!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $projectId
    itemId: $itemId
    fieldId: $fieldId
    value: $value
  }) {
    projectV2Item { id }
  }
}
`;

function parseDatesFromTitle(title) {
  if (!title) return null;

  // 1. 月/日-日 パターン (例: 【11/28-29】)
  let m = title.match(/【(\d{1,2})\/(\d{1,2})-(\d{1,2})(?:日|期限)?】/);
  if (m) {
    const month = m[1].padStart(2, '0');
    const d1 = m[2].padStart(2, '0');
    const d2 = m[3].padStart(2, '0');
    return { start: `2026-${month}-${d1}`, end: `2026-${month}-${d2}` };
  }

  // 2. 月/日-月/日 パターン (例: 【11/9-11/13】)
  m = title.match(/【(\d{1,2})\/(\d{1,2})-(\d{1,2})\/(\d{1,2})(?:日|期限)?】/);
  if (m) {
    const m1 = m[1].padStart(2, '0');
    const d1 = m[2].padStart(2, '0');
    const m2 = m[3].padStart(2, '0');
    const d2 = m[4].padStart(2, '0');
    return { start: `2026-${m1}-${d1}`, end: `2026-${m2}-${d2}` };
  }

  // 3. 月/日 期限 パターン (例: 【8/7期限】, 【9/25前期限】, 【9/1開始】)
  m = title.match(/【(\d{1,2})\/(\d{1,2})(?:前|開始)?(?:期限)?】/);
  if (m) {
    const month = m[1].padStart(2, '0');
    const day = m[2].padStart(2, '0');
    const end = `2026-${month}-${day}`;
    // 開始日は〆切の2週間前
    const d = new Date(`2026-${month}-${day}`);
    d.setDate(d.getDate() - 14);
    const sm = String(d.getMonth() + 1).padStart(2, '0');
    const sd = String(d.getDate()).padStart(2, '0');
    return { start: `2026-${sm}-${sd}`, end };
  }

  // 4. 月旬 パターン (例: 【9月中旬期限】, 【10月上旬期限】, 【8月中期限】, 【10月期限】)
  m = title.match(/【(\d{1,2})月(?:(上旬|中旬|下旬|中))?(?:期限)?】/);
  if (m) {
    const month = m[1].padStart(2, '0');
    const jun = m[2];
    let d = 15;
    if (jun === '上旬') d = 5;
    else if (jun === '中旬' || jun === '中') d = 15;
    else if (jun === '下旬') d = 25;
    else d = 28;

    const day = String(d).padStart(2, '0');
    const end = `2026-${month}-${day}`;
    const dObj = new Date(`2026-${month}-${day}`);
    dObj.setDate(dObj.getDate() - 14);
    const sm = String(dObj.getMonth() + 1).padStart(2, '0');
    const sd = String(dObj.getDate()).padStart(2, '0');
    return { start: `2026-${sm}-${sd}`, end };
  }

  return null;
}

async function main() {
  console.log('🌐 全タスク（旧概要タスク含む）の日付パースおよび更新処理を開始...');
  let hasNext = true, cursor = null;
  let projectId = null, startDateFieldId = null, targetDateFieldId = null;
  let allItems = [];

  while (hasNext) {
    const data = await graphql(getProjectQuery, { owner: OWNER, number: PROJECT_NUMBER, after: cursor });
    const project = data.user.projectV2;
    projectId = project.id;

    if (!startDateFieldId || !targetDateFieldId) {
      for (const f of project.fields.nodes) {
        if (f.name && f.name.toLowerCase() === 'start date') startDateFieldId = f.id;
        if (f.name && (f.name.toLowerCase() === 'target date' || f.name.toLowerCase() === 'end date')) targetDateFieldId = f.id;
      }
    }

    allItems = allItems.concat(project.items.nodes);
    hasNext = project.items.pageInfo.hasNextPage;
    cursor = project.items.pageInfo.endCursor;
  }

  let updatedCount = 0;
  for (const item of allItems) {
    let title = '';
    let hasStartDate = false;
    let hasTargetDate = false;

    item.fieldValues.nodes.forEach(fv => {
      if (fv.text && fv.field && fv.field.name === 'Title') title = fv.text;
      if (fv.date && fv.field && fv.field.name === 'Start date') hasStartDate = true;
      if (fv.date && fv.field && fv.field.name === 'Target date') hasTargetDate = true;
    });

    if (!title) continue;

    // 日付がまだセットされていないアイテムに日付を入れる
    if (!hasStartDate || !hasTargetDate) {
      const dates = parseDatesFromTitle(title);
      if (dates) {
        try {
          if (!hasStartDate && dates.start) {
            await graphql(updateFieldMutation, {
              projectId, itemId: item.id, fieldId: startDateFieldId, value: { date: dates.start }
            });
          }
          if (!hasTargetDate && dates.end) {
            await graphql(updateFieldMutation, {
              projectId, itemId: item.id, fieldId: targetDateFieldId, value: { date: dates.end }
            });
          }
          console.log(`  └ ✅ 日付補完成功: ${title} [${dates.start} 〜 ${dates.end}]`);
          updatedCount++;
        } catch (e) {
          console.error(`  └ ❌ 更新失敗: ${title} - ${e.message}`);
        }
      }
    }
  }

  console.log(`\n🎉 計 ${updatedCount} 件の旧概要タスクの日付・期間（バー）補完が完了しました！`);
}

main().catch(err => { console.error(err); process.exit(1); });
