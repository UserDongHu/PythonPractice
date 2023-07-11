from bs4 import BeautifulSoup
import requests

url = "https://www.fmkorea.com/hotdeal"
res = requests.get(url)
res.raise_for_status() #웹페이지를 정상적으로 사용할수있는지 확인.

soup = BeautifulSoup(res.text, "lxml") #가져온 html문서를 파서를 통해 객체로 만듦.

deallist = soup.find_all("div", attrs={"class":"li"})
for list in deallist:
    if(list.h3):
        print(list.h3.a.get_text()[:-6].strip())
        print(list.div.span.get_text().strip(),end=" / ")
        print(list.div.span.next_sibling.next_sibling.get_text().strip(), end=" / ")
        print(list.div.span.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip())
        print("링크 : https://www.fmkorea.com"+list.div.a["href"])
        print("-----------------------------------------")
