from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

# 체크박스(팝업이 떠서 선택)
chkvar = IntVar()   # chkvar 에 Int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) # 체크박스는 variable= Int값 필요
# chkbox.select()     # 자동 선택처리(디폴트가 선택)
# chkbox.deselect()   # 선택 해제처리
chkbox.pack()

chkvar2 = IntVar()   # chkvar2 에 Int형으로 값을 저장
chkbox2 = Checkbutton(root, text="일주일동안  보지 않기", variable=chkvar2) # 체크박스는 variable= Int값 필요
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

