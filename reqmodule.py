import requests
from bs4 import BeautifulSoup

# response = requests.get("https://sahikhao.com")
# print(response.text)
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
#
# data = {
#     "title": 'Nikul',
#     "body": 'Prajapati',
#     "userId": 100,
#   }
#
# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers = headers, json = data)
# print(response.text)


url = "https://newsapi.org/"

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h3"):
    print(heading.text)
