# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:25:51 2020

@author: kjpeng
"""

import csv

import requests
from bs4 import BeautifulSoup


url = 'https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2330'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

resp = requests.get(url, headers=headers)

# 設定編碼為 utf-8 避免中文亂碼問題
resp.encoding = 'utf-8'

# 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若該網站沒設定可能會有中文亂碼問題。所以通常會使用 resp.encoding 設定
raw_html = resp.text


# 將 HTML 轉成 BeautifulSoup 物件
soup = BeautifulSoup(raw_html, "html.parser")

def parse_str_to_float(raw_value):
    return float(raw_value.replace(',', ''))

# 開始寫入檔案，把資料存放到 list 裡面
# 若是忘記 list/dict 用法可以回去複習一下
performance_list = []

# 使用 CSS Selector 選到對應的元素位置，取出裡面的值 (1-9)
for index in range(1, 10):
    print('index', index)
    # 每次迴圈都是新的 dict 內容
    performance_dict = {}
    performance_dict['date'] = soup.select(f'#row{index} > td:nth-child(1) > nobr')[0].text
    performance_dict['final_price'] = soup.select(f'#row{index} > td:nth-child(3) > nobr')[0].text
    performance_dict['year_revenue'] = parse_str_to_float(soup.select(f'#row{index} > td:nth-child(11) > nobr')[0].text)
    # 每月資料寫入 list
    performance_list.append(performance_dict)

# CSV 檔案第一列標題會是 date, final_price, year_revenue，記得要和 dict 的 key 相同，不然會出現錯誤
headers = ['date', 'final_price', 'year_revenue']

# 使用檔案 with ... open 開啟寫入檔案模式，透過 csv 模組將資料寫入
with open('performance.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, headers)
    # 寫入標題
    dict_writer.writeheader()
    # 寫入值
    dict_writer.writerows(performance_list)