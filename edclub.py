
import re
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.edclub.com/sportal/catalog.html").text
soup = BeautifulSoup(html, 'lxml')

# next sibling method
d = soup.find_all('div', attrs={'class': 'ed-paper', 'id': 'article'})
print(len(d))
# d1 = d.find('div', attrs={'class': 'row'})
# print(d1.text)
