import os
import json
import re
import requests

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION
    }

def parse_inline_text(text):
    """
    太字 **text** や リンク [label](url) を検出し、Notionのリッチテキスト形式に変換する
    """
    # プレーンテキストとして初期化
    parts = []
    # 簡単なパース処理 (正規表現でリンクと太字を抽出)
    # pattern: (\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))
    pattern = re.compile(r'(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))')
    last_idx = 0
    
    for match in pattern.finditer(text):
        start, end = match.span()
        # マッチする前のテキストを追加
        if start > last_idx:
            parts.append({
                "type": "text",
                "text": {"content": text[last_idx:start]}
            })
            
        matched_str = match.group(0)
        if matched_str.startswith("**") and matched_str.endswith("**"):
            # 太字
            content = matched_str[2:-2]
            parts.append({
                "type": "text",
                "text": {"content": content},
                "annotations": {"bold": True}
            })
        elif matched_str.startswith("[") and ")" in matched_str:
            # リンク
            label = matched_str[1:matched_str.index("]")]
            url = matched_str[matched_str.index("(")+1:-1]
            parts.append({
                "type": "text",
                "text": {
                    "content": label,
                    "link": {"url": url}
                }
            })
        last_idx = end
        
    if last_idx < len(text):
        parts.append({
            "type": "text",
            "text": {"content": text[last_idx:]}
        })
        
    return parts if parts else [{"type": "text", "text": {"content": text}}]

def markdown_to_notion_blocks(md_content):
    """
    Markdown文字列を行ごとに解析し、NotionのBlockオブジェクト(JSON)のリストに変換する
    """
    blocks = []
    lines = md_content.split("\n")
    
    in_code_block = False
    code_lang = "plain text"
    code_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # 1. コードブロックの処理
        if stripped.startswith("```"):
            if in_code_block:
                # コードブロック終了
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": "\n".join(code_lines)}}],
                        "language": code_lang
                    }
                })
                in_code_block = False
                code_lines = []
            else:
                # コードブロック開始
                in_code_block = True
                lang = stripped[3:].strip()
                code_lang = lang if lang else "plain text"
            continue
            
        if in_code_block:
            code_lines.append(line)
            continue
            
        # 2. 空行
        if not stripped:
            continue
            
        # 3. 見出し (Heading)
        if stripped.startswith("# "):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": parse_inline_text(stripped[2:])
                }
            })
        elif stripped.startswith("## "):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": parse_inline_text(stripped[3:])
                }
            })
        elif stripped.startswith("### "):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": parse_inline_text(stripped[4:])
                }
            })
            
        # 4. 区切り線 (Divider)
        elif stripped == "---":
            blocks.append({
                "object": "block",
                "type": "divider",
                "divider": {}
            })
            
        # 5. To-Do リリスト
        elif stripped.startswith("- [ ] "):
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": parse_inline_text(line[line.index("- [ ] ")+6:]),
                    "checked": False
                }
            })
        elif stripped.startswith("- [x] "):
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": parse_inline_text(line[line.index("- [x] ")+6:]),
                    "checked": True
                }
            })
            
        # 6. 箇条書きリスト (Bulleted List)
        elif stripped.startswith("- ") or stripped.startswith("* "):
            content = line[line.index("- " if stripped.startswith("- ") else "* ")+2:]
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": parse_inline_text(content)
                }
            })
            
        # 7. 番号付きリスト (Numbered List)
        elif re.match(r'^\d+\.\s', stripped):
            match = re.match(r'^(\d+)\.\s', stripped)
            prefix_len = len(match.group(0))
            content = line[line.index(match.group(0)) + prefix_len:]
            blocks.append({
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": parse_inline_text(content)
                }
            })
            
        # 8. 通常の段落 (Paragraph)
        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": parse_inline_text(line)
                }
            })
            
    return blocks

def delete_all_blocks(headers, page_id):
    """
    ページの既存ブロック(本文)をすべて削除(アーカイブ)する
    """
    # 子ブロック一覧の取得
    url = f"{NOTION_API_URL}/blocks/{page_id}/children?page_size=100"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch blocks for page {page_id}: {response.text}")
        return False
        
    results = response.json().get("results", [])
    for block in results:
        block_id = block["id"]
        del_url = f"{NOTION_API_URL}/blocks/{block_id}"
        # Notion APIではDELETEリクエストでブロックを削除(アーカイブ)できる
        del_res = requests.delete(del_url, headers=headers)
        if del_res.status_code != 200:
            print(f"Failed to delete block {block_id}: {del_res.text}")
            
    return True

def append_blocks(headers, page_id, blocks):
    """
    Notionページに新しいブロックを追加する(API制限の1回100個単位で分割送信)
    """
    url = f"{NOTION_API_URL}/blocks/{page_id}/children"
    
    # Notion APIは1回のリクエストで最大100個のブロックしか追加できないため、100個ずつ分割して送信する
    chunk_size = 100
    for i in range(0, len(blocks), chunk_size):
        chunk = blocks[i:i+chunk_size]
        payload = {"children": chunk}
        response = requests.patch(url, headers=headers, json=payload)
        if response.status_code != 200:
            print(f"Failed to append blocks chunk to page {page_id}: {response.text}")
            return False
            
    return True

def main():
    token = os.environ.get("NOTION_TOKEN")
    page_map_str = os.environ.get("NOTION_PAGE_MAP")
    
    if not token:
        print("Error: NOTION_TOKEN environment variable is not set.")
        return
        
    if not page_map_str:
        print("Error: NOTION_PAGE_MAP environment variable is not set.")
        return
        
    try:
        page_map = json.loads(page_map_str)
    except json.JSONDecodeError as e:
        print(f"Error parsing NOTION_PAGE_MAP JSON: {e}")
        return
        
    headers = get_headers(token)
    
    for file_path, page_id in page_map.items():
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} not found. Skipping.")
            continue
            
        print(f"Syncing {file_path} to Notion page {page_id}...")
        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()
            
        # MarkdownをNotionブロックに変換
        blocks = markdown_to_notion_blocks(md_content)
        
        # 既存ブロックの削除
        if delete_all_blocks(headers, page_id):
            # 新しいブロックのアペンド
            if append_blocks(headers, page_id, blocks):
                print(f"Successfully synced {file_path} to Notion page {page_id}.")
            else:
                print(f"Failed to write blocks for {file_path}.")
        else:
            print(f"Failed to clear page content for page {page_id}.")

if __name__ == "__main__":
    main()
