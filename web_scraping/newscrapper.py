
from bs4 import BeautifulSoup
import requests

with open('D:\WebScrapingwithPython\index.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

# print(soup.prettify()) # <- will print the html file in a readable format

t = soup.title.text # <- only grabbing the title content not the attributes
# . method gives only the first found element
print(t)

# to grab specific elements
# .find_all() method gives all the elements
p = soup.find_all('p')
# we can specify the element we want to grab by using the class name
# .find_all('div', class_='classname')
# .find_all('div', id='idname')
# if not specified it returns a list of all the elements
print(p)

footerline = soup.footer.p.text
print(footerline)

