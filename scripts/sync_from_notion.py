import os
import json
import requests

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION
    }

def richtext_to_markdown(rich_text):
    """
    Notionのリッチテキスト形式の配列をMarkdownテキストに変換する(太字、リンクに対応)
    """
    result = ""
    for r in rich_text:
        text = r.get("plain_text", "")
        annotations = r.get("annotations", {})
        link = r.get("text", {}).get("link")
        
        # リンクの復元
        if link and link.get("url"):
            text = f"[{text}]({link['url']})"
            
        # 太字の復元
        if annotations.get("bold"):
            text = f"**{text}**"
            
        result += text
    return result

def block_to_markdown(block):
    """
    Notionブロック1個をMarkdownの1行(または複数行)に変換する
    """
    b_type = block["type"]
    
    if b_type == "paragraph":
        rt = block["paragraph"]["rich_text"]
        return richtext_to_markdown(rt) + "\n"
        
    elif b_type == "heading_1":
        rt = block["heading_1"]["rich_text"]
        return f"# {richtext_to_markdown(rt)}\n"
        
    elif b_type == "heading_2":
        rt = block["heading_2"]["rich_text"]
        return f"## {richtext_to_markdown(rt)}\n"
        
    elif b_type == "heading_3":
        rt = block["heading_3"]["rich_text"]
        return f"### {richtext_to_markdown(rt)}\n"
        
    elif b_type == "divider":
        return "---\n"
        
    elif b_type == "to_do":
        rt = block["to_do"]["rich_text"]
        checked = block["to_do"]["checked"]
        mark = "x" if checked else " "
        return f"- [{mark}] {richtext_to_markdown(rt)}\n"
        
    elif b_type == "bulleted_list_item":
        rt = block["bulleted_list_item"]["rich_text"]
        return f"- {richtext_to_markdown(rt)}\n"
        
    elif b_type == "numbered_list_item":
        rt = block["numbered_list_item"]["rich_text"]
        # マークダウンとしては 1. で出力すればレンダラー側で自動採番されるためこれで十分
        return f"1. {richtext_to_markdown(rt)}\n"
        
    elif b_type == "code":
        rt = block["code"]["rich_text"]
        lang = block["code"]["language"]
        code_text = richtext_to_markdown(rt)
        return f"```{lang}\n{code_text}\n```\n"
        
    return ""

def fetch_all_blocks(headers, page_id):
    """
    指定されたNotionページの子ブロックをすべて取得する(ページネーション対応)
    """
    blocks = []
    url = f"{NOTION_API_URL}/blocks/{page_id}/children?page_size=100"
    has_more = True
    next_cursor = None
    
    while has_more:
        query_url = url
        if next_cursor:
            query_url += f"&start_cursor={next_cursor}"
            
        response = requests.get(query_url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch blocks for page {page_id}: {response.text}")
            break
            
        data = response.json()
        blocks.extend(data.get("results", []))
        has_more = data.get("has_more", False)
        next_cursor = data.get("next_cursor")
        
    return blocks

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
        print(f"Fetching content from Notion page {page_id} for {file_path}...")
        blocks = fetch_all_blocks(headers, page_id)
        
        if not blocks:
            print(f"Warning: No content fetched for page {page_id}. Skipping.")
            continue
            
        md_lines = []
        for block in blocks:
            md_lines.append(block_to_markdown(block))
            
        # Markdown文字列の組み立て (各ブロックの末尾改行に配慮して結合)
        md_content = "".join(md_lines)
        
        # フォルダが存在しない場合は作成
        dir_name = os.path.dirname(file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"Successfully synced Notion page {page_id} to local file {file_path}.")

if __name__ == "__main__":
    main()
