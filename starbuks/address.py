from bs4 import BeautifulSoup 
from selenium import webdriver 
import time 

driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
driver.get('https://www.starbucks.co.kr/store/store_map.do?disp=locale') 
time.sleep(20) 

loca = driver.find_element_by_class_name('loca_search') 
loca.click() 
time.sleep(20) 

sido = driver.find_element_by_class_name('sido_arae_box') 
li=sido.find_elements_by_tag_name('li') 
li[0].click() 
time.sleep(20) 

gugun = driver.find_element_by_class_name('gugun_arae_box') 
li=gugun.find_elements_by_tag_name('li') 
li[1].click() 
time.sleep(20) 

source=driver.page_source 

bs=BeautifulSoup(source,'lxml') 
entire=bs.find('ul', class_='quickSearchResultBoxSidoGugun') 
starbucksGangnam_list=entire.find_all('li') 

print("매장 수 : ", len(starbucksGangnam_list)) 
for stores in starbucksGangnam_list: 
    print("매장명 :", stores.find('strong').text, "매장 주소 :" , stores.find('p').text)


