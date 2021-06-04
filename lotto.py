# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:42:33 2021

@author: julian
"""
mysuccess = [2,3,12,22,32,42,18,19,20]

mylist = [
    [1,2,3,4,5],
    [6,7,8,9,10,18,29,19,20,3,12,22],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]
]

mycnt = 0
myresult = ""

for listno in mylist:
    for listnum in listno:
        for mynum in mysuccess:
            if(listnum == mynum):
                myresult = myresult + str(mynum) + ' '
                mycnt = mycnt + 1
    print(f'{myresult:20} mycnt : {mycnt}')
    mycnt = 0
    myresult = ""
    print("================================")
#print(mylist[3][4])