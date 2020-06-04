# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:33:45 2020

@author: kjpeng
"""

# 請設計一個程式可以讓使用者輸入希望從多少數字開始累加到多少數字（三個使用者輸入變數，一個為起始值，一個為結束值，一個為間隔值），然後使用 while 迴圈印出累加結果（含結束值）。舉例：使用者輸入 0、10 和 1 代表從 0 累加到 10，間隔為 1，結果應該為 55。

start = int(input('請輸入起始值:'))
end = int(input('請輸入結束值:'))
step = int(input('請輸入間隔值:'))


result = start

while start <= end:
  result += start

  start += step

print(result)
