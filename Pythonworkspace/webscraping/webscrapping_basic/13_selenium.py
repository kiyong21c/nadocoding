# 크롬 드라이버 설치 필요( 크롬 버전과 호환 여부 확인 필요, chrome://version)
# https://chromedriver.chromium.org/downloads
# 윈도우 버전(32bit) 다운로드 받아서 PYTHONWORKSPACE에 압축해제

import time
from selenium import webdriver

# browser = webdriver.Chrome("./chromedriver.exe")    # C대문자
browser = webdriver.Chrome()                        # 같은 경로에 있으면 로컬주소 필요 없음

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 아이디와 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)   # 3초대기

# 5. 아이디 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()    # 기존 naver_id라고 써진것 삭제
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)  # browser 페이지에 있는 html을 그대로 출력

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료


# 터미널에서 파이썬 사용
#   python  : 사용 시작
#   exit()  : 사용 종료
