# Regular Expression : RE, 정규 표현식

# 주민등록번호
# 891113-1111111 (o)
# abcdef-1111111 (x)

# 이메일 주소
# wjkajkejk@gmail.com
# kiyong21c@gmail.com@gmail.com (x)

# 차량번호
# 11가 1234
# 11가가 1234 (x)

# 정규식은 내용이 아주 많으므로 모두 다룰수가 없다.

import re   # 정규식 라이브러리 사용
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# casae, cabe, cace, cade, ...

p = re.compile("ca.e")      # pattern의 p
# . (ca.e): 하나의 문자 의미 > care, cafe (o) | caffe(x)
# ^ (^de): 문자열의 시작 > desk, destination (o) | fade(x)
# $ (se$): 문자열의 끝 > case, base (o) | face(x)

def print_match(m):
    if m:   # .match() 매치되는지
        print("m.group():", m.group())    # .group() 매치되지 않으면 에러발생, 일치하는 문자열반환
        print("m.string:", m.string)      # .string 입력받은 문자열 반환(함수가 아닌 변수: ()없음)
        print("m.start():", m.start())      # 일치하는 문자열의 시작 index 반환
        print("m.end():", m.end())        # 일치하는 문자열의 끝 index 반환
        print("m.span():", m.span())      # 일치하는 문자열의 시작/끝 index 반환
    else:
        print("매칭되지 않음")

# m = p.match("careless")    # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care")   # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# list = p.findall("good care cafe")   # findall() : 일치하는 모든것을 리스트 형태로 반환
# print(list)

# 1. p = re.compile("원하는 정규식 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 리스트 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e): 하나의 문자 의미 > care, cafe (o) | caffe(x)
# ^ (^de): 문자열의 시작 > desk, destination (o) | fade(x)
# $ (se$): 문자열의 끝 > case, base (o) | face(x)

# 구글에서 : w3school, pythonre 검색해서 공부