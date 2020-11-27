# lxml教程网址https://lxml.de/tutorial.html

from lxml import etree
#使用元素工厂方式创建元素
root   = etree.Element("root")

#得到元素的tag属性
print(root.tag)

#使用append在父节点新增下新增一个子节点
root.append(etree.Element("child1"))

#使用subelement工厂函数在父节点root下新增一个子节点
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

#使用tostring方法使xml序列化，可以pring序列化后xml树
print(etree.tostring(root,pretty_print=True))

