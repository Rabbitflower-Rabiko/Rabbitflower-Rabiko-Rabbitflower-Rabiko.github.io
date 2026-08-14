import os
import urllib.request
import json

# 環境変数からスプレッドシートIDを取得
SHEET_ID = os.environ.get("SPREADSHEET_ID")
# 上書き対象のファイルパス（Jekyllのトップページ）
TARGET_FILE = "index.html"

# Jekyllでヘッダー/フッター等の共通レイアウトを適用したい場合に使用
# 不要（完全なHTMLコード）の場合は空文字 "" にしてください
JEKYLL_FRONT_MATTER = """---
layout: default
---
"""

def fetch_html_from_sheet(sheet_id):
    # Google Visualisation APIを利用してJSONで取得
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:json"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        
    # 余分なレスポンスヘッダー文字列を削ってJSON化
    json_str = content[content.find('{'):content.rfind('}')+1]
    data = json.loads(json_str)
    
    # A1セル（0行目0列目）の値を取得
    try:
        html_content = data['table']['rows'][0]['c'][0]['v']
        return html_content
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error extracting data from spreadsheet: {e}")
        return None

def main():
    if not SHEET_ID:
        print("Error: SPREADSHEET_ID environment variable is not set.")
        return

    print("Fetching HTML from Google Sheets...")
    html_content = fetch_html_from_sheet(SHEET_ID)

    if html_content:
        # JekyllのFront Matterを付与して書き込み
        full_content = JEKYLL_FRONT_MATTER + html_content
        
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"Successfully updated {TARGET_FILE}")
    else:
        print("Failed to fetch HTML content.")

if __name__ == "__main__":
    main()
