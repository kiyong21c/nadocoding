import tkinter.ttk as ttk   # 콤보박스 사용하려면(tkinter패키지 안에 ttk모듈 사용)
from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

# 콤보 박스(여러 목록 중 선택)
values = [str(i) + "일" for i in range(1,32)]   # 1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 콤보박스에 입력 불가
readonly_combobox.current(0)    # 0번째 인덱스값 선택
readonly_combobox.pack()



def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

