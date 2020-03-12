# urllib을 사용한 Request 보내기
#import urllib.request
 
#url = "http://www.welkeepsmall.com/"
#req = urllib.request.urlopen(url) # url에 대한 연결요청
#res = req.read() # 연결요청에 대한 응답

from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import time

#html = urlopen("http://www.welkeepsmall.com")
html = urlopen("https://smartstore.naver.com/etiqa")

bsObject = BeautifulSoup(html, "html.parser") 


print(bsObject) # 웹 문서 전체가 출력됩니다. 
   
