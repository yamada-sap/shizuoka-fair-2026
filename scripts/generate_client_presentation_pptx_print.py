"""
WEBプロモーション統合計画書 2026 ─ 印刷版（ミニマル白紙デザイン）
デザイン方針：
  - 背景：純白
  - 余白を広めに確保、詰め込みすぎない
  - 見出しは大きく左揃え。細い横線/左縦線アクセントのみ
  - 色は「1スライドに1色のみ」。帯やカードは最小限
  - 数値・重要キーワードは大きく太く見せる
  - ページ番号：右下に小さく
"""

import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# ─────────────────────────────────────────
# カラーパレット（シンプル・印刷安全）
# ─────────────────────────────────────────
BLACK    = RGBColor(20, 20, 20)       # ほぼ黒
NAVY     = RGBColor(21, 45, 82)       # ディープネイビー
BLUE     = RGBColor(37, 99, 169)      # アクセントブルー
AMBER    = RGBColor(166, 80, 0)       # ゴールドアンバー（印刷用）
GREEN    = RGBColor(4, 120, 87)       # エメラルドグリーン
RED      = RGBColor(175, 28, 28)      # ディープレッド
WHITE    = RGBColor(255, 255, 255)
GRAY1    = RGBColor(235, 237, 242)    # ごく薄グレー（罫線・背景）
GRAY2    = RGBColor(130, 140, 158)    # 補足テキスト用ミドルグレー
GRAY3    = RGBColor(90, 100, 118)     # やや暗いグレー

FONT = "Hiragino Sans"
blank = prs.slide_layouts[6]

# ─────────────────────────────────────────
# ユーティリティ
# ─────────────────────────────────────────
def line(slide, left, top, width, height, color=GRAY1, no_line=True):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    sh.fill.solid(); sh.fill.fore_color.rgb = color
    if no_line: sh.line.fill.background()
    else: sh.line.color.rgb = color
    return sh

def tb(slide, left, top, w, h):
    b = slide.shapes.add_textbox(left, top, w, h)
    b.text_frame.word_wrap = True
    return b.text_frame

def p(tf, text, size, bold=False, color=None, align=PP_ALIGN.LEFT,
      sp_before=0, sp_after=0, italic=False):
    if tf.paragraphs and tf.paragraphs[0].text == "":
        para = tf.paragraphs[0]
    else:
        para = tf.add_paragraph()
    para.text = text
    para.font.size = Pt(size)
    para.font.bold = bold
    para.font.italic = italic
    para.font.color.rgb = color or BLACK
    para.font.name = FONT
    para.alignment = align
    para.space_before = Pt(sp_before)
    para.space_after = Pt(sp_after)
    return para

def add_page_num(slide, num, accent_color=NAVY):
    """右下ページ番号（シンプル）"""
    f = tb(slide, Inches(12.5), Inches(7.1), Inches(0.7), Inches(0.32))
    p(f, str(num), 9.5, color=accent_color, align=PP_ALIGN.RIGHT)

def chap_header(slide, page_num, chap, title, subtitle=None, accent=NAVY):
    """
    ミニマルヘッダー：
      - 細い上部アクセントライン（左から width 13.333 全幅）
      - 章ラベル（小・グレー）
      - タイトル（大・黒・太）
      - サブタイトル（中・グレー）
      - 細い分割横線
    """
    # 上部カラーライン（3pt相当の細線）
    line(slide, 0, 0, Inches(13.333), Inches(0.06), accent)

    # 章ラベル
    f_ch = tb(slide, Inches(0.7), Inches(0.2), Inches(8.0), Inches(0.35))
    p(f_ch, chap, 10, bold=True, color=accent)

    # タイトル
    f_t = tb(slide, Inches(0.7), Inches(0.52), Inches(12.2), Inches(0.72))
    p(f_t, title, 22, bold=True, color=NAVY)

    # サブタイトル
    if subtitle:
        f_s = tb(slide, Inches(0.7), Inches(1.22), Inches(12.2), Inches(0.38))
        p(f_s, subtitle, 10.5, color=GRAY2)

    # 区切り横線（細・グレー）
    line(slide, Inches(0.7), Inches(1.6), Inches(12.0), Inches(0.018), GRAY1)

    add_page_num(slide, page_num, accent)


def section_label(slide, left, top, text, color=NAVY):
    """セクション小見出し（太・カラー・左線なし）"""
    f = tb(slide, left, top, Inches(11.0), Inches(0.4))
    p(f, text, 11, bold=True, color=color)

def divider(slide, left, top, width, color=GRAY1):
    line(slide, left, top, width, Inches(0.015), color)

def body_text(slide, left, top, width, height):
    f = tb(slide, left, top, width, height)
    return f


# ─────────────────────────────────────────
# Slide 01：表紙（左右分割型・説得力強化版）
# 左40%：ネイビー面（タイトルエリア）
# 右60%：白地（詳細情報エリア）
# ─────────────────────────────────────────
s1 = prs.slides.add_slide(blank)

# 左ネイビー面（左40%）
line(s1, 0, 0, Inches(5.3), Inches(7.5), NAVY)

# 左面：アンバーのアクセントライン（縦）
line(s1, Inches(5.3), 0, Inches(0.12), Inches(7.5), AMBER)

# 左面：プロジェクトカテゴリ
f1_cat = tb(s1, Inches(0.5), Inches(1.1), Inches(4.5), Inches(0.4))
p(f1_cat, "企画提案書  ｜  2026年9月", 10, color=RGBColor(155, 185, 225))

# 左面：タイトル（大きく）
f1_main = tb(s1, Inches(0.5), Inches(1.65), Inches(4.5), Inches(3.2))
p(f1_main, "WEB\nプロモーション\n統合計画書", 36, bold=True, color=WHITE)

# 左面：プロジェクト名（小・下部）
f1_proj = tb(s1, Inches(0.5), Inches(5.2), Inches(4.5), Inches(0.42))
p(f1_proj, "産業フェアしずおか 2026", 12, bold=True, color=AMBER)

# 右面：背景は白（デフォルト）
# 右面：上部のアクセント横線
line(s1, Inches(5.8), Inches(1.5), Inches(7.0), Inches(0.04), AMBER)

# 右面：キャッチコピー（大きめ）
f1_catch = tb(s1, Inches(5.8), Inches(1.7), Inches(7.0), Inches(1.4))
p(f1_catch, "テレビCM × WEB広告 × 地域メディアの\n相乗効果で来場を最大化", 16, bold=True, color=NAVY)

# 右面：区切り線
line(s1, Inches(5.8), Inches(3.25), Inches(7.0), Inches(0.02), GRAY1)

# 右面：開催情報（大きく・明確に）
f1_ev = tb(s1, Inches(5.8), Inches(3.5), Inches(7.0), Inches(1.6))
p(f1_ev, "開催日", 10, bold=True, color=GRAY2)
p(f1_ev, "2026年11月28日（土）・29日（日）", 17, bold=True, color=NAVY)
p(f1_ev, "会　場", 10, bold=True, color=GRAY2, sp_before=10)
p(f1_ev, "ツインメッセ静岡", 17, bold=True, color=NAVY)

# 右面：3つのキーポイント
line(s1, Inches(5.8), Inches(5.28), Inches(7.0), Inches(0.02), GRAY1)
f1_pts = tb(s1, Inches(5.8), Inches(5.45), Inches(7.0), Inches(1.52))
for kp, col in [
    ("デジタル総表示回数　　約 296.6 万回", NAVY),
    ("配信エリア　　　　　　静岡県内8市町限定", NAVY),
    ("地域インフルエンサー　2組（17万人以上）と連携", NAVY),
]:
    p(f1_pts, "・ " + kp, 11, color=col, sp_before=4)

# 右面：制作クレジット
f1_by = tb(s1, Inches(5.8), Inches(7.0), Inches(7.0), Inches(0.35))
p(f1_by, "企画・制作　静鉄アド・パートナーズ株式会社", 9, color=GRAY2)


# ─────────────────────────────────────────
# Slide 02：第1章 目的
# ─────────────────────────────────────────
s2 = prs.slides.add_slide(blank)
chap_header(s2, 2, "第1章", "本書の目的：なぜ今、WEBプロモーションが必要なのか",
            "生活スタイルの変化に対応し、テレビCMとスマホ動線を結んで来場意欲を確実な行動へ変える")

steps2 = [
    ("01", "時代の変化と生活スタイル",
     "現代の来場者（特に子育て世代）は、テレビCMで催事を知った後、必ずスマートフォンで出店者・見どころ・アクセスを検索します。日常のスマホ画面に情報が存在することが、来場決定の前提条件です。",
     NAVY),
    ("02", "テレビCMとWEBの相乗効果",
     "テレビCMは「県内全域へ開催とお祭り感を一気に広げる」役割。WEB広告は「日常のスマホ画面で何度も見かけ、関心を高める」役割。どちらか一方ではなく両輪で展開することで効果が最大化します。",
     BLUE),
    ("03", "「行こう！」を着火する後押し",
     "主催者からの一方的な宣伝だけでなく、普段から信頼されている身近な地域メディア（おちゃさん等）が紹介することで、「遠くの広告」から「今週末に行くべき身近なおすすめ」へと変わります。",
     AMBER),
]

col_x = [Inches(0.7), Inches(4.65), Inches(8.6)]
for idx, (num, title, body, col) in enumerate(steps2):
    cx = col_x[idx]
    # 番号アクセントライン（細い縦線）
    line(s2, cx, Inches(1.75), Inches(0.04), Inches(3.8), col)
    # 番号
    f_n = tb(s2, cx + Inches(0.15), Inches(1.75), Inches(3.7), Inches(0.55))
    p(f_n, num, 26, bold=True, color=col)
    # タイトル
    f_t = tb(s2, cx + Inches(0.15), Inches(2.35), Inches(3.7), Inches(0.52))
    p(f_t, title, 13, bold=True, color=NAVY)
    # 区切り線
    divider(s2, cx + Inches(0.15), Inches(2.9), Inches(3.5))
    # 本文
    f_b = tb(s2, cx + Inches(0.15), Inches(3.0), Inches(3.65), Inches(2.6))
    p(f_b, body, 10.5, color=GRAY3)

# 結論
line(s2, 0, Inches(6.75), Inches(13.333), Inches(0.75), NAVY)
f_cl = tb(s2, Inches(0.9), Inches(6.82), Inches(12.0), Inches(0.62))
p(f_cl, "結論：テレビCMで「認知」を獲得し、WEB広告と地域メディアがスマホ上で「来場の決定打」を与えます。",
  12, bold=True, color=WHITE)


# ─────────────────────────────────────────
# Slide 03：第2章 全体像・役割分担
# ─────────────────────────────────────────
s3 = prs.slides.add_slide(blank)
chap_header(s3, 3, "第2章", "全体プロモーションの全体像と役割分担",
            "テレビCM・WEB広告・地域メディアの相乗効果。合計約296.6万回の確実なお届け")

# 左：表（媒体一覧）
tbl3_s = s3.shapes.add_table(5, 3, Inches(0.7), Inches(1.72), Inches(8.1), Inches(3.95))
tbl3 = tbl3_s.table
tbl3.columns[0].width = Inches(2.0)
tbl3.columns[1].width = Inches(4.7)
tbl3.columns[2].width = Inches(1.4)

for ci, h in enumerate(["媒体名", "主な役割と特徴", "表示見込み"]):
    cell = tbl3.cell(0, ci)
    cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
    pp = cell.text_frame.paragraphs[0]
    pp.text = h; pp.font.size = Pt(10.5); pp.font.bold = True
    pp.font.color.rgb = WHITE; pp.font.name = FONT; pp.alignment = PP_ALIGN.CENTER

rows3 = [
    ("テレビCM\n（マス媒体）", "県内全域のリビングへ開催とお祭り感を一気に浸透", "県内放送"),
    ("Google広告\n（WEBバナー）", "ニュースやYouTube等、日常ネット閲覧時の確実な刷り込み", "約142.9万回"),
    ("Yahoo!・LINE広告\n（スマホ通知）", "県民大半の日常アプリ（LINEトーク最上部等）での接触", "約125.0万回"),
    ("Instagram広告\n（SNS広告）", "子育て世代へ写真・カルーセル・人気投稿で直感訴求", "約28.8万回"),
]
row_bgs = [GRAY1, WHITE, GRAY1, WHITE]
for ri, (r0, r1, r2) in enumerate(rows3):
    bg = row_bgs[ri]
    for ci, val in enumerate([r0, r1, r2]):
        cell = tbl3.cell(ri + 1, ci)
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        pp = cell.text_frame.paragraphs[0]
        pp.text = val; pp.font.size = Pt(10); pp.font.name = FONT
        if ci in [0, 2]: pp.alignment = PP_ALIGN.CENTER; pp.font.bold = True

# 右：大きな数値ハイライト＋バーチャート
f3_big = tb(s3, Inches(9.1), Inches(1.72), Inches(3.8), Inches(0.38))
p(f3_big, "デジタル広告　総表示回数", 10, bold=True, color=GRAY2)
f3_num = tb(s3, Inches(9.1), Inches(2.08), Inches(3.8), Inches(0.72))
p(f3_num, "296.6 万回", 34, bold=True, color=AMBER)
line(s3, Inches(9.1), Inches(2.88), Inches(3.8), Inches(0.02), GRAY1)

# バーチャート（3媒体の比率を視覚化）
BAR_MAX = Inches(3.5)  # 100%の幅
bar_items = [
    ("Google広告",      142.9, 296.6, NAVY,   "約142.9万回  48%"),
    ("Yahoo!/LINE広告", 125.0, 296.6, BLUE,   "約125.0万回  42%"),
    ("Instagram広告",    28.8, 296.6, AMBER,  "約28.8万回   10%"),
]
by = Inches(3.05)
for b_label, b_val, b_total, b_col, b_txt in bar_items:
    # ラベル
    f_bl = tb(s3, Inches(9.1), by, Inches(3.8), Inches(0.28))
    p(f_bl, b_label, 8.5, bold=True, color=GRAY3)
    # バー背景（薄グレー）
    line(s3, Inches(9.1), by + Inches(0.3), BAR_MAX, Inches(0.22), GRAY1)
    # バー本体
    bar_w = BAR_MAX * (b_val / b_total)
    line(s3, Inches(9.1), by + Inches(0.3), bar_w, Inches(0.22), b_col)
    # 数値テキスト
    f_bv = tb(s3, Inches(9.1), by + Inches(0.54), Inches(3.8), Inches(0.26))
    p(f_bv, b_txt, 8, color=GRAY2)
    by += Inches(1.05)

# 下部：補足
line(s3, Inches(0.7), Inches(5.82), Inches(3.0), Inches(0.03), BLUE)
f3_bot = tb(s3, Inches(0.7), Inches(6.0), Inches(12.0), Inches(1.15))
p(f3_bot, "媒体別の相乗効果ポイント", 11, bold=True, color=NAVY)
p(f3_bot, "・ LINE/Yahoo!で全世代の日常動線を網羅し、Googleで興味関心層を捕捉。", 10.5, color=GRAY3)
p(f3_bot, "・ Instagramでは子育てファミリーへ写真・動画で共感を呼び起こし、3媒体が相互に補完し合います。", 10.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 04：第2章 4層連携フロー
# ─────────────────────────────────────────
s4 = prs.slides.add_slide(blank)
chap_header(s4, 4, "第2章", "4層連携ストーリー：来場者の心を動かすステップ",
            "4つの媒体が1本の導線として連携し、県民の「認知」を「当日の来場」へ確実に導く")

flow4 = [
    ("第1層", "テレビCM", "【全体認知・お祭り感】\n「産業フェアが今年も開催されるぞ！」\n県内全域へ広く開催を浸透", NAVY),
    ("第2層", "WEB広告", "【日常の刷り込み】\n「あ、ネットでもLINEでも見かけるな」\n8市町へ約268万回表示", BLUE),
    ("第3層", "地域メディア", "【信頼・熱量の着火】\n「普段見てるおちゃさんも紹介！行こう！」\n身近なおすすめで来場決定", AMBER),
    ("第4層", "公式リール", "【詳細確認・出店PR】\n「この体験をしよう！駐車場はここね！」\n目的を持って当日来場", GREEN),
]

box_y = Inches(1.75)
for idx, (layer, name, desc, col) in enumerate(flow4):
    cx = Inches(0.7) + idx * Inches(3.0)
    # 上部縦アクセントライン
    line(s4, cx, box_y, Inches(0.045), Inches(4.65), col)
    # 層ラベル
    f_lyr = tb(s4, cx + Inches(0.15), box_y + Inches(0.05), Inches(2.7), Inches(0.38))
    p(f_lyr, layer, 9.5, bold=True, color=col)
    # 媒体名
    f_nm = tb(s4, cx + Inches(0.15), box_y + Inches(0.45), Inches(2.7), Inches(0.52))
    p(f_nm, name, 17, bold=True, color=NAVY)
    # 区切り線
    divider(s4, cx + Inches(0.15), box_y + Inches(1.0), Inches(2.65))
    # 説明
    f_d = tb(s4, cx + Inches(0.15), box_y + Inches(1.15), Inches(2.75), Inches(3.0))
    p(f_d, desc, 10.5, color=GRAY3)

    # 矢印シェイプ（実際のShape）
    if idx < 3:
        arr = s4.shapes.add_shape(
            MSO_SHAPE.RIGHT_ARROW,
            cx + Inches(2.87), box_y + Inches(2.05),
            Inches(0.2), Inches(0.42)
        )
        arr.fill.solid(); arr.fill.fore_color.rgb = GRAY1
        arr.line.fill.background()

# 結論バナー
line(s4, 0, Inches(6.62), Inches(13.333), Inches(0.88), NAVY)
f_cl4 = tb(s4, Inches(0.9), Inches(6.7), Inches(12.0), Inches(0.72))
p(f_cl4, "ゴール：テレビCMで「知っている」状態を作り、WEB広告と地域メディアが「行く！」という決定打を与え、満員でのご来場を実現します。",
  12, bold=True, color=WHITE)


# ─────────────────────────────────────────
# Slide 05：第3章 ターゲット層
# ─────────────────────────────────────────
s5 = prs.slides.add_slide(blank)
chap_header(s5, 5, "第3章", "ターゲット層（お届けする対象）の設定",
            "子育て世代を最重要ターゲットに設定し、3つの魅力的な要素をダイレクトに訴求")

# 左カラム：ターゲット2層
line(s5, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.25), NAVY)
f5_lt = tb(s5, Inches(0.9), Inches(1.75), Inches(5.3), Inches(0.45))
p(f5_lt, "ターゲット層の2層構造", 13, bold=True, color=NAVY)

divider(s5, Inches(0.9), Inches(2.25), Inches(5.3))

# 最重点
f5_b1 = tb(s5, Inches(0.9), Inches(2.38), Inches(5.3), Inches(0.38))
p(f5_b1, "最重点　子育て世代（25〜45歳）", 11, bold=True, color=BLUE)
f5_m = tb(s5, Inches(0.9), Inches(2.82), Inches(5.3), Inches(1.2))
for t in ["・ 週末に家族みんなで楽しめるお出かけ先・体験先を探している層",
          "・ 日常的にInstagramやLINEを最も活用している世代"]:
    p(f5_m, t, 10.5, color=GRAY3)

divider(s5, Inches(0.9), Inches(4.18), Inches(5.3))

# 準重点
f5_b2 = tb(s5, Inches(0.9), Inches(4.3), Inches(5.3), Inches(0.38))
p(f5_b2, "準重点　一般・シニア層", 11, bold=True, color=AMBER)
f5_s = tb(s5, Inches(0.9), Inches(4.74), Inches(5.3), Inches(1.2))
for t in ["・ 地元特産品、静岡グルメ、伝統工芸、ものづくりに関心のある層",
          "・ Yahoo!ニュースやLINEを通じて確実にアプローチ"]:
    p(f5_s, t, 10.5, color=GRAY3)

# 右カラム：3大魅力要素
line(s5, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.25), AMBER)
f5_rt = tb(s5, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.45))
p(f5_rt, "ターゲットへ届ける3大魅力要素", 13, bold=True, color=NAVY)

el5 = [
    ("要素 01", "子どもの笑顔・特別な体験",
     "木工体験、キッズワークショップ、サンリオステージ、よしもとお笑いなど、子どもが主役になって楽しめる催事を前面に案内します。", BLUE),
    ("要素 02", "美味しい地元グルメ・物産",
     "静岡ならではの名物グルメや普段なかなか出会えない名店が集まるワクワク感を写真・ショート動画で訴求します。", AMBER),
    ("要素 03", "家族で安心の屋内・快適空間",
     "雨でも快適な全天候型屋内会場、入場無料、充実の付帯設備など、子連れ来場の安心感を担保します。", GREEN),
]
y_el = Inches(2.28)
for tag, title, desc, col in el5:
    f_tag = tb(s5, Inches(6.9), y_el, Inches(6.0), Inches(0.3))
    p(f_tag, tag, 9.5, bold=True, color=col)
    f_t = tb(s5, Inches(6.9), y_el + Inches(0.3), Inches(6.0), Inches(0.38))
    p(f_t, title, 12.5, bold=True, color=NAVY)
    f_d = tb(s5, Inches(6.9), y_el + Inches(0.7), Inches(6.0), Inches(0.6))
    p(f_d, desc, 9.5, color=GRAY3)
    divider(s5, Inches(6.9), y_el + Inches(1.38), Inches(6.0))
    y_el += Inches(1.58)


# ─────────────────────────────────────────
# Slide 06：第4章 配信エリア
# ─────────────────────────────────────────
s6 = prs.slides.add_slide(blank)
chap_header(s6, 6, "第4章", "配信エリアの厳格な設定（静岡県内8市町限定）",
            "ツインメッセ静岡へアクセス可能な地域に絞り込み、広告予算の無駄遣いを徹底的に排除")

# 左：8市町タグ
line(s6, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.2), BLUE)
f6_lt = tb(s6, Inches(0.9), Inches(1.75), Inches(5.3), Inches(0.45))
p(f6_lt, "配信対象エリア（県内8市町）", 13, bold=True, color=NAVY)
f6_ls = tb(s6, Inches(0.9), Inches(2.28), Inches(5.3), Inches(0.38))
p(f6_ls, "ツインメッセ静岡へ車・交通機関で1時間圏内の世帯に集中配信", 9.5, color=GRAY2)

cities = ["静岡市", "焼津市", "藤枝市", "富士市", "島田市", "吉田町", "牧之原市", "富士宮市"]
for idx, city in enumerate(cities):
    ci = idx % 2; ri = idx // 2
    cx = Inches(0.9) + ci * Inches(2.65)
    cy = Inches(2.8) + ri * Inches(0.58)
    # 細い左線のみ
    line(s6, cx, cy + Inches(0.05), Inches(0.04), Inches(0.38), BLUE)
    fc = tb(s6, cx + Inches(0.12), cy, Inches(2.4), Inches(0.48))
    p(fc, city, 12, bold=True, color=NAVY)

f6_loc = tb(s6, Inches(0.9), Inches(5.22), Inches(5.3), Inches(1.5))
p(f6_loc, "位置情報技術によるロック配信", 11, bold=True, color=AMBER)
p(f6_loc, "「旅行等で通過しただけの人」を自動除外し、「現在地に居住または滞在している人」に限定配信。県外への誤配信を100%防止します。",
  9.5, color=GRAY3, sp_before=4)

# 右：3大メリット
line(s6, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.2), AMBER)
f6_rt = tb(s6, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.45))
p(f6_rt, "エリア厳格指定の3大メリット", 13, bold=True, color=NAVY)

ben6 = [
    ("メリット 01", "広告予算の無駄遣いを完全排除",
     "来場が難しい遠方の地域へ配信せず、来場確率が極めて高い近隣世帯へ予算を100%集中投下。", BLUE),
    ("メリット 02", "ターゲットへの接触頻度を高める",
     "限られた対象層へ期間中に何度も繰り返し表示されるため、「気になり度」を着実に高めます。", AMBER),
    ("メリット 03", "「私たちの街の催事」という地元感",
     "「静岡市で開催される身近なイベント」として受け入れられ、家族での参加障壁を劇的に下げます。", GREEN),
]
y_b6 = Inches(2.28)
for tag, title, desc, col in ben6:
    f_tag = tb(s6, Inches(6.9), y_b6, Inches(6.0), Inches(0.3))
    p(f_tag, tag, 9.5, bold=True, color=col)
    f_t = tb(s6, Inches(6.9), y_b6 + Inches(0.3), Inches(6.0), Inches(0.38))
    p(f_t, title, 12.5, bold=True, color=NAVY)
    f_d = tb(s6, Inches(6.9), y_b6 + Inches(0.7), Inches(6.0), Inches(0.58))
    p(f_d, desc, 9.5, color=GRAY3)
    divider(s6, Inches(6.9), y_b6 + Inches(1.35), Inches(6.0))
    y_b6 += Inches(1.55)


# ─────────────────────────────────────────
# Slide 07：第5章① 全体タイムライン
# ─────────────────────────────────────────
s7 = prs.slides.add_slide(blank)
chap_header(s7, 7, "第5章 ①", "Instagramプロモーション全体タイムライン",
            "公式アカウント（全10回）と地域メディア（計3回）を連動させ、途切れなく来場意欲を高める")

tbl7_s = s7.shapes.add_table(11, 5, Inches(0.7), Inches(1.72), Inches(12.22), Inches(5.0))
tbl7 = tbl7_s.table
tbl7.columns[0].width = Inches(1.9)
tbl7.columns[1].width = Inches(1.55)
tbl7.columns[2].width = Inches(3.35)
tbl7.columns[3].width = Inches(1.85)
tbl7.columns[4].width = Inches(3.57)

for ci, h in enumerate(["日程・時期", "区分", "投稿内容・アクション", "形式", "狙い・掲載の工夫"]):
    cell = tbl7.cell(0, ci)
    cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
    pp = cell.text_frame.paragraphs[0]
    pp.text = h; pp.font.size = Pt(10.5); pp.font.bold = True
    pp.font.color.rgb = WHITE; pp.font.name = FONT; pp.alignment = PP_ALIGN.CENTER

t7_rows = [
    ("〜 10/23（金）", "【素材締切】", "出店者様　動画素材の回収", "─", "専用フォームにて動画・情報を提出いただく期日"),
    ("10/25（日）", "公式 01", "イベント全体概要", "画像（フィード）", "【公式HP更新連動】プロフィール先頭固定"),
    ("10月下旬〜11月中旬", "公式 02〜06", "出店者様ご紹介（計5本・最大15社）", "動画（リール）", "週1〜2本ペース順次公開。おちゃ様と共同投稿"),
    ("11/15（日）", "メディア 01", "静岡県コンシェルジュ（おちゃさん）", "画像＋ストーリーズ", "【開催2週間前】見どころ紹介・週末の予定に保存"),
    ("11/24（火）", "メディア 02", "静岡県コンシェルジュ（おちゃさん）", "動画＋ストーリーズ", "【直前決定打】体験やグルメの魅力をショート動画発信"),
    ("11/24（火）", "メディア 03", "静岡県ニュース速報", "動画＋ストーリーズ", "【直前速報】地域のビッグイベントとして速報拡散"),
    ("11/27（金）", "公式 07", "前日・直前告知", "画像（フィード）", "【出展者搬入日・夕方】「いよいよ明日開催！」案内"),
    ("11/28（土）", "公式 08", "当日リアルタイム発信（1日目）", "ストーリーズ/写真", "オープニング・会場の賑わい・熱気をリアルタイム発信"),
    ("11/29（日）", "公式 09", "当日リアルタイム発信（2日目）", "ストーリーズ/写真", "「本日最終日！」呼びかけとステージの熱気をお届け"),
    ("12/2（水）", "公式 10", "開催報告・振り返り", "画像（フィード）", "盛況御礼・出店者の実績PRと次回開催へ繋げる"),
]

media_bg  = RGBColor(255, 249, 231)
締切_bg   = RGBColor(255, 237, 237)
for ri, rd in enumerate(t7_rows, start=1):
    if "メディア" in rd[1]:   bg = media_bg
    elif "素材" in rd[1]:     bg = 締切_bg
    elif ri % 2 == 1:         bg = GRAY1
    else:                     bg = WHITE
    for ci, val in enumerate(rd):
        cell = tbl7.cell(ri, ci)
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        pp = cell.text_frame.paragraphs[0]
        pp.text = val; pp.font.size = Pt(9.5); pp.font.name = FONT
        if ci in [0, 1, 3]: pp.alignment = PP_ALIGN.CENTER
        if ci == 1:
            pp.font.bold = True
            if "メディア" in val: pp.font.color.rgb = AMBER
            elif "素材" in val:   pp.font.color.rgb = RED

f7_n = tb(s7, Inches(0.7), Inches(6.85), Inches(12.22), Inches(0.38))
p(f7_n, "※発信するすべての投稿は、事前に内容（画像・動画・テキスト）をご確認・承認いただいた上で公開いたします。",
  9.5, bold=True, color=GRAY2)


# ─────────────────────────────────────────
# Slide 08：第5章② 公式10回構成
# ─────────────────────────────────────────
s8 = prs.slides.add_slide(blank)
chap_header(s8, 8, "第5章 ②", "公式Instagram（基本10回）の投稿スケジュール構成",
            "公式アカウント（@sangyofair_shizuoka）から計画的に全10回の発信を実施")

s8_cards = [
    ("01　全体概要案内（1本）", "10月25日(日) 公開予定", [
        "公式ホームページの情報更新タイミングに合わせて公開",
        "開催日時、ツインメッセ静岡、見どころを分かりやすく案内",
        "アカウントのプロフィール先頭に固定し常時閲覧可能に",
    ], BLUE),
    ("02　出店者紹介（5本）", "10月下旬〜11月中旬", [
        "1本のショート動画（リール）に2〜3社をテーマ別にまとめ紹介",
        "全5本の投稿で合計「最大15社」をテンポよくご紹介",
        "動画素材を提供いただいた出店者様から順次PR（不公平感解消）",
        "静岡県コンシェルジュ（おちゃ様）と共同投稿で露出爆発",
    ], AMBER),
    ("03　直前・当日・事後（4本）", "11月27日〜12月2日", [
        "前日告知（11/27 金）：搬入風景と「明日開催！」の直前案内",
        "当日速報（11/28 土・29 日）：熱気・混雑・ステージ速報（計2本）",
        "開催報告（12/2 水）：盛況御礼・出店者の実績PRと次回へ繋げる",
    ], NAVY),
]

for idx, (ct, cs, items, col) in enumerate(s8_cards):
    cx = Inches(0.7) + idx * Inches(3.97)
    line(s8, cx, Inches(1.75), Inches(0.045), Inches(5.0), col)
    f_badge = tb(s8, cx + Inches(0.15), Inches(1.75), Inches(3.65), Inches(0.38))
    p(f_badge, ct, 11, bold=True, color=col)
    f_d = tb(s8, cx + Inches(0.15), Inches(2.18), Inches(3.65), Inches(0.38))
    p(f_d, f"【時期：{cs}】", 10, bold=True, color=GRAY2)
    divider(s8, cx + Inches(0.15), Inches(2.6), Inches(3.65))
    f_items = tb(s8, cx + Inches(0.15), Inches(2.75), Inches(3.72), Inches(3.8))
    for it in items:
        p(f_items, "・ " + it, 10.5, color=GRAY3, sp_before=4)


# ─────────────────────────────────────────
# Slide 09：第5章③ デザインの工夫
# ─────────────────────────────────────────
s9 = prs.slides.add_slide(blank)
chap_header(s9, 9, "第5章 ③", "忙しいママ・パパでも伝わりやすいデザインの工夫（検討案）",
            "片手操作の子育て世代に配慮した視認性重視のデザイン設計（柔軟にご相談・調整）")

s9_cards = [
    ("工夫 01", "視認性の重視（1投稿＝1要点）",
     "スマートフォンを片手で見ている子育て世代を意識し、1つの投稿に情報を詰め込みすぎず、「何が魅力か」「いつ開催か」の要点を絞って伝えます。"),
    ("工夫 02", "写真の邪魔をしない文字配置",
     "写真や動画の魅力を引き立てつつ、パッと目に飛び込んでくる読みやすい日本語フォントと配色を採用。忙しい合間でも瞬時に理解できます。"),
    ("工夫 03", "ハッシュタグ活用と口コミ連鎖",
     "「#産業フェアしずおか2026」「#静岡子連れお出かけ」などを投稿内で案内。来場者が当日の様子を投稿しやすくなり、口コミ拡散を後押しします。"),
]

for idx, (dt, dsub, dbody) in enumerate(s9_cards):
    cx = Inches(0.7) + idx * Inches(3.97)
    line(s9, cx, Inches(1.75), Inches(0.045), Inches(4.0), BLUE)
    f_tag = tb(s9, cx + Inches(0.15), Inches(1.78), Inches(3.65), Inches(0.35))
    p(f_tag, dt, 9.5, bold=True, color=BLUE)
    f_t = tb(s9, cx + Inches(0.15), Inches(2.2), Inches(3.65), Inches(0.5))
    p(f_t, dsub, 13, bold=True, color=NAVY)
    divider(s9, cx + Inches(0.15), Inches(2.75), Inches(3.65))
    f_b = tb(s9, cx + Inches(0.15), Inches(2.9), Inches(3.72), Inches(2.55))
    p(f_b, dbody, 10.5, color=GRAY3)

line(s9, Inches(0.7), Inches(6.35), Inches(12.22), Inches(0.015), GRAY1)
f9_n = tb(s9, Inches(0.7), Inches(6.45), Inches(12.22), Inches(0.72))
p(f9_n, "※具体的なデザインや見せ方は確定事項ではなく、主催者様のご意向や各ブースの実際の写真素材に合わせて柔軟にご相談・調整いたします。",
  10.5, bold=True, color=NAVY)


# ─────────────────────────────────────────
# Slide 10：第6章① ウィンザー効果・三者関係
# ─────────────────────────────────────────
s10 = prs.slides.add_slide(blank)
chap_header(s10, 10, "第6章 ①", "インフルエンサー起用の心理的根拠（ウィンザー効果と三者関係）",
            "なぜ主催者の直接発信だけでなく、地域インフルエンサーとの「共同投稿」が必要なのか？", accent=AMBER)

# 左：ウィンザー効果
line(s10, Inches(0.7), Inches(1.75), Inches(0.045), Inches(4.82), AMBER)
f10_lt = tb(s10, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f10_lt, "行動心理：ウィンザー効果の活用", 12.5, bold=True, color=AMBER)

# 比較（シンプル横線区切り）
f10_ng_l = tb(s10, Inches(0.9), Inches(2.28), Inches(5.5), Inches(0.35))
p(f10_ng_l, "▼ 自社・主催者からの直接発信（広告離れ）", 10.5, bold=True, color=RED)
f10_ng_b = tb(s10, Inches(0.9), Inches(2.68), Inches(5.5), Inches(0.7))
p(f10_ng_b, "「自分たちの催事は楽しいですよ」という企業広告は、警戒され流されやすい傾向にあります。",
  9.5, color=GRAY3)

divider(s10, Inches(0.9), Inches(3.45), Inches(5.5), GRAY1)

f10_ok_l = tb(s10, Inches(0.9), Inches(3.58), Inches(5.5), Inches(0.35))
p(f10_ok_l, "▲ 地域メディアを介した第三者発信（ウィンザー効果）", 10.5, bold=True, color=GREEN)
f10_ok_b = tb(s10, Inches(0.9), Inches(3.98), Inches(5.5), Inches(1.15))
p(f10_ok_b, "普段から信頼しているお出かけの達人が薦めることで、「遠くの企業広告」から「身近で信頼できる推奨品」へと昇華し、抜群の共感と納得を生みます。",
  9.5, color=GRAY3)

# 右：三者関係
line(s10, Inches(6.7), Inches(1.75), Inches(0.045), Inches(4.82), AMBER)
f10_rt = tb(s10, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f10_rt, "三者関係構造：自然な拡散の循環", 12.5, bold=True, color=AMBER)

boxes10 = [
    ("① 主催者・出店企業（産業フェアしずおか）",
     "魅力的な体験・出店者素材・安心の公式情報を準備・提供", NAVY),
    ("② 地域メディア（おちゃさん ＆ 静岡県ニュース速報）",
     "普段通りの切り口で生活者へ紹介（共同投稿で17万人以上へ配信）", BLUE),
    ("③ 生活者（一般ファミリー・県民） ➔ 来場・UGC拡散",
     "「身近なおすすめ」として受け入れ、来場後に自らSNS投稿（好循環）", GREEN),
]
y10 = Inches(2.28)
for b1, b2, col in boxes10:
    line(s10, Inches(6.9), y10 + Inches(0.05), Inches(0.04), Inches(0.8), col)
    f_b1 = tb(s10, Inches(7.08), y10, Inches(5.8), Inches(0.38))
    p(f_b1, b1, 11, bold=True, color=col)
    f_b2 = tb(s10, Inches(7.08), y10 + Inches(0.38), Inches(5.8), Inches(0.5))
    p(f_b2, b2, 9.5, color=GRAY3)
    divider(s10, Inches(7.08), y10 + Inches(0.95), Inches(5.8))
    y10 += Inches(1.2)

# バナー
line(s10, 0, Inches(6.62), Inches(13.333), Inches(0.88), NAVY)
f10_bot = tb(s10, Inches(0.9), Inches(6.7), Inches(12.0), Inches(0.72))
p(f10_bot, "キーポイント：主催者の一方通行発信から、共感と信頼を獲得する協調型プロモーションへ",
  12, bold=True, color=WHITE)


# ─────────────────────────────────────────
# Slide 11：第6章②③ インサイトデータ
# ─────────────────────────────────────────
s11 = prs.slides.add_slide(blank)
chap_header(s11, 11, "第6章 ②③", "起用メディア2組の選定理由 ＆ 詳細インサイトデータ",
            "「なぜこの2組なのか？」県内最大級の圧倒的リーチ力と客観的実績数値", accent=AMBER)

# 左：おちゃさん
line(s11, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.0), AMBER)
f11_lt = tb(s11, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.38))
p(f11_lt, "メディア 01　静岡県コンシェルジュ（おちゃ さん）", 11.5, bold=True, color=AMBER)
f11_lh = tb(s11, Inches(0.9), Inches(2.15), Inches(5.5), Inches(0.35))
p(f11_lh, "@shizuoka_info", 9.5, color=GRAY2)

# 数値3つ（ラベル + 大きな値 + 視覚バー）
STAT_MAX = Inches(5.2)  # バー全幅
stat11L = [
    ("フォロワー数",  "17.3万人",    173000, 173000),
    ("平均閲覧数",   "約200,000回", 200000, 200000),
    ("平均リーチ数", "約70,000件",   70000, 200000),
]
sy = Inches(2.55)
for lbl, val_str, val_num, bar_max_num in stat11L:
    f_lbl = tb(s11, Inches(0.9), sy, STAT_MAX, Inches(0.28))
    p(f_lbl, lbl, 8.5, color=GRAY2)
    f_val = tb(s11, Inches(0.9), sy + Inches(0.28), STAT_MAX, Inches(0.42))
    p(f_val, val_str, 15, bold=True, color=AMBER)
    # バー背景
    line(s11, Inches(0.9), sy + Inches(0.72), STAT_MAX, Inches(0.16), GRAY1)
    # バー本体（173000を100%として比率計算）
    bar_w = STAT_MAX * min(val_num / 200000, 1.0)
    line(s11, Inches(0.9), sy + Inches(0.72), bar_w, Inches(0.16), AMBER)
    sy += Inches(1.02)

divider(s11, Inches(0.9), sy, Inches(5.5))

f11_ld = tb(s11, Inches(0.9), sy + Inches(0.12), Inches(5.5), Inches(1.8))
for t in [
    "フォロワー属性：女性 54% / 男性 46%（子育て世代・主婦層中心）",
    "主要年齢層：18歳〜44歳（ファミリーお出かけ層が集中）",
    "得意エリア：静岡市 23%、浜松市 10%、富士市 8%（全県をカバー）",
    "アカウント価値：県民の「週末お出かけインフラ」。来場転換力が桁違い。",
]:
    p(f11_ld, "・ " + t, 9.5, color=GRAY3, sp_before=3)

# 右：ニュース速報
line(s11, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.0), BLUE)
f11_rt = tb(s11, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.38))
p(f11_rt, "メディア 02　静岡県ニュース速報", 11.5, bold=True, color=BLUE)
f11_rh = tb(s11, Inches(6.9), Inches(2.15), Inches(6.0), Inches(0.35))
p(f11_rh, "@shizuoka_news_ai", 9.5, color=GRAY2)

# ニュース速報の数値＋視覚バー（おちゃさんとの比較で小さいことが一目でわかる）
STAT_MAXR = Inches(5.8)
stat11R = [
    ("フォロワー数",  "約4,000人",   4000, 173000),
    ("平均閲覧数",   "約10,000回", 10000, 200000),
    ("平均リーチ数", "約5,000件",   5000, 200000),
]
sy2 = Inches(2.55)
for lbl, val_str, val_num, bar_max_num in stat11R:
    f_lbl = tb(s11, Inches(6.9), sy2, STAT_MAXR, Inches(0.28))
    p(f_lbl, lbl, 8.5, color=GRAY2)
    f_val = tb(s11, Inches(6.9), sy2 + Inches(0.28), STAT_MAXR, Inches(0.42))
    p(f_val, val_str, 15, bold=True, color=BLUE)
    # バー背景
    line(s11, Inches(6.9), sy2 + Inches(0.72), STAT_MAXR, Inches(0.16), GRAY1)
    # バー本体（200000を100%として比率計算）
    bar_w2 = STAT_MAXR * min(val_num / 200000, 1.0)
    line(s11, Inches(6.9), sy2 + Inches(0.72), bar_w2, Inches(0.16), BLUE)
    sy2 += Inches(1.02)

divider(s11, Inches(6.9), sy2, Inches(5.8))

f11_rd = tb(s11, Inches(6.9), sy2 + Inches(0.12), Inches(6.0), Inches(1.8))
for t in [
    "フォロワー属性：男性 60% / 女性 40%（現役世代・ビジネス層）",
    "主要年齢層：25歳〜54歳（情報感度の高い現役県民層）",
    "得意エリア：静岡市 20%、浜松市 15%（都市部中心に急成長）",
    "「【速報】産業フェア開催！」というニュース形式で、普段お出かけ情報を見ない層も強力に誘引。",
]:
    p(f11_rd, "・ " + t, 9.5, color=GRAY3, sp_before=3)

# 合計成果バナー
line(s11, 0, Inches(6.88), Inches(13.333), Inches(0.62), AMBER)
f11_tot = tb(s11, Inches(0.9), Inches(6.93), Inches(12.0), Inches(0.52))
p(f11_tot, "【2組連携の想定合計波及効果】　想定閲覧数：約300,000回以上　｜　想定獲得リーチ数：約110,000アカウント",
  12.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────
# Slide 12：第6章④ タッグ効果・確定投稿計画
# ─────────────────────────────────────────
s12 = prs.slides.add_slide(blank)
chap_header(s12, 12, "第6章 ④", "2組のタッグ効果 ＆ 確定投稿計画（合計3回）",
            "「体験の深掘り」×「ニュース速報」の完全補完で、県民全域へ抜け漏れなく届く布陣が完成", accent=AMBER)

line(s12, Inches(0.7), Inches(1.75), Inches(0.045), Inches(4.82), AMBER)
f12_lt = tb(s12, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f12_lt, "この2組のタッグでしかできないこと", 13, bold=True, color=NAVY)

f12_l = tb(s12, Inches(0.9), Inches(2.28), Inches(5.5), Inches(4.3))
for st, sd, col in [
    ("体験の深掘り × ニュース速報の完全補完", "おちゃさんが「体験・感情（楽しそう！行きたい！）」を刺激し、静岡県ニュース速報が「話題性・速報性（今週末こんなイベントが！）」で注意を引きます。", AMBER),
    ("ファミリー層 ＆ 幅広い県民層の両取り", "「週末の家族お出かけ先を探す子育て世帯」と「地域の身近な話題を追う幅広い県民層」の双方に確実に届く完璧な布陣となります。", BLUE),
    ("共同投稿による既存枠の超越", "公式アカウント単独のフォロワー数に留まらず、おちゃさんの持つ17万人以上の読者画面へも直接届きます。", NAVY),
]:
    p(f12_l, "・ " + st, 11, bold=True, color=col, sp_before=10)
    p(f12_l, sd, 9.5, color=GRAY3)

line(s12, Inches(6.7), Inches(1.75), Inches(0.045), Inches(4.82), AMBER)
f12_rt = tb(s12, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f12_rt, "起用メディア2組の確定投稿内容", 13, bold=True, color=NAVY)

m_posts = [
    ("おちゃさん 第1回", "11月15日（日）", "写真フィード ＋ ストーリーズ", "【開催約2週間前の認知拡大】\n会場の見どころをまとめ、お出かけ候補として保存促進。", AMBER),
    ("おちゃさん 第2回", "11月24日（火）", "動画リール ＋ ストーリーズ", "【直前の来場決定打】\n体験やグルメの魅力をショート動画で発信。「今週末行こう！」と後押し。", AMBER),
    ("静岡県ニュース速報", "11月24日（火）", "動画リール ＋ ストーリーズ", "【直前の速報】\n産業フェアの概要・見どころをニュース速報リールで紹介。地域の話題として拡散。", BLUE),
]
f12_r = tb(s12, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for m_name, m_date, m_fmt, m_desc, col in m_posts:
    p(f12_r, f"    {m_name}　実施日：{m_date}", 11, bold=True, color=col, sp_before=10)
    p(f12_r, f"    形式：{m_fmt}", 9.5, color=GRAY2)
    p(f12_r, m_desc, 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 13：第6章⑤ 事前審査体制
# ─────────────────────────────────────────
s13 = prs.slides.add_slide(blank)
chap_header(s13, 13, "第6章 ⑤", "担当者が安心できる「安全・確実な事前審査体制」",
            "公的催事としての信頼性・品位を100%維持したまま、安全・確実にプロモーションを実施", accent=GREEN)

flow13 = [
    ("PHASE 01", "企画・制作", "インフルエンサーおよび事務局が、催事の趣旨に沿った投稿案（画像・動画・テキスト）を作成。"),
    ("PHASE 02", "事前提出", "公開の一定期間前に、すべての投稿原稿を事務局へ提出。"),
    ("PHASE 03", "内容確認・監修", "公的催事としての品位、誤認の有無、出店者情報の正確性を事務局にて厳格に審査・承認。"),
    ("PHASE 04", "公開・配信", "承認を受けた原稿のみをスケジュール通りに公開。無許可の投稿は100%防止。"),
]

for idx, (p_tag, p_title, p_desc) in enumerate(flow13):
    cx = Inches(0.7) + idx * Inches(3.05)
    # フェーズライン（上部）
    line(s13, cx, Inches(1.75), Inches(2.88), Inches(0.035), GREEN)
    f_tag = tb(s13, cx, Inches(1.9), Inches(2.88), Inches(0.35))
    p(f_tag, p_tag, 9.5, bold=True, color=GREEN)
    f_t = tb(s13, cx, Inches(2.3), Inches(2.88), Inches(0.52))
    p(f_t, p_title, 15, bold=True, color=NAVY)
    divider(s13, cx, Inches(2.87), Inches(2.85))
    f_d = tb(s13, cx, Inches(3.0), Inches(2.88), Inches(2.55))
    p(f_d, p_desc, 10, color=GRAY3)
    if idx < 3:
        f_arr = tb(s13, cx + Inches(2.9), Inches(3.3), Inches(0.25), Inches(0.55))
        p(f_arr, "→", 16, color=GRAY1)

# 下部
line(s13, Inches(0.7), Inches(5.72), Inches(3.5), Inches(0.03), GREEN)
f13_bh = tb(s13, Inches(0.7), Inches(5.9), Inches(12.22), Inches(0.38))
p(f13_bh, "事前審査体制の3つの約束", 11, bold=True, color=GREEN)
f13_b = tb(s13, Inches(0.7), Inches(6.3), Inches(12.22), Inches(1.0))
for sp in [
    "1. 事前承認のない公開は一切行いません（すべての発信物を事前にご確認いただきます）。",
    "2. 公的催事としての信頼性を損なう不適切な表現、誇大広告、公序良俗に反する内容は100%排除します。",
    "3. 出店者様向け情報や著名人出演情報など、権利関係の審査も事前に完全にクリアしてから発信します。",
]:
    p(f13_b, "・ " + sp, 10, color=GRAY3, sp_before=2)


# ─────────────────────────────────────────
# Slide 14：第7章① 共同投稿の仕組み
# ─────────────────────────────────────────
s14 = prs.slides.add_slide(blank)
chap_header(s14, 14, "第7章 ①", "地域メディア連携でリーチと来場が確実に伸びる理由",
            "「身近なおすすめ」としての信頼感と、「共同投稿（コラボ機能）」による17万人以上への同時露出")

# 上部図解（横フロー）
line(s14, Inches(0.7), Inches(1.75), Inches(12.0), Inches(0.025), GRAY1)
labels14 = [
    ("公式アカウントの投稿\n（出店者リール等）", NAVY),
    ("インフルエンサー\n（おちゃさん 17.3万人）", BLUE),
    ("両方のタイムラインへ\n【同時表示】！\n（17万人以上へ自動拡散）", AMBER),
]
bx_width = Inches(3.2)
for bi, (btxt, col) in enumerate(labels14):
    bx = Inches(0.7) + bi * Inches(4.15)
    line(s14, bx, Inches(1.78), Inches(3.0), Inches(0.045), col)
    f_bx = tb(s14, bx + Inches(0.15), Inches(1.95), Inches(3.0), Inches(1.0))
    p(f_bx, btxt, 12, bold=True, color=col)
    if bi < 2:
        f_arr = tb(s14, bx + Inches(3.15), Inches(2.28), Inches(0.95), Inches(0.48))
        p(f_arr, "→", 22, color=GRAY1, align=PP_ALIGN.CENTER)

divider(s14, Inches(0.7), Inches(3.12), Inches(12.0))

# 下部：3つの理由
pts14 = [
    ("理由 01　身近なおすすめ",
     "企業からの宣伝ではなく、普段から見ているお出かけメディアの紹介だからこそ「遠くの広告」ではなく「身近なおすすめ」として信頼されます。", NAVY),
    ("理由 02　ファミリー＆県民層",
     "子育て世代に強いおちゃさんと、ニュースを追う県民層に強い速報の2組で、産業フェアの多彩な魅力を全方位へ広げられます。", BLUE),
    ("理由 03　来場・口コミの好循環",
     "テレビCM・WEB・インスタで認知 ➔ 保存・シェア ➔ HP確認 ➔ 来場 ➔ 会場写真を投稿して友達へ広がる自然な好循環を形成します。", AMBER),
]
for idx, (st, sd, col) in enumerate(pts14):
    cx = Inches(0.7) + idx * Inches(4.15)
    line(s14, cx, Inches(3.22), Inches(0.04), Inches(3.5), col)
    f_t = tb(s14, cx + Inches(0.15), Inches(3.25), Inches(3.9), Inches(0.42))
    p(f_t, st, 12, bold=True, color=col)
    f_d = tb(s14, cx + Inches(0.15), Inches(3.72), Inches(3.9), Inches(2.6))
    p(f_d, sd, 10, color=GRAY3)


# ─────────────────────────────────────────
# Slide 15：第7章② ULSSASモデル
# ─────────────────────────────────────────
s15 = prs.slides.add_slide(blank)
chap_header(s15, 15, "第7章 ②", "SNS時代の行動プロセス「ULSSAS」による来場促進サイクル",
            "単発の広告表示で終わらせず、生活者の保存・検索・来場・クチコミ拡散が自走するサイクルを構築")

ulssas = [
    ("U", "UGC / 発見", "共同投稿や出店者リール動画が「おすすめ・発見欄」に自動表示される。", BLUE),
    ("L", "Like / 保存", "「これ楽しそう！」「今週末行きたい！」と直感的にいいね・保存される。", BLUE),
    ("S", "Search 1\nSNS検索", "Instagram内で公式アカウントや出店情報、ハッシュタグをチェック。", BLUE),
    ("S", "Search 2\nWEB検索", "Google等で「産業フェア」を検索し、駐車場や特設サイト詳細を確認。", BLUE),
    ("A", "Action\n来場", "会期当日（11/28・29）、家族や友人とツインメッセ静岡へ満員来場！", AMBER),
    ("S", "Spread\n拡散", "「楽しかった！」と来場者自身が会場写真をSNS投稿 ➔ 次のUGCへ循環！", AMBER),
]

for idx, (u_char, u_title, u_desc, col) in enumerate(ulssas):
    cx = Inches(0.7) + idx * Inches(2.05)
    # 上部カラーライン
    line(s15, cx, Inches(1.75), Inches(1.9), Inches(0.04), col)
    # 大文字
    f_char = tb(s15, cx, Inches(1.88), Inches(1.88), Inches(0.7))
    p(f_char, u_char, 30, bold=True, color=col)
    # タイトル
    f_t = tb(s15, cx, Inches(2.62), Inches(1.9), Inches(0.52))
    p(f_t, u_title, 11, bold=True, color=NAVY)
    divider(s15, cx, Inches(3.18), Inches(1.88))
    # 説明
    f_d = tb(s15, cx, Inches(3.3), Inches(1.9), Inches(2.3))
    p(f_d, u_desc, 9, color=GRAY3)
    if idx < 5:
        f_arr = tb(s15, cx + Inches(1.95), Inches(2.1), Inches(0.12), Inches(0.48))
        p(f_arr, "→", 14, color=GRAY1)

# 強み
line(s15, Inches(0.7), Inches(5.75), Inches(3.5), Inches(0.03), NAVY)
f15_bh = tb(s15, Inches(0.7), Inches(5.9), Inches(12.22), Inches(0.35))
p(f15_bh, "ULSSASモデルがもたらす「自走型プロモーション」の3大強み", 11, bold=True, color=NAVY)
f15_b = tb(s15, Inches(0.7), Inches(6.28), Inches(12.22), Inches(1.0))
p(f15_b, "1. 広告費に依存しない自走力：良質なリール動画とインフルエンサー投稿が起点となり、ユーザー自らの保存・検索を誘発。", 9.5, color=GRAY3)
p(f15_b, "2. 迷いをなくす2段階検索：SNSで雰囲気を掴み（Search1）、WEB検索で安心の公式情報（Search2）へ誘導し来場を決定づける。", 9.5, color=GRAY3)
p(f15_b, "3. 当日の来場者が次の宣伝役に：会場での楽しい体験が「Spread（拡散）」され、2日目の動員や次回開催の資産へ直結。", 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 16：第8章 出店者リール企画
# ─────────────────────────────────────────
s16 = prs.slides.add_slide(blank)
chap_header(s16, 16, "第8章", "出店者様ご紹介（5本投稿・最大15社）リール動画企画",
            "通常投稿とリール動画のアルゴリズム対比。おすすめ画面への自動拡散で来場者を増やす")

line(s16, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.0), NAVY)
f16_lt = tb(s16, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f16_lt, "通常投稿 vs リール動画（拡散の仕組み）", 13, bold=True, color=NAVY)

# 比較
f16_nh = tb(s16, Inches(0.9), Inches(2.3), Inches(5.5), Inches(0.35))
p(f16_nh, "▼ 通常の写真投稿：フォロワーだけに届く（狭い輪）", 10.5, bold=True, color=RED)
f16_nb = tb(s16, Inches(0.9), Inches(2.72), Inches(5.5), Inches(0.75))
p(f16_nb, "アカウントをフォローしている人だけにしか届かず、まだ産業フェアを知らない新規層へ情報が広がりません。",
  9.5, color=GRAY3)
divider(s16, Inches(0.9), Inches(3.52), Inches(5.5))
f16_oh = tb(s16, Inches(0.9), Inches(3.65), Inches(5.5), Inches(0.35))
p(f16_oh, "▲ リール（ショート動画）：未認知層へ自動拡散（広い輪）", 10.5, bold=True, color=GREEN)
f16_ob = tb(s16, Inches(0.9), Inches(4.07), Inches(5.5), Inches(1.35))
p(f16_ob, "Instagramのアルゴリズムにより、静岡県内の子育て・グルメ関心層の「おすすめ画面」へ次々と自動表示されます。フォロワー数に関係なく、県民全体へ届くため来場者数が確実に伸びます。",
  9.5, color=GRAY3)

line(s16, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.0), AMBER)
f16_rt = tb(s16, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f16_rt, "「出店者リール」が生み出す来場増加の5ステップ", 13, bold=True, color=NAVY)
f16_r = tb(s16, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for sn, st, sd in [
    ("STEP 01", "リール動画が自動で広がる", "おすすめ欄に表示→「このグルメ美味しそう！」「この工芸品すごい！」と興味を持たれる。"),
    ("STEP 02", "その出店者のことを調べる", "興味を持った商品・お店の名前をSNS・Web検索→産業フェアで出てることを把握。"),
    ("STEP 03", "産業フェア自体に興味が移る", "「この出店者が来るイベントってどんな感じ？」→公式アカウントや特設サイトをチェック。"),
    ("STEP 04", "「行こう！」と決断する", "見どころが多いと分かり、家族に共有→週末の予定として確定。"),
    ("STEP 05", "当日来場＋SNS投稿の連鎖", "会場での写真・動画を投稿→次の来場者を呼ぶ好循環が自然に生まれる。"),
]:
    p(f16_r, f"    [{sn}] {st}", 11, bold=True, color=AMBER, sp_before=8)
    p(f16_r, f"    {sd}", 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 17：第9章① 撮影ルール
# ─────────────────────────────────────────
s17 = prs.slides.add_slide(blank)
chap_header(s17, 17, "第9章 ①", "出店者様向け　動画の基本仕様 ＆ 失敗しない4つの撮影ルール",
            "スマホで撮影して送るだけ。編集・文字入れは一切不要。誰でも簡単に撮影できる実践ルール")

rules17 = [
    ("ルール 01", "カメラを固定して撮る", "[手ブレの防止]\nNG：カメラを激しく動かしたりズームする\nOK：構図を決めたら「5〜10秒間じっと固定」して撮影。", NAVY),
    ("ルール 02", "縦向きで撮影する", "[スマホ画面に最適化]\nNG：横向き撮影（画面の上下が黒くなる）\nOK：スマホを縦にして撮影（全画面で表示される）。", BLUE),
    ("ルール 03", "明るい場所・時間帯を選ぶ", "[画質・見映えの向上]\nNG：薄暗い場所や逆光での撮影\nOK：窓の近く・屋外・照明の当たる場所での撮影。", AMBER),
    ("ルール 04", "商品・体験のシーンを撮る", "[内容の明確さ]\nNG：看板や背景だけが写っている映像\nOK：商品・作業工程・体験の様子がはっきり分かる映像。", GREEN),
]

for idx, (tag, title, desc, col) in enumerate(rules17):
    cx = Inches(0.7) + (idx % 2) * Inches(6.25)
    cy = Inches(1.75) + (idx // 2) * Inches(2.55)
    line(s17, cx, cy, Inches(5.98), Inches(0.04), col)
    f_tag = tb(s17, cx, cy + Inches(0.1), Inches(5.9), Inches(0.32))
    p(f_tag, tag, 9.5, bold=True, color=col)
    f_t = tb(s17, cx, cy + Inches(0.45), Inches(5.9), Inches(0.45))
    p(f_t, title, 13.5, bold=True, color=NAVY)
    f_d = tb(s17, cx, cy + Inches(0.95), Inches(5.9), Inches(1.45))
    p(f_d, desc, 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 18：第9章② 提出フロー
# ─────────────────────────────────────────
s18 = prs.slides.add_slide(blank)
chap_header(s18, 18, "第9章 ②", "撮影対象例・確認シート ＆ ご提出フロー",
            "出店者が迷わない具体例の提示と専用フォームによるスムーズな回収体制（10/23締切）")

line(s18, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.0), NAVY)
f18_lt = tb(s18, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f18_lt, "撮影対象の具体例 ＆ 確認シート項目", 13, bold=True, color=NAVY)

f18_l = tb(s18, Inches(0.9), Inches(2.28), Inches(5.5), Inches(4.3))
for sec_title, items in [
    ("撮影シーンの具体例", [
        "お店・会社の顔：外観、看板、入口、のれん",
        "空間・雰囲気：店内全体の様子、ブースのレイアウト",
        "商品・サービス：メイン商品、こだわり素材、制作工程",
        "体験・動き：ワークショップ作業、試食、使用中の様子",
        "スタッフ・職人：笑顔での作業・接客（許可を得て）",
    ]),
    ("提出前の最終確認", [
        "画面がブレていないか／暗すぎないか",
        "縦向きで撮影されているか",
        "著作権のある音楽やBGMが入っていないか",
        "映り込んでいる方の許可は取れているか",
    ]),
]:
    p(f18_l, f"【{sec_title}】", 11, bold=True, color=BLUE, sp_before=10)
    for it in items:
        p(f18_l, "・ " + it, 9.5, color=GRAY3, sp_before=2)

line(s18, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.0), AMBER)
f18_rt = tb(s18, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f18_rt, "ご案内とご提出の流れ（スマホ専用フォーム）", 13, bold=True, color=NAVY)

f18_r = tb(s18, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for sn, st, sd in [
    ("ステップ 01", "ご案内シートの配布", "出店確定後、出店者様へ撮影要綱と入力フォームのURLをご案内。"),
    ("ステップ 02", "スマホから直接送信", "専用フォームから、動画ファイルと出店者情報（店名・説明文等）を直接アップロードして送信。"),
    ("ステップ 03", "事務局にて内容確認", "送信された素材をもとに動画を編集・テロップ挿入。発信前に内容を事務局が承認。"),
    ("ステップ 04", "公式Instagramで公開", "【提出締切：10月23日（金）】承認後、おちゃ様との共同投稿で10月下旬〜順次公開。"),
]:
    p(f18_r, f"    [{sn}] {st}", 11, bold=True, color=AMBER, sp_before=10)
    p(f18_r, f"    {sd}", 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 19：第10章 Instagram広告①
# ─────────────────────────────────────────
s19 = prs.slides.add_slide(blank)
chap_header(s19, 19, "第10章", "Instagram広告戦略①：人気投稿の活用 ＆ 画像スライド",
            "反響の大きい「画像スライド（カルーセル）」と「インフルエンサー投稿」を活用")

line(s19, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.0), BLUE)
f19_lt = tb(s19, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f19_lt, "正方形5枚スライド広告（カルーセル）の構成イメージ", 13, bold=True, color=NAVY)
f19_l = tb(s19, Inches(0.9), Inches(2.28), Inches(5.5), Inches(4.3))
for c_title, c_desc in [
    ("1枚目（表紙）", "「入場無料！週末どこ行く？」と目を引く表紙。スワイプを促す導線設計"),
    ("2〜4枚目（見どころ）", "子どもの体験・グルメ・ステージの各魅力を1枚1テーマでわかりやすく紹介"),
    ("最終枚（行動喚起）", "「詳細はここをタップ！」特設サイトへの導線。出演者・タイムスケジュール確認"),
]:
    p(f19_l, f"【{c_title}】", 11, bold=True, color=BLUE, sp_before=12)
    p(f19_l, c_desc, 9.5, color=GRAY3)

line(s19, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.0), AMBER)
f19_rt = tb(s19, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f19_rt, "インフルエンサー投稿をそのまま広告に活用", 13, bold=True, color=NAVY)
f19_r = tb(s19, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for pt_title, pt_desc in [
    ("広告のように見えない広告", "インフルエンサーが普段どおりに紹介する投稿フォーマットのまま、広告として配信。Instagram利用者に広告だと感じさせにくく、自然なアプローチが可能です。"),
    ("安心感のある広告配信", "主催者側からの一方的な広告ではなく、普段から親しまれているインフルエンサーの投稿として配信されるため、読者に信頼されやすく、高い関心を集められます。"),
    ("ターゲット層への精密配信", "Meta広告の精密なターゲティングと、インフルエンサー自身の読者データを組み合わせることで、「今週末お出かけ先を探しているパパ・ママ」に確実にリーチします。"),
]:
    p(f19_r, f"【{pt_title}】", 11, bold=True, color=AMBER, sp_before=12)
    p(f19_r, pt_desc, 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 20：第11章 Instagram広告② 詳細設定
# ─────────────────────────────────────────
s20 = prs.slides.add_slide(blank)
chap_header(s20, 20, "第11章", "Instagram広告戦略②：配信対象の詳細設定と見込み人数",
            "Instagram（Meta）公式管理画面にて試算・検証済みの確実な配信設定（約15.5万〜18.2万人）")

tbl20_s = s20.shapes.add_table(6, 2, Inches(0.7), Inches(1.72), Inches(12.22), Inches(3.7))
tbl20 = tbl20_s.table
tbl20.columns[0].width = Inches(3.3)
tbl20.columns[1].width = Inches(8.92)
for ci, h in enumerate(["項目", "設定内容（どのような人にお届けするか）"]):
    cell = tbl20.cell(0, ci)
    cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
    pp = cell.text_frame.paragraphs[0]
    pp.text = h; pp.font.size = Pt(10.5); pp.font.bold = True
    pp.font.color.rgb = WHITE; pp.font.name = FONT; pp.alignment = PP_ALIGN.CENTER

rows20 = [
    ("お届けする地域", "静岡県内8市町限定（お住まいの方・滞在している方）\n（静岡市、焼津市、藤枝市、富士市、島田市、吉田町、牧之原市、富士宮市）"),
    ("年齢・性別", "25歳〜45歳の男女（お出かけ先を決めるお父さん・お母さん世代）"),
    ("家族・子育て", "子育て（育児・子ども）に関心がある方"),
    ("お買い物・趣味", "おもちゃ（玩具）に関心がある方"),
    ("その他の関心事", "工作・DIYのアイデア / サンリオ / ハローキティ / 教育・学習 / お祭り・イベント / 子ども・子育て / 木工・工芸"),
]
for ri, (r0, r1) in enumerate(rows20):
    bg = GRAY1 if ri % 2 == 0 else WHITE
    for ci, val in enumerate([r0, r1]):
        cell = tbl20.cell(ri + 1, ci)
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        pp = cell.text_frame.paragraphs[0]
        pp.text = val; pp.font.size = Pt(10); pp.font.name = FONT
        if ci == 0: pp.alignment = PP_ALIGN.CENTER; pp.font.bold = True

# 大きな数値ハイライト
line(s20, Inches(0.7), Inches(5.6), Inches(3.5), Inches(0.03), BLUE)
f20_bh = tb(s20, Inches(0.7), Inches(5.8), Inches(12.22), Inches(0.35))
p(f20_bh, "広告が届く見込みの人数（Meta公式試算結果）", 11, bold=True, color=NAVY)
f20_b = tb(s20, Inches(0.7), Inches(6.18), Inches(12.22), Inches(1.1))
p(f20_b, "・ 対象となる人数：約154,600人 〜 181,900人　｜　想定表示回数：約 28.3 万回", 11, bold=True, color=BLUE)
p(f20_b, "・ 8市町にお住まいの25〜45歳で、子育てやイベントに関心がある方に絞っても約15.5万〜18.2万人の十分な規模があります。期間中に一人あたり複数回しっかり案内が届く、ちょうど良い規模感です。",
  9.5, color=GRAY3, sp_before=4)


# ─────────────────────────────────────────
# Slide 21：第12・13章 Google広告
# ─────────────────────────────────────────
s21 = prs.slides.add_slide(blank)
chap_header(s21, 21, "第12・13章", "Google広告戦略：掲載場所と配信の仕組み",
            "地元のニュースサイトやブログ、YouTube画面へ約142.9万回表示。関心・検索語句で捕捉")

line(s21, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.0), NAVY)
f21_lt = tb(s21, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f21_lt, "掲載場所とスマート配信の仕組み", 13, bold=True, color=NAVY)
f21_l = tb(s21, Inches(0.9), Inches(2.28), Inches(5.5), Inches(4.3))
p(f21_l, "【世界最大手のGoogleネットワーク】", 11, bold=True, color=NAVY)
p(f21_l, "静岡県民が普段見ている地元ニュースサイト、天気予報、YouTubeの画面などに自然にバナーを表示します。", 9.5, color=GRAY3, sp_before=4)
p(f21_l, "【1つの広告設定で自動的に最適配置】", 11, bold=True, color=NAVY, sp_before=12)
p(f21_l, "Google AIが「このユーザーは今どのサイトを見ているか」「どんな関心があるか」を自動で判断し、最も効果的な場所へ最適なタイミングで表示します。", 9.5, color=GRAY3, sp_before=4)

line(s21, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.0), NAVY)
f21_rt = tb(s21, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f21_rt, "配信対象の詳細設定（関心・検索キーワード）", 13, bold=True, color=NAVY)
f21_r = tb(s21, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for g_title, g_desc in [
    ("子ども・子育て向け", "未就学児・小学生の子どもを持つ保護者、家族レジャーに関心のある層"),
    ("検索キーワード連動（カスタム）", "「産業フェア静岡」「ツインメッセ静岡」「静岡 子供 イベント」「静岡 週末 お出かけ」などの検索者"),
    ("行動・関心ターゲティング", "木工・DIY、工芸品、地域イベント、静岡グルメ、ファミリーレジャーに関心があると判定された層"),
]:
    p(f21_r, f"【設定】 {g_title}", 11, bold=True, color=BLUE, sp_before=12)
    p(f21_r, g_desc, 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 22：第14・15章 Yahoo!・LINE広告
# ─────────────────────────────────────────
s22 = prs.slides.add_slide(blank)
chap_header(s22, 22, "第14・15章", "Yahoo!・LINE広告戦略：掲載場所とターゲティング",
            "LINEトーク最上部＆Yahoo!トップ画面。全世代を網羅する日常動線へ約125.0万回表示")

line(s22, Inches(0.7), Inches(1.75), Inches(0.045), Inches(5.0), GREEN)
f22_lt = tb(s22, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f22_lt, "掲載場所と媒体の強み", 13, bold=True, color=NAVY)
f22_l = tb(s22, Inches(0.9), Inches(2.28), Inches(5.5), Inches(4.3))
p(f22_l, "【LINEのトーク画面の最上部】", 11, bold=True, color=GREEN)
p(f22_l, "静岡県民の大半が毎日家族や友人とやりとりするLINEのトーク一覧トップに表示。日常の視線動線に自然に入り込みます。", 9.5, color=GRAY3, sp_before=4)
p(f22_l, "【Yahoo!ニュース・Topページ】", 11, bold=True, color=GREEN, sp_before=12)
p(f22_l, "県内の幅広い世代が毎日ニュースを確認するYahoo!の最上部に表示。家族の話題・地域情報として目に触れる頻度が非常に高い配置です。", 9.5, color=GRAY3, sp_before=4)

line(s22, Inches(6.7), Inches(1.75), Inches(0.045), Inches(5.0), GREEN)
f22_rt = tb(s22, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f22_rt, "サーチ・行動ターゲティングの詳細", 13, bold=True, color=NAVY)
f22_r = tb(s22, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for y_title, y_desc in [
    ("Yahoo!検索キーワード（サーチターゲティング）", "直近で「静岡 イベント」「週末 お出かけ」「サンリオ」「お笑いライブ」などを検索した人に狙い撃ちで配信。"),
    ("行動ターゲティング", "子育て、レジャー、地元グルメ、家族向けお出かけを日常的に調べている行動パターンの人を自動捕捉。"),
    ("LINE年齢・エリア設定", "静岡県内8市町の25歳〜55歳に絞って配信。Yahoo!のビッグデータを活用した高精度なセグメント。"),
]:
    p(f22_r, f"【設定】 {y_title}", 11, bold=True, color=GREEN, sp_before=12)
    p(f22_r, y_desc, 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 23：第16章 広告クリエイティブ
# ─────────────────────────────────────────
s23 = prs.slides.add_slide(blank)
chap_header(s23, 23, "第16章", "広告クリエイティブ（文章・画像）の具体案",
            "各広告媒体の文字数制限を厳格にクリアした、来場意欲を刺激する実践的な広告文案")

c_cards = [
    ("Instagram広告", [
        ("メインテキスト", "11/28(土)・29(日)ツインメッセ静岡！よしもと芸人＆サンリオキャラクターが登場！木工体験や静岡グルメも満載の産業フェアしずおかへGO！"),
        ("画像の中の文字", "「2026年11月28日(土)・29日(日) 産業フェアしずおか　入場無料！」"),
        ("ストーリーズテキスト", "「入場無料！ 今週末は産業フェアへ→特設サイトはプロフィールURLから」"),
    ], BLUE),
    ("Google広告", [
        ("見出し①（全角15文字）", "産業フェアしずおか2026"),
        ("見出し②（全角15文字）", "11月28・29日無料入場！"),
        ("見出し③（全角15文字）", "サンリオ＆芸人が登場"),
        ("説明文①（全角45文字）", "ツインメッセ静岡で開催！木工体験・地元グルメ・よしもとライブ。週末のお出かけはここで決まり！"),
    ], NAVY),
    ("Yahoo!/LINE広告", [
        ("LINEトーク最上部（18文字）", "【入場無料】ツインメッセ静岡イベント！"),
        ("Yahoo!タイトル（20文字）", "28日ジョイマン／29日プリン登場！"),
        ("Yahoo!説明文章（44文字）", "11/28・29ツインメッセ静岡！工作体験や静岡グルメ、豪華ステージが大集合！入場無料"),
    ], GREEN),
]

for idx, (ct, citems, col) in enumerate(c_cards):
    cx = Inches(0.7) + idx * Inches(3.97)
    line(s23, cx, Inches(1.75), Inches(3.75), Inches(0.04), col)
    f_ct = tb(s23, cx, Inches(1.9), Inches(3.75), Inches(0.38))
    p(f_ct, ct, 12, bold=True, color=col)
    divider(s23, cx, Inches(2.35), Inches(3.75))
    f_c = tb(s23, cx, Inches(2.5), Inches(3.82), Inches(4.45))
    for ititle, itxt in citems:
        p(f_c, f"【{ititle}】", 10, bold=True, color=NAVY, sp_before=10)
        p(f_c, itxt, 9.5, color=GRAY3)


# ─────────────────────────────────────────
# Slide 24：第17章 テンプレート投稿オプション
# ─────────────────────────────────────────
s24 = prs.slides.add_slide(blank)
chap_header(s24, 24, "第17章", "【追加オプション案】出店者様紹介「テンプレート投稿」の展開",
            "決定事項ではなく、公式アカウントの投稿数・露出ボリュームをさらに増やしたい場合の選択肢")

# 上部フロー
line(s24, Inches(0.7), Inches(1.75), Inches(12.0), Inches(0.03), NAVY)
f24_th = tb(s24, Inches(0.7), Inches(1.88), Inches(12.0), Inches(0.35))
p(f24_th, "1つの共通デザイン枠で手軽に量産するスキーム", 11.5, bold=True, color=NAVY)

for idx, (f_head, f_body) in enumerate([
    ("出店者様より", "写真・情報のご提供\n（静止画1〜2枚＋文章）"),
    ("事務局にて", "共通デザイン枠に\n写真・テキストを配置"),
    ("公式SNSから", "統一感のある投稿を\nテンポよく大量発信！"),
]):
    bx = Inches(0.7) + idx * Inches(3.95)
    line(s24, bx, Inches(2.35), Inches(3.7), Inches(0.035), BLUE)
    f_fh = tb(s24, bx, Inches(2.48), Inches(3.7), Inches(0.38))
    p(f_fh, f_head, 12, bold=True, color=BLUE)
    f_fb = tb(s24, bx, Inches(2.92), Inches(3.7), Inches(0.65))
    p(f_fb, f_body, 10.5, color=GRAY3)
    if idx < 2:
        f_arr = tb(s24, bx + Inches(3.75), Inches(2.7), Inches(0.25), Inches(0.45))
        p(f_arr, "→", 18, color=GRAY1)

divider(s24, Inches(0.7), Inches(3.72), Inches(12.0))

# 3メリット
f24_mh = tb(s24, Inches(0.7), Inches(3.9), Inches(12.0), Inches(0.38))
p(f24_mh, "テンプレート投稿オプションの3大メリット", 11.5, bold=True, color=NAVY)

for idx, (tag, title, desc, col) in enumerate([
    ("メリット 01", "より多くの出店者様をPR可能", "リール動画（15社）から溢れた店舗や、動画撮影が難しい店舗も含め、広く公平に紹介機会を提供できます。", BLUE),
    ("メリット 02", "アカウントの統一感と見やすさ", "デザインの揃った美しい投稿が並ぶことで、公式アカウントの信頼性・見栄え・品位が高まります。", AMBER),
    ("メリット 03", "出店者様ご自身による拡散", "「公式で紹介されました！」と出店者様自身が自分のSNSでシェアしやすくなり、外部への波及効果が加速します。", GREEN),
]):
    cx = Inches(0.7) + idx * Inches(3.97)
    line(s24, cx, Inches(4.42), Inches(0.04), Inches(2.65), col)
    f_tag = tb(s24, cx + Inches(0.12), Inches(4.42), Inches(3.7), Inches(0.32))
    p(f_tag, tag, 9.5, bold=True, color=col)
    f_tt = tb(s24, cx + Inches(0.12), Inches(4.78), Inches(3.7), Inches(0.45))
    p(f_tt, title, 12.5, bold=True, color=NAVY)
    f_td = tb(s24, cx + Inches(0.12), Inches(5.28), Inches(3.72), Inches(1.7))
    p(f_td, desc, 10, color=GRAY3)


# ─────────────────────────────────────────
# Slide 25：第18章 まとめ ＆ 進め方
# ─────────────────────────────────────────
s25 = prs.slides.add_slide(blank)
chap_header(s25, 25, "第18章", "まとめ ＆ 今後の進め方・ご確認事項",
            "本計画の強みを活かし、安心・確実なプロモーション準備を進めてまいります")

line(s25, Inches(0.7), Inches(1.75), Inches(0.045), Inches(4.82), NAVY)
f25_lt = tb(s25, Inches(0.9), Inches(1.75), Inches(5.5), Inches(0.42))
p(f25_lt, "本計画の3つの強み", 13, bold=True, color=NAVY)
f25_l = tb(s25, Inches(0.9), Inches(2.28), Inches(5.5), Inches(4.3))
for st, sd, col in [
    ("高い情報伝達力（4層連携）", "テレビCM・WEB広告と地域メディア（2組）の連携により、子育て世代へイベントの魅力をダイレクトにお届け。", NAVY),
    ("地域密着・確実なお届け", "静岡県内8市町の子育て世代（約15.5万〜18.2万人）へ、期間中しっかりと複数回お届け（約296.6万回表示）。", BLUE),
    ("分かりやすい結果のご報告", "アクセス解析や広告レポートを用いて、「何回表示され、何人が見に来たか」を明確にご報告いたします。", GREEN),
]:
    p(f25_l, "・ " + st, 12, bold=True, color=col, sp_before=14)
    p(f25_l, sd, 10, color=GRAY3)

line(s25, Inches(6.7), Inches(1.75), Inches(0.045), Inches(4.82), AMBER)
f25_rt = tb(s25, Inches(6.9), Inches(1.75), Inches(6.0), Inches(0.42))
p(f25_rt, "今後のお願い・ご確認事項", 13, bold=True, color=NAVY)
f25_r = tb(s25, Inches(6.9), Inches(2.28), Inches(6.0), Inches(4.45))
for rq in [
    "1. 本計画内容についてのご確認・ご了承",
    "2. 起用メディア2組（静岡県コンシェルジュ様、静岡県ニュース速報様）の投稿スケジュール（11/15・11/24）および広告連携の最終確認",
    "3. 出店者様向けのご案内（撮影要綱・申請フォーム・動画提供依頼）の配布と素材収集（10月23日(金) 素材締切）",
    "4. 公式Instagramの全体概要投稿（10月25日(日)仮設定・HP更新連動）用素材のご共有",
    "5. Instagram広告配信に伴う連携のご協力（公式アカウントの共有、およびFacebookページ等の操作・権限付与のお願い）",
]:
    p(f25_r, rq, 10.5, color=GRAY3, sp_before=8)

p(f25_r, "\n※ご不明な点や調整のご要望がございましたら、いつでもお気軽にお申し付けください。",
  10, bold=True, color=GRAY2, sp_before=10)


# ─────────────────────────────────────────
# 保存
# ─────────────────────────────────────────
out = "/Users/sap220701/Desktop/産業フェア_ローカル/docs/02_プロモーション計画/クライアント説明用_WEBプロモーション統合計画書_2026_印刷版.pptx"
prs.save(out)
print(f"保存完了: {out}")
print(f"Total slides: {len(prs.slides)}")
