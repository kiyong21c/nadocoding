# 구글 무비에서 인기차트에서 할인중인 영화만 뽑아오기

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    "Accept-Language":"ko-KR,ko"
    }   # ,"Accept-Language":"ko-KR,ko" -> 한글언어로 된 페이지를 달라고 요청(없으면 기본설정 언어요청됨)
# headers를 이용해서 사용자 정보를 넘겨주지 않으면 기본언어 설정인 영어 페이지를 받아오게되어 오류가 발생할 수 있음
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

# print(len(movies))  # movies의 element 개수 확인
# 동적페이지(스크롤 내릴때마다 로딩이 뜨고 영화가 추가됨)이기 떄문에 10개 elements만 가져옴
# Selenium을 이용해야지 동적페이지도 전체 스크래핑이 가능함

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(res.text)           # html 어떻게 구성되어있나 파일로 열어봄
#     f.write(soup.prettify())    # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)