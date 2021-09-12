from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자, root는 메인 창 의미
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(높이)값 변경 불가: 창 크기 변경 불가

# 버튼 생성
btn1 = Button(root, text="버튼1")
btn1.pack()     # pack() 함수를 사용해야 버튼이 보임

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # padx, pady 버튼 크기 조절
btn2.pack()                                                   # 버튼text 길어져도 공간확보

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")   #width, height 정해진 크기
btn4.pack()                                             # 버튼 text 길어지면 text잘림

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")  # fg : forward Ground (글자색), bg : background(배경색)
btn5.pack()

photo = PhotoImage(file="gui_basic/image.png")      # 그림판으로 28 * 28 이미지 저장함
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() # 창이 닫히지 않도록하는 mainloop()
