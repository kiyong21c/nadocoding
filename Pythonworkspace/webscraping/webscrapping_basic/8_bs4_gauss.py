import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()  # 문제있으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]    # 속성은 대괄호로 가져온다.
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()   # cartoon 객체에서 처음으로 만나는 strong엘리먼트 가져와서 텍스트 가져옴
    print(rate) # text로 가져온 str 형태임
    total_rates += float(rate)
print("전체점수:", total_rates)
print("평균점수 :", total_rates / len(cartoons))

# 터미널 클리어 : cls
# 터미널 빠져나가기 : exit()
