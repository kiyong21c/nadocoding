import time
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk   # 프로그레스바 사용하려면(tkinter패키지 안에 ttk모듈/클래스 사용)
from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.
# __init__모듈안에 __all__=["여기있는것들만 import * 할수 있음"]

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

def info():
    msgbox.showinfo("알림","정상적으로 예매 완료됨")      

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생.")

def okcancel():
    msgbox.askokcancel("확인/취소", "유아동방석입니다 예매하시겠습니까?")     # 사용자에게 물어봄(ok/cancel)

def retrycancel():
    response = msgbox.askretrycancel("재시도/취소", "일시적 오류입니다. 재시도하시겠습니까?")     # 사용자에게 물어봄(ok/cancel)
    print("응답:", response)   
    if response ==1:    # 재시도
        print("재시도")
    elif response ==0:  # 취소
        print("취소")

def yesno():
    msgbox.askyesno("예/아니오", "해당 좌석은 역방향입니다 예매하시겠습니까?")     # 사용자에게 물어봄(ok/cancel)

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매내역 저장안됨 \n 진행하시겠습니까?")     # 사용자에게 물어봄(ok/cancel)
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소(현재 화면에서 계속 작업)
    print("응답:", response)    # True, False, None -> 예:1, 아니오:0, 그외:
    if response ==1:
        print("예")
    elif response ==0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()



root.mainloop() # 창이 닫히지 않도록하는 mainloop()

