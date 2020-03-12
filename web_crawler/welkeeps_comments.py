from urllib.request import urlopen
from bs4 import BeautifulSoup
#from tkinter import *
#from tkinter import messagebox
import time
import webbrowser

#window = Tk()

while(1):												# 지구 멸망 전까지는 아래 명령을 계속 수행하라 !!
    html = urlopen("http://www.welkeepsmall.com")		# 웰킵스 쇼핑몰에 접속하기
    
    bsObject = BeautifulSoup(html, "html.parser")		# 홈페이지 내용 전부 가져오기
    
    paragraph_data = bsObject.find(class_='dsc')		# 내용 중에서 dsc class 내용 가져오기

    ori = '웰킵스 프리미엄 미세먼지 마스크 소형[KF94][25개입]'		# 현재 기준 가장 위에 있는 (최신) 상품 저장해 놓기
    #print(paragraph_data.get_text())
    
    if paragraph_data.get_text() != ori:				# 저장해 놓은 상품 내용과 지금 방금 읽어온 상품이 다르면
        print('새 상품 떴어')								# 최신 상품이 새로 뜬 것이고
        #messagebox.showinfo("알림창", "새 상품이 떴어요 !!")
        webbrowser.open("http://www.welkeepsmall.com/", new=1, autoraise=True)	# 풍악을 울려라 !!  웰킵스 홈페이지 브라우저 띄우기
    else:
        print('상품 같아')									# 아니면 상품이 아직 그대로인 것이다 !!
        
    time.sleep(20)										# 20초만 쉬었다가 다시 체크해 !!


	