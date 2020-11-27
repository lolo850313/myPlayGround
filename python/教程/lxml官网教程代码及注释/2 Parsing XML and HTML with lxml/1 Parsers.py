from lxml import etree
xml = '<a xmlns="test"><b xmlns="test"/></a>'
root = etree.fromstring(xml)
print(etree.tostring(root))
# b'<a xmlns="test"><b xmlns="test"/></a>'