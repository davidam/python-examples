#!/usr/bin/python# -*- coding: utf-8 -*-
import mechanicalsoup, requests
from bs4 import BeautifulSoup



# Connect tog duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://www.duckduckgo.com")

# Fill-in the search form
browser.select_form('#search_form_homepage')
browser["q"] = "MechanicalSoup"
browser.submit_selected()

# Display the results
for link in browser.get_current_page().select('a.result__a'):
    print(link.text, '->', link.attrs['href'])

url =  'http://www.gnu.org'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

pages = []

for i in range(1, 6):
    url = 'https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
