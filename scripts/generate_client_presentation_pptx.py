import os
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette - Professional Business Tone (No Emoji)
C_NAVY = RGBColor(26, 54, 93)          # #1A365D Deep Navy
C_BLUE = RGBColor(43, 108, 176)        # #2B6CB0 Vibrant Blue
C_LIGHT_BLUE = RGBColor(237, 248, 254) # #EDF8FE Clean Light Blue
C_AMBER = RGBColor(217, 119, 6)        # #D97706 Warm Gold/Amber
C_LIGHT_AMBER = RGBColor(254, 243, 199)# Soft Amber
C_BG_GRAY = RGBColor(248, 250, 252)    # #F8FAFC Neutral Gray
C_CARD_BG = RGBColor(255, 255, 255)    # Pure White
C_BORDER = RGBColor(226, 232, 240)     # #E2E8F0 Subtle Border
C_BORDER_DARK = RGBColor(203, 213, 225)# #CBD5E1 Darker Border
C_TEXT_DARK = RGBColor(30, 41, 59)     # #1E293B Primary Text
C_TEXT_MUTED = RGBColor(100, 116, 139) # #64748B Secondary Text
C_WHITE = RGBColor(255, 255, 255)
C_EMERALD = RGBColor(5, 150, 105)      # #059669 Success Green
C_LIGHT_EMERALD = RGBColor(209, 250, 229)
C_RED = RGBColor(220, 38, 38)          # Warning/NG Red
C_LIGHT_RED = RGBColor(254, 226, 226)

FONT_JP = "Hiragino Sans"
FONT_JP_BOLD = "Hiragino Sans"

blank_layout = prs.slide_layouts[6]

def add_header(slide, category_en, title_jp, subtitle_jp=None):
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8.0), Inches(0.3))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category_en.upper()
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = C_BLUE
    p_c.font.name = FONT_JP_BOLD

    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.65))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_jp
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY
    p_t.font.name = FONT_JP_BOLD

    if subtitle_jp:
        p_sub = tf_t.add_paragraph()
        p_sub.text = subtitle_jp
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_TEXT_MUTED
        p_sub.font.name = FONT_JP

    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0.8), Inches(1.42), Inches(11.7), Inches(0.02)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = C_BORDER
    line.line.color.rgb = C_BORDER

def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1)
    return shape

def add_badge(slide, left, top, width, height, text, bg_color=C_BLUE, text_color=C_WHITE, font_size=10):
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    badge.fill.solid()
    badge.fill.fore_color.rgb = bg_color
    badge.line.fill.background()
    tf = badge.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = True
    p.font.color.rgb = text_color
    p.font.name = FONT_JP_BOLD
    p.alignment = PP_ALIGN.CENTER
    return badge

def add_arrow(slide, left, top, width, height, color=C_BLUE):
    arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
    arrow.fill.solid()
    arrow.fill.fore_color.rgb = color
    arrow.line.fill.background()
    return arrow

# ====================================================
# Slide 01: Cover (表紙)
# ====================================================
s1 = prs.slides.add_slide(blank_layout)
bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = C_NAVY
bg1.line.fill.background()

bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.12), Inches(4.5))
bar1.fill.solid()
bar1.fill.fore_color.rgb = C_AMBER
bar1.line.fill.background()

tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
tf1 = tb1.text_frame
tf1.word_wrap = True

p0 = tf1.paragraphs[0]
p0.text = "産業フェアしずおか2026 企画提案書"
p0.font.size = Pt(16)
p0.font.color.rgb = RGBColor(190, 215, 250)
p0.font.bold = True

p1 = tf1.add_paragraph()
p1.text = "WEBプロモーション統合計画書"
p1.font.size = Pt(36)
p1.font.bold = True
p1.font.color.rgb = C_WHITE
p1.space_before = Pt(14)
p1.space_after = Pt(14)

p2 = tf1.add_paragraph()
p2.text = "テレビCM × WEB広告 × 地域メディアの相乗効果で来場を最大化"
p2.font.size = Pt(18)
p2.font.color.rgb = RGBColor(226, 232, 240)

p3 = tf1.add_paragraph()
p3.text = "\n開催期日：2026年11月28日(土)・29日(日) ｜ 会場：ツインメッセ静岡"
p3.font.size = Pt(13)
p3.font.color.rgb = RGBColor(203, 213, 225)

p4 = tf1.add_paragraph()
p4.text = "企画・制作：静鉄アド・パートナーズ ｜ 2026年9月"
p4.font.size = Pt(12)
p4.font.color.rgb = RGBColor(148, 163, 184)

# ====================================================
# Slide 02: Purpose & Flow (第1章：本書の目的・3段階フロー図解)
# ====================================================
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Purpose & Background", "第1章：本書の目的（なぜ今、WEBプロモーションが必要なのか）", "生活スタイルの変化に対応し、テレビCMと日常のスマホを結ぶことで来場意欲を確実な行動へ")

s2_steps = [
    ("STEP 01", "時代の変化と生活スタイル", "現代の来場者（特に子育て世代）は、テレビCMで催事を知った後、必ずスマートフォンで出店者、見どころ、アクセスを検索します。日常のスマホ画面に情報が存在することが、来場決定の前提条件です。"),
    ("STEP 02", "テレビCMとWEBの相乗効果", "テレビCMは「県内全域へ開催とお祭り感を一気に広げる」役割。WEB広告は「日常のスマホ画面で何度も見かけ、関心を高める」役割。どちらか一方ではなく、両輪で展開することで効果が最大化します。"),
    ("STEP 03", "「行こう！」を着火する後押し", "主催者からの一方的な宣伝だけでなく、普段から信頼されている身近な地域メディア（おちゃさん等）が紹介することで、「遠くの広告」から「今週末に行くべき身近なおすすめ」へと変わります。")
]

for idx, (step_num, title, body) in enumerate(s2_steps):
    card_x = Inches(0.8) + idx * Inches(3.95)
    add_card(s2, card_x, Inches(1.7), Inches(3.6), Inches(4.5))
    add_badge(s2, card_x + Inches(0.2), Inches(1.9), Inches(1.2), Inches(0.35), step_num, C_BLUE, C_WHITE, 11)
    
    tb = s2.shapes.add_textbox(card_x + Inches(0.2), Inches(2.4), Inches(3.2), Inches(3.6))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(8)
    
    p_b = tf.add_paragraph()
    p_b.text = body
    p_b.font.size = Pt(10.5)
    p_b.font.color.rgb = C_TEXT_DARK
    
    if idx < 2:
        add_arrow(s2, card_x + Inches(3.65), Inches(3.6), Inches(0.25), Inches(0.4), C_BORDER_DARK)

add_card(s2, Inches(0.8), Inches(6.35), Inches(11.7), Inches(0.75), C_LIGHT_BLUE, C_BLUE)
tb2_b = s2.shapes.add_textbox(Inches(1.0), Inches(6.4), Inches(11.3), Inches(0.65))
p = tb2_b.text_frame.paragraphs[0]
p.text = "結論：テレビCMで「認知」を獲得し、WEB広告と地域メディアがスマホ上で「来場の決定打」を与えます。"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_NAVY

# ====================================================
# Slide 03: Overview & Roles (第2章：役割分担一覧・数値配分図解)
# ====================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Media Mix Overview", "第2章：全体プロモーションの全体像と役割分担", "テレビCM・WEB広告・地域メディアの相乗効果。合計約296.6万回の確実なお届け")

tbl3_s = s3.shapes.add_table(5, 3, Inches(0.8), Inches(1.6), Inches(7.5), Inches(3.8))
tbl3 = tbl3_s.table
tbl3.columns[0].width = Inches(1.8)
tbl3.columns[1].width = Inches(4.2)
tbl3.columns[2].width = Inches(1.5)

h3 = ["媒体名", "主な役割と特徴", "表示見込み"]
for i, h in enumerate(h3):
    cell = tbl3.cell(0, i)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

r3 = [
    ("テレビCM\n（マス媒体）", "県内全域のリビングへ開催とお祭り感を一気に浸透", "県内放送"),
    ("Google広告\n（WEBバナー）", "ニュースやYouTube等、日常ネット閲覧時の確実な刷り込み", "約134.1万回"),
    ("Yahoo!・LINE広告\n（スマホ通知）", "県民大半の日常アプリ（LINEトーク最上部等）での接触", "約134.1万回"),
    ("Instagram広告\n（SNS広告）", "子育て世代へ写真・カルーセル・人気投稿で直感訴求", "約 28.3万回")
]
for r_i, r_data in enumerate(r3, start=1):
    for c_i, val in enumerate(r_data):
        cell = tbl3.cell(r_i, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_BG_GRAY if r_i % 2 == 1 else C_WHITE
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(9.5)
        if c_i in [0, 2]:
            p.alignment = PP_ALIGN.CENTER
            if c_i == 0 or "約" in val:
                p.font.bold = True

add_card(s3, Inches(8.6), Inches(1.6), Inches(3.9), Inches(3.8), C_LIGHT_BLUE, C_BLUE)
tb3_m = s3.shapes.add_textbox(Inches(8.8), Inches(1.8), Inches(3.5), Inches(3.4))
tf3_m = tb3_m.text_frame
tf3_m.word_wrap = True

p = tf3_m.paragraphs[0]
p.text = "デジタル総表示回数"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY

p_val = tf3_m.add_paragraph()
p_val.text = "約 296.6 万回"
p_val.font.size = Pt(26)
p_val.font.bold = True
p_val.font.color.rgb = C_AMBER
p_val.space_before = Pt(4)
p_val.space_after = Pt(8)

p_break = tf3_m.add_paragraph()
p_break.text = "【内訳】\n・ Google広告：約134.1万回 (45%)\n・ Yahoo!/LINE：約134.1万回 (45%)\n・ Instagram：約28.3万回 (10%)\n\n※静岡県内8市町限定配信により、対象世帯へ期間中複数回確実にリーチします。"
p_break.font.size = Pt(10)
p_break.font.color.rgb = C_TEXT_DARK

add_card(s3, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.5), C_CARD_BG, C_BORDER)
tb3_bot = s3.shapes.add_textbox(Inches(1.0), Inches(5.7), Inches(11.3), Inches(1.3))
tf3_bot = tb3_bot.text_frame
tf3_bot.word_wrap = True
p = tf3_bot.paragraphs[0]
p.text = "媒体別の相乗効果ポイント"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_NAVY

p_sub = tf3_bot.add_paragraph()
p_sub.text = "・ LINE/Yahoo!で全世代の日常動線を網羅し、Googleで興味関心層を捕捉。\n・ Instagramでは子育てファミリーへ写真・動画で共感を呼び起こし、3媒体が相互に補完し合います。"
p_sub.font.size = Pt(10.5)
p_sub.font.color.rgb = C_TEXT_DARK
p_sub.space_before = Pt(2)

# ====================================================
# Slide 04: 4-Layer Flow Diagram (第2章：4層連携フロー図解)
# ====================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "4-Layer Synergy Flow", "第2章：4層連携ストーリー（来場者の心を動かすステップ）", "4つの媒体が1本の導線として連携し、県民の「認知」を「当日の来場」へ確実に導く図解")

flow4 = [
    ("第1層", "テレビCM", "【全体認知・お祭り感】", "『産業フェアが今年も開催されるぞ！』", "県内全域へ広く開催を浸透", C_NAVY),
    ("第2層", "WEB広告", "【日常の刷り込み】", "『あ、ネットでもLINEでも見かけるな』", "8市町へ約268万回表示", C_BLUE),
    ("第3層", "地域メディア", "【信頼・熱量の着火】", "『普段見てるおちゃさんも紹介！行こう！』", "身近なおすすめで来場決定", C_AMBER),
    ("第4層", "公式リール", "【詳細確認・出店PR】", "『この体験をしよう！駐車場はここね！』", "目的意識を持って当日来場", C_EMERALD)
]

for idx, (layer_num, m_name, role_tag, quote_txt, sub_txt, col) in enumerate(flow4):
    card_x = Inches(0.8) + idx * Inches(2.95)
    add_card(s4, card_x, Inches(1.6), Inches(2.75), Inches(4.5))
    add_badge(s4, card_x + Inches(0.15), Inches(1.8), Inches(1.0), Inches(0.3), layer_num, col, C_WHITE, 10)
    
    tb = s4.shapes.add_textbox(card_x + Inches(0.15), Inches(2.2), Inches(2.45), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = m_name
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = col
    
    p_tag = tf.add_paragraph()
    p_tag.text = role_tag
    p_tag.font.size = Pt(10)
    p_tag.font.bold = True
    p_tag.font.color.rgb = C_NAVY
    p_tag.space_after = Pt(8)
    
    p_q = tf.add_paragraph()
    p_q.text = quote_txt
    p_q.font.size = Pt(10)
    p_q.font.bold = True
    p_q.font.color.rgb = col
    p_q.space_after = Pt(8)
    
    p_s = tf.add_paragraph()
    p_s.text = sub_txt
    p_s.font.size = Pt(9.5)
    p_s.font.color.rgb = C_TEXT_DARK
    
    if idx < 3:
        add_arrow(s4, card_x + Inches(2.8), Inches(3.6), Inches(0.15), Inches(0.35), C_BORDER_DARK)

add_card(s4, Inches(0.8), Inches(6.3), Inches(11.7), Inches(0.8), C_LIGHT_BLUE, C_BLUE)
tb4_b = s4.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.3), Inches(0.7))
p = tb4_b.text_frame.paragraphs[0]
p.text = "ゴール：テレビCMで「知っている」状態を作り、WEB広告と地域メディアが「行く！」という決定打を与え、満員でのご来場を実現します。"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_NAVY

# ====================================================
# Slide 05: Target Segments (第3章：ターゲット層の設定)
# ====================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Audience Segments", "第3章：ターゲット層（お届けする対象）の設定", "子育て世代を最重要ターゲットに設定し、3つの魅力的な要素をダイレクトに訴求")

add_card(s5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb5_l = s5.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf5_l = tb5_l.text_frame
tf5_l.word_wrap = True

p = tf5_l.paragraphs[0]
p.text = "ターゲット層の2層構造"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

add_badge(s5, Inches(1.0), Inches(2.3), Inches(2.2), Inches(0.35), "最重点：子育て世代", C_BLUE, C_WHITE, 10)
tb5_m = s5.shapes.add_textbox(Inches(1.0), Inches(2.7), Inches(5.2), Inches(1.5))
tf5_m = tb5_m.text_frame
tf5_m.word_wrap = True
p = tf5_m.paragraphs[0]
p.text = "・ 25歳〜45歳の男女（未就学児〜小学生の保護者）\n・ 週末に家族みんなで楽しめるお出かけ先・体験先を探している層\n・ 日常的にInstagramやLINEを最も活用している層"
p.font.size = Pt(10)
p.font.color.rgb = C_TEXT_DARK

add_badge(s5, Inches(1.0), Inches(4.3), Inches(2.2), Inches(0.35), "準重点：一般・シニア層", C_AMBER, C_WHITE, 10)
tb5_s = s5.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(5.2), Inches(1.5))
tf5_s = tb5_s.text_frame
tf5_s.word_wrap = True
p = tf5_s.paragraphs[0]
p.text = "・ 地元特産品、静岡グルメ、伝統工芸、ものづくりに関心のある層\n・ お孫さんと一緒に安心してお出かけしたいシニア世代\n・ Yahoo!ニュースやLINEを通じて確実にアプローチ"
p.font.size = Pt(10)
p.font.color.rgb = C_TEXT_DARK

add_card(s5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb5_r = s5.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf5_r = tb5_r.text_frame
tf5_r.word_wrap = True

p_r = tf5_r.paragraphs[0]
p_r.text = "ターゲットへ届ける3大魅力要素"
p_r.font.size = Pt(15)
p_r.font.bold = True
p_r.font.color.rgb = C_NAVY

el_cards = [
    ("要素01", "子どもの笑顔・特別な体験", "木工体験、キッズワークショップ、サンリオステージ、よしもとお笑いなど、「子どもが主役になって楽しめる」催事を前面に案内。"),
    ("要素02", "美味しい地元グルメ・物産", "静岡ならではの名物グルメや普段なかなか出会えない名店が集まるワクワク感を写真・ショート動画で訴求。"),
    ("要素03", "家族で安心の屋内・快適空間", "雨でも快適な全天候型屋内会場（ツインメッセ静岡）、入場無料、充実の付帯設備など、子連れ来場の安心感を担保。")
]
for idx, (tag, t_title, t_desc) in enumerate(el_cards):
    y_c = Inches(2.4) + idx * Inches(1.3)
    add_card(s5, Inches(7.0), y_c, Inches(5.3), Inches(1.15), C_BG_GRAY, C_BORDER)
    tb_c = s5.shapes.add_textbox(Inches(7.15), y_c + Inches(0.08), Inches(5.0), Inches(1.0))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    
    p = tf_c.paragraphs[0]
    p.text = f"[{tag}] {t_title}"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    
    p_d = tf_c.add_paragraph()
    p_d.text = t_desc
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# ====================================================
# Slide 06: Area Lock (第4章：配信エリア厳格設定図解)
# ====================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Area Lock Diagram", "第4章：配信エリアの厳格な設定（静岡県内8市町限定）", "ツインメッセ静岡へアクセス可能な地域に絞り込み、広告予算の無駄遣いを徹底的に排除")

# Left: 8 municipalities tags
add_card(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb6_l = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf6_l = tb6_l.text_frame
tf6_l.word_wrap = True

p = tf6_l.paragraphs[0]
p.text = "配信対象エリア（県内8市町）"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

p_desc = tf6_l.add_paragraph()
p_desc.text = "ツインメッセ静岡へ車・交通機関で1時間圏内の世帯に集中配信。"
p_desc.font.size = Pt(10)
p_desc.font.color.rgb = C_TEXT_MUTED
p_desc.space_after = Pt(8)

cities = ["静岡市", "焼津市", "藤枝市", "富士市", "島田市", "吉田町", "牧之原市", "富士宮市"]
for idx, city in enumerate(cities):
    col_i = idx % 2
    row_i = idx // 2
    bx = Inches(1.0) + col_i * Inches(2.6)
    by = Inches(2.6) + row_i * Inches(0.55)
    add_badge(s6, bx, by, Inches(2.4), Inches(0.42), city, C_LIGHT_BLUE, C_NAVY, 11)

tb6_loc = s6.shapes.add_textbox(Inches(1.0), Inches(5.0), Inches(5.2), Inches(1.8))
tf6_loc = tb6_loc.text_frame
tf6_loc.word_wrap = True
p = tf6_loc.paragraphs[0]
p.text = "位置情報技術によるロック配信"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_AMBER

p_ld = tf6_loc.add_paragraph()
p_ld.text = "「旅行等で通過しただけの人」を自動除外し、「現在地に居住または滞在している人」に限定配信。県外への誤配信を100%防止します。"
p_ld.font.size = Pt(9.5)
p_ld.font.color.rgb = C_TEXT_DARK
p_ld.space_before = Pt(2)

# Right: 3 Benefits
add_card(s6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb6_r = s6.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf6_r = tb6_r.text_frame
tf6_r.word_wrap = True

p_r = tf6_r.paragraphs[0]
p_r.text = "エリア厳格指定の3大メリット"
p_r.font.size = Pt(15)
p_r.font.bold = True
p_r.font.color.rgb = C_NAVY

benefits = [
    ("メリット01", "広告予算の無駄遣いを完全排除", "来場が難しい遠方の地域へ配信せず、来場確率が極めて高い近隣世帯へ予算を100%集中投下。"),
    ("メリット02", "ターゲットへの接触頻度を高める", "限られた対象層へ期間中に何度も繰り返し表示されるため、「気になり度」を着実に高めます。"),
    ("メリット03", "「私たちの街の催事」という地元感", "「静岡市で開催される身近なイベント」として受け入れられ、家族での参加障壁を劇的に下げます。")
]
for idx, (b_tag, b_title, b_desc) in enumerate(benefits):
    y_b = Inches(2.4) + idx * Inches(1.3)
    add_card(s6, Inches(7.0), y_b, Inches(5.3), Inches(1.15), C_BG_GRAY, C_BORDER)
    tb_b = s6.shapes.add_textbox(Inches(7.15), y_b + Inches(0.08), Inches(5.0), Inches(1.0))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    
    p = tf_b.paragraphs[0]
    p.text = f"[{b_tag}] {b_title}"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    
    p_d = tf_b.add_paragraph()
    p_d.text = b_desc
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# ====================================================
# Slide 07: Instagram Timeline (第5章 ① 全体タイムライン)
# ====================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Timeline Schedule", "第5章 ①：Instagramプロモーション全体タイムライン", "公式アカウント（全10回）と地域メディア（計3回）を連動させ、途切れなく来場意欲を高める")

tbl7_s = s7.shapes.add_table(11, 5, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.1))
tbl7 = tbl7_s.table
tbl7.columns[0].width = Inches(1.8)
tbl7.columns[1].width = Inches(1.4)
tbl7.columns[2].width = Inches(3.2)
tbl7.columns[3].width = Inches(1.8)
tbl7.columns[4].width = Inches(3.5)

h7_txt = ["日程・時期", "区分", "投稿内容・アクション", "形式", "狙い・掲載の工夫"]
for c_i, h in enumerate(h7_txt):
    cell = tbl7.cell(0, c_i)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

t7_rows = [
    ("〜 10/23 (金)", "[素材締切]", "出店者様 動画素材の回収", "―", "専用フォームにて動画・情報を提出いただく期日"),
    ("10/25 (日)", "公式 01", "イベント全体概要", "画像（フィード）", "【公式HP更新連動】プロフィール先頭固定"),
    ("10月下旬〜11月中旬", "公式 02〜06", "出店者様ご紹介（計5本・最大15社）", "動画（リール）", "週1〜2本ペース順次公開。おちゃ様と共同投稿"),
    ("11/15 (日)", "メディア 01", "静岡県コンシェルジュ（おちゃさん）", "画像＋ストーリーズ", "【開催2週間前】見どころ紹介・週末の予定に保存"),
    ("11/24 (火)", "メディア 02", "静岡県コンシェルジュ（おちゃさん）", "動画＋ストーリーズ", "【直前決定打】体験やグルメの魅力をショート動画発信"),
    ("11/24 (火)", "メディア 03", "静岡県ニュース速報", "動画＋ストーリーズ", "【直前速報】地域のビッグイベントとして速報拡散"),
    ("11/27 (金)", "公式 07", "前日・直前告知", "画像（フィード）", "【出展者搬入日・夕方】「いよいよ明日開催！」案内"),
    ("11/28 (土)", "公式 08", "当日リアルタイム発信（1日目）", "ストーリーズ/写真", "オープニング・会場の賑わい・熱気をリアルタイム発信"),
    ("11/29 (日)", "公式 09", "当日リアルタイム発信（2日目）", "ストーリーズ/写真", "「本日最終日！」呼びかけとステージの熱気をお届け"),
    ("12/2 (水)", "公式 10", "開催報告・振り返り", "画像（フィード）", "盛況御礼・出店者の実績PRと次回開催へ繋げる")
]

for r_i, r_data in enumerate(t7_rows, start=1):
    for c_i, val in enumerate(r_data):
        cell = tbl7.cell(r_i, c_i)
        cell.fill.solid()
        if "メディア" in r_data[1]:
            cell.fill.fore_color.rgb = C_LIGHT_AMBER
        elif "素材締切" in r_data[1]:
            cell.fill.fore_color.rgb = C_LIGHT_RED
        elif r_i % 2 == 1:
            cell.fill.fore_color.rgb = C_BG_GRAY
        else:
            cell.fill.fore_color.rgb = C_WHITE
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(9)
        if c_i in [0, 1, 3]:
            p.alignment = PP_ALIGN.CENTER
            if c_i == 1:
                p.font.bold = True

tb7_n = s7.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.7), Inches(0.4))
p = tb7_n.text_frame.paragraphs[0]
p.text = "※発信するすべての投稿は、事前に内容（画像・動画・テキスト）をご確認・承認いただいた上で公開いたします。"
p.font.size = Pt(10)
p.font.color.rgb = C_TEXT_MUTED
p.font.bold = True

# ====================================================
# Slide 08: Official Instagram Structure (第5章 ② 公式10回の構成)
# ====================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Official Instagram", "第5章 ②：公式Instagram（基本10回）の投稿スケジュール構成", "公式アカウント（@sangyofair_shizuoka）から計画的に全10回の発信を実施")

s8_cards = [
    ("01 全体概要案内（1本）", "10月25日(日) 公開予定", [
        "公式ホームページの情報更新タイミングに合わせて公開",
        "開催日時、ツインメッセ静岡、見どころを分かりやすく案内",
        "アカウントのプロフィール先頭に固定し常時閲覧可能に"
    ], C_BLUE),
    ("02 出店者紹介（5本）", "10月下旬〜11月中旬", [
        "1本のショート動画（リール）に2〜3社をテーマ別にまとめ紹介",
        "全5本の投稿で合計「最大15社」をテンポよくご紹介",
        "動画素材を提供いただいた出店者様から順次PR（不公平感解消）",
        "静岡県コンシェルジュ（おちゃ様）と共同投稿で露出爆発"
    ], C_AMBER),
    ("03 直前・当日・事後（4本）", "11月27日〜12月2日", [
        "前日告知(11/27 金)：搬入風景と「明日開催！」の直前案内",
        "当日速報(11/28 土・29 日)：熱気・混雑・ステージ速報（計2本）",
        "開催報告(12/2 水)：盛況御礼・出店者の実績PRと次回へ繋げる"
    ], C_NAVY)
]

for idx, (ct, cs, items, col) in enumerate(s8_cards):
    cx = Inches(0.8) + idx * Inches(3.95)
    add_card(s8, cx, Inches(1.6), Inches(3.75), Inches(5.3))
    add_badge(s8, cx + Inches(0.2), Inches(1.8), Inches(3.35), Inches(0.35), ct, col, C_WHITE, 11)
    
    tb = s8.shapes.add_textbox(cx + Inches(0.15), Inches(2.3), Inches(3.45), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True
    
    ps = tf.paragraphs[0]
    ps.text = f"【時期：{cs}】"
    ps.font.size = Pt(11)
    ps.font.bold = True
    ps.font.color.rgb = C_TEXT_DARK
    ps.space_after = Pt(8)
    
    for it in items:
        pi = tf.add_paragraph()
        pi.text = "・ " + it
        pi.font.size = Pt(10)
        pi.font.color.rgb = C_TEXT_DARK
        pi.space_before = Pt(4)

# ====================================================
# Slide 09: Design Approach (第5章 ③ デザインの工夫)
# ====================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "UI/UX & Design", "第5章 ③：忙しいママ・パパでも伝わりやすいデザインの工夫（検討案）", "片手操作の子育て世代に配慮した視認性重視のデザイン設計（柔軟にご相談・調整）")

s9_cards = [
    ("工夫 01", "視認性の重視（1投稿＝1要点）", "スマートフォンを片手で見ている子育て世代を意識し、1つの投稿に情報を詰め込みすぎず、「何が魅力か」「いつ開催か」の要点を絞って伝えます。"),
    ("工夫 02", "写真の邪魔をしない文字配置", "写真や動画の魅力を引き立てつつ、パッと目に飛び込んでくる読みやすい日本語フォントと配色を採用。忙しい合間でも瞬時に理解できます。"),
    ("工夫 03", "ハッシュタグ活用と口コミ連鎖", "「#産業フェアしずおか2026」「#静岡子連れお出かけ」などを投稿内で案内。来場者が当日の様子を投稿しやすくなり、口コミ拡散を後押しします。")
]

for idx, (dt, dsub, dbody) in enumerate(s9_cards):
    dx = Inches(0.8) + idx * Inches(3.95)
    add_card(s9, dx, Inches(1.6), Inches(3.75), Inches(4.3))
    add_badge(s9, dx + Inches(0.2), Inches(1.8), Inches(1.2), Inches(0.32), dt, C_BLUE, C_WHITE, 10)
    
    tb = s9.shapes.add_textbox(dx + Inches(0.15), Inches(2.25), Inches(3.45), Inches(3.5))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = dsub
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(8)
    
    pb = tf.add_paragraph()
    pb.text = dbody
    pb.font.size = Pt(10)
    pb.font.color.rgb = C_TEXT_DARK

add_card(s9, Inches(0.8), Inches(6.1), Inches(11.7), Inches(1.0), C_LIGHT_BLUE, C_BLUE)
tb9_b = s9.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(11.3), Inches(0.9))
p = tb9_b.text_frame.paragraphs[0]
p.text = "※具体的なデザインや見せ方は確定事項ではなく、主催者様のご意向や各ブースの実際の写真素材に合わせて柔軟にご相談・調整いたします。"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_NAVY

# ====================================================
# ====================================================
# Slide 10: Psychological Basis (第6章 ① インフルエンサー起用の心理的根拠)
# ====================================================
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "Psychological Basis", "第6章 ①：インフルエンサー起用の心理的根拠（ウィンザー効果と三者関係）", "なぜ主催者の直接発信だけでなく、地域インフルエンサーとの「共同投稿」が必要なのか？")

# Left: Windsor Effect Box
add_card(s10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.3))
add_badge(s10, Inches(1.0), Inches(1.8), Inches(2.8), Inches(0.35), "行動心理：ウィンザー効果の活用", C_AMBER, C_WHITE, 10)

tb10_l = s10.shapes.add_textbox(Inches(1.0), Inches(2.25), Inches(5.2), Inches(3.5))
tf10_l = tb10_l.text_frame
tf10_l.word_wrap = True

p = tf10_l.paragraphs[0]
p.text = "第三者発信による「圧倒的な信頼性」"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

add_card(s10, Inches(1.0), Inches(2.7), Inches(5.2), Inches(1.3), C_LIGHT_RED, C_BORDER)
tb_comp1 = s10.shapes.add_textbox(Inches(1.15), Inches(2.75), Inches(4.9), Inches(1.2))
tb_comp1.text_frame.word_wrap = True
p = tb_comp1.text_frame.paragraphs[0]
p.text = "自社・主催者からの直接発信（広告離れ）"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_RED
p2 = tb_comp1.text_frame.add_paragraph()
p2.text = "「自分たちの催事は楽しいですよ」という企業広告は、警戒され流されやすい傾向にあります。"
p2.font.size = Pt(9)
p2.font.color.rgb = C_TEXT_DARK

add_card(s10, Inches(1.0), Inches(4.1), Inches(5.2), Inches(1.65), C_LIGHT_EMERALD, C_BORDER)
tb_comp2 = s10.shapes.add_textbox(Inches(1.15), Inches(4.15), Inches(4.9), Inches(1.55))
tb_comp2.text_frame.word_wrap = True
p = tb_comp2.text_frame.paragraphs[0]
p.text = "地域メディアを介した第三者発信（ウィンザー効果）"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_EMERALD
p2 = tb_comp2.text_frame.add_paragraph()
p2.text = "普段から信頼しているお出かけの達人が薦めることで、「遠くの企業広告」から「身近で信頼できる推奨品」へと昇華し、抜群の共感と納得を生みます。"
p2.font.size = Pt(9)
p2.font.color.rgb = C_TEXT_DARK

# Right: Tri-party Diagram
add_card(s10, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.3))
add_badge(s10, Inches(7.0), Inches(1.8), Inches(2.8), Inches(0.35), "三者関係構造：自然な拡散の循環", C_BLUE, C_WHITE, 10)

tb10_r = s10.shapes.add_textbox(Inches(7.0), Inches(2.25), Inches(5.3), Inches(0.5))
tf10_r = tb10_r.text_frame
tf10_r.word_wrap = True
p = tf10_r.paragraphs[0]
p.text = "事業者・インフルエンサー・生活者の共感構造"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

# 3 vertical cards
add_card(s10, Inches(7.0), Inches(2.75), Inches(5.3), Inches(0.85), C_BG_GRAY, C_BORDER)
tb_b1 = s10.shapes.add_textbox(Inches(7.1), Inches(2.8), Inches(5.1), Inches(0.75))
tb_b1.text_frame.word_wrap = True
p = tb_b1.text_frame.paragraphs[0]
p.text = "① 主催者・出店企業（産業フェアしずおか）"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_NAVY
p2 = tb_b1.text_frame.add_paragraph()
p2.text = "魅力的な体験・出店者素材・安心の公式情報を準備・提供"
p2.font.size = Pt(8.5)
p2.font.color.rgb = C_TEXT_MUTED

add_badge(s10, Inches(9.1), Inches(3.68), Inches(1.1), Inches(0.28), "PR連携・素材提供", C_BORDER_DARK, C_NAVY, 8.5)

add_card(s10, Inches(7.0), Inches(4.02), Inches(5.3), Inches(0.85), C_LIGHT_BLUE, C_BLUE)
tb_b2 = s10.shapes.add_textbox(Inches(7.1), Inches(4.07), Inches(5.1), Inches(0.75))
tb_b2.text_frame.word_wrap = True
p = tb_b2.text_frame.paragraphs[0]
p.text = "② 地域メディア（おちゃさん ＆ 静岡県ニュース速報）"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_BLUE
p2 = tb_b2.text_frame.add_paragraph()
p2.text = "普段通りの切り口で生活者へ紹介（共同投稿で17万人以上へ配信）"
p2.font.size = Pt(8.5)
p2.font.color.rgb = C_TEXT_DARK

add_badge(s10, Inches(9.1), Inches(4.93), Inches(1.1), Inches(0.28), "共同投稿・共感拡散", C_BORDER_DARK, C_NAVY, 8.5)

add_card(s10, Inches(7.0), Inches(5.27), Inches(5.3), Inches(0.85), C_LIGHT_AMBER, C_AMBER)
tb_b3 = s10.shapes.add_textbox(Inches(7.1), Inches(5.32), Inches(5.1), Inches(0.75))
tb_b3.text_frame.word_wrap = True
p = tb_b3.text_frame.paragraphs[0]
p.text = "③ 生活者（一般ファミリー・県民） ➔ 会場来場・UGC拡散"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_AMBER
p2 = tb_b3.text_frame.add_paragraph()
p2.text = "「身近なおすすめ」として受け入れ、来場後に自らSNS投稿（好循環）"
p2.font.size = Pt(8.5)
p2.font.color.rgb = C_TEXT_DARK

# Bottom banner
add_card(s10, Inches(0.8), Inches(6.05), Inches(11.7), Inches(0.9), C_CARD_BG, C_BORDER_DARK)
tb10_bot = s10.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(11.3), Inches(0.8))
tf10_bot = tb10_bot.text_frame
tf10_bot.word_wrap = True
p = tf10_bot.paragraphs[0]
p.text = "キーポイント：主催者の一方通行発信から、共感と信頼を獲得する協調型プロモーションへ"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_BLUE
p2 = tf10_bot.add_paragraph()
p2.text = "広告を敬遠する生活者に対し、地域に根ざしたインフルエンサーの推奨を介すことで、来場意欲を劇的に高めます。"
p2.font.size = Pt(9)
p2.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 11: Media Insights & Selection (第6章 ②③ メディア選定理由 ＆ 詳細インサイトデータ)
# ====================================================
s11 = prs.slides.add_slide(blank_layout)
add_header(s11, "Media Insights & Selection", "第6章 ②③：起用メディア2組の選定理由 ＆ 詳細インサイトデータ", "「なぜこの2組なのか？」県内最大級の圧倒的リーチ力と客観的実績数値")

# Left: おちゃさん
add_card(s11, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.3))
add_badge(s11, Inches(1.0), Inches(1.8), Inches(2.6), Inches(0.35), "メディア01：体験・感情・ファミリー", C_AMBER, C_WHITE, 10)

tb11_l = s11.shapes.add_textbox(Inches(1.0), Inches(2.25), Inches(5.2), Inches(3.5))
tf11_l = tb11_l.text_frame
tf11_l.word_wrap = True

p = tf11_l.paragraphs[0]
p.text = "静岡県コンシェルジュ（おちゃ さん）"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

p_sub = tf11_l.add_paragraph()
p_sub.text = "@shizuoka_info ｜ 県内最大級（17.3万人）の信頼"
p_sub.font.size = Pt(10)
p_sub.font.bold = True
p_sub.font.color.rgb = C_AMBER
p_sub.space_after = Pt(4)

# 3 Stat Cards inside Left
add_card(s11, Inches(1.0), Inches(2.85), Inches(1.65), Inches(0.7), C_LIGHT_AMBER, C_AMBER)
tb_s1 = s11.shapes.add_textbox(Inches(1.05), Inches(2.88), Inches(1.55), Inches(0.65))
tb_s1.text_frame.word_wrap = True
tb_s1.text_frame.paragraphs[0].text = "フォロワー数\n17.3 万人"
tb_s1.text_frame.paragraphs[0].font.size = Pt(9.5)
tb_s1.text_frame.paragraphs[0].font.bold = True
tb_s1.text_frame.paragraphs[0].font.color.rgb = C_NAVY
tb_s1.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

add_card(s11, Inches(2.75), Inches(2.85), Inches(1.75), Inches(0.7), C_BG_GRAY, C_BORDER)
tb_s2 = s11.shapes.add_textbox(Inches(2.8), Inches(2.88), Inches(1.65), Inches(0.65))
tb_s2.text_frame.word_wrap = True
tb_s2.text_frame.paragraphs[0].text = "平均閲覧数\n約 200,000 回"
tb_s2.text_frame.paragraphs[0].font.size = Pt(9.5)
tb_s2.text_frame.paragraphs[0].font.bold = True
tb_s2.text_frame.paragraphs[0].font.color.rgb = C_NAVY
tb_s2.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

add_card(s11, Inches(4.6), Inches(2.85), Inches(1.6), Inches(0.7), C_BG_GRAY, C_BORDER)
tb_s3 = s11.shapes.add_textbox(Inches(4.65), Inches(2.88), Inches(1.5), Inches(0.65))
tb_s3.text_frame.word_wrap = True
tb_s3.text_frame.paragraphs[0].text = "平均リーチ数\n約 70,000 件"
tb_s3.text_frame.paragraphs[0].font.size = Pt(9.5)
tb_s3.text_frame.paragraphs[0].font.bold = True
tb_s3.text_frame.paragraphs[0].font.color.rgb = C_NAVY
tb_s3.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

# Detail bullets
add_card(s11, Inches(1.0), Inches(3.65), Inches(5.2), Inches(2.15), C_CARD_BG, C_BORDER)
tb_d1 = s11.shapes.add_textbox(Inches(1.1), Inches(3.7), Inches(5.0), Inches(2.05))
tf_d1 = tb_d1.text_frame
tf_d1.word_wrap = True

pts_ocha = [
    "フォロワー属性：女性 54% / 男性 46%（子育て世代・主婦層中心）",
    "主要年齢層：18歳〜44歳（ファミリーお出かけ層が集中）",
    "得意エリア：静岡市 23%、浜松市 10%、富士市 8%（全県をカバー）",
    "アカウント価値：単なる有名人ではなく、県民の「週末お出かけインフラ」。フォロワーは行く気満々で閲覧するため、実際の来場行動力が桁違い。"
]
for idx, pt in enumerate(pts_ocha):
    p = tf_d1.paragraphs[0] if idx == 0 else tf_d1.add_paragraph()
    p.text = "・ " + pt
    p.font.size = Pt(8.5)
    p.font.color.rgb = C_TEXT_DARK
    p.space_after = Pt(2)

# Right: 静岡県ニュース速報
add_card(s11, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.3))
add_badge(s11, Inches(7.0), Inches(1.8), Inches(2.6), Inches(0.35), "メディア02：話題性・速報・県民層", C_BLUE, C_WHITE, 10)

tb11_r = s11.shapes.add_textbox(Inches(7.0), Inches(2.25), Inches(5.3), Inches(3.5))
tf11_r = tb11_r.text_frame
tf11_r.word_wrap = True

p = tf11_r.paragraphs[0]
p.text = "静岡県ニュース速報"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

p_sub = tf11_r.add_paragraph()
p_sub.text = "@shizuoka_news_ai ｜ 話題沸騰の地域ニュース速報"
p_sub.font.size = Pt(10)
p_sub.font.bold = True
p_sub.font.color.rgb = C_BLUE
p_sub.space_after = Pt(4)

# 3 Stat Cards inside Right
add_card(s11, Inches(7.0), Inches(2.85), Inches(1.65), Inches(0.7), C_LIGHT_BLUE, C_BLUE)
tb_s4 = s11.shapes.add_textbox(Inches(7.05), Inches(2.88), Inches(1.55), Inches(0.65))
tb_s4.text_frame.word_wrap = True
tb_s4.text_frame.paragraphs[0].text = "フォロワー数\n約 4,000 人"
tb_s4.text_frame.paragraphs[0].font.size = Pt(9.5)
tb_s4.text_frame.paragraphs[0].font.bold = True
tb_s4.text_frame.paragraphs[0].font.color.rgb = C_NAVY
tb_s4.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

add_card(s11, Inches(8.75), Inches(2.85), Inches(1.75), Inches(0.7), C_BG_GRAY, C_BORDER)
tb_s5 = s11.shapes.add_textbox(Inches(8.8), Inches(2.88), Inches(1.65), Inches(0.65))
tb_s5.text_frame.word_wrap = True
tb_s5.text_frame.paragraphs[0].text = "平均閲覧数\n約 10,000 回"
tb_s5.text_frame.paragraphs[0].font.size = Pt(9.5)
tb_s5.text_frame.paragraphs[0].font.bold = True
tb_s5.text_frame.paragraphs[0].font.color.rgb = C_NAVY
tb_s5.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

add_card(s11, Inches(10.6), Inches(2.85), Inches(1.7), Inches(0.7), C_BG_GRAY, C_BORDER)
tb_s6 = s11.shapes.add_textbox(Inches(10.65), Inches(2.88), Inches(1.6), Inches(0.65))
tb_s6.text_frame.word_wrap = True
tb_s6.text_frame.paragraphs[0].text = "平均リーチ数\n約 5,000 件"
tb_s6.text_frame.paragraphs[0].font.size = Pt(9.5)
tb_s6.text_frame.paragraphs[0].font.bold = True
tb_s6.text_frame.paragraphs[0].font.color.rgb = C_NAVY
tb_s6.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

# Detail bullets
add_card(s11, Inches(7.0), Inches(3.65), Inches(5.3), Inches(2.15), C_CARD_BG, C_BORDER)
tb_d2 = s11.shapes.add_textbox(Inches(7.1), Inches(3.7), Inches(5.1), Inches(2.05))
tf_d2 = tb_d2.text_frame
tf_d2.word_wrap = True

pts_news = [
    "フォロワー属性：男性 60% / 女性 40%（現役世代・ビジネス層）",
    "主要年齢層：25歳〜54歳（情報感度の高い現役県民層）",
    "得意エリア：静岡市 20%、浜松市 15%（都市部を中心に急成長）",
    "アカウント価値：運用数か月で1万再生連発。「【速報】今週末ツインメッセで大型催事開催！」という客観ニュース形式で、普段お出かけ情報を見ない層も強力に誘引。"
]
for idx, pt in enumerate(pts_news):
    p = tf_d2.paragraphs[0] if idx == 0 else tf_d2.add_paragraph()
    p.text = "・ " + pt
    p.font.size = Pt(8.5)
    p.font.color.rgb = C_TEXT_DARK
    p.space_after = Pt(2)

# Bottom Banner: Total Estimated Impact
add_card(s11, Inches(0.8), Inches(6.05), Inches(11.7), Inches(0.9), C_NAVY, C_NAVY)
tb11_tot = s11.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(11.3), Inches(0.8))
tf11_tot = tb11_tot.text_frame
tf11_tot.word_wrap = True
p = tf11_tot.paragraphs[0]
p.text = "【2組連携による想定合計波及効果】 想定閲覧数：300,000回以上 ｜ 想定獲得リーチ数：110,000アカウント獲得"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_WHITE
p.alignment = PP_ALIGN.CENTER

p2 = tf11_tot.add_paragraph()
p2.text = "体験特化メディア（おちゃさん）とニュース速報（静岡県ニュース速報）の完全補完により、県内全域へ圧倒的な熱量と話題性を届けます。"
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_LIGHT_BLUE
p2.alignment = PP_ALIGN.CENTER

# ====================================================
# Slide 12: Media Synergy & Details (第6章 ④ タッグ効果 ＆ 確定投稿計画)
# ====================================================
s12 = prs.slides.add_slide(blank_layout)
add_header(s12, "Media Synergy & Schedule", "第6章 ④：2組のタッグ効果 ＆ 確定投稿計画（合計3回）", "「体験の深掘り」×「ニュース速報」の完全補完で、県民全域へ抜け漏れなく届く布陣が完成")

add_card(s12, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb12_l = s12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf12_l = tb12_l.text_frame
tf12_l.word_wrap = True

p = tf12_l.paragraphs[0]
p.text = "この2組のタッグでしかできないこと"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

syn_pts = [
    ("体験の深掘り × ニュース速報の完全補完", "おちゃさんが「体験・感情（楽しそう！行きたい！）」を刺激し、静岡県ニュース速報が「話題性・速報性（今週末こんなイベントが！）」で注意を引きます。"),
    ("ファミリー層 ＆ 幅広い県民層の両取り", "「週末の家族お出かけ先を探す子育て世帯」と「地域の身近な話題を追う幅広い県民層」の双方に確実に届く完璧な布陣となります。"),
    ("共同投稿による既存枠の超越", "公式アカウント単独のフォロワー数に留まらず、おちゃさんの持つ17万人以上の読者画面へも直接届きます。")
]
for st, sd in syn_pts:
    p_t = tf12_l.add_paragraph()
    p_t.text = "・ " + st
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = C_BLUE
    p_t.space_before = Pt(8)
    
    p_d = tf12_l.add_paragraph()
    p_d.text = sd
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK

add_card(s12, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb12_r = s12.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf12_r = tb12_r.text_frame
tf12_r.word_wrap = True

p = tf12_r.paragraphs[0]
p.text = "起用メディア2組の確定投稿内容"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

m_posts = [
    ("おちゃさん 第1回", "11月15日(日)", "写真フィード ＋ ストーリーズ", "【開催約2週間前の認知拡大】\n会場の見どころをまとめ、お出かけ候補として保存促進。"),
    ("おちゃさん 第2回", "11月24日(火)", "動画リール ＋ ストーリーズ", "【直前の来場決定打】\n体験やグルメの魅力をショート動画で発信。「今週末行こう！」と後押し。"),
    ("静岡県ニュース速報", "11月24日(火)", "動画リール ＋ ストーリーズ", "【直前の速報】\n産業フェアの概要・見どころをニュース速報リールで紹介。地域の話題として拡散。")
]
for m_name, m_date, m_fmt, m_desc in m_posts:
    p_t = tf12_r.add_paragraph()
    p_t.text = f"[{m_name}] 実施日：{m_date}"
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = C_AMBER if "おちゃ" in m_name else C_BLUE
    p_t.space_before = Pt(6)
    
    p_d = tf12_r.add_paragraph()
    p_d.text = f"形式：{m_fmt}\n{m_desc}"
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 13: Safety & Pre-approval (第6章 ⑤ 事前審査体制フロー図解)
# ====================================================
s13 = prs.slides.add_slide(blank_layout)
add_header(s13, "Pre-Approval Flow", "第6章 ⑤：担当者が安心できる「安全・確実な事前審査体制」", "公的催事としての信頼性・品位を100%維持したまま、安全・確実にプロモーションを実施")

# Approval Flow Diagram (4 Boxes)
flow13_steps = [
    ("PHASE 01", "企画・制作", "インフルエンサーおよび事務局が、催事の趣旨に沿った投稿案（画像・動画・テキスト）を作成。"),
    ("PHASE 02", "事前提出", "公開の一定期間前に、すべての投稿原稿を事務局へ提出。"),
    ("PHASE 03", "内容確認・監修", "公的催事としての品位、誤認の有無、出店者情報の正確性を事務局にて厳格に審査・承認。"),
    ("PHASE 04", "公開・配信", "承認を受けた原稿のみをスケジュール通りに公開。無許可の投稿は100%防止。")
]

for idx, (p_tag, p_title, p_desc) in enumerate(flow13_steps):
    card_x = Inches(0.8) + idx * Inches(2.95)
    add_card(s13, card_x, Inches(1.8), Inches(2.75), Inches(3.2), C_BG_GRAY, C_BORDER)
    add_badge(s13, card_x + Inches(0.15), Inches(2.0), Inches(1.2), Inches(0.3), p_tag, C_EMERALD, C_WHITE, 10)
    
    tb = s13.shapes.add_textbox(card_x + Inches(0.15), Inches(2.45), Inches(2.45), Inches(2.4))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = p_title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    p_d = tf.add_paragraph()
    p_d.text = p_desc
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK
    
    if idx < 3:
        add_arrow(s13, card_x + Inches(2.8), Inches(3.2), Inches(0.15), Inches(0.35), C_EMERALD)

add_card(s13, Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.8), C_CARD_BG, C_EMERALD)
tb13_b = s13.shapes.add_textbox(Inches(1.0), Inches(5.4), Inches(11.3), Inches(1.6))
tf13_b = tb13_b.text_frame
tf13_b.word_wrap = True

p = tf13_b.paragraphs[0]
p.text = "事前審査体制の3つの約束"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_EMERALD

safe_promises = [
    "1. 事前承認のない公開は一切行いません（すべての発信物を事前にご確認いただきます）。",
    "2. 公的催事としての信頼性を損なう不適切な表現、誇大広告、公序良俗に反する内容は100%排除します。",
    "3. 出店者様向け情報や著名人出演情報など、権利関係の審査も事前に完全にクリアしてから発信します。"
]
for sp in safe_promises:
    pi = tf13_b.add_paragraph()
    pi.text = "・ " + sp
    pi.font.size = Pt(10)
    pi.font.color.rgb = C_TEXT_DARK
    pi.space_before = Pt(3)

# ====================================================
# Slide 14: Media Mechanism (第7章 ① 共同投稿の仕組み図解)
# ====================================================
s14 = prs.slides.add_slide(blank_layout)
add_header(s14, "Collaboration Mechanism", "第7章 ①：地域メディア連携でリーチと来場が確実に伸びる理由", "「身近なおすすめ」としての信頼感と、「共同投稿（コラボ機能）」による17万人以上への同時露出")

# Collaboration Diagram
add_card(s14, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.4), C_LIGHT_BLUE, C_BLUE)
tb14_col = s14.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(2.2))
tf14_col = tb14_col.text_frame
tf14_col.word_wrap = True

p = tf14_col.paragraphs[0]
p.text = "共同投稿（コラボレーション機能）の仕組み図解"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

add_card(s14, Inches(1.2), Inches(2.3), Inches(3.2), Inches(1.4), C_WHITE, C_BORDER)
tb_c1 = s14.shapes.add_textbox(Inches(1.3), Inches(2.4), Inches(3.0), Inches(1.2))
tb_c1.text_frame.word_wrap = True
tb_c1.text_frame.paragraphs[0].text = "公式アカウントの投稿\n（出店者リール等）"
tb_c1.text_frame.paragraphs[0].font.size = Pt(11)
tb_c1.text_frame.paragraphs[0].font.bold = True
tb_c1.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

plus_tb = s14.shapes.add_textbox(Inches(4.5), Inches(2.7), Inches(0.5), Inches(0.5))
plus_tb.text_frame.paragraphs[0].text = "＋"
plus_tb.text_frame.paragraphs[0].font.size = Pt(20)
plus_tb.text_frame.paragraphs[0].font.bold = True
plus_tb.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

add_card(s14, Inches(5.1), Inches(2.3), Inches(3.2), Inches(1.4), C_WHITE, C_BORDER)
tb_c2 = s14.shapes.add_textbox(Inches(5.2), Inches(2.4), Inches(3.0), Inches(1.2))
tb_c2.text_frame.word_wrap = True
tb_c2.text_frame.paragraphs[0].text = "インフルエンサー\n（おちゃさん 17.3万人）"
tb_c2.text_frame.paragraphs[0].font.size = Pt(11)
tb_c2.text_frame.paragraphs[0].font.bold = True
tb_c2.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

add_arrow(s14, Inches(8.45), Inches(2.8), Inches(0.4), Inches(0.4), C_BLUE)

add_card(s14, Inches(8.95), Inches(2.3), Inches(3.3), Inches(1.4), C_AMBER, C_AMBER)
tb_c3 = s14.shapes.add_textbox(Inches(9.0), Inches(2.4), Inches(3.2), Inches(1.2))
tb_c3.text_frame.word_wrap = True
p = tb_c3.text_frame.paragraphs[0]
p.text = "両方のタイムラインに\n【同時表示】！\n（17万人以上へ自動拡散）"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_WHITE
p.alignment = PP_ALIGN.CENTER

# 3 Supporting Points
s14_pts = [
    ("理由01: 身近なおすすめ", "企業からの宣伝ではなく、普段から見ているお出かけメディアの紹介だからこそ「遠くの広告」ではなく「身近なおすすめ」として信頼されます。"),
    ("理由02: ファミリー＆県民層", "子育て世代に強いおちゃさんと、ニュースを追う県民層に強い速報の2組で、産業フェアの多彩な魅力を全方位へ広げられます。"),
    ("理由03: 来場・口コミの好循環", "テレビCM・WEB・インスタで認知 ➔ 行きたいと保存・シェア ➔ HP確認 ➔ 来場 ➔ 会場写真を投稿して友達へ広がる自然な好循環を形成します。")
]
for idx, (st, sd) in enumerate(s14_pts):
    cx = Inches(0.8) + idx * Inches(3.95)
    add_card(s14, cx, Inches(4.3), Inches(3.75), Inches(2.6))
    tb = s14.shapes.add_textbox(cx + Inches(0.15), Inches(4.45), Inches(3.45), Inches(2.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = st
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(6)
    
    pd = tf.add_paragraph()
    pd.text = sd
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 15: ULSSAS Cycle (第7章 ② 行動プロセス「ULSSAS」来場促進サイクル)
# ====================================================
s15 = prs.slides.add_slide(blank_layout)
add_header(s15, "ULSSAS Cycle", "第7章 ②：SNS時代の行動プロセス「ULSSAS」による来場促進サイクル", "単発の広告表示で終わらせず、生活者の保存・検索・来場・クチコミ拡散が自走するサイクルを構築")

# 6 Horizontal Steps Flow (U -> L -> S -> S -> A -> S)
ulssas_steps = [
    ("U", "UGC / 発見", "共同投稿や出店者リール動画が「おすすめ・発見欄」に自動表示される。"),
    ("L", "Like / 保存", "「これ楽しそう！」「今週末行きたい！」と直感的にいいね・保存される。"),
    ("S", "Search 1", "Instagram内で公式アカウントや出店情報、ハッシュタグをチェック。"),
    ("S", "Search 2", "Google等で「産業フェア」を検索し、駐車場や特設サイト詳細を確認。"),
    ("A", "Action / 来場", "会期当日（11/28・29）、家族や友人とツインメッセ静岡へ満員来場！"),
    ("S", "Spread / 拡散", "「楽しかった！」と来場者自身が会場写真をSNS投稿 ➔ 次のUGCへ循環！")
]

for idx, (u_char, u_title, u_desc) in enumerate(ulssas_steps):
    card_x = Inches(0.8) + idx * Inches(1.97)
    
    bg_c = C_LIGHT_AMBER if idx >= 4 else C_BG_GRAY
    bd_c = C_AMBER if idx >= 4 else C_BORDER
    
    add_card(s15, card_x, Inches(1.7), Inches(1.85), Inches(3.6), bg_c, bd_c)
    
    badge_c = C_AMBER if idx >= 4 else C_BLUE
    add_badge(s15, card_x + Inches(0.42), Inches(1.9), Inches(1.0), Inches(0.55), u_char, badge_c, C_WHITE, 16)
    
    tb = s15.shapes.add_textbox(card_x + Inches(0.1), Inches(2.6), Inches(1.65), Inches(2.6))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = u_title
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(4)
    
    pd = tf.add_paragraph()
    pd.text = u_desc
    pd.font.size = Pt(8.5)
    pd.font.color.rgb = C_TEXT_DARK
    
    if idx < 5:
        add_arrow(s15, card_x + Inches(1.88), Inches(3.2), Inches(0.08), Inches(0.25), C_BLUE)

# Bottom: Strengths of ULSSAS Model
add_card(s15, Inches(0.8), Inches(5.5), Inches(11.7), Inches(1.5), C_LIGHT_BLUE, C_BLUE)
tb15_b = s15.shapes.add_textbox(Inches(1.0), Inches(5.6), Inches(11.3), Inches(1.3))
tf15_b = tb15_b.text_frame
tf15_b.word_wrap = True

p = tf15_b.paragraphs[0]
p.text = "ULSSASモデルがもたらす「自走型プロモーション」の3大強み"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_BLUE

strengths = [
    "1. 広告費に依存しない自走力：良質なリール動画とインフルエンサー投稿が起点となり、ユーザー自らの保存・検索を誘発。",
    "2. 迷いをなくす2段階検索：SNSで雰囲気を掴み（Search1）、WEB検索で安心の公式情報（Search2）へ誘導し来場を決定づける。",
    "3. 当日の来場者が次の宣伝役に：会場での楽しい体験が「Spread（拡散）」され、2日目の動員や次回開催の資産へ直結。"
]
for st in strengths:
    pi = tf15_b.add_paragraph()
    pi.text = "・ " + st
    pi.font.size = Pt(9.5)
    pi.font.color.rgb = C_TEXT_DARK
    pi.space_before = Pt(2)

# Slide 16: Vendor Reels Concept (第8章 出店者リール・アルゴリズム対比)
# ====================================================
s16 = prs.slides.add_slide(blank_layout)
add_header(s16, "Vendor Reels Mechanism", "第8章：出店者様ご紹介（5本投稿・最大15社）リール動画企画", "通常投稿とリール動画のアルゴリズム対比。おすすめ画面への自動拡散で来場者を増やす")

# Left: Comparison Box
add_card(s16, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb16_l = s16.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf16_l = tb16_l.text_frame
tf16_l.word_wrap = True

p = tf16_l.paragraphs[0]
p.text = "通常投稿 vs リール動画（拡散の仕組み）"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

add_card(s16, Inches(1.0), Inches(2.3), Inches(5.2), Inches(1.6), C_LIGHT_RED, C_BORDER)
tb_ng = s16.shapes.add_textbox(Inches(1.15), Inches(2.4), Inches(4.9), Inches(1.4))
tf_ng = tb_ng.text_frame
tf_ng.word_wrap = True
p = tf_ng.paragraphs[0]
p.text = "【通常の写真投稿】フォロワーだけに届く（狭い輪）"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_RED
p2 = tf_ng.add_paragraph()
p2.text = "アカウントをフォローしている人だけにしか届かず、まだ産業フェアを知らない新規層へ情報が広がりません。"
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_DARK

add_card(s16, Inches(1.0), Inches(4.1), Inches(5.2), Inches(2.4), C_LIGHT_EMERALD, C_BORDER)
tb_ok = s16.shapes.add_textbox(Inches(1.15), Inches(4.2), Inches(4.9), Inches(2.2))
tf_ok = tb_ok.text_frame
tf_ok.word_wrap = True
p = tf_ok.paragraphs[0]
p.text = "【リール（ショート動画）】未認知層へ自動拡散（広い輪）"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_EMERALD
p2 = tf_ok.add_paragraph()
p2.text = "Instagramのアルゴリズムにより、静岡県内の子育て・グルメ関心層の「おすすめ画面」へ次々と自動表示されます。フォロワー数に関係なく、県民全体へ届くため来場者数が確実に伸びます。"
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_DARK

# Right: 5 Steps to Visit
add_card(s16, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb16_r = s16.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf16_r = tb16_r.text_frame
tf16_r.word_wrap = True

p = tf16_r.paragraphs[0]
p.text = "認知から来場へ繋がる5つのステップ"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY

steps14 = [
    ("ステップ01: 発見", "おすすめ画面に「楽しそう！美味しそう！」なリールが自動表示。"),
    ("ステップ02: 興味", "職人の手元や限定グルメを見て「このお店に行ってみたい！」と関心。"),
    ("ステップ03: 詳細", "案内から公式ホームページへ遷移し、開催日・会場アクセスを確認。"),
    ("ステップ04: 保存・共有", "「週末ここ行こう！」と投稿を保存し、家族やママ友にLINEで共有。"),
    ("ステップ05: 来場", "目的の店舗や体験を目指してツインメッセ静岡へご来場！")
]
for idx, (st, sd) in enumerate(steps14):
    y_s = Inches(2.3) + idx * Inches(0.9)
    add_badge(s16, Inches(7.0), y_s, Inches(1.6), Inches(0.3), st, C_BLUE, C_WHITE, 9.5)
    tb_sd = s16.shapes.add_textbox(Inches(7.0), y_s + Inches(0.32), Inches(5.3), Inches(0.55))
    tf_sd = tb_sd.text_frame
    tf_sd.word_wrap = True
    p = tf_sd.paragraphs[0]
    p.text = sd
    p.font.size = Pt(9)
    p.font.color.rgb = C_TEXT_DARK

# Save progress
prs.save("/Users/sap220701/Desktop/産業フェア_ローカル/docs/02_プロモーション計画/クライアント説明用_WEBプロモーション統合計画書_2026.pptx")
print("Saved up to slide 14")

# ====================================================
# Slide 17: Vendor Shooting Guidelines ① (第9章 撮影ルール・OK/NG対比)
# ====================================================
s17 = prs.slides.add_slide(blank_layout)
add_header(s17, "Shooting Rules", "第9章 ①：出店者様向け 動画の基本仕様 ＆ 失敗しない4つの撮影ルール", "スマホで撮影して送るだけ。編集・文字入れは一切不要。誰でも簡単に撮影できる実践ルール")

rules15 = [
    ("ルール 01", "カメラを固定して撮る", "手ブレの防止", "NG: カメラを激しく動かしたりズームする\nOK: 構図を決めたら「5〜10秒間じっと固定」して撮影。"),
    ("ルール 02", "「全体」と「アップ」を撮る", "映像のメリハリ向上", "NG: お店全体の引きの映像だけ\nOK: 全体に加え、職人の手元や商品アップの2カットを用意。"),
    ("ルール 03", "現場の音はそのままでOK", "リアルな臨場感", "NG: 無理に無音にしたりBGMを後付けする\nOK: 調理音や作業音、会場の熱気をそのまま録音（私語のみ注意）。"),
    ("ルール 04", "無加工のまま送るだけ", "編集・加工は不要", "NG: スマホアプリで文字やフィルターを入れる\nOK: 撮ったそのままの元データを送信。事務局でプロ編集。")
]

for idx, (r_tag, r_title, r_sub, r_desc) in enumerate(rules15):
    rx = Inches(0.8) + idx * Inches(2.95)
    add_card(s17, rx, Inches(1.6), Inches(2.8), Inches(3.4))
    add_badge(s17, rx + Inches(0.15), Inches(1.8), Inches(1.0), Inches(0.3), r_tag, C_BLUE, C_WHITE, 9.5)
    
    tb = s17.shapes.add_textbox(rx + Inches(0.1), Inches(2.2), Inches(2.6), Inches(2.6))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = r_title
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    
    ps = tf.add_paragraph()
    ps.text = f"[{r_sub}]"
    ps.font.size = Pt(9.5)
    ps.font.bold = True
    ps.font.color.rgb = C_AMBER
    ps.space_after = Pt(4)
    
    pd = tf.add_paragraph()
    pd.text = r_desc
    pd.font.size = Pt(9)
    pd.font.color.rgb = C_TEXT_DARK

add_card(s17, Inches(0.8), Inches(5.2), Inches(11.7), Inches(1.8), C_LIGHT_BLUE, C_BLUE)
tb17_b = s17.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.3), Inches(1.6))
tf17_b = tb17_b.text_frame
tf17_b.word_wrap = True

p = tf17_b.paragraphs[0]
p.text = "出店者様にお願いする動画の基本仕様"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY

specs15 = [
    ("撮影の向き", "スマートフォン縦向き（9:16 縦画面）リール動画は縦画面いっぱいに表示されるため"),
    ("カット数", "10カット程度（難しければ5カット以上）素材が多いほど編集の質が上がり見応えが出ます"),
    ("1カットの長さ", "5秒〜10秒程度（手ブレを防ぎ、テンポよく切り替えるため）"),
    ("編集の有無", "編集・文字入れ・BGMは一切不要（事務局にて統一感のあるプロの編集を行います）")
]
for st, sd in specs15:
    pi = tf17_b.add_paragraph()
    pi.text = f"・ {st}：{sd}"
    pi.font.size = Pt(9.5)
    pi.font.color.rgb = C_TEXT_DARK
    pi.space_before = Pt(2)

# ====================================================
# Slide 18: Vendor Guidelines ② (第9章 撮影ガイド②)
# ====================================================
s18 = prs.slides.add_slide(blank_layout)
add_header(s18, "Submission Flow", "第9章 ②：撮影対象例・確認シート ＆ ご提出フロー", "出店者が迷わない具体例の提示と専用フォームによるスムーズな回収体制（10/23締切）")

add_card(s18, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb18_l = s18.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf18_l = tb18_l.text_frame
tf18_l.word_wrap = True

p = tf18_l.paragraphs[0]
p.text = "撮影対象の具体例 ＆ 確認シート項目"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

p_target = tf18_l.add_paragraph()
p_target.text = "\n[撮影シーンの具体例]"
p_target.font.size = Pt(11.5)
p_target.font.bold = True
p_target.font.color.rgb = C_BLUE

t_examples = [
    "お店・会社の顔：外観、看板、入口、のれん",
    "空間・雰囲気：店内全体の様子、ブースのレイアウト",
    "商品・サービス：販売するイチ押し商品、体験キット",
    "職人・製造の様子：職人の手元作業、工程アップ（大人気シーン）",
    "スタッフの様子：笑顔の接客風景、真剣な表情"
]
for te in t_examples:
    pi = tf18_l.add_paragraph()
    pi.text = "・ " + te
    pi.font.size = Pt(9.5)
    pi.font.color.rgb = C_TEXT_DARK

p_sheet = tf18_l.add_paragraph()
p_sheet.text = "\n[同時に提出いただく確認シート]"
p_sheet.font.size = Pt(11.5)
p_sheet.font.bold = True
p_sheet.font.color.rgb = C_AMBER

s_examples = [
    "店舗名、所在地、Instagramアカウント、HP URL",
    "事業コンセプト、主な商品、こだわり",
    "イチ押し商品・体験名、価格、来場者へのメッセージ"
]
for se in s_examples:
    pi = tf18_l.add_paragraph()
    pi.text = "・ " + se
    pi.font.size = Pt(9.5)
    pi.font.color.rgb = C_TEXT_DARK

add_card(s18, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb18_r = s18.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf18_r = tb18_r.text_frame
tf18_r.word_wrap = True

p = tf18_r.paragraphs[0]
p.text = "ご案内とご提出の流れ（スマホ専用フォーム）"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

flow18 = [
    ("ステップ01", "ご案内シートの配布", "出店確定後、出店者様へ撮影要綱と入力フォームのURLをご案内。"),
    ("ステップ02", "スマホから直接送信", "専用フォームから、スマホで撮影した写真・動画をそのままアップロード。"),
    ("ステップ03", "事務局による統一編集", "事務局側で統一テンプレートに沿って高品質に編集し、事前に確認。"),
    ("提出期日", "10月23日(金) 素材提出締切", "10月25日の公式運用開始・11月上旬の投稿展開に向け、余裕を持った期日で回収。")
]
for tag, ft, fd in flow18:
    p_t = tf18_r.add_paragraph()
    p_t.text = f"[{tag}] {ft}"
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = C_EMERALD if "締切" in ft else C_BLUE
    p_t.space_before = Pt(8)
    
    p_d = tf18_r.add_paragraph()
    p_d.text = fd
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 19: Instagram Ads Strategy ① (第10章 カルーセルUI図解)
# ====================================================
s19 = prs.slides.add_slide(blank_layout)
add_header(s19, "Carousel UI Design", "第10章：Instagram広告戦略①：人気投稿の活用 ＆ 画像スライド", "反響の大きい「画像スライド（カルーセル）」と「インフルエンサー投稿」を活用")

add_card(s19, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.6), C_LIGHT_BLUE, C_BLUE)
tb19_top = s19.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(2.4))
tf19_top = tb19_top.text_frame
tf19_top.word_wrap = True

p = tf19_top.paragraphs[0]
p.text = "正方形5枚スライド広告（カルーセル広告）の画面構成イメージ"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY

c_slides = [
    ("1枚目（表紙）", "「入場無料！週末どこ行く？」と目を引く表紙。スワイプを促す導線設計"),
    ("2枚目（見どころ）", "「28日よしもと芸人登場！」ジョイマン・ぬまんづの写真・紹介"),
    ("3枚目（見どころ）", "「29日ポムポムプリン＆シナモロール！」ステージ案内"),
    ("4枚目（体験・食）", "「木工体験＆絶品静岡グルメ！」家族で楽しめるブース紹介"),
    ("5枚目（案内）", "「開催日時・ツインメッセ静岡アクセス・公式HP案内」")
]
for idx, (c_num, c_txt) in enumerate(c_slides):
    bx = Inches(1.0) + idx * Inches(2.26)
    add_card(s19, bx, Inches(2.2), Inches(2.15), Inches(1.8), C_WHITE, C_BORDER)
    tb_c = s19.shapes.add_textbox(bx + Inches(0.08), Inches(2.25), Inches(2.0), Inches(1.7))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = c_num
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    p_b = tf_c.add_paragraph()
    p_b.text = c_txt
    p_b.font.size = Pt(8.5)
    p_b.font.color.rgb = C_TEXT_DARK
    p_b.space_before = Pt(3)

# Bottom Row: Influencer Ad & Request
add_card(s19, Inches(0.8), Inches(4.4), Inches(5.6), Inches(2.5))
tb19_l = s19.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.2), Inches(2.3))
tf19_l = tb19_l.text_frame
tf19_l.word_wrap = True
p = tf19_l.paragraphs[0]
p.text = "地元人気投稿の広告二次活用"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY
p2 = tf19_l.add_paragraph()
p2.text = "・ 主催者の一方的な宣伝ではなく、普段から親しまれているインフルエンサーの投稿として配信。\n・ 読者に警戒されず自然に受け入れられ、高い保存率と関心を集めます。"
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_DARK
p2.space_before = Pt(4)

add_card(s19, Inches(6.8), Inches(4.4), Inches(5.7), Inches(2.5))
tb19_r = s19.shapes.add_textbox(Inches(7.0), Inches(4.5), Inches(5.3), Inches(2.3))
tf19_r = tb19_r.text_frame
tf19_r.word_wrap = True
p = tf19_r.paragraphs[0]
p.text = "広告配信に向けた事前準備・ご協力のお願い"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_AMBER
p2 = tf19_r.add_paragraph()
p2.text = "・ 公式Instagramアカウントの共有：連携・管理設定のためアカウント共有をお願いいたします。\n・ Facebookページ等の操作：配信システムの仕様上、連携ページの操作をお願いする場合があります。\n※設定手順は弊社にて丁寧にサポート・ご案内いたします。"
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_DARK
p2.space_before = Pt(4)

# ====================================================
# Slide 20: Instagram Ads Strategy ② (第11章 ターゲティング)
# ====================================================
s20 = prs.slides.add_slide(blank_layout)
add_header(s20, "Audience Settings", "第11章：Instagram広告戦略②：配信対象の詳細設定と見込み人数", "Instagram（Meta）公式管理画面にて試算・検証済みの確実な配信設定（約15.5万〜18.2万人）")

tbl18_s = s20.shapes.add_table(6, 2, Inches(0.8), Inches(1.6), Inches(11.7), Inches(3.6))
tbl18 = tbl18_s.table
tbl18.columns[0].width = Inches(3.2)
tbl18.columns[1].width = Inches(8.5)

h18 = ["項目", "設定内容（どのような人にお届けするか）"]
for i, h in enumerate(h18):
    cell = tbl18.cell(0, i)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

r18 = [
    ("お届けする地域", "静岡県内8市町限定（お住まいの方・滞在している方）\n（静岡市、焼津市、藤枝市、富士市、島田市、吉田町、牧之原市、富士宮市）"),
    ("年齢・性別", "25歳〜45歳の男女（お出かけ先を決めるお父さん・お母さん世代）"),
    ("家族・子育て", "子育て（育児・子ども）に関心がある方"),
    ("お買い物・趣味", "おもちゃ（玩具）に関心がある方"),
    ("その他の関心事", "工作・DIYのアイデア / サンリオ / ハローキティ / 教育・学習 / お祭り・イベント / 子ども・子育て / 木工・工芸")
]
for r_i, r_data in enumerate(r18, start=1):
    for c_i, val in enumerate(r_data):
        cell = tbl18.cell(r_i, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_BG_GRAY if r_i % 2 == 1 else C_WHITE
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(9.5)
        if c_i == 0:
            p.font.bold = True
            p.alignment = PP_ALIGN.CENTER

add_card(s20, Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.6), C_LIGHT_BLUE, C_BLUE)
tb20_b = s20.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(11.3), Inches(1.4))
tf20_b = tb20_b.text_frame
tf20_b.word_wrap = True

p = tf20_b.paragraphs[0]
p.text = "広告が届く見込みの人数（Meta公式試算結果）"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY

p2 = tf20_b.add_paragraph()
p2.text = "・ 対象となる人数：約154,600人 〜 181,900人 ｜ 想定表示回数：約 28.3 万回\n・ 8市町にお住まいの25〜45歳で、子育てやイベントに関心がある方に絞っても約15.5万〜18.2万人の十分な規模があります。期間中に一人あたり複数回しっかり案内が届く、ちょうど良い規模感です。"
p2.font.size = Pt(10.5)
p2.font.color.rgb = C_TEXT_DARK
p2.space_before = Pt(3)

# ====================================================
# Slide 21: Google Ads Strategy (第12・13章 Google広告)
# ====================================================
s21 = prs.slides.add_slide(blank_layout)
add_header(s21, "Google Display Ads", "第12・13章：Google広告戦略：掲載場所と配信の仕組み", "地元のニュースサイトやブログ、YouTube画面へ約134.1万回表示。関心・検索語句で捕捉")

add_card(s21, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb21_l = s21.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf21_l = tb21_l.text_frame
tf21_l.word_wrap = True

p = tf21_l.paragraphs[0]
p.text = "掲載場所とスマート配信の仕組み"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

g_pts = [
    ("世界最大手のGoogleネットワーク", "静岡県民が普段見ている地元ニュースサイト、天気予報、YouTubeの画面などに自然にバナーを表示します。"),
    ("1つのまとまりで無駄なく賢く配信", "興味のない人へ無差別に配るのではなく、AIが過去の閲覧傾向から関心の高いユーザーへ自動最適配分します。"),
    ("最適な画面サイズに自動調整", "スマホ、パソコン、タブレットなど、見る人の端末に合わせて最も美しく読みやすい形に自動組み替えて表示されます。")
]
for gt, gd in g_pts:
    p_t = tf21_l.add_paragraph()
    p_t.text = "・ " + gt
    p_t.font.size = Pt(12)
    p_t.font.bold = True
    p_t.font.color.rgb = C_BLUE
    p_t.space_before = Pt(8)
    
    p_d = tf21_l.add_paragraph()
    p_d.text = gd
    p_d.font.size = Pt(10)
    p_d.font.color.rgb = C_TEXT_DARK

add_card(s21, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb21_r = s21.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf21_r = tb21_r.text_frame
tf21_r.word_wrap = True

p = tf21_r.paragraphs[0]
p.text = "配信対象の詳細設定（関心・検索キーワード）"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

g_target_details = [
    ("子ども・子育て向け", "未就学児・小学生の子どもを持つ保護者、家族レジャーに関心のある層"),
    ("検索キーワード連動（カスタム）", "「静岡市 イベント」「ツインメッセ」「ポムポムプリン」「シナモロール」「木工体験」「よしもとお笑い」などを最近検索した人"),
    ("地場産業・グルメ関心層", "静岡グルメ、物産展、DIY、伝統工芸に関心のある幅広い県民"),
    ("想定表示回数", "静岡県内8市町限定で 約134.1万回 の表示を予定")
]
for gt, gd in g_target_details:
    p_t = tf21_r.add_paragraph()
    p_t.text = "[設定] " + gt
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = C_AMBER
    p_t.space_before = Pt(8)
    
    p_d = tf21_r.add_paragraph()
    p_d.text = gd
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 22: Yahoo! & LINE Ads Strategy (第14・15章 Yahoo/LINE)
# ====================================================
s22 = prs.slides.add_slide(blank_layout)
add_header(s22, "Yahoo! & LINE Ads", "第14・15章：Yahoo!・LINE広告戦略：掲載場所とターゲティング", "LINEトーク最上部＆Yahoo!トップ画面。全世代を網羅する日常動線へ約134.1万回表示")

add_card(s22, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb22_l = s22.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf22_l = tb22_l.text_frame
tf22_l.word_wrap = True

p = tf22_l.paragraphs[0]
p.text = "掲載場所と媒体の強み"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

y_pts = [
    ("LINEのトーク画面の最上部", "静岡県民の大半が毎日家族や友人とやりとりするLINEのトーク一覧トップに表示。日常の視線動線に自然に入り込みます。"),
    ("Yahoo!JAPANのトップ・ニュース", "日本最大級のポータルサイト。普段SNSをあまり使わないお父さん世代やシニア層へも確実に情報が届きます。"),
    ("全世代を網羅する包容力", "Instagram（若年〜子育て主婦層）に加え、LINE・Yahoo!で家族全員（父母・祖父母）を全方位カバーします。")
]
for yt, yd in y_pts:
    p_t = tf22_l.add_paragraph()
    p_t.text = "・ " + yt
    p_t.font.size = Pt(12)
    p_t.font.bold = True
    p_t.font.color.rgb = C_BLUE
    p_t.space_before = Pt(8)
    
    p_d = tf22_l.add_paragraph()
    p_d.text = yd
    p_d.font.size = Pt(10)
    p_d.font.color.rgb = C_TEXT_DARK

add_card(s22, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb22_r = s22.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf22_r = tb22_r.text_frame
tf22_r.word_wrap = True

p = tf22_r.paragraphs[0]
p.text = "サーチ・行動ターゲティングの詳細"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

y_target_details = [
    ("Yahoo!検索キーワード（サーチターゲティング）", "直近で「静岡 イベント」「週末 お出かけ」「サンリオ」「お笑いライブ」などを検索した人に狙い撃ち配信。"),
    ("LINE興味・関心ターゲティング", "「ショッピング・グルメ」「ファミリー・子育て」「レジャー」など、登録行動データに基づく高精度ターゲティング。"),
    ("想定表示回数", "静岡県内8市町限定で 約134.1万回 の表示を予定（Googleと同規模の強力な動線）")
]
for yt, yd in y_target_details:
    p_t = tf22_r.add_paragraph()
    p_t.text = "[設定] " + yt
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = C_AMBER
    p_t.space_before = Pt(8)
    
    p_d = tf22_r.add_paragraph()
    p_d.text = yd
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 23: Creative & Copy Examples (第16章 広告クリエイティブ案)
# ====================================================
s23 = prs.slides.add_slide(blank_layout)
add_header(s23, "Ad Creatives", "第16章：広告クリエイティブ（文章・画像）の具体案", "各広告媒体の文字数制限を厳格にクリアした、来場意欲を刺激する実践的な広告文案")

c_cards = [
    ("Instagram広告", [
        ("メインテキスト", "11/28(土)・29(日)ツインメッセ静岡！よしもと芸人＆サンリオキャラクターが登場！木工体験や静岡グルメも満載の産業フェアしずおかへGO！"),
        ("画像の中の文字", "「28日ジョイマン＆ぬまんづ！」「29日ポムポムプリン＆シナモロール！」"),
        ("ボタンの文字", "「詳細を見る」")
    ], C_AMBER),
    ("Google広告（バナー）", [
        ("短い見出し（15文字以内）", "【入場無料】産業フェアしずおか\n週末はツインメッセ静岡へ！"),
        ("長い見出し（45文字以内）", "28日よしもと芸人／29日ポムポムプリン登場！体験＆グルメ満載"),
        ("説明の文章（45文字以内）", "11/28・29ツインメッセ静岡！ステージや工作体験、静岡グルメが大集合！入場無料")
    ], C_BLUE),
    ("Yahoo!・LINE広告", [
        ("LINEトーク最上部（18文字）", "【入場無料】ツインメッセ静岡イベント！"),
        ("Yahoo!タイトル（20文字）", "28日ジョイマン／29日プリン登場！"),
        ("Yahoo!説明文章（44文字）", "11/28・29ツインメッセ静岡！工作体験や静岡グルメ、豪華ステージが大集合！入場無料")
    ], C_EMERALD)
]

for idx, (ct, citems, col) in enumerate(c_cards):
    cx = Inches(0.8) + idx * Inches(3.95)
    add_card(s23, cx, Inches(1.6), Inches(3.75), Inches(5.3))
    add_badge(s23, cx + Inches(0.2), Inches(1.8), Inches(3.35), Inches(0.35), ct, col, C_WHITE, 11)
    
    tb = s23.shapes.add_textbox(cx + Inches(0.15), Inches(2.25), Inches(3.45), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    
    for ititle, itxt in citems:
        pt = tf.add_paragraph()
        pt.text = f"[{ititle}]"
        pt.font.size = Pt(10.5)
        pt.font.bold = True
        pt.font.color.rgb = C_NAVY
        pt.space_before = Pt(6)
        
        pd = tf.add_paragraph()
        pd.text = itxt
        pd.font.size = Pt(9.5)
        pd.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 24: Optional Add-on (第17章 テンプレート投稿量産スキーム図解)
# ====================================================
s24 = prs.slides.add_slide(blank_layout)
add_header(s24, "Template Options Flow", "第17章：【追加オプション案】出店者様紹介「テンプレート投稿」の展開", "決定事項ではなく、公式アカウントの投稿数・露出ボリュームをさらに増やしたい場合の選択肢")

# Top: Process Diagram (3 Boxes)
add_card(s24, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.2), C_LIGHT_BLUE, C_BLUE)
tb24_top = s24.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(2.0))
tf24_top = tb24_top.text_frame
tf24_top.word_wrap = True
p = tf24_top.paragraphs[0]
p.text = "1つの共通デザイン枠で手軽に量産するスキーム図解"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY

flow24 = [
    ("出店者様より", "写真・情報のご提供\n（静止画1〜2枚＋文章）"),
    ("事務局にて", "共通デザイン枠に\n写真・テキストを配置"),
    ("公式SNSから", "統一感のある投稿を\nテンポよく大量発信！")
]
for idx, (f_head, f_body) in enumerate(flow24):
    bx = Inches(1.2) + idx * Inches(3.8)
    add_card(s24, bx, Inches(2.2), Inches(3.0), Inches(1.3), C_WHITE, C_BORDER)
    tb_fb = s24.shapes.add_textbox(bx + Inches(0.1), Inches(2.3), Inches(2.8), Inches(1.1))
    tf_fb = tb_fb.text_frame
    tf_fb.word_wrap = True
    p = tf_fb.paragraphs[0]
    p.text = f_head
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf_fb.add_paragraph()
    p2.text = f_body
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = C_TEXT_DARK
    p2.alignment = PP_ALIGN.CENTER
    
    if idx < 2:
        add_arrow(s24, bx + Inches(3.15), Inches(2.7), Inches(0.5), Inches(0.35), C_BLUE)

# Bottom: 3 Benefits
b_op = [
    ("メリット 01", "より多くの出店者様をPR可能", "リール動画（15社）から溢れた店舗や、動画撮影が難しい店舗も含め、広く公平に紹介機会を提供できます。"),
    ("メリット 02", "アカウントの統一感と見やすさ", "デザインの揃った美しい投稿が並ぶことで、公式アカウントの信頼性・見栄え・品位が高まります。"),
    ("メリット 03", "出店者様ご自身による拡散", "「公式で紹介されました！」と出店者様自身が自分のSNSでシェアしやすくなり、外部への波及効果が加速します。")
]
for idx, (btag, btitle, bdesc) in enumerate(b_op):
    cx = Inches(0.8) + idx * Inches(3.95)
    add_card(s24, cx, Inches(4.0), Inches(3.75), Inches(2.9))
    add_badge(s24, cx + Inches(0.2), Inches(4.2), Inches(1.2), Inches(0.3), btag, C_AMBER, C_WHITE, 10)
    
    tb = s24.shapes.add_textbox(cx + Inches(0.15), Inches(4.6), Inches(3.45), Inches(2.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = btitle
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    pd = tf.add_paragraph()
    pd.text = bdesc
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = C_TEXT_DARK

# ====================================================
# Slide 25: Summary & Next Steps (第18章 まとめと進め方)
# ====================================================
s25 = prs.slides.add_slide(blank_layout)
add_header(s25, "Summary & Next Steps", "第18章：まとめ ＆ 今後の進め方・ご確認事項", "本計画の強みを活かし、安心・確実なプロモーション準備を進めてまいります")

add_card(s25, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
tb25_l = s25.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
tf25_l = tb25_l.text_frame
tf25_l.word_wrap = True

p = tf25_l.paragraphs[0]
p.text = "本計画の3つの強み"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

str_pts = [
    ("高い情報伝達力（4層連携）", "テレビCM・WEB広告と地域メディア（2組）の連携により、子育て世代へイベントの魅力をダイレクトにお届け。"),
    ("地域密着・確実なお届け", "静岡県内8市町の子育て世代（約15.5万〜18.2万人）へ、期間中しっかりと複数回お届け（約296.6万回表示）。"),
    ("分かりやすい結果のご報告", "アクセス解析や広告レポートを用いて、「何回表示され、何人が見に来たか」を明確にご報告いたします。")
]
for st, sd in str_pts:
    p_t = tf25_l.add_paragraph()
    p_t.text = "・ " + st
    p_t.font.size = Pt(11.5)
    p_t.font.bold = True
    p_t.font.color.rgb = C_BLUE
    p_t.space_before = Pt(8)
    
    p_d = tf25_l.add_paragraph()
    p_d.text = sd
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = C_TEXT_DARK

add_card(s25, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
tb25_r = s25.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
tf25_r = tb25_r.text_frame
tf25_r.word_wrap = True

p = tf25_r.paragraphs[0]
p.text = "今後のお願い・ご確認事項"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY

reqs = [
    "1. 本計画内容についてのご確認・ご了承",
    "2. 起用メディア2組（静岡県コンシェルジュ様、静岡県ニュース速報様）の投稿スケジュール（11/15・11/24）および広告連携の最終確認",
    "3. 出店者様向けのご案内（撮影要綱・申請フォーム・動画提供依頼）の配布と素材収集（10月23日(金) 素材締切）",
    "4. 公式Instagramの全体概要投稿（10月25日(日)仮設定・HP更新連動）用素材のご共有",
    "5. Instagram広告配信に伴う連携のご協力（公式アカウントの共有、およびFacebookページ等の操作・権限付与のお願い）"
]
for rq in reqs:
    p_q = tf25_r.add_paragraph()
    p_q.text = rq
    p_q.font.size = Pt(10)
    p_q.font.color.rgb = C_TEXT_DARK
    p_q.space_before = Pt(6)

p_foot = tf25_r.add_paragraph()
p_foot.text = "\n※ご不明な点や調整のご要望がございましたら、いつでもお気軽にお申し付けください。"
p_foot.font.size = Pt(10)
p_foot.font.color.rgb = C_TEXT_MUTED
p_foot.font.bold = True

# ----------------------------------------------------
# Save Final Presentation
# ----------------------------------------------------
out_path = "/Users/sap220701/Desktop/産業フェア_ローカル/docs/02_プロモーション計画/クライアント説明用_WEBプロモーション統合計画書_2026.pptx"
prs.save(out_path)
print(f"Complete Presentation successfully saved to: {out_path} (Total slides: {len(prs.slides)})")
