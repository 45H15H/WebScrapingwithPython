from bs4 import BeautifulSoup
import requests

html = requests.get("https://store.dftba.com/collections/posters").text
html2 = requests.get("https://io.google/2022/products/").text

soup = BeautifulSoup(html, 'lxml')
soup2 = BeautifulSoup(html2, 'lxml')

title = soup.title.text
print(title)

items = soup.find_all('div', class_ = "grid-view-item")
print(len(items))

for i in items:
    itemName = i.find('div', class_ = "h4 grid-view-item__title")
    print(itemName.text)