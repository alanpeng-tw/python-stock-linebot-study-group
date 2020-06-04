# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:15:22 2020

@author: kjpeng
"""

language_1 = 'Python'

language_2 = language_1

language_2 = 'Java'

# language_1 沒有影響，還是 Python
print(language_1)
# language_2 指到新的字串物件 Java
print(language_2)

# 兩者指到的記憶體位置不同
print(id(language_1))
print(id(language_2))


stock_price_1 = [240, 245, 241, 243, 242, 245, 247]

stock_price_2 = stock_price_1

# 更改第一筆資料
stock_price_1[0] = 250
# stock_price_1 變成 [250, 245, 241, 243, 242, 245, 247]
print(stock_price_1)
# stock_price_2 也受影響變成 [250, 245, 241, 243, 242, 245, 247]
print(stock_price_2)

# 兩者指到記憶體位置相同
print(id(stock_price_1))
print(id(stock_price_2))