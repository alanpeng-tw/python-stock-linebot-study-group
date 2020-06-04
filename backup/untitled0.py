# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:16:34 2020

@author: kjpeng
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

stock_num = '2412'
url = f'https://goodinfo.tw/StockInfo/StockFinDetail.asp?STEP=DATA&STOCK_ID={stock_num}&RPT_CAT=XX_M_YEAR&QRY_TIME=20193'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2891'
}

resp = requests.post(url, headers=headers)
resp.encoding = 'utf-8'
# 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8）
raw_html = resp.text

# 將擷取內容轉為 BeautifulSoup 物件
soup = BeautifulSoup(raw_html, 'html.parser')

# 透過選擇器選取到我們要的資料
roe_rows = soup.select('#row8 td nobr')
print(roe_rows)

# 將 ROE 數值儲存到 list 中
roe_list = []
for roe_row in roe_rows:
    # text 屬性可以取出我們在標籤內的值
    print(roe_row.text)
    roe_list.append(roe_row.text)

# 將資料轉為 DataFrame
df = pd.DataFrame({
    '股東權益報酬率': roe_list
})
# 第一列是標頭欄位，將第一列移除
df = df.drop(0)

print('roe_rows', df)
# 儲存為 csv 檔案，這邊我們格式不希望把 Pandas DataFrame index 寫入所設為 False
df.to_csv(f'roe_{stock_num}.csv', index=False)