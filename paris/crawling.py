from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import folium
import collections
from collections import OrderedDict
import csv
import lxml

chrome_driver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chrome_driver)
driver.implicitly_wait(5) # 응답의 시간 지연
# url = 'https://www.paris.co.kr/store'
url = 'https://www.paris.co.kr/store'
# chrome driver로 해당 페이지가 물리적으로 open
driver.get(url)

# 값을 담을 리스트
starbucks = []

# 열린 페이지에서 '지역 검색' 탭 클릭
search = driver.find_element_by_link_text('검색해서 찾기')
time.sleep(1)
search.click()

time.sleep(1)
# 개발자도구로 class : set_sido_cd_btn의 데이터 긁어옴
search = driver.find_elements_by_class_name('selected highlighted')

for item in search:
    item.click()
    time.sleep(1)
    
    # data-sidocd='01~17' 서울~충북 
    if '17' == item.get_attribute('data-index'):
        # 소스 가져오기
        src = driver.page_source
        
        # BeautifulSoup 객체로 변환
        soup = BeautifulSoup(src, 'lxml')
        name = soup.select('li[data-name]')
        for name_one in name:
            x = name_one['data-latitude'] # 위도 저장
            y = name_one['data-longtitude'] # 경도 저장
            z = name_one['store-name'] # 지점명 저장
            p = name_one.select_one('p').text.split('혜택보기')[0] # 번호는 모든 지점이 동일하여 crawling에서 제외
            starbucks.append({'name': z, 'address': p, 'lat': x, 'long':y}) # dict 형태로 리스트에 저장
        time.sleep(1)
        
        # 열린 페이지 닫기
        driver.close()
    else:
        search2 = driver.find_element_by_link_text('전체')
        search2.click()
        driver.implicitly_wait(5)
        time.sleep(1)
        
        src = driver.page_source

        soup = BeautifulSoup(src, 'lxml') 
        name = soup.select('li[data-name]')
        for name_one in name:
            x = name_one['data-latitude']
            y = name_one['data-longtitude']
            z = name_one['store-name']
            p = name_one.select_one('p').text.split('혜택보기')[0]
            starbucks.append({'name': z, 'address': p, 'lat': x, 'long':y})
        time.sleep(0)
        
        # 다시 지역 검색 탭으로 돌아가기위한 소스
        search3 = driver.find_element_by_link_text('검색해서 찾기')
        search3.click()
        time.sleep(1)


# newline=''을 넣으면 공백라인 제거
with open('starbucks_final.csv', 'w', newline='') as f:
    fieldnames =['지점명', '주소', '위도', '경도']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in starbucks:
        writer.writerow({'지점명': (i['name']), '주소': (i['address']), '위도': (i['lat']), '경도': (i['long'])})

