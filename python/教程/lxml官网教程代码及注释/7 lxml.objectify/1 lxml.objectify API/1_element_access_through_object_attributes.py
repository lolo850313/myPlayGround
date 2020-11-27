from lxml import etree
from lxml import objectify

root = objectify.Element("root")
b = objectify.SubElement(root,"b")
print(root.b[0].tag)

b = objectify.SubElement(root,"b")
print(root.b[1].tag)

#可使用index找出子元素对应的序列号
print(root.index(root.b[1]))

x1 = objectify.SubElement(root,"x")
x2 = objectify.SubElement(root,"x")
x3 = objectify.SubElement(root,"x")

#注意此时xml是有命名空间的
print(etree.tostring(root))
#对tag可以进行迭代和切片操作
print([el.tag for el in root.x])

print([el.tag for el in root.x[-1:]])

del root.x[1:2]
print([el.tag for el in root.x])

#迭代所有子元素或者使用命名空间，则可用iterchilder()
print([el.tag for el in root.iterchildren()])

#iterchildren(tag="b")的参数后可类似于 root.b
print([el.tag for el in root.iterchildren(tag="b")])
print([el.tag for el in root.b])

#生成有属性的子元素,方法有2种
c = objectify.SubElement(root,"c",myattr="someval")
print(root.c.get("myattr"))

root.c.set("cAttr","oh-oh")
print(root.c.get("cAttr"))

#直接给xml添加一个子树为new_child节点，其值为el的子树
el = objectify.Element("yet_another_child")
root.new_child = el
print(root.new_child.tag)
print(el.tag)
print(etree.tostring(root))

#一次添加多个子树
root.y = [objectify.Element("y"),objectify.Element("y")]
print([el.tag for el in root.y])
print(etree.tostring(root))

#可通过列表的slice方法来操作子元素
root.y[:] = [objectify.Element("y")]
print([el.tag for el in root.y])
print(etree.tostring(root))

#可以用以下方法替换子元素,注意其中el，subel并不是tag，并没有在xml树中出现，他们只是一个子树，
#其中第1和第3个的el被添加进了child标签中，el子树的内容是<sub/>
child1 = objectify.SubElement(root,"child")
child2 = objectify.SubElement(root,"child")
child3 = objectify.SubElement(root,"child")

el = objectify.Element("new_child1")
subel = objectify.SubElement(el,"sub")

root.child = el
print(root.child.sub.tag)

root.child[2] = el
print(root.child.sub.tag)
print(etree.tostring(root))

#尤其注意改变元素的tag
print(root.b.tag)

root.b.tag = "notB"
#此时已不能用root.b.tag，而应该使用
print(root.notB.tag)