# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:35:12 2020

@author: kjpeng
"""

import matplotlib.pyplot as plt

# X 軸
stock_list = ['2031', '2341', '2342', '2345']
# Y 軸
volumes = [34123, 122212, 41907, 3115987]


#長條圖
#plt.bar(stock_list, volumes)

#折線圖
#plt.plot(stock_list,volumes)

#圓餅圖
plt.pie(stock_list,labels=volumes)
# 若使用 VS Code 搭配 terminal 終端機或 Jupyter Notebook 執行使用
plt.show()
# 若使用 repl.it 執行需要將圖表存為圖片後於左方資料夾選擇圖片檔案觀看結果
plt.savefig('plot.png')