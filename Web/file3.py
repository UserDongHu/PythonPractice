from bs4 import BeautifulSoup
import urllib.request as req

res = req.urlopen("http://127.0.0.1:5500/Web/daum.html")
soup = BeautifulSoup(res, 'html.parser')
print(soup.find('img')['src'])
for tag in soup.find_all('a'):
    print(tag['href'])
print(soup.select('#test1 > img'))