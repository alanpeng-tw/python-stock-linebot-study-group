# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:41:27 2020

@author: kjpeng
"""

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
作業任務十五
1.當使用者點選「圖片」文字會回傳圖片
2.當使用者點選「貼圖」文字會回傳貼圖
'''

app = Flask(__name__)


# LINE_CHANNEL_SECRET 和 LINE_CHANNEL_ACCESS_TOKEN 類似聊天機器人的密碼，記得不要放到 repl.it 或是和他人分享
line_bot_api = LineBotApi('V0FTu96Cc41aeivIQLBLPUUPnxFuFu+BbDsoKUpaxzHFfO4kEu9zKBAxuS3XxuT82nEhZuAd59aE+9SVKcnJoOQo/JSV6GUf+F5PIQFzpvmgBvCLYWRMhqUSOFNr33tA5hQgVv730DbgHKCaLzzFlQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('862e746dbb01f6e912bddf2d58faf593')

@app.route('/callback', methods=['POST'])
def callback():
    # 取得網路請求的標頭 X-Line-Signature 內容，會確認請求是從 LINE Server 送來的避免資訊安全問題
    signature = request.headers['X-Line-Signature']
    
    #將送來的request內容取出
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)
        
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    user_message = event.message.text
    reply_message = TextSendMessage(text='請輸入指令')
    
    if user_message == '@圖片':
         reply_message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/0Ps4kYi.jpg',
                preview_image_url = 'https://i.imgur.com/0Ps4kYi.jpg'
                )
    elif user_message == '@貼圖':
         reply_message = StickerSendMessage(
                package_id='1',
                sticker_id='106'
                )
    else :
        reply_message = LocationSendMessage(
            title = 'My Location',
            address = 'Taipei City Goverment',
            latitude = 25.037707,
            longitude = 121.564422
            )


    line_bot_api.reply_message(
        event.reply_token,
        reply_message)
    
if __name__ == "__main__":
    app.run()
