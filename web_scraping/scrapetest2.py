
from urllib.request import urlopen
from urllib.error import HTTPError # to handle errors in getting the page
from urllib.error import URLError # to handle errors

from bs4 import BeautifulSoup

try:
    html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")


bs = BeautifulSoup(html.read(), 'html.parser')

# to get content by specified class
naemList = bs.findAll('span', {'class':'green'}) # notice the syntax for class
for i in naemList:
    print(i.get_text()) # <-- get_text will only give content withoud the tag enclosing it


# syntax of .find() and .find_all()
# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

# tag > takes a sting of tag or a list of stirng of tags
# .find_all(['h1','h2','h3','h4','h5','h6']) <-- will find all heading tags

# attributes > The attributes argument takes a Python dictionary of attributes 
# and matches tags that contain any one of those attributes.

# recursive > if set True it will even look in the future generations 
# if False it will only look at top-level tags

# text > it is like RegEx it finds the exact match in the HTML not the tag but the content

# limit > if set to 1 it will work as .find(). its like limit to how many more to search

# keyword > allows to select tags that contain a particular attribute or set of attributes
# title = bs.find_all(id='title', class_='text')
# notice class is either used as class_='green' or in {'class':'green'}


# to go deeper into tags with bs object
# bs.tag.subTag.anotherSumTag

# next_siblings() function is used to get the next siblings of the current tag
# previous_siblings() function is used to get the previous siblings of the current tag



