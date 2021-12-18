# # 구글 무비에서 인기차트에서 할인중인 영화만 뽑아오기

from bs4.element import ContentMetaAttributeValue
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920*1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 홈페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# PC 해상도 가로 정보 : 1080 -> 1080만큼 위치로 스크롤 다운
# browser.execute_script("window.scrollTo(0, 1080)")
# browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

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
browser.get_screenshot_as_file("google_movie.png")  # headless를 이용해서 크롬창이 안떠도 스크린샷으로 찍을수 있음

import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))  # movies의 element 개수 확인

# 동적페이지(스크롤 내릴때마다 로딩이 뜨고 영화가 추가됨)이기 떄문에 10개 elements만 가져옴
# Selenium을 이용해야지 동적페이지도 전체 스크래핑이 가능함

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:  # original_price가 존재한다면
        original_price = original_price.get_text()
    else:
        # print(title, "<할인되지 않은 영화 제외>")
        continue

    # 할인 후 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]    # a태그의 href 속성
    # 올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)
    
browser.quit()

# 화면을 볼필요 없으면 브라우저를 띄울 필요가 없음 : Headless(Chrome을 띄우지 않음)