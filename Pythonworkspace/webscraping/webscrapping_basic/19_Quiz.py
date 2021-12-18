# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ========= 매물 1 ==========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# ========== 매물 2 ==========
#     ...

import requests
from bs4 import BeautifulSoup
from bs4.element import ContentMetaAttributeValue
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 홈페이지 이동
url = "https://new.land.naver.com/complexes/111515?ms=37.49751,127.107693,17&a=APT:JGC:ABYG&e=RETAIL"
browser.get(url)
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# soup객체를 이용해서 html 파일을 만든다음에 원하는 정보가 있는지확인(동적페이지인지도 확인가능)
# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 문서의 스크롤 높이를 받아와서(return) prev_height변수에 저장

# 반복 수행:
while True: # 무한반복
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 탈출 조건
    if curr_height == prev_height:
        break

    prev_height = curr_height   # 문서높이 업데이트

print("스크롤 완료")