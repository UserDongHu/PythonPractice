# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

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

querys = ["파이썬 Selenium", "python flask"]
target_blog_links = ["https://blog.naver.com/lsy86825/222481340392", "https://cafe.naver.com/hacosa/"]

for query, target_blog_link in zip(querys, target_blog_links):
    search_link = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}"
    driver.get(search_link)

    link_selector = f'a[href^="{target_blog_link}"]'

    current_rank = -1
    BLOG_FOUND = False

    for _ in range(7): #최대 7번 하위 랭크 블로그 글을 불러오겠음.   
        try:
            element = driver.find_element(By.CSS_SELECTOR, link_selector)
            while True:
                new_element = element.find_element(By.XPATH, "./..")
                current_rank = new_element.get_attribute("data-cr-rank")
                if current_rank != None:
                    BLOG_FOUND = True
                    break
                element = new_element
            if BLOG_FOUND:
                break
        except:
            print("타겟 블로그를 못 찾음 -> 스크롤하겠습니다.")
            driver.execute_script("window.scrollBy(0,10000);")
            time.sleep(3)
    print(f"{query}를 검색했을때 {target_blog_link}의 순위는 {current_rank}등 입니다.")