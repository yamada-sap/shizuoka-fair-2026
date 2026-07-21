#!/usr/bin/env python3
"""
毎週月曜日午前10:00にGitHub Actions等から自動実行され、
README.mdの「今週のタスクステータス」の日付および最新タスクリストを動的に更新する自動化スクリプト
"""

import os
import re
import datetime

def get_jst_now():
    # JST時刻の取得 (UTC+9)
    tz_jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(tz_jst)

def calculate_week_info():
    now = get_jst_now()
    year = now.year
    month = now.month
    
    # 月の第何週かを計算
    first_day = datetime.date(year, month, 1)
    day_of_month = now.day
    adjusted_dom = day_of_month + first_day.weekday()
    week_number = int((adjusted_dom - 1) / 7) + 1
    
    # 月曜〜日曜の日付計算
    monday = now - datetime.timedelta(days=now.weekday())
    sunday = monday + datetime.timedelta(days=6)
    
    date_range = f"{monday.month}/{monday.day}〜{sunday.month}/{sunday.day}"
    week_label = f"{year}年{month}月第{week_number}週：{date_range}"
    return week_label

def update_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    readme_path = os.path.abspath(readme_path)
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    week_label = calculate_week_info()
    
    # 日付ヘッダーの置換
    header_pattern = r"## 📌 今週のタスクステータス（[^）]+）"
    new_header = f"## 📌 今週のタスクステータス（{week_label}）"
    
    updated_content = re.sub(header_pattern, new_header, content)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
        
    print(f"Successfully updated README.md header to: {new_header}")

if __name__ == "__main__":
    update_readme()
