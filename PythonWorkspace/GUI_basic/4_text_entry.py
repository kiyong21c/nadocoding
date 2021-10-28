from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5)  # 글상자 넣기 Text() : 여러줄 입력가능 
txt.pack()
txt.insert(END, "글자를 입력하세요")    # 글상자에 글추가(insert) 글자입력 인덱스의 위치 END

e = Entry(root, width=30)       # Entry는 한줄로 입력받는 글상자(엔터 안쳐짐)
e.pack()
e.insert(0, "한 줄만 입력해요")  # END 와 0 동일


def btncmd():
    #내용 출력
    print(txt.get("1.0", END))      # "1.0" ; 첫행.0번째열(인덱스) 부터 끝(END)까지
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

