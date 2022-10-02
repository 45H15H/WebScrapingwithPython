
from bs4 import BeautifulSoup

import requests

html = requests.get('https://www.linkedin.com/in/45h15h/')

print(html) # <- this will print if the request is done succesfully 
# 200 is successful

# to get text add .text at the end
html_text = requests.get('https://www.linkedin.com/in/45h15h/').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
#print(soup.prettify())

n = soup.find('div', class_='display-flex align-items-center').text

print(n)

