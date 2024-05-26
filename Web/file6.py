from bs4 import BeautifulSoup
import requests

response = requests.get("https://cse.inu.ac.kr/bbs/isis/376/374805/artclView.do")

html = response.text

soup = BeautifulSoup(html, 'html.parser')

a = soup.select('.view-con')

for i in a:
    print(i.text.replace(' ', '').replace('\n', '').replace('\xa0', ''))