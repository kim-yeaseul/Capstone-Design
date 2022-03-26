import csv , re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


context = ssl._create_unverified_context()
result = urlopen("https://sktmembership.tworld.co.kr/mps/pc-bff/benefitbrand/list-tab2.do", context=context)
soup = BeautifulSoup(result.read(), "html.parser")

category = soup.find_all('a', class_="benefit-box")
for benefit in category:
    print(benefit.text)




