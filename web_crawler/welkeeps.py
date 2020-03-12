# urllib을 사용한 Request 보내기
#import urllib.request
 
#url = "http://www.welkeepsmall.com/"
#req = urllib.request.urlopen(url) # url에 대한 연결요청
#res = req.read() # 연결요청에 대한 응답

from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from email.mime.text import MIMEText

import time
import webbrowser
import smtplib

def SendMail():
    smtpName = "smtp.naver.com" #smtp 서버 주소
    smtpPort = 587 #smtp 포트 번호
    
    text = "신규상품 등록"
    msg = MIMEText(text) #MIMEText(text , _charset = "utf8")
    
    msg['Subject'] ="상품 새로 등록"
    msg['From'] = 'niemand@naver.com'
    msg['To'] = 'narago@gmail.com'
    print(msg.as_string())
    
    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( 'niemand' , 'skfkrh./01' ) #로그인
    s.sendmail( 'niemand@naver.com', 'narago@gmail.com', msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.close() #smtp 서버 연결을 종료합니다.

flag = 0;

while(1):
    html = urlopen("http://www.welkeepsmall.com")  
    
    bsObject = BeautifulSoup(html, "html.parser") 
    paragraph_data = bsObject.find(class_='dsc')
    
    if(flag == 0):        
        ori = paragraph_data.get_text()
        print("현재 상품 : " + ori)
        flag = 1
        
    if paragraph_data.get_text() != ori:
        print('새 상품 떴어' + paragraph_data.get_text())
        #messagebox.showinfo("알림창", "새 상품이 떴어요 !!")
        SendMail()
        webbrowser.open("http://www.welkeepsmall.com/", new=1, autoraise=True)
        exit(0)
        
    else:
        print('상품 같아 : ' + paragraph_data.get_text())
        #messagebox.showinfo("알림창", "아직 아니야 !!")
        #SendMail()
        #webbrowser.open("http://www.welkeepsmall.com/", new=1, autoraise=True)
        
    time.sleep(7)
