from lxml import html
import requests

print("Introduce an url from webometrics, for example, https://www.webometrics.info/en/GoogleScholar/Spain")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="display the gender")
args = parser.parse_args()

page = requests.get(args.url)
tree = html.fromstring(page.content)

#This will create a list of buyers:
scientifics = tree.xpath('//tr/td/a/strong/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

print('Scientifics: %s' % scientifics)
#print('Prices: %s' % prices)
