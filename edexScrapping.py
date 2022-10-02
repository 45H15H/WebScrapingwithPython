
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.edx.org/').text

soup = BeautifulSoup(html, 'lxml')

print("\n")
inspire = soup.find('div', class_ = 'edx-vision border mt-4 text-white').p.text
print(inspire)
print("\n")


category = ['Computer Science', 'Languages', 'Data Science', 'Business Management', 'Engineering', 'Humanities']
links = soup.find_all('div', class_ = 'mb-4')
print(len(links))
for k, i in enumerate(links):
    if k < 6:
        print(category[k])
    langs = i.find_all('div', class_ = 'topic-link mb-3')
    print()
    for j in langs:
        print(j.a.text)
        

