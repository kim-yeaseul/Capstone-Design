from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



context = ssl._create_unverified_context()
result = urlopen("https://sktmembership.tworld.co.kr/mps/pc-bff/benefitbrand/list-tab1.do?mediumCategoryId=55", context=context)
soup = BeautifulSoup(result.read(), "html.parser")


brand = soup.select('div')
for div in brand:
    print(div.text)