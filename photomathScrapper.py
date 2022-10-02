
from bs4 import BeautifulSoup
import requests

html = requests.get('https://hackspace.raspberrypi.com/').text

soup = BeautifulSoup(html, 'lxml')

division = soup.find('div', class_='o-grid o-grid--equal-height')

articleList = division.find_all('article')

for i, j in enumerate(articleList):
    print("Case #{}: {}".format(i, j.find('p').text))
    print()


import re
soup2 = BeautifulSoup(html, 'lxml')
footer = soup2.find('footer', class_ = re.compile(r'c-footer'))
print(footer.text)

