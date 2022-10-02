
# first install beautifulsoup4:
# pip3 install beautifulsoup4

# then install parser:
# pip3 install lxml

from bs4 import BeautifulSoup

# using local file
with open('index.html', 'r') as htmlFile:
    content = htmlFile.read()
    #print(content)

    # now to pretify and able to work with the tags
    soup = BeautifulSoup(content, 'lxml')
    # pretify is used to make the html readable
    #print(soup.prettify())
    
    tags = soup.find('p') # <-- this will give only the first occurance of 
    # the p tag with its contents
    print(tags.prettify())

    tags_all = soup.find_all('p') # <-- this will give list with all the p tags
    print(tags_all)

    # to print only the text inside the tag
    for i in tags_all:
        print(i.text)

    div_tags = soup.find_all('div', class_='class-1') # <-- this will give list with all the div tags with class class-1
    # notice class_ is used instead of class




