# 産業フェアしずおか2026：提出書類・手引き自動生成システム

## 📌 現在のタスクステータス

- [x] フェーズ 1：環境構築（シェルスクリプト実行）
- [x] フェーズ 2：2026年新変数の流し込み (`data/2026_config.txt` の更新)
- [x] フェーズ 3：2026年版書類テキストドラフト生成 (`doc_scaffolder` の起動)
- [x] フェーズ 4：公式Instagram広告・運用計画 ＆ Google/Yahooディスプレイ広告計画の構築（完了）
- [x] フェーズ 5：Marpスライド ＆ Mermaid搬入図解生成 (`marp_generator` の起動)

> [!TIP]
> **エディタ編集画面から各計画書ファイルを開く方法**
> 各計画書へのリンクは、**`Cmd` + クリック（Mac）** または **`Ctrl` + クリック（Windows）** を押すことで、エディタ内で直接ファイルを開く（ジャンプする）ことができます。

---

## 📱 スマートフォン/PC閲覧用 スライドショー一覧 (GitHub Pages公開中)

Markdownから自動ビルドされた、PCおよびスマートフォン（横画面推奨）でフリックしながら閲覧できるスライドショーです。

### 🎯 【最重要】進捗会議用コックピットポータル
* 👑 **[静岡フェア2026 進捗会議ポータル (これ1枚で会議を回す)](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/進捗会議ポータル.html)**
* 📋 **[GitHubタスク管理ボード (カンバン・ガント・一括入力)](https://github.com/users/yamada-sap/projects/1/views/4)**
* 📊 **[マスタータスク管理簿 (全タスク一覧スライド)](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/マスタータスク管理簿.html)**

### 🚦 進行管理・スケジュール
* 🚦 **[プロジェクト全体タスク管理簿 (有言実行TODO)](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/プロジェクト全体タスク管理簿.html)**
* 📅 **[全体スケジュール・マイルストーン計画書](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/全体スケジュール_マイルストーン計画書.html)**
* 📐 **[全体未決課題管理簿 ＆ 出展者関係フロー設計書](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/全体未決課題管理簿_出展者フロー設計.html)**

### 📝 実務指示・チェックリスト
* 📋 **[リアル社員向けタスク指示書 (具体的実務指示)](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/AIからリアル社員への具体的タスク指示書.html)**
* 🛡 **[プロジェクトメンバー役割別・抜け漏れ防止タスクチェックリスト](https://yamada-sap.github.io/shizuoka-fair-2026/docs/04_体制・評価/プロジェクトメンバー役割別_抜け漏れ防止タスクチェックリスト.html)**

### 📖 出展者向け公式手引き
* 🏢 **[【企業ゾーン】出展の手引き2026](https://yamada-sap.github.io/shizuoka-fair-2026/docs/01_出展関係書類/【企業ゾーン】出展の手引き2026.html)**
* 🌊 **[【地場産業観光ゾーン】出展の手引き2026](https://yamada-sap.github.io/shizuoka-fair-2026/docs/01_出展関係書類/【地場産業観光ゾーン】出展の手引き2026.html)**

### 🤝 打合せ資料
* 🤝 **[インフルエンサーキックオフ打合せ資料](https://yamada-sap.github.io/shizuoka-fair-2026/docs/03_インフルエンサー/インフルエンサーキックオフ打合せ資料.html)**

---

## ⚙️ 組織設計 & ガバナンス（v1.8.3 適用）

本プロジェクトは、AIと人間の共創組織 **Yamada Digital Partners (YDP) v1.8.3** の体制で運営されています。

### 📄 主要な統治ファイル
- **[最高憲法: organization_policy.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/organization_policy.md)**: 組織目的、SLAルール、回答フォーマットなどを定義。
- **[監査役: organization_ceo.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/organization_ceo.md)**: AIのCEO（ファクトチェック・外部公開表現監査役）のアサイン定義。
- **[名簿: role_registry.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/role_registry.md)**: 精鋭20名のアサインとRACI責任分界の定義。
- **[パラメータ: event_parameters.json](file:///Users/sap220701/Desktop/産業フェア_ローカル/event_parameters.json)**: 会期やターゲットなどのグローバル変数を一元管理。
- **[会議ポータル: 進捗会議ポータル.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/進捗会議ポータル.md)**: 全シグナル、メンバー別確認事項、重要スライドリンクを一括集約した会議用ポータル。
- **[のびのびワークライフバランス計画書](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/全体スケジュール_マイルストーン計画書.md)**: 残業禁止・2週間バッファ原則などのプロジェクト進行ルールを定義。
- **[全体未決課題管理簿・出展者フロー設計](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/全体未決課題管理簿_出展者フロー設計.md)**: TVCM、サンリオ、きのいい羊たち等の未決項目や出展者ライフサイクルの可視化。
- **[メンバー役割別・抜け漏れ防止タスクチェックリスト](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/プロジェクトメンバー役割別_抜け漏れ防止タスクチェックリスト.md)**: 全20名の担当ToDoと直前トラブル防止策の網羅。
- **[リアル社員向けタスク指示書 (アクション仕様詳細)](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/AIからリアル社員への具体的タスク指示書.md)**: 人間メンバー（梅原・山田・長島・鈴木等）への具体的実務指示。
- **[プロジェクト全体タスク管理簿 (環境信号システムつき)](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/プロジェクト全体タスク管理簿.md)**: すべての実務タスクのリアルタイム進捗と信号状態（🟢🟡🔴）の可視化。
- **[Notion同期セットアップ手順書](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/Notion同期セットアップ手順書.md)**: GitHubとNotionを双方向同期させるインテグレーション・シークレットの設定ガイド。
- **[GitHub Pagesによるスマホプレビュー設定](file:///Users/sap220701/Desktop/産業フェア_ローカル/docs/04_体制・評価/GitHub_Pages%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%89%E5%85%AC%E9%96%8B%E6%89%8B%E9%A0%86%E6%9B%B8.md)**: Marpで出力したHTMLスライドをスマホでフリックして見るための自動デプロイ設定ガイド。
- **[意思決定記録 (ADR)](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/adr/)**: 組織設計の変遷を記録。
  - [ADR-004 (SLA化とKPI)](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/adr/ADR-004-kpi-expansion-and-objective-formulation.md)
  - [ADR-005 (RACIと絶対表現排除)](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/adr/ADR-005-raci-realignment-and-absolute-expression-elimination.md)

### 💬 主な合意形成討論ログ
- **[TVCM制作・放映シミュレーション討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/TVCM%E5%88%B6%E4%BD%9C%E3%83%BB%E6%94%BE%E6%98%A0%E3%82%B7%E3%83%9F%E3%83%A5%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: 15秒CMコンテ案・放送局配分の社内合意。
- **[デジタルスタンプラリーシステム仕様・回遊設計討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%97%E3%83%A9%E3%83%AA%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E4%BB%95%E6%A7%98%E3%83%BB%E5%9B%9E%E9%81%8A%E8%A8%AD%E8%A8%88%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: QRコードシステム要件・回遊設計・バックアップ紙台紙対策。
- **[サンリオステージ運営・音響・セキュリティ討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/%E3%82%B5%E3%83%B3%E3%83%AA%E3%82%AA%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E9%81%8B%E5%96%B6_%E9%9F%B3%E9%9F%BF_%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: ポムポムプリン等のキャスト稼働制限・セキュリティ・撮影制限。
- **[AIカメラ設置・プライバシー分析討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/AI%E3%82%AB%E3%83%A1%E3%83%A9%E8%A8%AD%EBD%E3%82%AB%E3%83%A1%E3%83%A9%E8%A8%AD%E7%BD%AE_%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E5%88%86%E6%9E%90%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: 入場カウント位置・エッジデータ即時破棄・マイルドな告知看板。
- **[きのいい羊たちコラボ・安全対策討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/%E3%81%8D%E3%81%AE%E3%81%84%E3%81%84%E7%BE%8A%E3%81%9F%E3%81%A1%E3%82%B3%E3%83%A9%E3%83%9C_%E5%AE%89%E5%85%A8%E5%AF%BE%E7%AD%96%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: 体操体験プログラム・衝撃緩和マット敷設・1分以内救護搬送連携。
- **[印刷物制作・FSC認証・学校配布申請討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/%E5%8D%B0%E5%88%B7%E7%89%A9%E5%88%B6%E4%BD%9C_FSC%E8%AA%8D%E8%A8%BC_%E5%AD%A6%E6%A0%A1%E9%85%8D%E5%B8%83%E7%94%B3%E8%AB%8B%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: FSC森林づくり紙・植物性インキ指定・全小学校へ学級仕分けバンド納品。
- **[会場施工・搬入出ヤード監督調整討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/%E4%BC%9A%E5%A0%B4%E6%96%BD%E5%B7%A5%E3%83%BB%E6%90%AC%E5%85%A5%E5%87%BA%E3%83%A4%E3%83%BC%E3%83%89%E7%9B%A3%E7%9D%A3%E8%AA%BF%E6%95%B4%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: 15分ヤード退去制限や無断電気チェックの合意。
- **[出展者問合せ削減＆経理調整討論ログ](file:///Users/sap220701/Desktop/産業フェア_ローカル/discussions/%E5%87%BA%E5%B1%95%E8%80%85%E5%95%8F%E5%90%88%E3%81%9B%E5%89%8A%E6%B8%9B%EF%BC%86%E7%B5%8C%E7%90%86%E8%AA%BF%E6%95%B4%E8%A8%8E%E8%AB%96%E3%83%AD%E3%82%B0.md)**: 口座分離誤入金対策・防災火気消火器の合意。

### 📈 組織のコアKPI
1. **人間修正率 (Human Intervention Rate: HIR)**: トモさんが直接手動修正した成果物の割合（ターゲット: 5%以下）
2. **差し戻し率 (Rejection Rate: RR)**: AI監査レイヤー（Validator）で修正を指示された割合（ターゲット: 30%以下）

### 🗺️ RACIレビューパイプライン
無限レビューを防ぐため、以下の順にバトンを渡す一方向パイプラインを厳守します。
1. **R (実務AI)** ➔ 2. **C (ペルソナ/地元民レビュー)** ➔ 3. **R (冷徹な監査役)** ➔ 4. **R (AI COO)** ➔ 5. **R (AI CEO/最終ファクト・表現監査役)** ➔ 6. **R (AI EA)** ➔ 7. **A (山田プロデューサー/人間: 最終決裁)**

---

## 👥 AI社員および役割定義
すべての就業規則・指示書は [`.agents/rules/`](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/) 配下に格納されています。

| No. | 役割名 | パス | 責任区分 | 主な専門領域 |
|---|---|---|---|---|
| 1 | 総合ディレクター | [web_promoter.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/web_promoter.md) | `R` | 全体ハブ、タスク進行管理、広告文管理 |
| 2 | アカウントプランナー | [web_account_planner.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/web_account_planner.md) | `R` | 予算配分、CPA/ROI試算、効果シミュレーション |
| 3 | 協賛営業進行 | [ad_sales_manager.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/ad_sales_manager.md) | `R` | 新規広告「ジャック」営業、進行、入稿管理 |
| 4 | 経理・財務担当 | [finance_accounting_manager.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/finance_accounting_manager.md) | `R` | 予算管理、入出金監視、請求・売上精算 |
| 5 | ビジュアルデザイナー | [visual_designer.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/visual_designer.md) | `R` | 全ビジュアル設計、印刷物の環境配慮（FSC） |
| 6 | 行政・広報渉外ディレクター | [public_relations_director.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/public_relations_director.md) | `R` | 主催者折衝、官公庁届出、プレスリリース管理 |
| 7 | 会場施工・調達監督 | [venue_logistics_director.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/venue_logistics_director.md) | `R` | 施工進行、搬入ヤード（15分単位）管理、資機材調達 |
| 8 | イベント運営責任者 | [event_operations_manager.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/event_operations_manager.md) | `R` | 当日進行、ステージMC、現場トラブル対応 |
| 9 | イベント企画・全体設計担当 | [event_content_planner.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/event_content_planner.md) | `R` | 体験ブース企画、ステージ企画・設計 |
| 10 | 出展者管理・とりまとめ担当 | [exhibitor_coordination_chief.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/exhibitor_coordination_chief.md) | `R` | 200社説明会（9/25）、紹介画像回収（SLA 98%以上） |
| 11 | スタッフ・アルバイト管理担当 | [staff_management_coordinator.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/staff_management_coordinator.md) | `R` | 現場スタッフ・警備シフト、配置・休憩管理 |
| 12 | キャラクター・キャスト管理 | [cast_backstage_manager.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/cast_backstage_manager.md) | `R` | キャラ・キャスト動線、連続稼働（1回 15-20分）管理 |
| 13 | デジタル・WEBマネージャー | [digital_web_manager.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/digital_web_manager.md) | `R` | HP改修、スタンプラリーフォーム、プライバシー対策 |
| 14 | AV・テクニカル演出 | [av_production_manager.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/av_production_manager.md) | `R` | 会場内音響、著作権管理、駅ビジョン映像送出 |
| 15 | 安全・衛生・警備責任者 | [safety_security_marshal.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/safety_security_marshal.md) | `R` | 駐車場誘導、食中毒・ゴミ回収、救護所運営 |
| 16 | 組織改善責任者 (AI COO) | [organization_coo.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/organization_coo.md) | `R` | 運営・KPI監視、ボトルネック分析、週次改善レポート作成 |
| 17 | 組織アーキテクト (AI EA) | [organization_architect.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/organization_architect.md) | `R` | 静的組織設計の監査、ミニマリズム追求、ADR起草 |
| 18 | 冷徹な監査役 | [cool_headed_validator.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/cool_headed_validator.md) | `R` | ドラフトの冷徹な監査、不整合・リスク特定、論点整理 |
| 19 | 静岡ファミリーペルソナ | [persona_shizuoka_family.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/persona_shizuoka_family.md) | `C` | 家族（マイママ、タカシパパ他）目線でのUXレビュー |
| 20 | 地元ローカルご意見番 | [local_neighborhood_observer.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/local_neighborhood_observer.md) | `C` | シニア・周辺住民（ヨシコおばちゃん他）のローカル目線 |
| 21 | 最高経営責任者 (AI CEO) | [organization_ceo.md](file:///Users/sap220701/Desktop/産業フェア_ローカル/.agents/rules/organization_ceo.md) | `R` | 対外向け最終ファクトチェック、プロフェッショナル表現推敲 |

---

## 📱 SNS（Instagram）プロモーション関連資料

本プロジェクトにおけるSNS集客用の計画書および配布資料テンプレートです。最新のMetaアルゴリズムに準拠し、実務でペタッと貼れる原稿案やモックアップ画像を内包しています。

- **[Instagram広告配信計画書\_2026.md](./docs/Instagram広告配信計画書_2026.md)**
  - 広告予算（100,000円）のハイブリッド配分計画、Advantage+ターゲティング設定、コピペで使える広告テキスト（各5案）、リール/カルーセルのビジュアル絵コンテを格納。
- **[Instagram運用計画書\_2026.md](./docs/Instagram運用計画書_2026.md)**
  - 公式アカウントのオーガニック運用マニュアル、3フェーズ投稿スケジュール、出展者自社発信による相互送客スキーム、カルーセル（画像5枚）プレビュー表示。
- **[出展者PR用インタビューシートテンプレート.md](./docs/出展者PR用インタビューシートテンプレート.md)**
  - 出展者説明会（9/25）時等に出展者へ配布する紹介文作成・画像回収用アンケート項目、および出展者自身のSNSで公式アカウントをメンション・タグ付けしてもらうための協力依頼マニュアル。

## 💻 WEBディスプレイ広告（Google・Yahoo!）関連資料

本プロジェクトにおけるWEBディスプレイ広告（GDN・YDA）の集客用計画書です。ファミリー層と一般・シニア層へのアプローチセグメント、LINE広告配信面を含む連携設計、および詳細な費用シミュレーションを含みます。

- **[Googleディスプレイ広告配信計画書\_2026.md](./docs/Googleディスプレイ広告配信計画書_2026.md)**
  - 広告予算（100,000円）の運用設計。ファミリー層と一般・シニア層のセグメント分け（予算6:4比率）、レスポンシブディスプレイ広告（RDA）のアセットコピー案（各ターゲット5案）、および詳細な成果シミュレーション（CPM 90円、表示回数 1,111,111回目標）。
- **[Yahooディスプレイ広告配信計画書\_2026.md](./docs/Yahooディスプレイ広告配信計画書_2026.md)**
  - 広告予算（100,000円）の運用設計。YDA経由でのLINE広告配信枠（トークリスト、LINE NEWS等）の包含プラン、ファミリー層と一般・シニア層のレスポンシブ広告コピー案（各ターゲット5案）、詳細シミュレーション（CPM 90円、表示回数 1,111,111回目標）。

---

## 📋 GitHub Projects（タスク管理ボード）の操作方法

タスクの進行管理には、以下のGitHub公式ボードを使用します。メンバーのITリテラシーや好みに合わせて、ビュー（見え方）をクリック一つで瞬時に切り替えられます。

👉 **[GitHubプロジェクトボードを開く](https://github.com/users/yamada-sap/projects/1/views/4)**

### 1. タスクの一括登録・編集（Tableビュー）- 推奨
* **操作感**: エクセルやGoogleスプレッドシートとほぼ同じです。
* **手順**: 
  1. 画面最下部の **`＋ Add item`** をダブルクリックしてタスク名を入力。
  2. `Assignees` 列で担当者（梅原、長島等）を選択。
  3. `Status` 列で進捗（未着手・進行中・完了）を選択。
  4. `Start date`（開始日）と `Date`（期限）を入力すると、自動的にガントチャートへグラフが描画されます。

### 2. 進捗の直感的なドラッグ更新（Boardビュー）
* **操作感**: カンバン（看板）方式のカード画面です。
* **手順**: 
  * タスクカードをつまんで、左右のステータス列（「未着手」➔「進行中」➔「完了」）へドラッグ＆ドロップするだけで、進捗状態が更新されます。

### 3. スケジュールの可視化（Roadmap/Timelineビュー）
* **操作感**: ガントチャートです。
* **機能**: 
  * 横型バーで全体のタイムラインを確認できます。ドラッグで期間（開始・終了日）を変更することも可能です。

---

## 🛠️ スライドショーの書き出し（デプロイ）規程と操作方法

GitHubのビルド時間制限やシークレットトークンの消費を抑えるため、**通常のコミット・プッシュではスライドの自動ビルド（デプロイ）は走りません**。資料を最新のスライドHTMLに変換して公開（更新）したい場合は、以下のいずれかの方法でアクションを行ってください。

### 1. コミット時にメッセージでトリガーする（推奨）
Gitコミットを行う際、コミットメッセージの中に **`[deploy]`** という半角キーワードを含めてプッシュしてください。GitHub Actionsが自動的に検知して、スライドのビルド＆デプロイを自動実行します。

* **コマンドの記述例**:
  ```bash
  git add -A
  git commit -m "インフルエンサー資料の表現を修正 [deploy]"
  git push origin main
  ```

### 2. GitHubのWeb画面から手動でデプロイする（手動トリガー）
Gitのコミットログに `[deploy]` を残したくない場合や、すでにプッシュした後に手動でデプロイだけを走らせたい場合は、GitHubのブラウザ画面からいつでも手動ビルドできます。

* **操作手順**:
  1. GitHub上のプロジェクトリポジトリをブラウザで開きます。
  2. 画面上部タブメニューの **`Actions`** をクリックします。
  3. 左側のワークフロー一覧から **`Deploy Slides to GitHub Pages`** を選択します。
  4. 画面右上に現れる **`Run workflow`** というグレーのボタンをクリックします。
  5. ブランチが `main` になっていることを確認し、緑色の **`Run workflow`** ボタンをクリックして実行します。
  6. 約30秒で自動ビルドと公開サーバへのデプロイが完了します。
