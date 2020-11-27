#将s1000d的xml文件按章节合并
from lxml import etree
import os

# dirPath = "D:\\程序源数据\\手册\\201912\\dmrl\\ndt\\"
# dirPath = "D:\\程序源数据\\手册\\201912\\dmrl\\fim\\"
# dirPath = "D:\\程序源数据\\手册\\201912\\dmrl\\ssm\\"
dirPath = "D:\\临时文件\\DDN-ARJ21-07482-SVV19-2020-00034(1)\\"

parser = etree.XMLParser(resolve_entities=False)
fileArr = os.listdir(dirPath)
pre = None
newRoot = None
fileDic = {}
for file in fileArr:
    if file[:11] == "DMC-ARJ21-A":
        chap = file[12:14]
        if chap not in fileDic:
            fileDic[chap] =[file]
        else:
            fileDic[chap].append(file)

for chap in fileDic:
    newFile = chap + ".XML"
    newRoot = etree.Element("chap")
    for file in fileDic[chap]:
        tree = etree.parse(dirPath + file)
        root = tree.getroot()
        newRoot.append(root)
    etree.ElementTree(newRoot).write(dirPath + newFile, xml_declaration=True,pretty_print=True,encoding="utf-8")
            