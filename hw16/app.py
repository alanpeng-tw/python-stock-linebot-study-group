# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:54:13 2020

@author: kjpeng
"""

from flask import Flask, request

# 使用 __name__ 代表目前運作的程式的模組名稱當作辨識名稱使用，下面產生一個網頁伺服器的實例物件
app = Flask(__name__)

# 此為 decorator 為當網址為 / 時由這個函式負責處理
@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    
    return f'Hello, {name}'

# run Flask server，setup port 8080
app.run(host='0.0.0.0', port=8080)