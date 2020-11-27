# file = "D:\\测试\\enToZh\\DMC-ARJ21-A-11-21-01-02A-941A-A_002-00_ZH-CN.XML"
dirPath = "D:\\测试\\enToZh\\"
import os
from lxml import etree
parser=etree.XMLParser(resolve_entities = False)
newFile = "merge.XML"
fileArr = os.listdir(dirPath)
newRoot = etree.Element("root")
for file in fileArr:
    tree = etree.parse(dirPath + file)
    root = tree.getroot()
    newRoot.append(root)

etree.ElementTree(newRoot).write(dirPath+newFile,xml_declaration=True,pretty_print=True,encoding="utf-8")

# f = open(file,"r",encoding="utf-8")
# content = f.readlines()
# newf = open("D:\\测试\\enToZh\\test.xml","w",encoding="utf-8")
# for i in (content):
#     if "<dmodule" in (i):
#         print(i)