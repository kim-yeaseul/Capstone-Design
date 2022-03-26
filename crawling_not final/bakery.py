from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



context = ssl._create_unverified_context()
result = urlopen("https://sktmembership.tworld.co.kr/mps/pc-bff/benefitbrand/detail.do?brandId=1053#", context=context)
result2 = urlopen("https://sktmembership.tworld.co.kr/mps/pc-bff/benefitbrand/list-tab1.do?mediumCategoryId=55", context=context)
soup = BeautifulSoup(result.read(), "html.parser")
soup2 = BeautifulSoup(result2.read(), "html.parser")


brand = soup.select('div')
for div in brand:
    print(div.text)

brand2 = soup2.select('div')
for div in brand2:
    print(div.text)
