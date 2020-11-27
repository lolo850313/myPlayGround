import xml.dom.minidom
# dom = xml.dom.minidom.parse('d:/TP700018A-05-51-00-02-810-802-TASK_002.xml')

# root = dom.documentElement
# root.nodeName
# root.nodeType
# root.childNodes
# root.getElementsByTagName('effect')
# for i in root.getElementsByTagName('effect'):
# 	print(i.nodeName)

# for i in root.getElementsByTagName('effect'):
# 	print(i.nodeValue)

# for i in root.getElementsByTagName('effect'):
# 	print(i.getAttribute("label"))

#创建一个dom对象some_tag
from xml.dom.minidom import getDOMImplementation
impl = getDOMImplementation()
newdoc = impl.createDocument(None, "some_tag", None)
top_element = newdoc.documentElement
text = newdoc.createTextNode('Some textual content.')
top_element.appendChild(text)