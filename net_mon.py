# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:03:52 2021

@author: julian
"""

from time import sleep
from ping3 import ping
from email.mime.text import MIMEText
import smtplib
import os

def SendMail(hostname):
    smtpName = "smtp.naver.com" #smtp 서버 주소
    smtpPort = 587 #smtp 포트 번호
    
    text = hostname + " 서버 접속이 안 됩니다."
    msg = MIMEText(text) #MIMEText(text , _charset = "utf8")
    
    msg['Subject'] = hostname + " 서버 접속 실패"
    msg['From'] = 'niemand@naver.com'
    msg['To'] = 'narago@gmail.com'
    print(msg.as_string())
    
    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( 'niemand' , 'skfkrh./01' ) #로그인
    s.sendmail( 'niemand@naver.com', 'kjn@unet.kr', msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.sendmail( 'niemand@naver.com', 'gspark@unet.kr', msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.sendmail( 'niemand@naver.com', 'tykwon@unet.kr', msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    
    s.close() #smtp 서버 연결을 종료합니다.

hosts = [
#'wolf',
'wolf2',
'tiger',
'tiger_bak',
'fox',
'anakin',
'yoda',
'han',
'Jedi',
'Xwing',
'darthvader',
'luke',
'hulk',
'hawkeye',
'trustkms1',
'trustkms2',
'trustkms3',
'svn',
#'ncipher',
'marvel',
'pkid'
]

#while 1:
os.system('cls')
print('============================')
for hostname in hosts:
    result = ping(hostname)
    if result == None:
        print(f'{hostname:12} : ______')
        if hostname == 'pkid':
            SendMail(hostname)
            sleep(600)
    else:
        print(f'{hostname:12} : Active')            
print('============================')
#sleep(5)
    