# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:03:42 2020

@author: kjpeng
"""


color = str(input('請輸入您喜歡的四種顏色(每個顏色以 , 分隔):'))

color = color.split(',')

print(color[len(color) - 1])