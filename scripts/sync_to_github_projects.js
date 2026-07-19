const https = require('https');
const fs = require('fs');
const path = require('path');

// GitHub APIのトークンチェック
const token = process.env.GITHUB_TOKEN;
if (!token) {
  console.error("❌ エラー: 環境変数 GITHUB_TOKEN が設定されていません。");
  console.error("実行方法: GITHUB_TOKEN=ghp_xxxxxxxxx node scripts/sync_to_github_projects.js");
  process.exit(1);
}

const OWNER = 'yamada-sap';
const PROJECT_NUMBER = 1;
const MD_PATH = path.join(__dirname, '../docs/04_体制・評価/詳細実行タスク管理簿_ガントチャート.md');

// GraphQLリクエストを送信する共通関数
function graphql(query, variables = {}) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ query, variables });
    const req = https.request({
      hostname: 'api.github.com',
      path: '/graphql',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'User-Agent': 'Antigravity-IDE-Sync-Script',
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

// プロジェクトとフィールド情報を取得するクエリ
const getProjectQuery = `
query($owner: String!, $number: Int!) {
  user(login: $owner) {
    projectV2(number: $number) {
      id
      title
      fields(first: 50) {
        nodes {
          ... on ProjectV2Field {
            id
            name
          }
          ... on ProjectV2SingleSelectField {
            id
            name
            options {
              id
              name
            }
          }
        }
      }
    }
  }
}
`;

// ドラフトイシューを追加するミューテーション
const addDraftMutation = `
mutation($projectId: ID!, $title: String!, $body: String!) {
  addProjectV2DraftIssue(input: {projectId: $projectId, title: $title, body: $body}) {
    projectItem {
      id
    }
  }
}
`;

// フィールド値を更新するミューテーション
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

// マークダウンファイルからタスクをパース
function parseTasksFromMarkdown() {
  if (!fs.existsSync(MD_PATH)) {
    console.error(`❌ エラー: ファイルが見つかりません: ${MD_PATH}`);
    process.exit(1);
  }

  const content = fs.readFileSync(MD_PATH, 'utf-8');
  const lines = content.split('\n');
  const tasks = [];
  let inTable = false;

  for (const line of lines) {
    // テーブル行の判定
    if (line.trim().startsWith('|')) {
      const cols = line.split('|').map(c => c.trim());
      // ヘッダー行や区切り行をスキップ
      if (cols.length < 10 || cols[1].includes('ID') || cols[1].includes('---')) {
        continue;
      }
      
      const id = cols[1].replace(/\*\*/g, '').trim(); // ID (e.g. T1.1)
      const title = cols[2].trim();
      const assignee = cols[3].replace(/\*\*/g, '').replace(/<br>/g, ' ').trim();
      const aiRole = cols[4].trim();
      const action = cols[5].trim();
      const start = cols[6].trim();
      const end = cols[7].trim();
      const deliverable = cols[8].trim();
      const statusRaw = cols[9].trim();

      if (id && title) {
        // ステータスの変換
        let status = 'Todo';
        if (statusRaw.includes('[x]')) {
          status = 'Done';
        } else if (statusRaw.includes('[/]')) {
          status = 'In Progress';
        }

        // 日付を YYYY-MM-DD 形式にフォーマット (2026年想定)
        const formatYearDate = (dateStr) => {
          if (!dateStr || dateStr === '-' || dateStr === '本番' || dateStr.includes('以降')) return null;
          const match = dateStr.match(/(\d{2})\/(\d{2})/);
          if (match) {
            return `2026-${match[1]}-${match[2]}`;
          }
          return dateStr; // すでに YYYY-MM-DD の場合など
        };

        tasks.push({
          id,
          title: `【${id}】${title}`,
          assignee,
          body: `**担当責任者**: ${assignee}\n**関連AI社員**: ${aiRole}\n**行動プロセス**: ${action}\n**成果物**: ${deliverable}`,
          startDate: formatYearDate(start),
          endDate: formatYearDate(end),
          status
        });
      }
    }
  }
  return tasks;
}

// メイン同期処理
async function sync() {
  console.log('📖 詳細タスク管理簿からタスクをロード中...');
  const tasks = parseTasksFromMarkdown();
  console.log(`✅ ${tasks.length} 件のタスクを読み込みました。`);

  console.log(`🌐 GitHub Project (ユーザー: ${OWNER}, No: ${PROJECT_NUMBER}) 情報を取得中...`);
  let projectData;
  try {
    const data = await graphql(getProjectQuery, { owner: OWNER, number: PROJECT_NUMBER });
    projectData = data.user.projectV2;
  } catch (err) {
    console.error('❌ GitHub Project情報の取得に失敗しました。');
    console.error(err.message);
    process.exit(1);
  }

  console.log(`✅ プロジェクト発見: "${projectData.title}" (ID: ${projectData.id})`);

  // フィールドのIDマップを作成
  const fieldMap = {};
  for (const field of projectData.fields.nodes) {
    fieldMap[field.name.toLowerCase()] = field;
  }

  const statusField = fieldMap['status'];
  const startDateField = fieldMap['start date'] || fieldMap['start_date'];
  const endDateField = fieldMap['date'] || fieldMap['end date'] || fieldMap['end_date'];

  if (!statusField) {
    console.warn('⚠️ 警告: "Status" フィールドが見つかりません。');
  }
  if (!startDateField) {
    console.warn('⚠️ 警告: "Start date" フィールドが見つかりません。ガントチャートの日付同期はスキップされます。');
  }
  if (!endDateField) {
    console.warn('⚠️ 警告: "Date" または "End date" フィールドが見つかりません。ガントチャートの期限同期はスキップされます。');
  }

  console.log('🚀 GitHub Projectへタスクを登録開始...');

  for (const task of tasks) {
    try {
      console.log(`➕ タスク登録中: ${task.title}`);
      
      // 1. ドラフトイシューとしてタスクを追加
      const addRes = await graphql(addDraftMutation, {
        projectId: projectData.id,
        title: task.title,
        body: task.body
      });
      const itemId = addRes.addProjectV2DraftIssue.projectItem.id;

      // 2. ステータスを設定
      if (statusField && task.status) {
        // StatusのオプションIDを見つける
        const option = statusField.options.find(o => o.name.toLowerCase() === task.status.toLowerCase());
        if (option) {
          await graphql(updateFieldMutation, {
            projectId: projectData.id,
            itemId,
            fieldId: statusField.id,
            value: { singleSelectOptionId: option.id }
          });
        }
      }

      // 3. 開始日を設定
      if (startDateField && task.startDate) {
        await graphql(updateFieldMutation, {
          projectId: projectData.id,
          itemId,
          fieldId: startDateField.id,
          value: { date: task.startDate }
        });
      }

      // 4. 終了日（期限）を設定
      if (endDateField && task.endDate) {
        await graphql(updateFieldMutation, {
          projectId: projectData.id,
          itemId,
          fieldId: endDateField.id,
          value: { date: task.endDate }
        });
      }

      console.log(`   └ ✅ 登録成功: ${task.title}`);
    } catch (err) {
      console.error(`   └ ❌ 登録失敗: ${task.title}`);
      console.error(`      エラー内容: ${err.message}`);
    }
  }

  console.log('\n🎉 すべてのタスクの同期処理が完了しました！');
}

sync();
