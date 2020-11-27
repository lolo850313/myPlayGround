def ddnCreat(xml_dir,date,ddnCode_para):
	from lxml import etree
	from headCreat import headxml
	from ddnContentCreat import ddnContent
	#写xml头
	root = etree.XML('<ddn xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/ddn.xsd"></ddn>')
	# #生成ident的xml树
	head = headxml(date,ddnCode_para)

	root.append(head)
	print(xml_dir)
	Content = ddnContent(xml_dir)

	root.append(Content)

	#输出ddn文档
	fileName = "DDN-" + ddnCode_para["modelIdentCode"] + "-" +  ddnCode_para["receiverIdent"] + "-" + ddnCode_para["senderIdent"] + "-" + ddnCode_para["yearOfDataIssue"] + "-" + ddnCode_para["seqNumber"] + ".XML"
	etree.ElementTree(root).write(xml_dir + "/" + fileName,pretty_print=True,encoding="utf-8",xml_declaration=True)

import os

dirPath = os.path.dirname(os.path.abspath(__file__)) + "\\"
inputTxt = dirPath + "input.txt"
f = open(inputTxt,"r",encoding="utf-8")
xmlPath = f.readlines()

path = xmlPath[0][:-1]
date = {}
date["year"] = xmlPath[1][:4]
date["month"] = xmlPath[1][5:7]
date["day"] = xmlPath[1][8:10]

ddnCode_para = {}
ddnCode_para["modelIdentCode"] = xmlPath[2][:5]
ddnCode_para["receiverIdent"] = xmlPath[2][6:11]
ddnCode_para["senderIdent"] = xmlPath[2][12:17]
ddnCode_para["seqNumber"] = xmlPath[2][-5:]
ddnCode_para["yearOfDataIssue"] = date["year"]

ddnCreat(path, date,ddnCode_para)

input("program finished! Press <enter>")