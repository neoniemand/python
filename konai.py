import urllib3
import io
import webbrowser
import time
import datetime
import winsound


def title_str(str1):
    str1_tail = str1[16:]
    str1_mid = str1_tail[:-5]
    return str1_mid

def status_str(str2):
    str2_tail = str2.split(">")[1]
    str2_mid = str2_tail[:-4]
    return str2_mid

target_url = "https://finance.naver.com/item/main.nhn?code=052400"

http = urllib3.PoolManager()

response = http.request('GET', target_url, preload_content=False)
response.auto_close = False


for line in io.TextIOWrapper(response):
    if '<dd>현재가 ' in line:        
        print(status_str(line.strip()))
            

    