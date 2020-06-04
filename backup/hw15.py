# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:27:55 2020

@author: kjpeng
"""

import random

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler        
)

from linebot.exceptions import (
    InvalidSignatureError    
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage    
)

'''
1.當使用者選擇 @查詢股價 選單，會回傳 請問你要查詢的股票是？ 文字，當使用者輸入該股票代號後回傳股價資訊
2.當使用者選擇 @報明牌 選單則隨機產生一個股票代碼和公司名稱回傳（當然你可以自己撰寫自己的報明牌邏輯）
3.當使用者選擇 @查詢股價 選單後又選擇 @報明牌 則下次還需要再次選擇 @查詢股價 才能輸入股票代碼
'''

# 當作報明牌隨機的股票 list
good_luck_list = ['2330 台積電', '2317 鴻海', '2308 台達電', '2454 聯發科']
# 範例股價資訊 dict，同學可以自行更換成查詢股價的爬蟲資料或是即時股價查詢套件的資料
stock_price_dict = {
    '2330': 210,
    '2317': 90,
    '2308': 150,
    '2454': 300
}

app = Flask(__name__)

# LINE_CHANNEL_SECRET 和 LINE_CHANNEL_ACCESS_TOKEN 類似聊天機器人的密碼，記得不要放到 repl.it 或是和他人分享
line_bot_api = LineBotApi('V0FTu96Cc41aeivIQLBLPUUPnxFuFu+BbDsoKUpaxzHFfO4kEu9zKBAxuS3XxuT82nEhZuAd59aE+9SVKcnJoOQo/JSV6GUf+F5PIQFzpvmgBvCLYWRMhqUSOFNr33tA5hQgVv730DbgHKCaLzzFlQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('862e746dbb01f6e912bddf2d58faf593')

@app.route('/callback', methods=['POST'])
def callback():
    # 取得網路請求的標頭 X-Line-Signature 內容，會確認請求是從 LINE Server 送來的避免資訊安全問題
    signature = request.headers['X-Line-Signature']
    
    #將送來的request內容取出
    body = request.get_data(as_Text=True)
    
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)
        
    return 'OK'


user_command_dict = {}

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_meesage = event.message.text
    reply_message = TextSendMessage(text='請輸入指令')
    
    user_id = event.source.user_id
    
    print('user_id',user_id)
    
    # 根據使用者 ID 暫存指令
    user_command = user_command_dict.get(user_id)
    
    print('user_command',user_command)
    
    if user_meesage == '@查詢股價' and user_command != '@查詢股價':
        reply_message = TextSendMessage(text='請問你要查詢的股票是？?')
        
        # 儲存使用者輸入了 @查詢股價 指令
        user_command_dict[user_id] = '@查詢股價'
        
    elif  user_meesage == '@報明牌':
        random_stock = random.choice(good_luck_list)
        reply_message = TextSendMessage(text=f'報明牌:{random_stock}')
        
        #清除指令暫存
        user_command_dict[user_id] = None
    
    #若上一個指令為@查詢股價
    elif user_command == '@查詢股價':
        print('user_message',user_message)
        stock_price = stock_price_dict[user_message]
        
        if stock_price:
            reply_message = TextSendMessage(text=f'成交價:{stock_price}')
            
            #清除指令暫存
            user_command_dict[user_id] = None
    
    line_bot_api.reply_message(
        event.reply_token,
        reply_message
    )
        
if __name__ == "__main__":
    app.run()