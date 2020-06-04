# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:07:59 2020

@author: kjpeng
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

stock_num = '2317'
url = f'https://goodinfo.tw/StockInfo/StockFinDetail.asp?STEP=DATA&STOCK_ID={stock_num}&RPT_CAT=XX_M_YEAR&QRY_TIME=20194'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2317'
}

resp = requests.post(url, headers=headers)
resp.encoding = 'utf-8'
# 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8）
raw_html = resp.text

# 將擷取內容轉為 BeautifulSoup 物件
soup = BeautifulSoup(raw_html, 'html.parser')

roe_rows = soup.select('#row8 td nobr')
                   
#print(roe_rows)

roe_list = []
for roe_row in roe_rows:
    #print(roe_row.text)
    roe_list.append(roe_row.text)

df = pd.DataFrame({
    '2019-ROE': roe_list
})
   
df = df.drop(0)

print('roe_rows',df)

df.to_csv(f'roe_{stock_num}.csv', index=False)