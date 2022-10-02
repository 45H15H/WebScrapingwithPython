
from urllib.request import urlopen
from urllib.error import HTTPError # to handle errors in getting the page
from urllib.error import URLError # to handle errors

from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
# this line will get the page from the web which may hit error
except HTTPError as e:
    print(e)
# 404 Page Not FOund
# 500 Internal Server Error
except URLError as e:
    print("The server could not be found!")


bs = BeautifulSoup(html.read(), 'html.parser') # <- creating bs object
# html.read() gets the HTML content of the page.
# however without .read() will also work
# 'html.parser' is the parser, another parser is 'lxml' (first install it)
# another parser is 'html5lib'

print(bs.h1) # <- this will give only the first instance of h1 tag
print(bs.html.body.h1)
print(bs.html.h1)
print(bs.body.h1)
# all will give same result. because of tag tree

# if you pass a tag which doesn't exist it will return None

