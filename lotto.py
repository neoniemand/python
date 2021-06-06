# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:42:33 2021

@author: julian
"""
mysuccess = [1,21,25,29,34,37]

mylist = [
    [8,16,18,24,30,44],
    [9,11,14,23,44,45],
    [3,4,18,24,25,29],
    [3,21,25,28,39,41],
    [4,5,17,23,38,43],
    
    [5,17,23,29,30,36],
    [12,14,17,30,40,41],
    [1,11,17,22,31,43],
    [3,5,9,11,18,32],
    [2,17,18,29,34,44],
    
    [5,9,16,18,26,44],
    [12,26,27,31,36,42],
    [1,2,5,10,34,42],
    [2,9,18,26,44,45],
    [1,16,23,27,35,41],
    
    [4,8,21,27,29,44],
    [3,4,7,15,25,39],
    [5,6,8,15,43,45],
    [17,20,21,25,29,44],
    [9,10,17,18,22,32]
]

mycnt = 0
myresult = ""

for listno in mylist:
    for listnum in listno:
        for mynum in mysuccess:
            if(listnum == mynum):
                myresult = myresult + str(mynum) + ' '
                mycnt = mycnt + 1
    if mycnt >= 3:
        print(f'{myresult:20} mycnt : {mycnt} SUCCESS')
    else:
        print(f'{myresult:20} mycnt : {mycnt}')
    mycnt = 0
    myresult = ""
    print("================================")
#print(mylist[3][4])