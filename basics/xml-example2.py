import xml.etree.ElementTree as ET

# Parse an XML file
tree = ET.parse('products.xml')
root = tree.getroot()

print(f"Root element: {root.tag}")
