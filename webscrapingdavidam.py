from lxml import html
import requests

page = requests.get('http://www.davidam.com/index.html')
tree = html.fromstring(page.content)

#This will create a list of prices
titles = tree.xpath('//div[@class="box-title"]/text()')

print 'Box titles: ', titles

