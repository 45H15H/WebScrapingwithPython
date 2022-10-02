from bs4 import BeautifulSoup
import requests
import re

html = requests.get('https://hackspace.raspberrypi.com/issues').text

soup = BeautifulSoup(html, 'lxml')

division = soup.find('div', class_='o-grid o-grid--equal')

issues = division.find_all('h2')
dates = division.find_all('time')
for i, j in zip(issues, dates):
    #if re.match(re.compile(r'^Issue'), i.text):
    # print(i.text)
    # print(j.text)
    print("{1}\n{2}".format(i.text, j.text))