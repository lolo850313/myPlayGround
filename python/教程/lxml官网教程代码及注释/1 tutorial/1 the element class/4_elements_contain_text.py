from lxml import etree
root = etree.Element("root")
root.text = "TEXT"

print(root.text)

print(etree.tostring(root,pretty_print=True))

#当 <br/> 包围文本时
from lxml import etree
html = etree.Element("html")
body = etree.SubElement(html,"body")

body.text = "TEXT"
print(etree.tostring(html))

br = etree.SubElement(body,"br")
print(etree.tostring(html))

br.tail = "TAIL"
print(etree.tostring(html))

#注意tostring中with_tail参数的区别
print(etree.tostring(br))
print(etree.tostring(br,with_tail=False))

#tostring中method参数，将只提取文本信息
print(etree.tostring(html,method="text"))

