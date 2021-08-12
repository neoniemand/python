# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:02:53 2021

@author: julian
"""

nVal = 0
nCnt = 3780
nPrice = 44250 # 2021/06/08
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