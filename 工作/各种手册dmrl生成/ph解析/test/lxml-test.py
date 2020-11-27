from lxml import etree
root   = etree.Element("root")
root.tag

root.append(etree.Element("child1"))
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

print(etree.tostring(root,pretty_print=True))

for child in root:
    print(child.tag)

root.insert(0, etree.Element("child0"))

print(root[:1])
print(root[-1:])

#判断root是不是元素
print(etree.iselement(root))

#判断root有没有子节点
if len(root):
    print("root element has children")

for child in root:
    print(child.tag)
#以下操作并不能交换子节点位置，而只能将root[0]删除掉
root[0] = root[-1]

for child in root:
    print(child.tag)

#得到父节点
print(root[0].getparent())
print(root[1].getprevious())
print(root[0].getnext())

#使用深复制将root[1]复制到neu树中
from copy import deepcopy

element = etree.Element("neu")
element.append(deepcopy(root[1]))

print(element[0].tag)

print([c.tag for c in root])

#通过工厂方式factory直接创建带有属性的xml元素
root = etree.Element("root", interesting="totally")
etree.tostring(root)
print(root.get("interesting"))

#使用set使root新增一个属性
root.set("hello","huhu")
print(root.get("hello"))

sorted(root.keys())

#使用attrib 得到形式字典的属性集合
attributes = root.attrib

print(attributes["interesting"])

attributes["hello"] = "Guten tag"
print(attributes["hello"])

#修改属性字典后，xml树也随之改变
print(root.get("hello"))