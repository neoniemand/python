import urllib3
import io
import webbrowser
import time
import datetime

target_url = "http://www.welkeepsmall.com"

http = urllib3.PoolManager()

while(1):
    response = http.request('GET', target_url, preload_content=False)
    response.auto_close = False
    
    buy_count = 0



    for line in io.TextIOWrapper(response):
        if "shopdetail.html" in line:
            url_detail = line.split('"')[1]
            full_url = target_url + url_detail        
        if '대형' in line:
        #if '웰킵스' in line:
            buy_count = 0
            buy_count += 1
            if 'KF' in line:
            #if '원더' in line:
                buy_count += 1
                #print("URL          : " + full_url)
                print("대상 제품 찾음 : " + line.strip())
        if 'soldout' in line:
            buy_count = 0
            #print("URL          : " + full_url)
            #print("판매종료 : " + line + ", 상태 = " + str(buy_count))
        if 'consumer' in line:
            if buy_count == 2:
                print("URL          : " + full_url)
                print("사야 함 : " + line.strip() + ", 상태 = " + str(buy_count))
                webbrowser.open(full_url, new=1, autoraise=True)
                time.sleep(300)
    
    d = datetime.datetime.today()
    print(d.strftime('%Y-%m-%d %H:%M:%S'))
    print("====================================================================")
    time.sleep(7)
    