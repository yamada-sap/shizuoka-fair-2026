---
marp: true
theme: default
size: A4
html: true
class: lead
paginate: false
style: |
  /* ==========================================================================
     産業フェアしずおか2026 A4縦型・提出書類専用カスタムCSS
     ========================================================================== */

  /* 1. 全体・ページの基本定義 (A4白背景前提) */
  section {
    width: 210mm;
    height: 297mm;
    padding: 12mm 15mm;
    box-sizing: border-box;
    background-color: #ffffff;
    color: #333333;
    font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'Meiryo', sans-serif;
    font-size: 8px;
    line-height: 1.3;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  /* 2. プロ仕様ヘッダーレイアウト (フレックス配置) */
  .header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #c01967; /* アクセントカラーのマゼンタピンク */
    padding-bottom: 4px;
    margin-bottom: 6px;
    height: 35px;
  }
  .header-logo {
    font-size: 9px;
    font-weight: 900;
    color: #c01967;
    line-height: 1.1;
  }
  .header-logo span {
    display: block;
    font-size: 7px;
    color: #666666;
    font-weight: normal;
  }
  .header-title-box {
    text-align: center;
    flex-grow: 1;
  }
  .header-title {
    font-size: 14px !important;
    font-weight: bold;
    margin: 0 !important;
    padding: 0 !important;
    letter-spacing: 1px;
    color: #333333;
  }
  .header-deadline-box {
    border: 1.5px solid #c01967;
    background-color: #fff0f5;
    padding: 2px 6px;
    text-align: center;
    font-size: 7px;
    font-weight: bold;
    line-height: 1.1;
    min-width: 65px;
    border-radius: 3px;
  }

  /* 3. 申請用紙テーブル (チマチマした調整を撲滅する厳格ルール) */
  table {
    width: 100% !important;
    border-collapse: collapse !important;
    margin-bottom: 6px !important;
    background-color: #ffffff;
  }
  th, td {
    border: 1px solid #444444 !important;
    padding: 3px 4px !important;
    font-size: 7.5px;
    height: auto;
    vertical-align: middle;
  }
  th {
    background-color: #f2f2f2 !important;
    font-weight: bold;
    text-align: center;
    color: #222222;
  }
  td input[type="checkbox"] {
    transform: scale(0.8);
    margin-right: 2px;
  }

  /* 4. アラート・インフォメーションボックス */
  .warning-box {
    border: 1.5px solid #deb887;
    background-color: #fffaf0;
    border-radius: 4px;
    padding: 4px 8px;
    color: #a0522d;
    margin-bottom: 5px;
  }
  .info-box {
    border: 1px solid #cccccc;
    background-color: #f9f9f9;
    border-radius: 4px;
    padding: 4px 8px;
    color: #555555;
  }
  .accent-color {
    color: #c01967;
    font-weight: bold;
  }

  /* 5. ページ5：消防提出用ブース内レイアウト「方眼紙グリッド」の完全CSS再現 */
  .grid-container {
    position: relative;
    width: 100%;
    height: 125px;
    border: 1.5px solid #444444;
    margin-top: 4px;
    /* CSSのグラデーションで正確な10px間隔の「点線方眼紙」を描画 */
    background-image: 
      linear-gradient(to right, #dddddd 1px, transparent 1px),
      linear-gradient(to bottom, #dddddd 1px, transparent 1px);
    background-size: 12px 12px;
    background-color: #ffffff;
  }
  .grid-label {
    position: absolute;
    border: 1px solid #444444;
    background-color: #ffffff;
    padding: 2px 4px;
    font-size: 6.5px;
    text-align: center;
    font-weight: bold;
    box-shadow: 1px 1px 2px rgba(0,0,0,0.05);
  }

  /* 6. 最下部固定フッター */
  .footer-container {
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #dddddd;
    padding-top: 3px;
    font-size: 6.5px;
    color: #888888;
  }
---

<!-- PAGE 1: ご提出シート -->

<div class="header-container">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7.5px; font-weight: bold; color: #333333; display: block;">出展者提出書類</span>
    <h1 class="header-title" style="color: #333333;">ご提出シート</h1>
  </div>
  <div style="width: 80px;"></div>
</div>

<p style="text-align: center; font-size: 9.5px; margin-bottom: 8px;">
  下記の該当するシートに必要事項をご記入の上、<br>
  <strong>締切日までにFAX、E-mailまたは郵送</strong>にてご提出ください。
</p>

<table style="margin-bottom: 8px;">
  <thead>
    <tr>
      <th style="width: 45%; padding: 2px 3px;">書類番号・名称</th>
      <th style="width: 25%; padding: 2px 3px;">提出対象</th>
      <th style="width: 30%; padding: 2px 3px;">提出締切日</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 2px 3px;"><strong>1．出展内容確認書</strong></td>
      <td style="text-align: center; padding: 2px 3px;">全出展者</td>
      <td style="text-align: center; font-weight: bold; color: #000000; font-size: 8.5px; padding: 2px 3px;">10月7日（水）</td>
    </tr>
    <tr>
      <td style="padding: 2px 3px;"><strong>2．追加備品申込書</strong></td>
      <td style="text-align: center; padding: 2px 3px;">全出展者</td>
      <td style="text-align: center; font-weight: bold; color: #000000; font-size: 8.5px; padding: 2px 3px;">10月7日（水）</td>
    </tr>
    <tr>
      <td style="padding: 2px 3px;"><strong>3．電気・火気・危険物使用申請書</strong></td>
      <td style="text-align: center; padding: 2px 3px;">全出展者</td>
      <td style="text-align: center; font-weight: bold; color: #000000; font-size: 8.5px; padding: 2px 3px;">10月7日（水）</td>
    </tr>
    <tr>
      <td style="padding: 2px 3px;"><strong>4．Instagram掲載入力フォーム</strong></td>
      <td style="text-align: center; padding: 2px 3px;">希望者のみ</td>
      <td style="text-align: center; font-weight: bold; color: #000000; font-size: 8.5px; padding: 2px 3px;">10月7日（水）</td>
    </tr>
    <tr>
      <td style="padding: 2px 3px;"><strong>5．ご協賛品確認シート</strong></td>
      <td style="text-align: center; padding: 2px 3px;">ご協力いただける出展者</td>
      <td style="text-align: center; font-weight: bold; color: #000000; font-size: 8.5px; padding: 2px 3px;">11月11日（水）</td>
    </tr>
  </tbody>
</table>

<div style="border: 1.5px dashed #333333; border-radius: 4px; padding: 6px 10px; background-color: #f9f9f9; margin-top: 8px;">
  <h3 style="text-align: center; color: #333333; margin-bottom: 3px; font-size: 9px;">■■■ シート提出先 ■■■</h3>
  <table style="border: none; margin-bottom: 0;">
    <tr style="border: none;">
      <td style="border: none; width: 25%; font-weight: bold; text-align: right; padding: 1px;">企画運営担当：</td>
      <td style="border: none; width: 75%; padding: 1px;">株式会社静鉄アド・パートナーズ 営業部 営業三課</td>
    </tr>
    <tr style="border: none;">
      <td style="border: none; font-weight: bold; text-align: right; padding: 1px;">担当者：</td>
      <td style="border: none; padding: 1px;">草ヶ谷・梅原・山田</td>
    </tr>
    <tr style="border: none;">
      <td style="border: none; font-weight: bold; text-align: right; padding: 1px;">TEL：</td>
      <td style="border: none; padding: 1px;">054-252-3132</td>
    </tr>
    <tr style="border: none;">
      <td style="border: none; font-weight: bold; text-align: right; padding: 1px;">FAX：</td>
      <td style="border: none; padding: 1px;">054-254-1831</td>
    </tr>
    <tr style="border: none;">
      <td style="border: none; font-weight: bold; text-align: right; padding: 1px;">Email：</td>
      <td style="border: none; padding: 1px;"><a href="mailto:sf-shizuoka2026@shizutetsu-ad.co.jp" style="color: #333333; text-decoration: underline;">sf-shizuoka2026@shizutetsu-ad.co.jp</a></td>
    </tr>
    <tr style="border: none;">
      <td style="border: none; font-weight: bold; text-align: right; padding: 1px;">郵送先住所：</td>
      <td style="border: none; padding: 1px;">〒420-0851 静岡市葵区日出町8-3 静鉄日出町ビル1F</td>
    </tr>
  </table>
</div>

<div class="footer-container">
  <span>産業フェアしずおか2026 出展者提出書類一式</span>
  <span>Page 1 / 7</span>
</div>

---

<!-- PAGE 2: 提出書類【1】出展内容確認書 -->

<div class="header-container">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7px; font-weight: bold; color: #666666; display: block;">提出書類 【1】</span>
    <h2 class="header-title" style="font-size: 11px;">出展内容確認書</h2>
  </div>
  <div class="header-deadline-box">
    全出展者<br>
    <span style="color: #000000; font-size: 8px;">10/7（水）</span><br>提出期限
  </div>
</div>

<div style="font-size: 7px; text-align: right; margin-bottom: 2px;">
  【提出・問合せ先】 株式会社静鉄アド・パートナーズ 担当：草ヶ谷・梅原・山田 FAX：054-254-1831 / Email：sf-shizuoka2026@shizutetsu-ad.co.jp
</div>

<table style="margin-bottom: 3px;">
  <tr>
    <th style="width: 15%; padding: 1px 2px;">出展ゾーン</th>
    <td style="width: 50%; font-size: 7.5px; padding: 1px 2px;">地場産業/観光 ・ 企業 ・ 物産ストリート （該当に〇）</td>
    <th style="width: 15%; padding: 1px 2px;">出展番号</th>
    <td style="width: 20%; background-color: #f9f9f9; text-align: center; padding: 1px 2px;">（主催者記入）</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">団体名・社名</th>
    <td colspan="3" style="height: 14px; padding: 1px 2px;"></td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">所属部署</th>
    <td style="height: 12px; padding: 1px 2px;"></td>
    <th style="padding: 1px 2px;">担当者名</th>
    <td style="padding: 1px 2px;"></td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">住所</th>
    <td colspan="3" style="height: 14px; font-size: 7px; color: #999999; padding: 1px 2px;">〒</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">TEL</th>
    <td style="padding: 1px 2px;"></td>
    <th style="padding: 1px 2px;">FAX</th>
    <td style="padding: 1px 2px;"></td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">E-mail</th>
    <td style="padding: 1px 2px;"></td>
    <th style="padding: 1px 2px;">携帯電話</th>
    <td style="padding: 1px 2px;"></td>
  </tr>
</table>

<h4 style="border-left: 2px solid #333333; padding-left: 3px; margin-top: 3px; color: #333333; font-size: 8px; margin-bottom: 1px;">1. 出展概要</h4>
<table style="margin-bottom: 3px;">
  <tr>
    <th style="width: 15%; padding: 1px 2px;">社名板表示名</th>
    <td style="width: 55%; height: 14px; font-size: 6.5px; color: #666666; vertical-align: bottom; padding: 1px 2px;">※株式会社は㈱、有限会社は㈲に省略します。</td>
    <th style="width: 15%; padding: 1px 2px;">小間数</th>
    <td style="width: 15%; text-align: right; font-size: 8px; padding: 1px 2px;">小間</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">出展内容</th>
    <td colspan="3" style="height: 18px; padding: 1px 2px;"></td>
  </tr>
</table>

<h4 style="border-left: 2px solid #333333; padding-left: 3px; margin-top: 2px; color: #333333; font-size: 8px; margin-bottom: 1px;">2. 申請関係</h4>
<table style="margin-bottom: 0;">
  <tr>
    <th rowspan="2" style="width: 15%; padding: 1px 2px;">ブース責任者</th>
    <td style="width: 42.5%; padding: 1px 2px;">11/28（土） 氏名：＿＿＿＿＿＿＿＿＿＿＿</td>
    <td style="width: 42.5%; padding: 1px 2px;">携帯：＿＿＿＿＿＿＿＿＿＿＿</td>
  </tr>
  <tr>
    <td style="padding: 1px 2px;">11/29（日） 氏名：＿＿＿＿＿＿＿＿＿＿＿</td>
    <td style="padding: 1px 2px;">携帯：＿＿＿＿＿＿＿＿＿＿＿</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">出展者パス</th>
    <td colspan="2" style="padding: 1px 2px;">2日間合計： ＿＿＿＿ 枚 （※スタッフ全員が2日間、必ず着用してください）</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">搬入出許可証</th>
    <td colspan="2" style="padding: 1px 2px;">必要 ・ 不要 （いずれかに〇） ※ 1ブースにつき1枚。許可証のない車は会場に入れません。</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">駐車許可証</th>
    <td colspan="2" style="padding: 1px 2px;">必要 ・ 不要 （いずれかに〇） ※ 1ブースにつき1枚。必要な場合は、該当する車両に〇を入れてください。
      <table style="width: 98%; margin: 1px auto 0 auto; font-size: 7px; margin-bottom: 0px;">
        <tr style="height: 8px;">
          <th style="width: 50%; padding: 0.5px 1px;">車種</th>
          <th style="width: 25%; padding: 0.5px 1px;">28日(土)</th>
          <th style="width: 25%; padding: 0.5px 1px;">29日(日)</th>
        </tr>
        <tr style="height: 8px;">
          <td style="padding: 0.5px 1px;">高さ2m以下の乗用車</td>
          <td style="height: 6px; padding: 0.5px 1px;"></td>
          <td style="padding: 0.5px 1px;"></td>
        </tr>
        <tr style="height: 8px;">
          <td style="padding: 0.5px 1px;">高さ2m以上の乗用車</td>
          <td style="height: 6px; padding: 0.5px 1px;"></td>
          <td style="padding: 0.5px 1px;"></td>
        </tr>
        <tr style="height: 8px;">
          <td style="padding: 0.5px 1px;">2tトラック</td>
          <td style="height: 6px; padding: 0.5px 1px;"></td>
          <td style="padding: 0.5px 1px;"></td>
        </tr>
        <tr style="height: 8px;">
          <td style="padding: 0.5px 1px;">2t以上のトラック</td>
          <td style="height: 6px; padding: 0.5px 1px;"></td>
          <td style="padding: 0.5px 1px;"></td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<div class="footer-container">
  <span>提出書類 【1】出展内容確認書</span>
  <span>Page 2 / 7</span>
</div>

---

<!-- PAGE 3: 提出書類【2】追加備品申込書 -->

<div class="header-container" style="margin-bottom: 3px;">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7px; font-weight: bold; color: #666666; display: block;">提出書類 【2】</span>
    <h2 class="header-title" style="font-size: 11px;">追加備品申込書</h2>
  </div>
  <div class="header-deadline-box">
    全出展者<br>
    <span style="color: #000000; font-size: 8px;">10/7（水）</span><br>提出期限
  </div>
</div>

<div style="font-size: 6.5px; text-align: right; margin-bottom: 1px;">
  【提出先】 株式会社静鉄アド・パートナーズ 担当：草ヶ谷・梅原・山田 FAX：054-254-1831 / Email：sf-shizuoka2026@shizutetsu-ad.co.jp
</div>

<table style="margin-bottom: 2px; font-size: 7.5px;">
  <tr>
    <th style="width: 15%; padding: 1px 2px;">出展者名</th>
    <td style="width: 55%; height: 11px; padding: 1px 2px;"></td>
    <th style="width: 15%; padding: 1px 2px;">出展番号</th>
    <td style="width: 15%; background-color: #f9f9f9; text-align: center; padding: 1px 2px;">（主催者記入）</td>
  </tr>
</table>

<div style="font-size: 6.5px; font-weight: bold; margin-bottom: 1px; color: #333333;">1. 基礎備品（無料）※テーブル2本・イス2脚まで無料</div>
<table style="margin-bottom: 2px; font-size: 6.5px;">
  <tr style="height: 8px;">
    <th style="width: 8%; padding: 0.5px 1px;">No</th>
    <th style="width: 32%; padding: 0.5px 1px;">項目</th>
    <th style="width: 32%; padding: 0.5px 1px;">仕様</th>
    <th style="width: 10%; padding: 0.5px 1px;">単価</th>
    <th style="width: 8%; padding: 0.5px 1px;">数量</th>
    <th style="width: 10%; padding: 0.5px 1px;">合計</th>
  </tr>
  <tr style="height: 8px; background-color: #fcfcfc;">
    <td style="text-align: center; padding: 0.5px 1px;">01</td>
    <td style="padding: 0.5px 1px;">テーブル（白布なし）</td>
    <td style="padding: 0.5px 1px;">W1800mm×D450mm</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥0</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; font-weight: bold; padding: 0.5px 1px;">￥0</td>
  </tr>
  <tr style="height: 8px; background-color: #fcfcfc;">
    <td style="text-align: center; padding: 0.5px 1px;">02</td>
    <td style="padding: 0.5px 1px;">イス</td>
    <td style="padding: 0.5px 1px;">スタッキング</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥0</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; font-weight: bold; padding: 0.5px 1px;">￥0</td>
  </tr>
</table>

<div style="font-size: 6.5px; font-weight: bold; margin-bottom: 1px; color: #333333;">2. 追加備品（有料・税込）</div>
<table style="margin-bottom: 2px; font-size: 6.5px;">
  <tr style="height: 8px;">
    <th style="width: 8%; padding: 0.5px 1px;">No</th>
    <th style="width: 32%; padding: 0.5px 1px;">項目</th>
    <th style="width: 32%; padding: 0.5px 1px;">仕様</th>
    <th style="width: 10%; padding: 0.5px 1px;">単価</th>
    <th style="width: 8%; padding: 0.5px 1px;">数量</th>
    <th style="width: 10%; padding: 0.5px 1px;">合計</th>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">03</td>
    <td style="padding: 0.5px 1px;">テーブル（追加分）</td>
    <td style="padding: 0.5px 1px;">W1800mm×D450mm</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥550</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">04</td>
    <td style="padding: 0.5px 1px;">イス（追加分）</td>
    <td style="padding: 0.5px 1px;">折りたたみ椅子</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥330</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">05</td>
    <td style="padding: 0.5px 1px;">白布</td>
    <td style="padding: 0.5px 1px;">W2400mm×D1300mm</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥1,320</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">06</td>
    <td style="padding: 0.5px 1px;">ビニールクロス</td>
    <td style="padding: 0.5px 1px;">W2400mm×D1300mm</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥1,650</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">07</td>
    <td style="padding: 0.5px 1px;">床面パンチカーペット</td>
    <td style="padding: 0.5px 1px;">W4000mm×D2000mm</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥17,600</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">08</td>
    <td style="padding: 0.5px 1px;">ヨウカン棒（展示用）</td>
    <td style="padding: 0.5px 1px;">W1800×D450×H450</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥3,850</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
</table>

<div style="font-size: 6.5px; font-weight: bold; margin-bottom: 1px; color: #333333;">3. 追加電気工事（有料・税込）</div>
<table style="margin-bottom: 2px; font-size: 6.5px;">
  <tr style="height: 8px;">
    <th style="width: 8%; padding: 0.5px 1px;">No</th>
    <th style="width: 32%; padding: 0.5px 1px;">項目</th>
    <th style="width: 32%; padding: 0.5px 1px;">仕様</th>
    <th style="width: 10%; padding: 0.5px 1px;">単価</th>
    <th style="width: 8%; padding: 0.5px 1px;">数量</th>
    <th style="width: 10%; padding: 0.5px 1px;">合計</th>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">09</td>
    <td style="padding: 0.5px 1px;">100V 2口コンセント</td>
    <td style="padding: 0.5px 1px;">100V 1.5kw</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥5,500</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">10</td>
    <td style="padding: 0.5px 1px;">単相200V 2口コンセント</td>
    <td style="padding: 0.5px 1px;">200V 1kw</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥12,100</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">11</td>
    <td style="padding: 0.5px 1px;">三相200V 2口コンセント</td>
    <td style="padding: 0.5px 1px;">200V 1kw</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥12,100</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">12</td>
    <td style="padding: 0.5px 1px;">アームスポット</td>
    <td style="padding: 0.5px 1px;">100w</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥6,050</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">13</td>
    <td style="padding: 0.5px 1px;">クリップライト</td>
    <td style="padding: 0.5px 1px;">100w</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥4,950</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">14</td>
    <td style="padding: 0.5px 1px;">スタンドスポット</td>
    <td style="padding: 0.5px 1px;">300w</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥8,800</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">15</td>
    <td style="padding: 0.5px 1px;">蛍光灯</td>
    <td style="padding: 0.5px 1px;">FL40w</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥4,950</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">16</td>
    <td style="padding: 0.5px 1px;">24時間通電</td>
    <td style="padding: 0.5px 1px;">1ブースごと</td>
    <td style="text-align: right; padding: 0.5px 1px;">￥2,200</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="text-align: right; padding: 0.5px 1px;">￥</td>
  </tr>
</table>

<div style="font-size: 6.5px; font-weight: bold; margin-bottom: 1px; color: #333333;">4. 追加給排水・その他（見積り）</div>
<table style="margin-bottom: 2px; font-size: 6.5px;">
  <tr style="height: 9px;">
    <th style="width: 8%; padding: 0.5px 1px;">No</th>
    <th style="width: 32%; padding: 0.5px 1px;">項目</th>
    <th style="width: 32%; padding: 0.5px 1px;">仕様</th>
    <th style="width: 8%; padding: 0.5px 1px;">数量</th>
    <th style="width: 20%; padding: 0.5px 1px;">合計金額</th>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">17</td>
    <td style="padding: 0.5px 1px;">1槽シンク</td>
    <td style="padding: 0.5px 1px;">別途お見積りいたします</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="background-color: #f9f9f9; text-align: center; padding: 0.5px 1px;">別途見積り</td>
  </tr>
  <tr style="height: 8px;">
    <td style="text-align: center; padding: 0.5px 1px;">18</td>
    <td style="padding: 0.5px 1px;">2槽シンク</td>
    <td style="padding: 0.5px 1px;">別途お見積りいたします</td>
    <td style="padding: 0.5px 1px;"></td>
    <td style="background-color: #f9f9f9; text-align: center; padding: 0.5px 1px;">別途見積り</td>
  </tr>
</table>

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1px; border: 1px solid #333; padding: 1px 3px; height: 12px; box-sizing: border-box;">
  <div style="font-size: 7.5px; font-weight: bold; color: #333333; line-height: 1.0;">総合計金額： ￥ ＿＿＿＿＿＿＿＿＿</div>
  <div style="font-size: 6.5px; line-height: 1.0;">
    <strong>お支払い方法：</strong>
    □ 銀行振り込み（11/13（金）まで） / □ 当日現金支払い
  </div>
</div>

<div class="info-box" style="margin-top: 1px; padding: 1px 3px; font-size: 6.5px; line-height: 1.1; margin-bottom: 0;">
  <strong>【請求およびお支払に関する注意事項】</strong><br>
  ※ お申込受付後、運営事務局（株式会社静鉄アド・パートナーズ）より順次請求書を送付いたします。記載 of 指定口座へ期限内にお振込みください。（振込手数料は出展者様のご負担となります。）<br>
  ※ 主催者（静岡産業振興協会）から請求される「出展料」とは請求元・お振込先が異なりますので、誤ってお振り込みされないよう十分ご注意ください。
</div>

<div class="footer-container">
  <span>提出書類 【2】追加備品申込書</span>
  <span>Page 3 / 7</span>
</div>

---

<!-- PAGE 4: 提出書類【3】電気・火気・危険物使用申請書 -->

<div class="header-container" style="margin-bottom: 4px;">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7.5px; font-weight: bold; color: #666666; display: block;">提出書類 【3】</span>
    <h2 class="header-title" style="font-size: 11px;">電気・火気・危険物使用申請書</h2>
  </div>
  <div class="header-deadline-box">
    全出展者<br>
    <span style="color: #000000; font-size: 8px;">10/7（水）</span><br>提出期限
  </div>
</div>

<div style="font-size: 7px; text-align: right; margin-bottom: 1px;">
  【提出・問合せ先】 株式会社静鉄アド・パートナーズ 担当：草ヶ谷・梅原・山田 FAX：054-254-1831 / Email：sf-shizuoka2026@shizutetsu-ad.co.jp
</div>

<div class="warning-box" style="padding: 2px 4px; font-size: 7px; line-height: 1.1; margin-bottom: 3px;">
  <strong>⚠️【火気使用に関する重要事項】</strong><br>
  消防条例および会場規定により、<strong>館内へのプロパンガスボンベ、カセットコンロの持ち込みは一切禁止</strong>されています。<br>
  実演で火気を使用する場合は既設の天然ガス（都市ガス）配管工事の申請が必須となります。ガスを使用する場合は必ず以下の「3. 火気使用」に都市ガス配管使用の旨をご記入ください。火気使用時は消火器の設置が義務付けられています。
</div>

<table style="margin-bottom: 3px; font-size: 7.5px;">
  <tr>
    <th style="width: 15%; padding: 1px 2px;">出展者名</th>
    <td style="width: 55%; height: 11px; padding: 1px 2px;"></td>
    <th style="width: 15%; padding: 1px 2px;">出展番号</th>
    <td style="width: 15%; background-color: #f9f9f9; text-align: center; padding: 1px 2px;">（主催者記入）</td>
  </tr>
</table>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 2px;">
  <div style="width: 49%; display: flex; flex-direction: column;">
    <div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">1. 電気の使用 （必ずいずれかに✓） □ 有 ／ □ 無</div>
    <table style="font-size: 6.5px; margin-bottom: 0; flex-grow: 1;">
      <tr>
        <th style="width: 15%; padding: 0.5px 2px;">No</th>
        <th style="width: 60%; padding: 0.5px 2px;">使用機器</th>
        <th style="width: 25%; padding: 0.5px 2px;">容量</th>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; padding: 0.5px 2px;">01</td>
        <td style="padding: 0.5px 2px;"></td>
        <td style="text-align: right; padding: 0.5px 2px;">kw</td>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; padding: 0.5px 2px;">02</td>
        <td style="padding: 0.5px 2px;"></td>
        <td style="text-align: right; padding: 0.5px 2px;">kw</td>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; padding: 0.5px 2px;">03</td>
        <td style="padding: 0.5px 2px;"></td>
        <td style="text-align: right; padding: 0.5px 2px;">kw</td>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; padding: 0.5px 2px;">04</td>
        <td style="padding: 0.5px 2px;"></td>
        <td style="text-align: right; padding: 0.5px 2px;">kw</td>
      </tr>
    </table>
  </div>
  <div style="width: 49%; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">2. 持ち込み危険物 （✓） □ 有 ／ □ 無</div>
      <table style="font-size: 6.5px; margin-bottom: 2px;">
        <tr>
          <th style="width: 15%; padding: 0.5px 2px;">No</th>
          <th style="width: 50%; padding: 0.5px 2px;">品名</th>
          <th style="width: 35%; padding: 0.5px 2px;">量</th>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; padding: 0.5px 2px;">01</td>
          <td style="padding: 0.5px 2px;"></td>
          <td style="padding: 0.5px 2px;"></td>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; padding: 0.5px 2px;">02</td>
          <td style="padding: 0.5px 2px;"></td>
          <td style="padding: 0.5px 2px;"></td>
        </tr>
      </table>
    </div>
    <div>
      <div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">3. 火気の使用 （✓） □ 有 ／ □ 無</div>
      <table style="font-size: 6.5px; margin-bottom: 0;">
        <tr>
          <th style="width: 15%; padding: 0.5px 2px;">No</th>
          <th style="width: 50%; padding: 0.5px 2px;">品名</th>
          <th style="width: 35%; padding: 0.5px 2px;">熱量</th>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; padding: 0.5px 2px;">01</td>
          <td style="padding: 0.5px 2px;"></td>
          <td style="text-align: right; padding: 0.5px 2px;">kcal</td>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; padding: 0.5px 2px;">02</td>
          <td style="padding: 0.5px 2px;"></td>
          <td style="text-align: right; padding: 0.5px 2px;">kcal</td>
        </tr>
      </table>
    </div>
  </div>
</div>

<div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">4. ブース内レイアウト</div>
<div class="grid-container">
  <div style="position: absolute; bottom: 1px; left: 50%; transform: translateX(-50%); font-size: 7px; font-weight: bold; color: #999999;">通路</div>
</div>
<div style="font-size: 6.5px; color: #666666; text-align: center; margin-top: 1px; line-height: 1.1;">
  ※ 2コマ使用、または壁を取り外す場合はその旨を必ずご記入ください。使用器具の仕様書を添付してください。
</div>

<div class="footer-container">
  <span>提出書類 【3】電気・火気・危険物使用申請書</span>
  <span>Page 4 / 7</span>
</div>

---

<!-- PAGE 5: 提出書類【3】電気・火気・危険物使用申請書（記入例） -->

<div class="header-container" style="margin-bottom: 4px;">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7.5px; font-weight: bold; color: #666666; display: block;">提出書類 【3】</span>
    <h2 class="header-title" style="font-size: 11px;">電気・火気・危険物使用申請書 <span class="accent-color">【記入例】</span></h2>
  </div>
  <div class="header-deadline-box" style="border-color: #333333; background-color: #f9f9f9; min-width: 50px;">
    <span style="color: #333333; font-size: 8px;">記入例</span>
  </div>
</div>

<table style="margin-bottom: 2px; font-size: 8px;">
  <tr>
    <th style="width: 15%; padding: 1px 3px;">出展者名</th>
    <td style="width: 55%; height: 12px; padding: 1px 3px; font-weight: bold; color: #333333;">○○商店</td>
    <th style="width: 15%; padding: 1px 3px;">出展番号</th>
    <td style="width: 15%; background-color: #f9f9f9; text-align: center; padding: 1px 3px; font-weight: bold; color: #333333;">A-01</td>
  </tr>
</table>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 2px;">
  <div style="width: 49%; display: flex; flex-direction: column;">
    <div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">1. 電気の使用： ☑ 有 ／ □ 無</div>
    <table style="font-size: 6.5px; margin-bottom: 0; flex-grow: 1; color: #333333; font-weight: bold;">
      <tr>
        <th style="width: 15%; padding: 0.5px 2px; color: #333333;">No</th>
        <th style="width: 60%; padding: 0.5px 2px; color: #333333;">使用機器</th>
        <th style="width: 25%; padding: 0.5px 2px; color: #333333;">容量</th>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; color: #333333; padding: 0.5px 2px;">01</td>
        <td style="padding: 0.5px 2px;">電気ポット</td>
        <td style="text-align: right; padding: 0.5px 2px;">1.0 kw</td>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; color: #333333; padding: 0.5px 2px;">02</td>
        <td style="padding: 0.5px 2px;">ホットプレート</td>
        <td style="text-align: right; padding: 0.5px 2px;">1.3 kw</td>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; color: #333333; padding: 0.5px 2px;">03</td>
        <td></td>
        <td></td>
      </tr>
      <tr style="height: 10px;">
        <td style="text-align: center; color: #333333; padding: 0.5px 2px;">04</td>
        <td></td>
        <td></td>
      </tr>
    </table>
  </div>
  <div style="width: 49%; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">2. 持ち込み危険物： ☑ 有 ／ □ 無</div>
      <table style="font-size: 6.5px; margin-bottom: 2px; color: #333333; font-weight: bold;">
        <tr>
          <th style="width: 15%; padding: 0.5px 2px; color: #333333;">No</th>
          <th style="width: 50%; padding: 0.5px 2px; color: #333333;">品名</th>
          <th style="width: 35%; padding: 0.5px 2px; color: #333333;">量</th>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; color: #333333; padding: 0.5px 2px;">01</td>
          <td style="padding: 0.5px 2px;">サラダ油</td>
          <td style="padding: 0.5px 2px;">2 L</td>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; color: #333333; padding: 0.5px 2px;">02</td>
          <td></td>
          <td></td>
        </tr>
      </table>
    </div>
    <div>
      <div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">3. 火気の使用： ☑ 有 ／ □ 無</div>
      <table style="font-size: 6.5px; margin-bottom: 0; color: #333333; font-weight: bold;">
        <tr>
          <th style="width: 15%; padding: 0.5px 2px; color: #333333;">No</th>
          <th style="width: 50%; padding: 0.5px 2px; color: #333333;">品名</th>
          <th style="width: 35%; padding: 0.5px 2px; color: #333333;">熱量</th>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; color: #333333; padding: 0.5px 2px;">01</td>
          <td style="padding: 0.5px 2px; font-size: 6px;">ガスコンロ(都市ガス配管)</td>
          <td style="text-align: right; padding: 0.5px 2px;">2,500kcal</td>
        </tr>
        <tr style="height: 10px;">
          <td style="text-align: center; color: #333333; padding: 0.5px 2px;">02</td>
          <td style="padding: 0.5px 2px; font-size: 6px;">ホットプレート(火気対象外)</td>
          <td style="text-align: right; padding: 0.5px 2px;">2,000kcal</td>
        </tr>
      </table>
    </div>
  </div>
</div>

<div style="font-size: 7px; font-weight: bold; margin-bottom: 1px;">4. ブース内レイアウト（記入例）</div>
<div class="grid-container" style="border: 1.5px solid #333333; height: 110px;">
  <div class="grid-label" style="top: 2px; left: 10px; border-color: #333333; color: #333333;">電気ポット<br>(1.0kw)</div>
  <div class="grid-label" style="top: 2px; left: 70px; border-color: #333333; color: #333333;">ホットプレート<br>(1.3kw)</div>
  <div class="grid-label" style="top: 2px; right: 10px; border-color: #333333; color: #ffffff; background-color: #333333; border-radius: 50%; width: 30px; height: 26px; line-height: 1.0; padding: 2px 0 0 0; box-sizing: border-box;">消火器<br>設置</div>
  <div class="grid-label" style="top: 35px; left: 10px; height: 50px; width: 25px; line-height: 1.1; border-color: #333333; color: #333333; padding: 12px 0 0 0; box-sizing: border-box;">追加<br>テ自</div>
  <div class="grid-label" style="top: 60px; left: 45px; border-color: #333333; color: #333333; width: 35px;">イス</div>
  <div class="grid-label" style="top: 60px; left: 85px; border-color: #333333; color: #333333; width: 35px;">イス</div>
  <div class="grid-label" style="bottom: 5px; left: 45px; border-color: #333333; color: #333333; width: 85px; font-size: 6.5px; line-height: 1.0;">ガスコンロ<br>(都市ガス・鉄板敷)</div>
  <div class="grid-label" style="bottom: 5px; left: 135px; border-color: #333333; color: #333333; width: 35px; line-height: 1.0;">ガス漏れ<br>警報器</div>
  <div style="position: absolute; top: 45px; left: 35px; font-size: 7px; font-weight: bold; color: #333333;">壁なし通路</div>
  <div style="position: absolute; bottom: 1px; left: 50%; transform: translateX(-50%); font-size: 7.5px; font-weight: bold; color: #333333;">通路</div>
</div>

<div class="footer-container">
  <span>提出書類 【3】電気・火気・危険物使用申請書（記入例）</span>
  <span>Page 5 / 7</span>
</div>

---

<!-- PAGE 6: 提出書類【4-1】掲載情報確認シート -->

<div class="header-container">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7.5px; font-weight: bold; color: #666666; display: block;">提出書類 【4-1】</span>
    <h2 class="header-title" style="font-size: 11px;">WEBページ・Instagram掲載情報確認シート</h2>
  </div>
  <div class="header-deadline-box">
    全出展者<br>
    <span style="color: #000000; font-size: 9px;">10/7（水）</span><br>提出期限
  </div>
</div>

<div style="font-size: 8px; text-align: right; margin-bottom: 3px;">
  【提出・問合せ先】 株式会社静鉄アド・パートナーズ 担当：草ヶ谷・梅原・山田 FAX：054-254-1831 / Email：sf-shizuoka2026@shizutetsu-ad.co.jp
</div>

<div style="border: 1.5px solid #333333; border-radius: 5px; padding: 12px; text-align: center; margin: 15px auto; width: 95%; background-color: #f9f9f9; box-sizing: border-box;">
  <h3 style="color: #333333; margin-bottom: 8px; font-size: 11px;">💻 掲載情報のWEB入稿について</h3>
  <p style="font-size: 8.5px; text-align: left; line-height: 1.4; color: #333333; margin-bottom: 8px;">
    手書きFAXによる文字誤認やメール添付における画像劣化を防ぐため、今年度より公式WEBページ・Instagramへの掲載情報の入稿は、<strong>WEBフォーム（Googleフォーム）からの入稿に完全移行</strong>いたしました。<br>
    お手数ですが、期限までに以下のリンクからアクセスし、掲載情報の入力と画像データのアップロードをお願いいたします。
  </p>

<div class="footer-container">
  <span>提出書類 【4-1】SNS掲載情報確認シート</span>
  <span>Page 6 / 7</span>
</div>

---

<!-- PAGE 7: 提出書類【5】ご協賛品確認シート -->

<div class="header-container" style="margin-bottom: 4px;">
  <div class="header-logo">
    <span>静岡「しん」発見！</span>
    産業フェアしずおか2026
  </div>
  <div class="header-title-box">
    <span style="font-size: 7.5px; font-weight: bold; color: #666666; display: block;">提出書類 【5】</span>
    <h2 class="header-title" style="font-size: 11px;">ご協賛品確認シート</h2>
  </div>
  <div class="header-deadline-box">
    希望者のみ<br>
    <span style="color: #000000; font-size: 8px;">11/11（水）</span><br>提出期限
  </div>
</div>

<div style="font-size: 7px; text-align: right; margin-bottom: 1px;">
  【書類提出先】 株式会社静鉄アド・パートナーズ 担当：草ヶ谷・梅原・山田 FAX：054-254-1831 / Email：sf-shizuoka2026@shizutetsu-ad.co.jp
</div>

<p style="font-size: 8px; line-height: 1.25; margin-bottom: 4px; color: #333333;">
  産業フェアしずおか2026では、来場者参加型スタンプラリー等の買物促進企画を実施します。<br>
  提供いただきました商品は景品として活用し、皆様のブースや商品の積極的なPRに繋げます。ご協力の程、宜しくお願い申し上げます。
</p>

<table style="margin-bottom: 3px; font-size: 7.5px;">
  <tr>
    <th style="width: 15%; padding: 1px 2px;">出展ゾーン</th>
    <td style="width: 50%; padding: 1px 2px;">地場産業/観光 ・ 企業 ・ 物産ストリート （該当に〇）</td>
    <th style="width: 15%; padding: 1px 2px;">出展番号</th>
    <td style="width: 20%; background-color: #f9f9f9; text-align: center; padding: 1px 2px;">（主催者記入）</td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">団体名・社名</th>
    <td colspan="3" style="height: 12px; padding: 1px 2px;"></td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">所属部署</th>
    <td style="padding: 1px 2px;"></td>
    <th style="padding: 1px 2px;">担当者名</th>
    <td style="padding: 1px 2px;"></td>
  </tr>
  <tr>
    <th style="padding: 1px 2px;">TEL</th>
    <td style="padding: 1px 2px;"></td>
    <th style="padding: 1px 2px;">携帯電話</th>
    <td style="padding: 1px 2px;"></td>
  </tr>
</table>

<div style="font-size: 7px; font-weight: bold; margin-bottom: 1px; color: #333333;">1. ご協賛品確認（無償にてご提供いただける商品をご記入ください）</div>
<table style="margin-bottom: 3px; font-size: 7px;">
  <thead>
    <tr style="height: 10px;">
      <th style="width: 10%; padding: 0.5px 2px;">No</th>
      <th style="width: 50%; padding: 0.5px 2px;">商品名</th>
      <th style="width: 20%; padding: 0.5px 2px;">数量</th>
      <th style="width: 20%; padding: 0.5px 2px;">参考単価</th>
    </tr>
  </thead>
  <tbody>
    <tr style="height: 10px;">
      <td style="text-align: center; padding: 0.5px 2px;">01</td>
      <td style="padding: 0.5px 2px;"></td>
      <td style="padding: 0.5px 2px;"></td>
      <td style="text-align: right; padding: 0.5px 2px;">￥</td>
    </tr>
    <tr style="height: 10px;">
      <td style="text-align: center; padding: 0.5px 2px;">02</td>
      <td style="padding: 0.5px 2px;"></td>
      <td style="padding: 0.5px 2px;"></td>
      <td style="text-align: right; padding: 0.5px 2px;">￥</td>
    </tr>
    <tr style="height: 10px;">
      <td style="text-align: center; padding: 0.5px 2px;">03</td>
      <td style="padding: 0.5px 2px;"></td>
      <td style="padding: 0.5px 2px;"></td>
      <td style="text-align: right; padding: 0.5px 2px;">￥</td>
    </tr>
  </tbody>
</table>

<div style="border: 1px dashed #333333; padding: 4px 6px; margin-top: 3px; font-size: 7.5px; background-color: #fcfcfc; line-height: 1.15; margin-bottom: 0;">
  <strong>■ご協賛品持込みのお願い■</strong><br>
  ご提供いただける協賛品については、大変お手数ですが、搬入時に<strong>「産業フェアしずおか2026 運営本部（北館）」</strong>までお持込みいただけますようお願いいたします。ご協力誠にありがとうございます。
</div>

<div class="footer-container">
  <span>提出書類 【5】ご協賛品確認シート</span>
  <span>Page 7 / 7</span>
</div>

---

## 🚨 人間での最終確認・作業タスクリスト（手戻り撲滅用）

- [x] **カレンダー・曜日チェック**
  - [x] 2026年本番日程が「11月28日（土）、29日（日）」とすべての書類で整合しているか確認する。
  - [x] 提出書類1〜4の期限が「10月7日（水）」、提出書類5の期限が「11月11日（水）」、振込期限が「11/13（金）」と、実際の2026年カレンダーの曜日と一致しているか再度目視確認する。
- [ ] **ロゴ・画像チェック**
  - [ ] 送付資料やWebサイト上のロゴマークを旧事務局（エイエイピー）のものから新事務局（静鉄アド・パートナーズ）のロゴへ差し替える。
- [ ] **インフラ・数値・火気チェック**
  - [ ] 電気工事・給排水の申込単価（テーブル￥550、コンセント￥5,500等）に変更がないか、施工協業会社等に料金表の確認を行う。
  - [ ] 会場規定（ツインメッセ静岡）でプロパンガスおよびカセットコンロが厳格に禁止されていることを再確認し、出展要項と本申請書の「都市ガス接続必須」の指示に齟齬がないか消防担当者に事前確認する。
- [ ] **WEB入稿フォームURLの設定**
  - [ ] PAGE 6に記載したGoogleフォーム等の本番URLが発行されたら、プレースホルダー部分（`https://forms.gle/...`）を本番URLに書き換える。
