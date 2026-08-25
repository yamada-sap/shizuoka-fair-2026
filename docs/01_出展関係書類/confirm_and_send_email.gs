/**
 * フォーム送信時に実行される関数
 * スプレッドシートにバインドされたGASプロジェクトに配置し、フォーム送信時トリガーを設定してください。
 * 
 * @param {Object} e フォーム送信時のイベントオブジェクト
 */
function onFormSubmit(e) {
  // トリガーから渡されるイベントデータの存在確認
  if (!e || !e.namedValues) {
    Logger.log("イベントデータが存在しないか、スプレッドシートのフォーム送信トリガーから実行されていません。");
    return;
  }

  try {
    // 設問名（項目名）をキーにして回答を取得
    // e.namedValues[キー][0] で最初の値（回答テキスト）を取り出します
    const companyName = e.namedValues['会社・団体名'] ? e.namedValues['会社・団体名'][0].trim() : '';
    const email = e.namedValues['担当者E-mail'] ? e.namedValues['担当者E-mail'][0].trim() : '';
    const boothType = e.namedValues['出店タイプ'] ? e.namedValues['出店タイプ'][0].trim() : '';
    const quantityStr = e.namedValues['申込数量'] ? e.namedValues['申込数量'][0].trim() : '0';

    // メールアドレスが取得できない場合は処理を中断
    if (!email) {
      Logger.log("送信先のメールアドレスが入力されていないため、処理を終了します。");
      return;
    }

    // 数量の文字列から数値を抽出（「1小間」や全角数字などの表記揺れ対策）
    const quantity = parseInt(quantityStr.replace(/[^0-9]/g, ""), 10) || 0;

    // 金額計算ロジック
    let unitPrice = 0;
    if (boothType.indexOf("基礎小間") !== -1) {
      unitPrice = 60000;
    } else if (boothType.indexOf("土間貸し") !== -1) {
      unitPrice = 200000;
    }

    // 合計金額の算出
    const totalPrice = unitPrice * quantity;
    
    // カンマ区切りのフォーマットを適用
    const formattedTotalPrice = totalPrice.toLocaleString('ja-JP');

    // メールの件名
    const subject = "【自動配信】産業フェアしずおか2026 企業ゾーン 出展申込を受付いたしました";

    // メールの本文（確約表現を排除し、事実のみを記載する仕様）
    let body = "";
    body += `${companyName}\n御中\n\n`;
    body += "この度は「産業フェアしずおか2026」にお申し込みいただき、誠にありがとうございます。\n";
    body += "以下の内容にて出展申込を受付いたしました。\n\n";
    body += "--------------------------------------------------\n";
    body += "■ お申込内容の控え\n";
    body += `・会社・団体名 : ${companyName}\n`;
    body += `・出店タイプ   : ${boothType}\n`;
    body += `・申込数量     : ${quantity} 小間\n`;
    body += `・合計金額     : ${formattedTotalPrice} 円\n`;
    body += "--------------------------------------------------\n\n";
    body += "【重要なお知らせ】\n";
    body += "本メールは出展申込の受付完了（控え）をお知らせするものであり、出展の「正式な受理」ではございません。\n";
    body += "お送りいただいた内容を確認の上、正式な受理通知の発送をもって出展成立となります。\n\n";
    body += "※お申し込み送信後の内容変更は、フォームからは行えません。\n";
    body += "万が一入力内容に誤りがあり、修正を希望される場合は、お手数ですが運営事務局（sf-shizuoka2026@shizutetsu-ad.co.jp）までメールにて直接ご連絡ください。\n\n";
    body += "※本メールはシステムによる自動返信メールです。心当たりのない場合は破棄してください。\n\n";
    body += "==================================================\n";
    body += "産業フェアしずおか2026 運営事務局\n";
    body += "株式会社静鉄・アドパートナーズ\n";
    body += "==================================================\n";

    // 送信オプション（送信者名の指定）
    const options = {
      name: "産業フェアしずおか2026 運営事務局"
    };

    // メールを送信
    GmailApp.sendEmail(email, subject, body, options);
    Logger.log(`メール送信成功: ${email}宛 (合計金額: ${formattedTotalPrice}円)`);

  } catch (error) {
    Logger.log("エラーが発生しました: " + error.toString());
  }
}
