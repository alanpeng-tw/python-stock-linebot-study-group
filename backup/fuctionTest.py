# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:02:56 2020

@author: kjpeng
"""


class Book:
  
  def __init__(self,name ,price ,category ):
    self.name = name
    self.price = price
    self.category = category
    
book1 = Book('哈利波特',200,15)

print(book1.name)