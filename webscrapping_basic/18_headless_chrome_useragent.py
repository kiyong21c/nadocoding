from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920*1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67")


browser = webdriver.Chrome(options=options)     # 여기서 계속 오류 발생
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# User-Agent
# 어떤 페이지를 보여줄지, 사람이 맞는지 확인
# Requests : 빠르다, 동적 웹페이지 X
# Selenium : 느리다, 동적 웹페이지 O, 로그인, 필터링 등 사용자가 어떤 동작을 해야하는 경우 (크롬 버전에 맞는 chromedriver.exe 필요 )
    # find_element(s)_by_id             : id로 찾기
    # find_element(s)_by_class_name     : class name으로 찾기
    # find_element(s)_by_link_text      : 링크 text로 찾기
    # find_element(s)_by_xpath          : xpath로 찾기
    # click()                           : 클릭
    # send_keys()                       : 글자 입력
    # 시간이 걸리는 경우 WebDriverWait()
    # 스크롤 내려줘야 하는 경우 
# BeautifulSoup
    # find                              : 조건에 맞는 첫번째 element
    # find_all                          : 조건에 맞는 모든 element 리스트로
    # find_next_sibling(s)              : 다음 형제 찾기
    # find_previous_sibling(s)          : 이전 형제 찾기
    # soup["href"]                      : 속성
    # soup.get_text()                   : 텍스트