import requests
from lxml import html
from pprint import pprint

start_url = 'http://www.davidam.com'
response = requests.get(start_url)
tree = html.fromstring(response.text)
links = tree.cssselect('a')  # or tree.xpath('//a')

out = []
for link in links:
    # we use this if just in case some <a> tags lack an href attribute
    if 'href' in link.attrib:
        out.append(link.attrib['href'])

pprint(out)
