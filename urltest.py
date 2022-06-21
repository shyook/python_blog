from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

#step2.검색할 키워드 입력
query = ['남동논현도서관 방학', '괴산 나무그늘 캠핑장', '논현동 황선장네', '논현동 빨간냄비', '서창2지구 땅스', '논산 탑정호 장어', '서창2지구 떡볶이 맛집', '도림동 냉면맛집'
         , '주안역 짬뽕 맛집', '인천 선학 빙상경기장 스케이트', '도림동 장어의신', '만수3지구 정정아', '인천대공원 재현', '주안 돌판향기', '주안역센트레빌 사전점검']
link = ['#twaColl > div.coll_cont > ul > li.scrollWrapper.ty_next > a.tit_main'
        , '#twaColl > div.coll_cont > ul > li.scrollWrapper.ty_next > a.tit_main'
        , '#twaColl > div.coll_cont > ul > li.scrollWrapper.ty_next > a.tit_main'
        , '#twaColl > div.coll_cont > ul > li:nth-child(3) > div > a'
        , '#twaColl > div.coll_cont > ul > li:nth-child(3) > div.wrap_cont > a'
        , '#twaColl > div.coll_cont > ul > li.scrollWrapper.ty_next > a.tit_main'
        , '#twaColl > div.coll_cont > ul > li:nth-child(4) > div > a'
        , '#twaColl > div.coll_cont > ul > li:nth-child(3) > div > a'
        , '#twaColl > div.coll_cont > ul > li:nth-child(1) > div > a'
        , '#twaColl > div.coll_cont > ul > li:nth-child(2) > div > a'
        , '#twaColl > div.coll_cont > ul > li.scrollWrapper.ty_next > a.tit_main'
        , '#twaColl > div.coll_cont > ul > li.scrollWrapper.ty_next > a.tit_main'
        , '#twaColl > div.coll_cont > ul > li:nth-child(2) > div > a'
        , '#twaColl > div.coll_cont > ul > li:nth-child(4) > div > a'
        , '#twaColl > div.coll_cont > ul > li:nth-child(6) > div > a']
# totalCount = len(query)
# input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.daum.net/'
driver = webdriver.Chrome('/Users/shyook/Desktop/3_shyook/1_Python/20220614_helloworld/venv/chromedriver')
driver.get(url)
time.sleep(3)

for count in range(0, len(query)):
#step4.검색창에 키워드 입력 후 엔터
    search_box = driver.find_element(by=By.CSS_SELECTOR, value="input#q.tf_keyword")
    search_box.clear()
    search_box.send_keys(query[count])
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

#step5.검색 결과중 원하는 링크 클릭
    web_find = driver.find_element(by=By.CSS_SELECTOR, value=link[count])
    web_find.click()

    driver.switch_to.window(driver.window_handles[-1])
    # driver.get_screenshot_as_file('capture.png')
    time.sleep(1)

    result = driver.find_element(by=By.CSS_SELECTOR, value='#mainFrame')
    result.click()

# driver.get_screenshot_as_file('capture.png')
    time.sleep(1)

    for i in range(1, 360):
        result.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
driver.close()



# time.sleep(2)
#
# driver.switch_to.window(driver.window_handles[-1])
# driver.get_screenshot_as_file('capture.png')
# web_find.click()
# time.sleep(2)


