from lxml import etree
parser = etree.XMLPullParser()
events = parser.read_events()

parser.feed('<root><element key="value">text</element>')
parser.feed('<element><child /></element>')
for action, elem in events:
    print('%s: %d' % (elem.tag, len(elem)))  # processing
    elem.clear()                             # delete children

parser.feed('<empty-element xmlns="http://testns/" /></root>')
for action, elem in events:
    print('%s: %d' % (elem.tag, len(elem)))  # processing
    elem.clear()                             # delete children


root = parser.close()
etree.tostring(root)
