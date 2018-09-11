import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('country_data.xml')
root = tree.getroot()
#root = ET.fromstring(countrydata)

# Top-level elements
print(root.findall("."))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
print(root.findall("./country/neighbor"))

# Nodes with name='Singapore' that have a 'year' child
print(root.findall(".//year/..[@name='Singapore']"))

# 'year' nodes that are children of nodes with name='Singapore'
print(root.findall(".//*[@name='Singapore']/year"))

# All 'neighbor' nodes that are the second child of their parent
print(root.findall(".//neighbor[2]"))

for country in root.findall('country'):
     name = country.get('name')
     print(name)

for elem in root.findall(".//*[@name='Singapore']/year"):
    pprint(elem)

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
for elem in tree.iter():
    print(elem)
