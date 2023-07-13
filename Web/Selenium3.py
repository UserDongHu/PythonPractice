# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())



driver = webdriver.Chrome(service=service, options=chrome_options)

w = open('Web/hotdeal.csv', 'a')
writer = csv.writer(w)

IS_DUPLICATE = False

# 웹페이지 해당 주소 이동
for i in range(3):
    if(IS_DUPLICATE):
        break
    driver.get(f"https://www.fmkorea.com/index.php?mid=hotdeal&page={i+1}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"Wrapper")))#10초까지 기다림
    webdriver.ActionChains(driver).key_down(u'\ue010').key_up(u'\ue010').perform()#페이지 끝까지 내린후에 크롤링

    elements = driver.find_elements(By.CLASS_NAME, "li_best2_pop0")
    for element in elements:
        if(IS_DUPLICATE):
            break
        title = element.find_element(By.CLASS_NAME, "title").text
        link = element.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, 'a').get_attribute('href')
        for j in range(len(title)):#댓글 몇개인지 없애기
            if title[len(title)-j-1] == "[":
                title = title[:len(title)-j-3]
                break
        imglink = element.find_element(By.TAG_NAME, "img").get_attribute('src')
        hotdeal_info = element.find_element(By.CLASS_NAME, "hotdeal_info").text

        hotdeal_data = []
        hotdeal_data.append(title)
        hotdeal_data.append(hotdeal_info)
        hotdeal_data.append(link)
        hotdeal_data.append(imglink)

        r = open('Web/hotdeal.csv', 'r')
        reader = csv.reader(r)
        for row in reader:
            if(row == hotdeal_data):
                IS_DUPLICATE = True
                break
        r.close()
        if(IS_DUPLICATE == False):
            writer.writerow(hotdeal_data)
            print(title)
            print(hotdeal_info)
            print(link)
            print(imglink)
            print("----------------------------------")
w.close()