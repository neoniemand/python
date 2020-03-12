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

flag = 0

while(1):
    response = http.request('GET', target_url, preload_content=False)
    response.auto_close = False
    
    for line in io.TextIOWrapper(response):
        if 'dsc' in line:
            if flag == 0:
                flag = 1
                dsc_ori = title_str(line.strip())
                print("원래 상품 : " + dsc_ori)
                break
            if flag == 1:
                dsc_now = title_str(line.strip())
                print("현재 상품 : " + dsc_now)
                if dsc_now != dsc_ori:
                    print("사야 돼 이건")
                    webbrowser.open(target_url, new=1, autoraise=True)
                    #winsound.Beep(freq, dur)
                    time.sleep(300)
                break
                    
    d = datetime.datetime.today()
    #print(d.strftime('%Y-%m-%d %H:%M:%S'))
    #print("====================================================================")
    time.sleep(7)
    