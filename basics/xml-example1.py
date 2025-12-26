import xml.etree.ElementTree as ET

xml_string = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
    </product>
</catalog>
"""

root = ET.fromstring(xml_string)
print(f"Root tag: {root.tag}")
print(f"Root attributes: {root.attrib}")
