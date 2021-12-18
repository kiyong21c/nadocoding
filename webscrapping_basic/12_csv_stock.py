import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 엑셀파일에서 열때 한글이 깨지면 encoding="utf-8-sig"
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# 탭으로 구분된 텍스트를 나누어서 리스트에 들어감
# print(type(title))
writer.writerow(title)   # writerow()안에는 리스트형태가 들어가야함

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    date_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in date_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:   # 의미없는 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns]    # strip() 불필요한것들 제거
        # print(data)
        writer.writerow(data)