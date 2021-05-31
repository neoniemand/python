# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:02:53 2021

@author: julian
"""

nVal = 0
nCnt = 3717
#nPrice = 41800
#nPrice = 44300 # 2021/05/20
#nPrice = 44500 # 2021/05/24
#nPrice = 44800 # 2021/05/25
nPrice = 46400 # 2021/05/27
njump = 100000000
nMax = 100000000
nLoop = 40

nSum = nCnt * nPrice

print(f'cnt {nCnt:,}    sum {nSum:14,}\n')
for i in range(0, nLoop):
    nVal = nVal + njump
    for j in range(100, nMax, 100):
        if(nCnt * j > nVal):
            print(f'{j:14,} = {nCnt * j:14,}')
            break;