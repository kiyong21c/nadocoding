from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자, root는 메인 창 의미
root.title("Nado GUI")      # 제목 설정
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")     #label1 을 변경 .config(변경할 내용)
    
    global photo2               # photo2를 전역변수로 지정(하지 않으면 사라짐)
                                # 함수내에서 이미지를 바꿀때 전역변수 선언해야됨
    photo2 = PhotoImage(file="gui_basic/image2.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop() # 창이 닫히지 않도록하는 mainloop()
