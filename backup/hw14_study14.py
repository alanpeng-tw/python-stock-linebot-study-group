# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:08:11 2020

@author: kjpeng
"""

from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, 
        StickerSendMessage, VideoSendMessage ,  LocationSendMessage
        )


app = Flask(__name__)

line_bot_api = LineBotApi('V0FTu96Cc41aeivIQLBLPUUPnxFuFu+BbDsoKUpaxzHFfO4kEu9zKBAxuS3XxuT82nEhZuAd59aE+9SVKcnJoOQo/JSV6GUf+F5PIQFzpvmgBvCLYWRMhqUSOFNr33tA5hQgVv730DbgHKCaLzzFlQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('862e746dbb01f6e912bddf2d58faf593')


@app.route("/callback", methods=['POST'])
def callback():
    # 取得網路請求的標頭 X-Line-Signature 內容，確認請求是從 LINE Server 送來的
    signature = request.headers['X-Line-Signature']
    
    
    # 將請求內容取出
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    
    return'OK'
    
# decorator 負責判斷 event 為 MessageEvent 實例，event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_message = TextSendMessage(text = '請輸入正確指令:「文字」、「圖片」、「貼圖」、「影片」、「地圖」')
    
    if user_message == '文字':
        reply_message = TextSendMessage(text = event.message.text)
    elif user_message == '圖片':
        reply_message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/0Ps4kYi.jpg',
                preview_image_url = 'https://i.imgur.com/0Ps4kYi.jpg'
                )
    elif user_message == '貼圖':
        reply_message = StickerSendMessage(
                package_id='1',
                sticker_id='106'
                )
    elif user_message == '影片':
        reply_message = VideoSendMessage(
                original_content_url='https://i.imgur.com/vxhjk3o.mp4',
                preview_image_url='https://i.imgur.com/0Ps4kYi.jpg'
                )
    elif user_message == '地圖':
        reply_message = LocationSendMessage(
                title = 'My Location',
                address = 'Taipei City Goverment',
                latitude = 25.037707,
                longitude = 121.564422
                )
    elif user_message == '快速選單':
        '''
         pass 為 Python 內部關鍵字，主要為佔位符號，
         待之後再補充區塊程式邏輯而不會產生錯誤
        '''
        pass


    line_bot_api.reply_message(
        event.reply_token,
        reply_message)
# __name__ 為內建變數，若程式不是被當作模組引入則為 __main__
if __name__ == "__main__":
    # 運行 Flask server，預設設定監聽 port 5000（網路 IP 位置搭配 Port 可以辨識出要把網路請求送到那邊 xxx.xxx.xxx.xxx:port）
    app.run()