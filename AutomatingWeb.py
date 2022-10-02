'''
from bs4 import BeautifulSoup
import webbrowser
webbrowser.open('')
import requests
res = requests.get("")
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
'''

from bs4 import BeautifulSoup
import requests

html = requests.get("https://typer.io/").text
soup = BeautifulSoup(html, 'lxml')

d = soup.find_all('div', attrs={'class': 'Hiscores_wrapper__0_j3j'})

for _ in d:
    itemName = _.find('div', class_ = "Hiscores_content__gHWzg")
    print(itemName.text)


'''
for _ in range(1, 9):
    d1 = d[_].find_all('div', attrs={'class': 'o-grid__col u-mb-x4 u-6/12@sm u-3/12@lg'})
    for i in d1:
        j = i.find('span', attrs={'class': 'c-product-card__heading c-card__heading'})
        print(j.text)
    print("\n")
'''
