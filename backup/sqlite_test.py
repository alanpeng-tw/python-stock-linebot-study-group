# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:32:41 2020

@author: kjpeng
"""

import sqlite3

connection = sqlite3.connect('demo.db')

cursor = connection.cursor();

cursor.execute(
        '''
        CREATE TABLE stocks(
                id TEXT PRIMARY KEY NOT NULL,
                company_name TEXT NOT NULL,
                price INT NOT NULL
        
        );
        
        '''
        )

connection.commit()
connection.close()