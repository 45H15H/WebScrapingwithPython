
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.raspberrypi.com/products/").text
soup = BeautifulSoup(html, 'lxml')

d = soup.find_all('div', attrs={'class': 'o-grid o-grid--equal-height'})

for _ in range(1, 9):
    d1 = d[_].find_all('div', attrs={'class': 'o-grid__col u-mb-x4 u-6/12@sm u-3/12@lg'})
    for i in d1:
        j = i.find('span', attrs={'class': 'c-product-card__heading c-card__heading'})
        print(j.text)
    print("\n")

