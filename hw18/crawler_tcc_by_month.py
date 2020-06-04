import requests
import statistics
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# 創建一個 Scheduler 物件實例
sched = BlockingScheduler()


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',}

#計算股價的均價
def counting_average(closing_price_list):    
   
    collected_list = list(map(float,closing_price_list))
   
    average = statistics.mean(collected_list)
    return str(round(average,2))

#股價list的slicing
def get_closing_price_by_range(start_index,closing_price_list):
    closing_price_list_temp = closing_price_list[start_index:]
    return closing_price_list_temp
  
#get stock price of average
def get_Tcc_Month_ave(stockNo):
    url = f'https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID={stockNo}&CHT_CAT2=MONTH'
   
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
   
    raw_html = response.text
   
    closing_price_list = []
    closing_price_month_list = []
   
    ave_price = []
   
    soup = BeautifulSoup(raw_html,'html.parser')
    for row_line in range(0,11):
       
        #取得台泥的月線收盤價
        closing_price_month = soup.select(f'#row{row_line} > td nobr')[0]
        closing_price_month_list.append(closing_price_month.text)
       
        closing_price = soup.select(f'#row{row_line} > td nobr')[5]
        closing_price_list.append(closing_price.text)
    
    for i in range(0,len(closing_price_list)):
        closing_price_list_temp = get_closing_price_by_range(i,closing_price_list)
        avePrice = counting_average(closing_price_list_temp)
        print(closing_price_month_list[i],avePrice)

def get_datetime_now():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")
    
job_interval_time = 1
# decorator 設定 Scheduler 的類型和參數，例如 interval 間隔多久執行
@sched.scheduled_job('interval', hours=job_interval_time)
def timed_job():
    print(get_datetime_now())
    print('crawler TCC(1101) month price average........')
    get_Tcc_Month_ave(1101)

print(f'every {job_interval_time} hour exec crawler')
sched.start()