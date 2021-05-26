# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:03:52 2021

@author: julian
"""


import time
from datetime import datetime
from ping3 import ping,verbose_ping

hostname = 'pkid'

result = ping(hostname)
if result == None:
    print(hostname + ': Error')
else:
    print(hostname + ': Active')
            