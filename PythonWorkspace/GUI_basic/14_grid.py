from tkinter import *
from typing import Coroutine, Sized  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# btn1.pack()
# btn2.pack()

# btn1.pack(side="left")
# btn2.pack(side="right")
# pack은 쌓는 느낌, grid는 해당위치에 넣는 느낌

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 첫 줄
btn_f16 = Button(root, text="F16", width=5, height=2)    # 버튼의 x,y 크기(padx는 여백, width는 크기)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)       # 동서남북으로 붙어라(sticky)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)       # 버튼간의 간격(그리드의 x,y 간격)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)   # row(줄) 아래 두줄을 합치겠다(rowspan)

# 둘째 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equl = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)   # column(열) 오른쪽 두줄 합치겠다
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop() # 창이 닫히지 않도록하는 mainloop()

