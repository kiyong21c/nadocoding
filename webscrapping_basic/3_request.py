import requests

res = requests.get("http://naver.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()  # 문제가 생기면 오류를 내고 끝내버림
print("응답코드:", res.status_code)     # 200 이면 정상 동작

# if res.status_code == requests.codes.ok:        # requests.codes.ok : 200(정상)
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mynaver.html", "w", encoding="utf8") as f:      # 파일을 만들기
    f.write(res.text)                                      # 파일 내용 쓰기 : res.text내용
