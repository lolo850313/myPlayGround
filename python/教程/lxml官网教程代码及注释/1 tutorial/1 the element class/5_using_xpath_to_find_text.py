from lxml import etree
html = etree.Element("html")
body = etree.SubElement(html,"body")

body.text = "TEXT"
br = etree.SubElement(body,"br")
br.tail = "TAIL"

#使用xpath提取文本信息
print(html.xpath("string()"))
print(html.xpath("//text()"))

#可将xpath包装成函数以便频繁使用
build_text_list = etree.XPath("//text()")
print(build_text_list(html))

#xpath搜索text()得到的字符串是一个跟原xml树有关系的对象，可以通过getparent方法来得到字符串的父节点
texts = build_text_list(html)
print(texts[0])

parent = texts[0].getparent()
print(parent.tag)

print(texts[1])
print(texts[1].getparent().tag)

#xpath搜索string()得到的字符串不能使用getparent方法得到其父节点
stringify = etree.XPath("string()")
print(stringify(html))
print(stringify(html).getparent())