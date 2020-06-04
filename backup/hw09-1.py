# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:20:44 2020

@author: kjpeng
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'./NotoSansCJK-Black.ttc')

df = pd.read_csv('stock_data.csv', encoding='utf-8').head(6)

#選取1-6列的證券代號及收盤價
data = df.loc[:,['證券代號','收盤價']]

#設定證券代號為X軸
data = data.set_index('證券代號')

#因收價盤的value有小數點,故將value轉為float格式
data = data['收盤價'].astype('float')

fig = data.plot(kind='line').get_figure()
plt.title('Stock Close Price')

plt.xlabel("證券代號", fontproperties=myfont)
plt.ylabel("收盤價", fontproperties=myfont)
plt.title('個股日成交資訊 ',fontproperties=myfont)
fig.savefig('HOME WORK-9-StockClosePrice.png')

fig.show()