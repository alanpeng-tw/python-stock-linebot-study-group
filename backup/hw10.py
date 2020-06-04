# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:42:35 2020

@author: kjpeng
"""

import sqlite3
import pandas as pd

#建立一個stock db
connection = sqlite3.connect('stock.db')

cursor = connection.cursor();

#建立stocks table
cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS stocks (
                id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                closing_price INT NOT NULL
        
        );
        
        '''
        )

connection.commit()

#先將table 中的資料清乾淨 
cursor.execute(
        '''
        DELETE FROM stocks;
        '''
)
connection.commit()


df = pd.read_csv('F:/PythonProjects/pythonStudy/stocks.csv', encoding='utf-8',dtype=str)

stockData = df.loc[:,['證券代號','證券名稱','收盤價']]
for index,row in stockData.iterrows():
    datalist = list(row['證券代號'],row['證券名稱'],row['收盤價'])
    #stockId = row['證券代號']
   # stockName = row['證券名稱']
   # closingPrice = row['收盤價']
   #print(f'{stockId}:{stockName}:{closingPrice}' )

    #建立stocks table
    cursor.execute(
        '''
        INSERT INTO stocks(id,name,closing_price)
        VALUES(?,?,?)        
        );        
        '''.format(row['證券代號'],row['證券名稱'],row['收盤價'])
    )

    connection.commit()

#print(stockData)

connection.close()