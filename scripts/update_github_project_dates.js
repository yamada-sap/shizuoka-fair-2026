const https = require('https');
const fs = require('fs');
const path = require('path');

const token = process.env.GITHUB_TOKEN;
if (!token) {
  console.error("❌ エラー: 環境変数 GITHUB_TOKEN が設定されていません。");
  process.exit(1);
}

const OWNER = 'yamada-sap';
const PROJECT_NUMBER = 1;
const MD_PATH = path.join(__dirname, '../docs/04_体制・評価/詳細実行タスク管理簿_ガントチャート.md');

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
          if (json.errors) {
            reject(new Error(JSON.stringify(json.errors, null, 2)));
          } else {
            resolve(json.data);
          }
        } catch (e) {
          reject(e);
        }
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function parseTasksFromMarkdown() {
  const content = fs.readFileSync(MD_PATH, 'utf-8');
  const lines = content.split('\n');
  const tasksMap = new Map();

  for (const line of lines) {
    if (line.trim().startsWith('|')) {
      const cols = line.split('|').map(c => c.trim());
      if (cols.length < 10 || cols[1].includes('ID') || cols[1].includes('---')) continue;
      
      const id = cols[1].replace(/\*\*/g, '').trim();
      const title = cols[2].trim();
      const start = cols[6].trim();
      const end = cols[7].trim();

      const formatYearDate = (dateStr) => {
        if (!dateStr || dateStr === '-' || dateStr === '本番' || dateStr.includes('以降')) return null;
        const match = dateStr.match(/(\d{2})\/(\d{2})/);
        if (match) return `2026-${match[1]}-${match[2]}`;
        return dateStr;
      };

      if (id && title) {
        const fullTitle = `【${id}】${title}`;
        tasksMap.set(fullTitle, {
          id,
          startDate: formatYearDate(start),
          endDate: formatYearDate(end)
        });
      }
    }
  }
  return tasksMap;
}

const getProjectAndItemsQuery = `
query($owner: String!, $number: Int!, $after: String) {
  user(login: $owner) {
    projectV2(number: $number) {
      id
      fields(first: 50) {
        nodes {
          ... on ProjectV2FieldCommon {
            id
            name
          }
        }
      }
      items(first: 100, after: $after) {
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes {
          id
          content {
            ... on DraftIssue {
              title
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
    projectV2Item {
      id
    }
  }
}
`;

async function main() {
  console.log('📖 マスクダウンから日付データを取得中...');
  const tasksMap = parseTasksFromMarkdown();
  console.log(`✅ ${tasksMap.size} 件のタスク定義を読み込みました。`);

  console.log('🌐 GitHub Projectの全アイテムおよびフィールド情報をロード中...');
  
  let allItems = [];
  let hasNext = true;
  let cursor = null;
  let projectId = null;
  let startDateFieldId = null;
  let targetDateFieldId = null;

  while (hasNext) {
    const data = await graphql(getProjectAndItemsQuery, { owner: OWNER, number: PROJECT_NUMBER, after: cursor });
    const project = data.user.projectV2;
    projectId = project.id;

    if (!startDateFieldId || !targetDateFieldId) {
      for (const f of project.fields.nodes) {
        if (f.name && f.name.toLowerCase() === 'start date') startDateFieldId = f.id;
        if (f.name && (f.name.toLowerCase() === 'target date' || f.name.toLowerCase() === 'end date')) targetDateFieldId = f.id;
      }
    }

    const itemsNode = project.items;
    allItems = allItems.concat(itemsNode.nodes);
    hasNext = itemsNode.pageInfo.hasNextPage;
    cursor = itemsNode.pageInfo.endCursor;
  }

  console.log(`✅ プロジェクト内の全 ${allItems.length} 件のアイテムを取得完了。`);
  console.log(`📌 Start Date フィールドID: ${startDateFieldId}`);
  console.log(`📌 Target Date フィールドID: ${targetDateFieldId}`);

  if (!startDateFieldId || !targetDateFieldId) {
    console.error('❌ 開始日または終了日のフィールドがプロジェクト内に見つかりません。');
    process.exit(1);
  }

  console.log('🚀 全アイテムへの日付セット（Start date / Target date）更新を開始...');

  let successCount = 0;
  for (const item of allItems) {
    const title = item.content && item.content.title;
    if (!title) continue;

    const taskInfo = tasksMap.get(title);
    if (taskInfo) {
      try {
        if (taskInfo.startDate) {
          await graphql(updateFieldMutation, {
            projectId,
            itemId: item.id,
            fieldId: startDateFieldId,
            value: { date: taskInfo.startDate }
          });
        }
        if (taskInfo.endDate) {
          await graphql(updateFieldMutation, {
            projectId,
            itemId: item.id,
            fieldId: targetDateFieldId,
            value: { date: taskInfo.endDate }
          });
        }
        console.log(`  └ ✅ 日付更新成功: ${title} [${taskInfo.startDate || 'なし'} 〜 ${taskInfo.endDate || 'なし'}]`);
        successCount++;
      } catch (e) {
        console.error(`  └ ❌ 日付更新失敗: ${title} - ${e.message}`);
      }
    }
  }

  console.log(`\n🎉 合計 ${successCount} 件のタスクに「Start date」および「Target date」の期間（バー）をセット完了しました！`);
}

main().catch(err => {
  console.error('エラー発生:', err);
  process.exit(1);
});
