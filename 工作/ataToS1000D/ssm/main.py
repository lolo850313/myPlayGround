# issueDate没有自动生成
from mainFrame import frame
from lxml import etree
from head import findDmCode,headxml,find_taskNum
import re
from graphic import graphicAdd
from entityAdd import entityStr
from effect import effect_insert_content,effect_to_dic
import os

##总路径
dirPath = "D:\\测试\\s1000d\\s1000d_ssm\\"

##手册xml存放路径
filePath = dirPath + "ssm\\"
#ICN对应关系表
ICNpath = dirPath +"SSM 9月ICN-确认后.xlsx"
#dmrl对应关系表
dmrl_excel = dirPath + "SSM-TP700029-$new$-amm-dmrl.xlsx"

#版本，升版需要更改
issueNumber = "001"
issueDate = {"day":"25","month":"06","year":"2019"}
#dmrl中task No.所在的列
location = 1
#初始化content_element，初始化参数start在后面循环生成content时会被覆盖掉

for xmlPath in os.listdir(filePath):
#将arj_sect_list手册元素化
	teman_arj = etree.parse(filePath + xmlPath)
	arj_subject_list = teman_arj.xpath("//subject")

	for subject in arj_subject_list:
		#获得dmrl号
		taskNum = find_taskNum(subject)
		#dmrl中task No.所在的列
		location = 1
		dmCode_para = findDmCode(dmrl_excel,location,taskNum)
		if(dmCode_para ==None):
			print(taskNum + " 未生产相应的dmCode_para @main ")
		print(taskNum)
		dmrl =  dmCode_para["modelIdentCode"] + "-" + dmCode_para["systemDiffCode"] + "-" + dmCode_para["systemCode"] + "-"+ dmCode_para["subSystemCode"] +  dmCode_para["subSubSystemCode"] + "-"+ dmCode_para["assyCode"] + "-"+ dmCode_para["disassyCode"] +  dmCode_para["disassyCodeVariant"] + "-"+ dmCode_para["infoCode"] + dmCode_para["infoCodeVariant"]  + "-"+dmCode_para["itemLocationCode"]
		
		# 生成effect字典
		effect_dic = effect_to_dic(subject)
		
		#获得有效性	
		if subject.find("effect") is not None:
			arj_subject_effect = subject.find("effect").attrib["label"]
		else:
			arj_subject_effect = "ALL"
			# 将章节有效性加入到有效性字典中
			if "ALL" not in effect_dic:
				tmpValue = "a"+str(len(effect_dic)+1).zfill(3)
				effect_dic["ALL"] = tmpValue
		# applicId = effect_dic[arj_subject_effect]

		#创建头xml
		head = headxml(subject,dmCode_para,issueNumber,issueDate,arj_subject_effect)

		content_xml = etree.Element("content")
		description_xml = etree.SubElement(content_xml,"description")
		foldout_xml = etree.SubElement(description_xml,"foldout")	
		figureAlts_xml = etree.SubElement(foldout_xml,"figureAlts")	
		for arj_graphic in subject.findall("graphic"):		
			figure_xml = etree.SubElement(figureAlts_xml,"figure")
			if arj_graphic.find("effect") != None:
				effect = arj_graphic.find("effect").attrib["label"]
				applicRef = effect_dic[effect]
				figure_xml.set("applicRefId",applicRef)
			key = arj_graphic.attrib["key"]
			figText = key.lower()
			figure_xml.set("id",figText)		
			title_xml = etree.SubElement(figure_xml,"title")
			title = arj_graphic.find("title").text
			title_xml.text = title
			for sheet in arj_graphic.findall("sheet"):			
				graphic_xml = etree.SubElement(figure_xml,"graphic")
				gnbr = sheet.attrib["gnbr"]
				infoEntityIdent = graphicAdd(ICNpath,gnbr)
				graphic_xml.set("infoEntityIdent",infoEntityIdent)
		#有效性
		effect_insert_content(subject,content_xml)

		#将description中entity信息提取出来，生产entityString
		entityString = entityStr(description_xml)
		# 	# #写xml头，并添加head部分和content部分
		# root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/descript.xsd"></dmodule>')
		root = etree.XML(entityString + '<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/descript.xsd"></dmodule>')	
		root.append(head)
		root.append(content_xml)		
			
		#输出大客文档
		etree.ElementTree(root).write(dirPath + "\\ssm_dmrl\\DMC-" + dmrl + '_'+issueNumber+'-00_ZH-CN.XML',xml_declaration=True,pretty_print=True,encoding="utf-8")
