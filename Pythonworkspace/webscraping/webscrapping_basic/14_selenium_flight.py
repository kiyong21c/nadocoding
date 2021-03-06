from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()   # 창을 전체 화면으로

url = "https://flight.naver.com/flights/"
browser.get(url)    # url로 이동

browser.find_element_by_link_text("가는날 선택").click()    # 가는날 선택 클릭

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달 달력에서 선택
# browser.find_elements_by_link_text("28")[0].click()  # [0] -> 이번달 달력에서 선택

# 다음달 27, 28일 선택
# browser.find_elements_by_link_text("27")[1].click()  # [0] -> 다음달 달력에서 선택
# browser.find_elements_by_link_text("28")[1].click()  # [0] -> 다음달 달력에서 선택

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # [0] -> 다음달 달력에서 선택
browser.find_elements_by_link_text("28")[1].click()  # [1] -> 다음달 달력에서 선택

# 제주도 선택(x path 활용)
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:    # 에러가 났을떄는 프로그램 종료 시켜버림(이후동작 필요없음) -> try:, finally 로 묶어줌
    # 로딩 처리방법(로딩끝나면 다음 명령 처리하게끔)
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 프로그램 (최대)10초간 대기하는데, EC(특정조건)인 XPAHT 의해(BY.) 주소("")에 해당하는 값이 위치할때 까지 
    print(elem.text)
finally:    
    browser.quit()

# # 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)