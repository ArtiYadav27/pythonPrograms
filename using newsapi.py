import requests
import json
query=input("what type of news you are intrested in..")
url=f'https://newsapi.org/v2/top-headlines?q={query}&apiKey=7dd955b2a1f541aead251bfc3ba2a1bc'
r=requests.get(url)
news=json.loads(r.text )
for articles in news['articles']:
    print(articles['title'])
    print(articles['description'])
    print('____________________________________________________________________________________________________')
