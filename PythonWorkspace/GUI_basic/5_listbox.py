from tkinter import *  
# tkinter 패키지/모듈(파이썬 기본내장 모듈)안에 있는 모든 함수를 사용하겠다.

root = Tk()     # T대문자 k소문자
root.title("Nado GUI")      # 제목 설정
#root.geometry("640x480")    # 창의 크기: 가로 * 세로( 곱하기*를 x소문자로 사용)
root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

# list box 는 여러줄에 걸친 목록 관리
listbox = Listbox(root, selectmode="extended", height=0)
# "extended" 항목 여러개 선택가능, "singel" 한항목만 선택, height 리스트 박스 보여줄 항목수(0은 전체)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")     # insert(인덱스, 추가항목)
listbox.insert(END, "수박")     # END 맨마지막 인덳스에 넣어줌
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    pass
    # 삭제
    # listbox.delete(END) # 맨뒤항목 삭제
    
    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인(시작 idx, 끝 idx)
    # print("1번 항목 부터 3번 항목까지의 항목:", listbox.get(0,2))

    # 선택된 항목 확인(위치(인덱스)로 반환)
    # print("선택된 항목:", listbox.curselection())   # 인덱스 값으로 나옴

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록하는 mainloop()

