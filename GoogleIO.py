
from bs4 import BeautifulSoup
import requests

html = requests.get("https://io.google/2022/program/").text
html2 = requests.get("https://io.google/2022/products/").text

soup = BeautifulSoup(html, 'lxml')
soup2 = BeautifulSoup(html2, 'lxml')

title = soup.find('div', class_ = 'program-hero__content').h1.text
print(title)

paragraph = soup.find('div', class_ = 'program-hero__content').p.text
print(paragraph)

time = soup.find('div', class_ = 'mb-4').p.text
print(time)

io = soup.find('div', class_ = 'mb-4').h3.text
print(io)

allPrograms = soup.find_all('div', class_ = 'mb-4')
print("This year we have {0} programs!".format(len(allPrograms)))
for i in range(len(allPrograms) - 1):
    print(allPrograms[i].h3.text)

allProductsDiv = soup2.find('div', class_ = 'page-wrapper grid grid-cols-2 mt-6 gap-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6')
allProducts = allProductsDiv.find_all('h2')
print("Number of products are {}".format(len(allProducts)))
for j in range(len(allProducts) - 1):
    print(allProducts[j].text)

head = soup.head.text
print(head)
