
# for navigating through the HTML tree
# xpath = '/html/body/div[2]'
# [] are used to select the sibling of the parent tag
# here body/div[2] means to select the second div tag of the body tag.
# counting for [] starts from 1, not 0.
# if the element contains more than 1 child, and you don't specify the index,
# it will select the first child.

# xpath = '//table' 
# // means to select all tags (table tag) that are descendants of the root tag.
# xpath = '/html/body/div[2]//table'
# means to select all tag (table tag) that are descendants of the second
# div tag that is a descendant of the body tag.

# we can also select elements by their attributes
# xpath = '//table[@id="myTable"]'
# other attributes are:
# @class
# @id
# @href
# @style
# @width
# @height
# @border
# @cellpadding
# @cellspacing
# @bgcolor
# @align
# @valign
# .
# .
# .


# the * wildcard means to select all tags that are descendants of the root tag.
# xpath = '/html/body/*' <-- this will select all tags that are descendants of the body tag.
# this is select one generation below of the body tag.
# xpath = '/html/body//*' <-- this will select all tags that are descendants of the body tag.
# xpath = '//*[@id="uid"]' <-- this will select all tags with the id attribute of uid.

# xpath contains functions to select elements by their attributes
# xpath = '//*[contains(@id, "uid")]' <-- is same as above but with contains function
# the only difference is that the contains function will even catch the substrings
# class="class-1" class="class-12" class="class-1 class-2" all will be selected by this xpath

# to select link of website: <a href="datacamp.com">DataCamp</a>
# use: '//a/@href'


from scrapy import Selector
import scrapy


html = '''
<html>
  <head>
    <title>Href Attribute Example</title>
  </head>
  <body>
    <h1>Href Attribute Example</h1>
    <p>
      <a href="https://www.freecodecamp.org/">freeCodeCamp</a> shows you how and where you can contribute to freeCodeCamp's community and growth.
    </p>
  </body>
</html>
'''

# Selector and SelectorList objects allow for chaining of xpath queries.
#sel.xpath('/html/body/div[2]')
#sel.xpath('/html').xpath('./body/div[2]')
# both are same

sel = Selector(text=html) # <-- creating sel object, text is argument

divs = sel.xpath('/html/body') # <-- create a selector list of all div tags

import requests
# for getting the html of a website
url = 'https://www.linkedin.com/in/45h15h/'
html2 = requests.get(url).content
sel2 = Selector(text=html2)

print(len(sel2.xpath('//*'))) # <-- print the number of tags in the website

# CSS locators
# css selector is a way to select elements in HTML documents.

# / is replaced by > (excpet for the first one)
# xpath: /html/body/div
# CSS Locator: html > body > div

# // is replaced by a blank space (except for the first one)
# xpath: //div/span//p
# CSS Locator: div > span p

# [N] is replaced by :nth-of-type(N)
# xpath: /html/body/div[2]
# CSS Locator: html > body > div:nth-of-type(2)

# to select attributes in css locator:
# use . notation for class only
# p.class-1 will select all the p tags with class-1 (no need to use "" for class)
# use # notation for id only
# p#id-1 will select all the p tags with id = id-1 (no need to use "" for id)

# css_locator = '.class-1' will select all the elements with class class-1
# css_locator = '#id-1 > *' will select all the elements with id id-1 and all its children

# to select dispalyed text on the website
# using xpath: <xpath-to-element>/@attr-name
# ex: xpath = '//div[@id="uid"]/a/@href'

# using CSS Locator: <css-to-element>::attr(attr-name)
# ex: css_locator = 'div#uid > a::attr(href)'

html3 = '''
<p id="p-example">
  Hello world!
  Try <a href="http://www.datacamp.com">DataCamp</a> for free!
</p>
'''
# in xpath using text() method to extract
sel3 = Selector(text=html3)
print(sel3.xpath('//p[@id="p-example"]/text()').extract()) # this will not go in the descendants
# to go into descendants, use .
print(sel3.xpath('//p[@id="p-example"]//text()').extract()) # notice // with text()

# same thing with css locator
print(sel3.css('p#p-example::text').extract())
# to get text from future generation also
print(sel3.css('p#p-example ::text').extract()) # notice the space before ::


linkein = 'https://www.linkedin.com/in/45h15h/'

linkhtml = requests.get(linkein).content

linksel = Selector(text=linkhtml)

linkxpath = '//*[@id="ember275"]/div[3]/ul/li[2]/div/div[2]/div/a/div/span/span[1]/text()'
print(linksel.xpath(linkxpath).extract())

# responce object
# response object is a wrapper around the response object
# response keeps track of the URL within the responce url variable
# we can follow the links in the responce object
# ex: response.follow(next_url)

htmlcourse = requests.get('https://www.datacamp.com/courses/all').content

selcourse = Selector(text=htmlcourse)
print(len(sel2.css('div.mfe-app-learn-hub-a0ry07'))) 

first_div = selcourse.css('div.mfe-app-learn-hub-a0ry07')[0]
children = first_div.xpath('./*')
print(len(children))

from scrapy.crawler import CrawlerProcess

class SpiderClassName(scrapy.Spider):
    name = 'spider_name'

    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
      
    def parse(self, response,):
        html_file = 'DC_courses.html'
        with open(html_file, 'wb') as f:
            f.write(response.body)
        