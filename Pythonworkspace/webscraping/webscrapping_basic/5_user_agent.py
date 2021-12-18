import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
res = requests.get(url, headers=headers)    # url에 접속할때, "User-Agent"키의 값을 넘겨줌
res.raise_for_status()  # 문제가 생기면 오류를 내고 끝내버림
with open("nadocoding.html", "w", encoding="utf8") as f:      # 파일을 만들기
    f.write(res.text)                                      # 파일 내용 쓰기 : res.text내용
