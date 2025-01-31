# GET https://newsapi.org/v2/everything?q=Apple&from=2025-01-31&sortBy=popularity&apiKey= 0cae33c3b8d5459792202a235ddd83e2

# import requests
# from bs4 import BeautifulSoup
#
# # Authorization: 0cae33c3b8d5459792202a235ddd83e2
#
# url = "https://newsapi.org/v2/everything?q=tesla&from=2024-12-31&sortBy=publishedAt&apiKey = 0cae33c3b8d5459792202a235ddd83e2"
#
# r = requests.get(url)
# # soup = BeautifulSoup(r.text, "html.parser")
#
# print(r.json)
# for news in soup.find_all(""):
#     print(news.text)

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2025-01-31&'
       'sortBy=popularity&'
       'apiKey=0cae33c3b8d5459792202a235ddd83e2')

response = requests.get(url)

# print (response)