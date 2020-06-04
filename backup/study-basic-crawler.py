# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:13:22 2020

@author: kjpeng
"""

import requests
from bs4 import BeautifulSoup

stock_id = input('股票代碼')
url = f'https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID={stock_id}'


print('URL: ' + url)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

resp = requests.get(url, headers=headers)

resp.encoding = 'utf-8'

raw_html = resp.text

soup =  BeautifulSoup(raw_html, 'html.parser')

for index in range(1,10):
    print('index',index)
    revenue_date = soup.select(f'#row{index} > td:nth-child(1) > nobr')[0].text
    final_price = soup.select(f'#row{index} > td:nth-child(3) > nobr')[0].text
    year_revenue = soup.select(f'#row{index} > td:nth-child(11) > nobr')[0].text
    print('revenue_date:', revenue_date, ',final_price:', final_price, ',year_revenue:', year_revenue)
    
'''    
with open('./data.txt','a') as file_demo:
  file_demo.write('hello world1')
  file_demo.write('hello world2')

file_content_list = file_demo.readlines()
for line in file_content_list:
  print(line)
  '''