# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:06:31 2020

@author: kjpeng
"""


import requests
from bs4 import BeautifulSoup
import sqlite3

stockNo = 2317
#url = 'https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID=2317&CHT_CAT2=YEAR'
url = f'https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID={stockNo}&CHT_CAT2=YEAR'

headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

resp = requests.get(url,headers=headers)
resp.encoding = 'utf-8'

raw_html = resp.text

soup = BeautifulSoup(raw_html,'html.parser')


#收盤價
closing_price_rows = []

for row_line in range(0,10):
    closing_price = soup.select(f'#row{row_line} > td nobr')[5].text
    
    closing_price_rows.append(closing_price)

max_price = max(closing_price_rows)
min_price = min(closing_price_rows)

avg_price = sum(float(x) for x in closing_price_rows) / len(closing_price_rows)
avg_price = '%2.f'%avg_price
print("closing price of the list =", closing_price_rows)
print("max price =", max_price)
print("min price =", min_price)
print("avg price =", avg_price)


#開始操作資料庫
connection = sqlite3.connect('stocks.db')
cursor = connection.cursor();

#建立table
cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS stock_year_price(
                stock_no TEXT PRIMARY KEY NOT NULL,
                max_price TEXT NOT NULL,
                min_price TEXT NOT NULL,
                avg_price TEXT NOT NULL
        
        );
        
        '''
        )

connection.commit()

#建立資料前先清除原本的資料
cursor.execute(
        '''
        DELETE FROM stock_year_price ;
        '''
)
connection.commit()

cursor.execute(
        '''
        INSERT INTO stock_year_price(stock_no,max_price,min_price,avg_price) values('{}','{}','{}',{});
        '''.format(stockNo,max_price,min_price,avg_price)
)
connection.commit()

connection.close()
