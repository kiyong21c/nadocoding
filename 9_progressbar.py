import time
import tkinter.ttk as ttk   # 프로그레스바 사용하려면(tkinter패키지 안에 ttk모듈/클래스 사용)
from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.
# __init__모듈안에 __all__=["여기있는것들만 import * 할수 있음"]

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표


# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")  # "언제끝날지모름"
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)   # 10ms 마다 움직임( 클수록 느리게 움직임)
# progressbar.pack()


# def btncmd():
#     progressbar.stop()  # 작동중지
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()    #실수반영
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)           # progress bar 의 값 설정
        progressbar2.update()   # for 문 동작할때 마다 update되도록 : 서서히 증가하는 모양
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop() # 창이 닫히지 않도록하는 mainloop()

