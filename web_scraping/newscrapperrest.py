
from bs4 import BeautifulSoup
import requests

html = requests.get('https://code.org/curriculum/csp/docs/hownottogethacked').text
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())

p = soup.div.h2.text
print(p)

# l = soup.find_all('div', class_ = 'container_responsive')
# for i in l:
#     print(i.prettify())
#     print()

hList = soup.div.find_all('h2')
pList = soup.div.find_all('p')

for i in hList:
    print(i.text)
'''
for j in pList:
    print(j.text)
'''

heading = soup.find('div', class_ = "container_responsive").h1.text
print(heading)

tabs = soup.find_all('div', id = 'headerlinks').a.text
print(tabs)