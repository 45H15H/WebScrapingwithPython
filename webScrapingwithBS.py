

from tkinter.ttk import Style
from bs4 import BeautifulSoup

import requests

html = requests.get('https://www.worldometers.info/coronavirus/')

print(html) # <- this will print if the request is done succesfully 
# 200 is successful

# to get text add .text at the end
html_text = requests.get('https://www.worldometers.info/coronavirus/').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
#print(soup.prettify())

n = soup.find('div', class_='maincounter-number').text

print(n)


