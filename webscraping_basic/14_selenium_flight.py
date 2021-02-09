from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 10일, 11일 선택
# browser.find_elements_by_link_text("10")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("11")[0].click() # [0] -> 이번달

# 다음 달 10일, 11일 선택
# browser.find_elements_by_link_text("10")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("11")[1].click() # [1] -> 다음달

# 이번 달 10일, 다음달 11일 선택
browser.find_elements_by_link_text("10")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("11")[1].click() # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행
    print(elem.text)
finally:
    browser.quit()


# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)