import csv , re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


context = ssl._create_unverified_context()
result = urlopen("https://sktmembership.tworld.co.kr/mps/pc-bff/benefitbrand/list-tab2.do", context=context)
soup = BeautifulSoup(result.read(), "html.parser")

f = open(r"data.csv", 'w', encoding='utf-8-sig', newline='')
csvWriter = csv.writer(f)


for key in soup.find_all('a', {'class':'benefit-box'}):
    data = key.text.strip()
    data=data.split()
    csvWriter.writerow(data)
f.close()





