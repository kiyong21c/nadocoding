import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()  # 문제있으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())    # title내에 텍스트만 받아오는함수
# print(soup.a)   # soup 객체에서 첫번째로 발견되는 a 엘리먼트 정보 출력
# print(soup.a.attrs) # a 엘리먼트의 속성 정보 출력
print(soup.a["href"])   # .a[] a엘리먼트의 href 속성 "값" 정보를 출력

# soup.find("a", attrs={"class":"Nbtn_upload"})
# 첫번째 a 엘리먼트에 해당하고, class가 Nbtn_upload에 해당하는것 찾기
# print(soup.find(attrs={"class":"Nbtn_upload"}))

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling # 다음 위치의 형제 엘리먼트로
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent) # rank1 의 부모엘리먼트 출력
# rank2 = rank1.find_next_sibling("li")   # rank1기준으로 다음 형제 엘리먼트를 찾는데 li인것만 찾는다.
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text)

# rank1.find_next_siblings("li")  # li 형제들 모두 가져옴

webtoon = soup.find("a", text="연애혁명-363. after raining")
print(webtoon)