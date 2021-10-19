# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:33:24 2021

@author: julian
"""

a = "이건"
print(len(a))

hello = '안녕하세요'
length = len(hello.encode('utf-8'))     # UTF-8 로 인코딩 했을 때 바이트 수 (결과는 15)
length = len(hello.encode('euc-kr'))     # EUC-KR로 인코딩 했을 때 바이트 수 (결과는 10)
print(length)