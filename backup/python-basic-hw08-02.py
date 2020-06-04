# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:39:03 2020

@author: kjpeng
"""


import csv

import requests
from bs4 import BeautifulSoup

print('程式開始執行...')
url = 'https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID=%E5%8A%A0%E6%AC%8A%E6%8C%87%E6%95%B8&CHT_CAT2=MONTH'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

print('擷取到網頁...')

soup = BeautifulSoup(resp.text,'html.parser')

priceMonth_list = []

print('對網頁進行剖析....')
for i in range(1,120):
    
    #每次的迴圈都產生一個新的dict
    performance_dict = {}
    
    #交易月份
    performance_dict['transMonth'] = soup.select(f'#row{i} > td:nth-child(1) > nobr')[0].text
    #開盤價                         
    performance_dict['openPrice'] = soup.select(f'#row{i} > td:nth-child(3) > nobr')[0].text                        
    #最高價
    performance_dict['highestPrice'] = soup.select(f'#row{i} > td:nth-child(4) > nobr')[0].text
    #最低價
    performance_dict['lowestPrice'] = soup.select(f'#row{i} > td:nth-child(5) > nobr')[0].text
    #收盤價
    performance_dict['closePrice'] =  soup.select(f'#row{i} > td:nth-child(6) > nobr')[0].text    
    priceMonth_list.append(performance_dict)
    print('已成功抓取'+performance_dict['transMonth']+'')
    
headers = ['transMonth','openPrice','highestPrice','lowestPrice','closePrice']

print('剖析結束,開始產生CSV檔案')
with open('transMonthly_price.csv','w') as output_file:
    dict_writer =  csv.DictWriter(output_file,headers)
    
    #寫入標題
    dict_writer.writeheader()
    
    #寫入值
    dict_writer.writerows(priceMonth_list)
    
print('程式執行完畢...')