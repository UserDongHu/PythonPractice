from bs4 import BeautifulSoup
import requests
import re

mykeyword = 'apple' # 검색하고싶은 키워드
res = requests.get(f'https://www.fmkorea.com/search.php?mid=hotdeal&category=1196845148&listStyle=webzine&search_keyword={mykeyword}&search_target=title') # 가전제품 카테고리에서 제목 검색
res.raise_for_status() # 200(정상)이 아니면 오류 발생

html = res.text
soup = BeautifulSoup(html, 'html.parser')
myproductlist = []
productlist = soup.select('#content>.content_dummy>div>div>div>ul>li')

for container in productlist:
    title = container.select('.title a')[0].text.strip()
    title = re.sub(r'\t|\xa0|\[\d+\]', '', title)

    price = container.select('.hotdeal_info>span')[1].select('.strong')[0].text

    myproductlist.append([title, price])
print(myproductlist)