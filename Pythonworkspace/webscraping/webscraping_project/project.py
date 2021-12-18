# Project) 웹 스크래핑 이용하여 나만의 비서를 만드시오.

# [조건]
# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다.
# 2. 헤드라인 뉴스 3건을 가져온다.
# 3. IT 뉴스 3건을 가져온다.
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.

# [출력 예시]

# [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도씨 (최저 00도/최고 00도)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00 좋음
# 초미세먼지 00 좋음

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이 ...
#  ( 링크 : http://...)
# 2. 어떤 어떤 일이 ...
#     ...
import requests
from bs4 import BeautifulSoup

def create_soup(url):       # 스크래핑 할때마다 사용되기 때문에 함수로 따뤄 빼줘서 사용(if __init__=="__main__": 에도 안들어가있는 함수 → 전역함수)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):     # 출력 할때마다 사용되기 때문에 함수로 따뤄 빼줘서 사용(if __init__=="__main__": 에도 안들어가있는 함수 → 전역함수)
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=heG1cdprvTVssRRrtpwssssstGN-367632"
    soup = create_soup(url)
    # 구름많음, 어제보다 3˚ 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 00도씨 (최저 00도/최고 00도)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")    # p 태그의 get_text()로 텍스트 가져오면 불필요한 "도씨"도 가져오게되어 replace()로 삭제
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()  # 최저온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()  # 최고온도
    # 오전 강수확률 00% / 오후 강수확률 00%
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()  # 텍스트 중 "% "의 공백 제거 → strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()  # 텍스트 중 "% "의 공백 제거 → strip()

    # 미세먼지 00 좋음
    # 초미세먼지 00 좋음
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()    # 미세먼지 : dl 태그의 indicator 클래스 안에 각각의 dd태그들 전체 텍스트를 인덱스로 불러옴
    pm25 = dust.find_all("dd")[1].get_text()    # 초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {}".format(curr_temp, min_temp, max_temp))
    print("오전 {}/ 오후{}".format(morning_rain_rate,afternoon_rain_rate))
    print() # 줄바꿈
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # li태그를 3개까지만
    for index, news in enumerate(news_list):
        title = news.div.a.get_text().strip()   # news.find("a").get_text() 이것과 동일
        link = url + news.find("a")["href"]    # a태그의 href 속성을 가져옴  <-  <a href="주소주소주소">
        # print("{}. {}".format(index+1, title))    # 자주 반복되므로 함수로 따로 정의
        # print("  (링크 : {})".format(link))
        print_news(index, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    new_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(new_list):
        a_idx = 0
        img = news.find("img")
        if img:         # img가 있으면
            a_idx = 1   # img 태그가 있으면 1번째 a 태그 정보를 사용
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
print()


if __name__ == "__main__":
    scrape_weather()    # 오늘의 날씨 정보 가져오기
# 이파일에서 직접 실행할때만 작동하고 다른파일에서 모듈로 사용하면 실행 안됨
    scrape_headline_news()    # 헤드라인 뉴스정보 가져오기
    scrape_it_news()
