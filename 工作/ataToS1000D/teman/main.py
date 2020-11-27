#表格中有4个表头内容没有放在thead中，导致tbody中第一行为表头，应手工删除。TEMAN22529，TEMAN22530，TEMAN28895，TEMAN25839
#TEMAN32673中的表的表头数据有误。
from mainFrame import frame
from lxml import etree
from head import headxml,findDmCode
import re
from graphic import graphicAdd
from entityAdd import entityStr
import os
##总路径
dirPath = "D:\\测试\\s1000d\\s1000d_teman\\"
filePath = dirPath + "teman\\"
##手册xml存放路径
dmrlPath = dirPath + "TEMAN-TP700031-$new$-amm-dmrl.xlsx"
#ICN对应关系表
ICNpath = dirPath +"ICN.xls"
res = dirPath + "teman_dmrl\\"
issueNumber = "001"
#初始化content_element，初始化参数start在后面循环生成content时会被覆盖掉

for i in os.listdir(filePath):
	#将arj_sect_list手册元素化
	teman_arj = etree.parse(filePath + i)
	for lsheet in teman_arj.xpath("/tlsheet"):
		taskNum = i[:6] + "_"+ i[7:-4]
		location = 1
		print(taskNum)
		dmCode_para = findDmCode(dmrlPath,location,taskNum)
		dmrl = dmCode_para["modelIdentCode"] + "-" + dmCode_para["systemDiffCode"] + "-" + dmCode_para["systemCode"] + "-" + dmCode_para["subSystemCode"] + dmCode_para["subSubSystemCode"] +"-" + dmCode_para["assyCode"] + "-" + dmCode_para["disassyCode"] + dmCode_para["disassyCodeVariant"] + "-" + dmCode_para["infoCode"]  + dmCode_para["infoCodeVariant"]+ "-" + dmCode_para["itemLocationCode"]	
		title = lsheet.find("title").text
		head = headxml(lsheet,dmCode_para,issueNumber)

		# content内容
		content_element = frame(lsheet,ICNpath)

		#entityString
		entityString = entityStr(content_element)
		# #写xml头，并添加head部分和content部分
		root = etree.XML(entityString + '<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/descript.xsd"></dmodule>')
		root.append(head)
		
		root.append(content_element)
			
		
		#输出大客文档
		etree.ElementTree(root).write(res + 'DMC-'+ dmrl + '_'+issueNumber+'-00_ZH-CN.XML',xml_declaration=True,pretty_print=True,encoding="utf-8")
