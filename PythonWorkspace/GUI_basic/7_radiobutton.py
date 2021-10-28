from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

# 라디오버튼(여러개중 택 1)
Label(root, text="메뉴를 선택하세요").pack()    # 변수에 저장했다가 pack()하지 않고 바로.pack()

burger_var = IntVar()   # Int형으로 변수 저장(value가 Int로 할당되므로)
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()    # 기본 선택되도록
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()    # 변수에 저장했다가 pack()하지 않고 바로.pack()

drink_var = StringVar() # Str형으로 변수 저장(value가 Str로 할당되므로)
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()     # 기본 선택되도록
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())     # 선택된 라디오 항목의 값(value) 반환
    print(drink_var.get())     # 선택된 라디오 항목의 값(value) 반환
    
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

