import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'b391124be29da95058f96106f9b92a1e'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'JF0jtAHk-tFSovZiMuPlW8aZSwQVwXpoJA9CRVTDbWm0byXJpY_E7SaySF6pCNOPuppDjgo9dBEAAAF7yW3tzg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"C:\Users\julian\Desktop\kakao_code.json","w") as fp:
    json.dump(tokens, fp)

#2.
#with open("kakao_code.json","w") as fp:
#    json.dump(tokens, fp)