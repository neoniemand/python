# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:47:34 2021

@author: julian
"""
import pandas as pd

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)

print(df.index)

print(df.columns)

print(df.values)