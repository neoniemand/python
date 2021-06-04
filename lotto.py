# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:42:33 2021

@author: julian
"""
mysuccess = [2,3,12,22,32,42,18,19,20]

mylist = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]
]

mycnt = 0

for listno in mylist:
    for listnum in listno:
        for mynum in mysuccess:
            if(listnum == mynum):
                print(mynum, end=' ')
                mycnt = mycnt+1
    print("mycnt : ", mycnt)
    mycnt = 0
    print("\n==============")
#print(mylist[3][4])