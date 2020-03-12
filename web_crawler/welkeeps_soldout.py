import urllib3
import io
import webbrowser
import time
import datetime
import winsound

freq = 3500 # Set frequency To 2500 Hertz
dur = 2000 # Set duration To 1000 ms == 1 second

def title_str(str1):
    str1_tail = str1[16:]
    str1_mid = str1_tail[:-5]
    return str1_mid

def status_str(str2):
    str2_tail = str2.split(">")[1]
    str2_mid = str2_tail[:-4]
    return str2_mid

target_url = "http://www.welkeepsmall.com"

http = urllib3.PoolManager()

while(1):
    response = http.request('GET', target_url, preload_content=False)
    response.auto_close = False
    
    found_dsc = 0
    soldout_cnt = 0

    for line in io.TextIOWrapper(response):
        if "shopdetail.html" in line:
            url_detail = line.split('"')[1]
            full_url = target_url + url_detail        
        if '대형' in line:
        #if '웰킵스' in line:
            if 'KF' in line:
            #if '원더' in line:
                #print("URL          : " + full_url)
                print("대상 제품 :             " + title_str(line.strip()))
                found_dsc = 1
                soldout_cnt = 0        
        if found_dsc == 1 and soldout_cnt == 2:
            soldout_cnt = 0
            found_dsc = 0
            print("제품 상태 : " + status_str(line.strip()))
            print("")
            if 'SOLD' not in line:
                print("사야 돼 이건")
                webbrowser.open(full_url, new=1, autoraise=True)
                winsound.Beep(freq, dur)
                time.sleep(300)
        if found_dsc == 1:
            soldout_cnt += 1
                
    
    d = datetime.datetime.today()
    print(d.strftime('%Y-%m-%d %H:%M:%S'))
    print("====================================================================")
    time.sleep(7)
    