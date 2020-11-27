#序列化是使用tostring()将xml树转换为string，或ElementTree.write()将xml写出来。
from lxml import etree
root = etree.XML("<root><a><b/></a></root>")
print(etree.tostring(root))

#在开始增加<?xml version....>的标签
print(etree.tostring(root,xml_declaration=True))

print(etree.tostring(root,encoding="ASCII"))

#是输出格式化
print(etree.tostring(root,pretty_print=True))

#通过method关键字序列化输出html，即在开始和结尾增加<html></html>
root = etree.XML('<html><head/><body><p>Hello<br/>World</p></body></html>')

etree.tostring(root,method="xml") #与tostring(root)相同

etree.tostring(root,method="html")
print(etree.tostring(root,method="html",pretty_print=True))

print(etree.tostring(root,method="text"))

#序列化默认编码是ASCII
br = next(root.iter("br"))  #得到["Hello","World"]
br.tail = u'W\xf6rld'

print(etree.tostring(root,method="text",encoding="UTF-8"))
print(etree.tostring(root,method="text",encoding="unicode"))

print(etree.tostring(root,method="text"))  #因为编码不一致，此句无法执行
