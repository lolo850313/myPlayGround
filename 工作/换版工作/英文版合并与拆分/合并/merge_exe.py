#将s1000d的xml文件按章节合并
from lxml import etree
import os

dirPath = os.path.dirname(os.path.abspath(__file__)) + "\\"
inputTxt = dirPath + "input.txt"
f = open(inputTxt,"r",encoding="utf-8")
xmlPath = f.read()

parser = etree.XMLParser(resolve_entities=False)
fileArr = os.listdir(xmlPath)
pre = None
newRoot = None
fileDic = {}
for file in fileArr:
    if file[:11] == "DMC-ARJ21-A" and file[-3:].upper() == "XML":
        chap = file[12:14]
        if chap not in fileDic:
            fileDic[chap] =[file]
        else:
            fileDic[chap].append(file)

for chap in fileDic:
    newFile = chap + ".XML"
    newRoot = etree.Element("chap")
    for file in fileDic[chap]:
        tree = etree.parse(xmlPath + "\\" + file)
        root = tree.getroot()
        newRoot.append(root)
    etree.ElementTree(newRoot).write(xmlPath + "\\" + newFile, xml_declaration=True,pretty_print=True,encoding="utf-8")
            
input("program finished! Press <enter>")
