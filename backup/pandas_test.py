# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:09:26 2020

@author: kjpeng
"""

import pandas as pd

movies = {
    '名稱': ['名偵探柯南', '復仇者聯盟', '那些年'],
    '票房金額（新台幣）': [1452324, 2324739, 1416601],
    '類別': ['動畫', '動作', '文藝']
}

df = pd.DataFrame(movies)
print(df.loc[1,'票房金額（新台幣）'])