from lxml import etree

#通过工厂方式factory直接创建带有属性的xml元素
root = etree.Element("root", interesting="totally")
print(etree.tostring(root,pretty_print=True))

print(root.get("interesting"))

#使用set使root新增一个属性
root.set("hello","huhu")
print(root.get("hello"))
print(etree.tostring(root,pretty_print=True))

print(sorted(root.keys()))

#使用items方法得到子元素字典的键值对
for name,value in sorted(root.items()):
    print('%s =  %r' %(name,value))

#使用attrib 得到形式字典的属性集合
attributes = root.attrib

print(attributes["interesting"])

attributes["hello"] = "Guten tag"
print(attributes["hello"])

#修改属性字典后，xml树也随之改变
print(root.get("hello"))

#如果想要得到一个独立的属性复制字典，可以将他复制到一个新字典中
d = dict(root.attrib)
print(sorted(d.items()))