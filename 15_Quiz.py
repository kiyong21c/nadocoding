# Quiz) tkinter 를 이용한 메모장 프로그램을 만드시오

# [GUI 조건]
# 1. title : 제목 없음 - windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 Status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기


import os   # 파일있는지 없는지 확인, 읽기, 쓰기 하는 함수 사용
from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("제목 없음")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):    # 파일 있으면 True
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)  # 처음(1행.0열(인덱스))부터 끝까지 본문변수(txt) 삭제
            txt.insert(END, file.read())    # 본문변수(txt)에 입력
    

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 본문변수(txt) 내용 가져와서 저장

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)  # 상단바(파일) 빈껍데기 

# 편집, 서식, 보기, 도움말
menu.add_cascade(label="편집")      # .add_casacade() 상단바에 빈껍데기 만듦
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root) # 매칭시킬 본문도 root에 위치하므로, root에 바로 넣어줌
scrollbar.pack(side="right", fill="y")  # 오른쪽 위치에 위아래로 채워줌

'''pack() 쌓는개념'''
'''grid() 배치개념'''
'''config() 매치개념'''

# 본문 영역 
txt = Text(root, yscrollcommand=scrollbar.set)   # txt와 scrollbar 매핑
txt.pack(side="left", fill="both", expand=True)  # 전체 공간을 꽉채움
scrollbar.config(command=txt.yview)  # txt와 scrollbar 매핑하여 그려줌(config)

root.config(menu=menu)  # menu함수에 작성한 menu변수를 그려줌(config)

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

