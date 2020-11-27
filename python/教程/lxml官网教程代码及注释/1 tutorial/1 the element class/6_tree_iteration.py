#树的迭代
from lxml import etree
root = etree.Element("root")

#注意：将子元素的.text的值赋予“child 1”
etree.SubElement(root,"child").text = "Child 1"
etree.SubElement(root,"child").text = "Child 2"
etree.SubElement(root,"another").text= "Child 3"

print(etree.tostring(root,pretty_print=True))

#迭代遍历xml树
for element in root.iter():
    print("%s - %s" %(element.tag, element.text))

#对tag进行搜索后，迭代输出
for element in root.iter("child"):
    print("%s - %s" %(element.tag, element.text))

#iter方法中可以添加多个元素
for element in root.iter("another","child"):
    print("%s - %s" %(element.tag, element.text))

#iter也会输出注释和entity instances
root.append(etree.Entity("#234"))
root.append(etree.Comment("some comment"))

for element in root.iter():
    if isinstance(element.tag,str):
        print("%s - %s" %(element.tag, element.text))
    else:
        print("SPECIAL : %s - %s" % (element, element.text))

#给iter参数可得到不含entity和comments的迭代
for element in root.iter(tag=etree.Element):
    print("%s - %s" %(element.tag, element.text))

#给iter参数设为*，则得到所有的元素节点，这些元素节点可以作为xml树继续迭代。
for element in root.iter(tag="*"):
    print("%s - %s" %(element.tag, element.text))

