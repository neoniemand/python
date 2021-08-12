# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:51:02 2021

@author: julian
"""

import requests
import json

url = "https://dapi.kakao.com/v2/search/web"
queryString = {'query':'양궁'}
header = {'authorization':'KakaoAK b391124be29da95058f96106f9b92a1e'}
response = requests.get(url, headers=header, params=queryString)
tokens = response.json()

print(response)
print(tokens)
