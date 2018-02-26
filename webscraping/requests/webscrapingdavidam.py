from lxml import html
import requests
from pprint import pprint

page = requests.get('http://www.davidam.com/index.html')
tree = html.fromstring(page.content)

#This will create a list of prices
titles = tree.xpath('//div[@class="box-title"]/text()')
pprint(titles)

hrefs = tree.xpath('//a//@href')
pprint(hrefs)

footer = tree.xpath('//div[@class="action-list"]//p/text()')
pprint(footer)

