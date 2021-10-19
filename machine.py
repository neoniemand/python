# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:09:12 2021

@author: julian
"""

import numpy
from scipy import stats

#speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#speed = [99,86,87,88,86,103,87,94,78,77,85,86]
#speed = [86,87,88,86,87,85,86]
speed = [32,111,138,28,59,77,97]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)
a = numpy.std(speed)
b = numpy.var(speed)

c = numpy.percentile(ages, 90)

print("평균    :", x)
print("중간    :", y)
print("빈도    :", z)
print("표준편차:", a)
print("분산    :", b)
print("백분위  :", c)