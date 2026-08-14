import os
import urllib.request
import json

# 環境変数からスプレッドシートIDを取得
SHEET_ID = os.environ.get("SPREADSHEET_ID")
# 上書き対象のファイルパス
TARGET_FILE = "index.html"

# 不要なヘッダー（Front Matter）がつかないよう空文字に設定
JEKYLL_FRONT_MATTER = ""

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
        
        # 文字列として取得された場合、先頭と末尾のダブルクォーテーションを除去
        if isinstance(html_content, str):
            html_content = html_content.strip()
            # 前後がダブルクォーテーションで囲まれている場合は削除
            if html_content.startswith('"') and html_content.endswith('"'):
                html_content = html_content[1:-1]
                
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
        full_content = JEKYLL_FRONT_MATTER + html_content
        
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"Successfully updated {TARGET_FILE}")
    else:
        print("Failed to fetch HTML content.")

if __name__ == "__main__":
    main()
