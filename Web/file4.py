from bs4 import BeautifulSoup
import requests

url = "http://www.inu.ac.kr/user/indexSub.do?codyMenuSeq=1101526&siteId=isis"
res = requests.get(url)
res.raise_for_status() #웹페이지를 정상적으로 사용할수있는지 확인.

soup = BeautifulSoup(res.text, "lxml") #가져온 html문서를 파서를 통해 객체로 만듦.

no = soup.find_all("td", attrs={"class":"no"})
titles = soup.find_all("td", attrs = {"class":"title"})
for i in range(len(titles)):
    print("No."+no[i+1].get_text().strip()+" ",end="")
    print(titles[i].get_text().strip())
    print("링크 : http://www.inu.ac.kr/user/"+titles[i].a["href"])