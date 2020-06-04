# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:54:14 2020

@author: kjpeng
"""

from flask import Flask,request

app = Flask(__name__)

@app.route('/test')
def hello():
    
    name = request.args.get('name','World')
    return f'Hello, {name}'

app.run()