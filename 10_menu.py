import time
import tkinter.ttk as ttk   # 프로그레스바 사용하려면(tkinter패키지 안에 ttk모듈/클래스 사용)
from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.
# __init__모듈안에 __all__=["여기있는것들만 import * 할수 있음"]

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

menu = Menu(root)

def create_new_file():
    print("새파일을 만듭니다.")

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()           # 구분하는 줄 생성
menu_file.add_command(label="Open File...")
menu_file.add_separator()           # 구분하는 줄 생성
menu_file.add_command(label="Save All", state="disable")    # 비활성화
menu_file.add_separator()           # 구분하는 줄 생성
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)  # menu file 들을 묶어서 창에 File 만들어줌

# Edit 메뉴( 빈값)
menu.add_cascade(label="Edit")  # 클릭해도 하단에 아무것도 없음

# Language 메뉴 추가(radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 추가(체크박스 메뉴 추가)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)



root.config(menu=menu)
root.mainloop() # 창이 닫히지 않도록하는 mainloop()

