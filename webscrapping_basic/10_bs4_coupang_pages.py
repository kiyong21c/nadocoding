# HTTP METHOD
# GET, POST 방식
# GET : 누구나 볼수 있게 URL에 적어서 보내는 방식(? 뒤에 변수와 값, 변수와 값)
        # 큰데이터는 보내지 못함, 웹스크래핑 용이
# POST : 보안데이터는 숨겨서 보냄, 큰데이터(파일같은) 전송방식

# URL 조작만으로 웹스크래핑 가능 : GET 방식
# 페이지는 변하는데 URL정보는 그대로인 경우 : POST 방식

import requests
import re       # 정규식 사용하기 위함
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
# headers 변수로 구글에서 나의 유저 에이전트 값을 받아옴(사람이 접속하는것으로 인식시켜줌)

for i in range(1,6):
    # print("페이지:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})       # ^ : search-product로 시작하는 li엘리먼트 가져오게됨
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:

            # 광고 제품은 제외
            ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
            if ad_badge:    # ad_badge 변수가 존재한다면
                    print("  <광고 상품 제외합니다.>")
                    continue

            name = item.find("div", attrs={"class":"name"}).get_text()
            
            # 애플 제품 제외
            if "Apple" in name:     # apple 문자가 name에 있으면
                    print("  <Apple 상품 제외합니다.>")
                    continue

            price = item.find("strong", attrs={"class":"price-value"}).get_text()
            
            # 리뷰 100개 이상, 평점 4.5 이상 되는것만 조회

            rate = item.find("em", attrs={"class":"rating"})        # 평점이 없는 항목이 있으므로 if문 작성
            if rate:        # rate 가 있으면
                rate = rate.get_text()
            else:
                print("  <평점 없는 상품 제외합니다.>")
                continue

            rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
            if rate_cnt:        # rate_cnt 가 있으면
                rate_cnt = rate_cnt.get_text()       # 예 : (26)
                rate_cnt = rate_cnt[1:-1]            # 예 :  26
            else:
                print("  <평점 수 없는 상품 제외합니다.>")
                continue
            
            link = item.find("a", attrs={"class":"search-product-link"})["href"]


            if float(rate) >= 4.5 and int(rate_cnt) >= 100 :
                    # print(name, price, rate, rate_cnt)
                    print(f"제품명 : {name}")
                    print(f"가격 : {price}")
                    print(f"평점 : {rate}점 ({rate_cnt})")
                    print("바로가기: {}".format("https://www.coupang.com/"+link))
                    print("-"*100) # 줄 긋기
    