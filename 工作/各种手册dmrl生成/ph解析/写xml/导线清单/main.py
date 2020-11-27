#整个导线生成程序思路
#1.xml生成程序
#2.excel 不同有效性合并 （G20 G21 G22等）
#3.使用合并有效性后的excel生成xml


from lxml import etree
from content import contentxml
import os
from head import headxml
# path = "d:/wb103+/"
path = "/Users/Hewenhao/wb103+/"

#将文件夹中的xls文件录入excelfile列表中
excelFile = []
for i in os.listdir(path):
	if i[-3:] =="xls":
		excelFile.append(i) 

for i in excelFile:   
	filePath = path + i
	
	#写xml头
	root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/wrngdata.xsd"></dmodule>')
	#创建identAndStatusSection子树
	head = headxml(filePath)
	#创建content子树
	content = contentxml(filePath)
	root.append(head)
	root.append(content)

	#将完成的树写入文件中
	etree.ElementTree(root).write(filePath[:-3] + "xml",pretty_print=True,encoding="utf-8",xml_declaration=True)
	# # etree.ElementTree(content_xml).write(filePath[:-3] + "xml",pretty_print=True,encoding="utf-8")