
import requests
from lxml import html
from pprint import pprint
import os,re

start_url = 'http://www.davidam.com'
response = requests.get(start_url)
tree = html.fromstring(response.text)
links = tree.cssselect('a')  # or tree.xpath('//a')

out = []
for link in links:
    # we use this if just in case some <a> tags lack an href attribute
    if 'href' in link.attrib:
        out.append(link.attrib['href'])

absoluteurls = []
for o in out:
    if 'http' in o:
        print(o)
        absoluteurls.append(o)
    else:
        o = start_url + '/' + o
        print(o)
        absoluteurls.append(o)

buggyurls = []
for l in absoluteurls:
    print(l)
    try:
        r = requests.get(l)
        r.raise_for_status()
        print(r.status_code)
    except:
        buggyurls.append(l)
        print("Error")

print("Urls with troubles:")
print(buggyurls)
