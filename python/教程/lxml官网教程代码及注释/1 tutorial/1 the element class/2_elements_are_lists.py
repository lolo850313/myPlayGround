from lxml import etree
root   = etree.Element("root")
root.append(etree.Element("child1"))
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

#子元素类似于list
child = root[0]

#得到子元素的tag值
print(child.tag)

#得到root的子元素个数
print(len(root))

root.index(root['1'])  # 得到1

children = list(root)

for child in root:
    print(child.tag)

#在root位置0处新增一个子元素child0
root.insert(0, etree.Element("child0"))

print(root[:1])
print(root[-1:])

#判断root是不是xml元素
print(etree.iselement(root))

#判断root有没有子节点
if len(root):
    print("root element has children")

for child in root:
    print(child.tag)
#以下操作并不能交换子节点位置，而只能将root[0]删除掉
root[0] = root[-1]

#遍历root下的子元素的tag
for child in root:
    print(child.tag)

#得到父节点，前一个节点，后一个节点
print(root[0].getparent())
print(root[1].getprevious())
print(root[0].getnext())

#使用深复制将root[1]复制到neu树中
from copy import deepcopy

element = etree.Element("neu")
element.append(deepcopy(root[1]))

print(element[0].tag)

print([c.tag for c in root])
