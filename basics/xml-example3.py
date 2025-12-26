import xml.etree.ElementTree as ET

xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <categories>
            <category>Electronics</category>
            <category>Accessories</category>
        </categories>
    </product>
    <product id="102">
        <name>USB Mouse</name>
        <categories>
            <category>Electronics</category>
        </categories>
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)

# Method 1: find() - returns the FIRST matching element
first_product = root.find('product')
print(f"First product ID: {first_product.get('id')}")

# Method 2: findall() - returns ALL direct children that match
all_products = root.findall('product')
print(f"Total products: {len(all_products)}")

# Method 3: iter() - recursively finds ALL matching elements
all_categories = root.iter('category')

category_list = []
for cat in all_categories:
    if cat.text not in category_list:
        category_list = category_list + [cat.text]
print("All categories:", category_list)


