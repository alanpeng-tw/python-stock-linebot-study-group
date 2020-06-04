# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:35:06 2020

@author: kjpeng
"""

from flask import Flask,request

app = Flask(__name__)

@app.route('/hello')
def hello():
    
    name = request.args.get('name','World')
    return f'Hello, {name}'

app.run()