# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#https://0433.tistory.com/41 << 참고할 블로그

# 1.네비게이션 관련 툴
driver.get("https://www.naver.com")
time.sleep(3)
# driver.get("https://google.com")
# time.sleep(3)

# driver.back()
# time.sleep(3)

# driver.forward()
# time.sleep(3)

# driver.refresh()
# time.sleep(3)



# 2.browser information
# title = driver.title
# print(title)

# current_url = driver.current_url
# print(current_url)

# if "nid.naver.com" in current_url:
#     print("지금은 로그인 하는 로직이 필요함.")
# else:
#     print("내가 계획한 로직 그대로 실행하면 됨")



# 3. Driver Wait
# 10초까지는 기다리겠다 selector가 찾아질때까지.
selector = "#shortcutArea > ul > li:nth-child(2) > a"
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
except:
    print("예외발생")
print("다음 코드 실행")

#selector = "#shortcutArea > ul" #요소 찾아서 가져오기
# group_navigation = driver.find_element(By.CSS_SELECTOR, selector) #찾아온 요소 가져와서 담기
# print(group_navigation.text)
# group_navigation.click()
# input()