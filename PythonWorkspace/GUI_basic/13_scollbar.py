from tkinter import *
from typing import Coroutine, Sized  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스크롤 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)
# scrollbar와 listbox를 하나의 frame에 넣어놓고 서로를 바라보도록(config) 맵핑

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

