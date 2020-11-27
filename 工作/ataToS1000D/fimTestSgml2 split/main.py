# cautionRef未测试正确
#有些初步评估里没有label标签，有效性写入ALL+ 比如ARJ21-A-21-00-00-AAA-421A-A
# DMC-ARJ21-A-26-00-00-04A-421D-A_001-00_ZH-CN 中 欧姆符号Ω不能正常显示
# 29-12-00-810-829故障隔离程序不在topic/subtask下，而在pretopic下用item的层级来写，无法转换

# 有几个topic 生成几个isolationprocedureEndAlts
# 一些参引未转换：AMM 49-15-01-200-801
# DMC-ARJ21-A-49-10-00-09A-421A-A_001-00_ZH-CN中AMM TASK 49-10-00-860-801
# DMC-ARJ21-A-29-14-00-02A-421A-A_001-00_ZH-CN AMM TASK 29-14-00-720-801

#21-31-00-A1A中由于故障代码子l1item中，导致出错。此故障属于手册编写问题。
#2列的断路器未转换为CB
#73-21-00-AEA

from mainFrame import frame
from lxml import etree
from subtask import subtask_merge
from effect import effect_to_dic,effect_xml,faultcode
from head import headxml,findDmCode,find_dmc
from warningAndCaution import warningRefCreat,cautionRefCreat,cirList,warningsAndCautionsRef_insertTo_content
from possibleCause import possibleCause_creat, topicCauseCreat
from faultdescr import descr_creat
from pretopic import commonInfo_creat,cbpgCreat,stepEndCreat
from ref_replace import dmrlRef_modify
from note import topicNoteCreat,noteChange
from table import table_modify
from blank import blankTag
from cblist import cb
from xml_declaration_add import addxml
from strDelete import strDelete
import os
##总路径
dirPath = "D:\\测试\\s1000d\\s1000d_fim\\"
issueNumber = "003"
date = {"day":"20","month":"09","year":"2019"}
# 手册xml存放路径
# 手册xml存放路径
filePath = "D:\\测试\\s1000d\\s1000d_fim\\20191101-fim替换数据版-二室自行替换-20191111-V2\\"
resPath = "D:\\测试\\s1000d\\s1000d_fim\\split_To\\"

# dmrl转换规则存放路径，从fimDMRL获得
dmrl_excel = dirPath + "ARJFRMFIM-TP700018A-DMRL-2019.9-汇总-20191105.xlsx"

# 警告库，从warningXML获得
warning_xml = dirPath + "ARJ21-A-00-00-00-01A-012A-A.xml"
# 警戒库，从cautionXML获得
caution_xml = dirPath + "ARJ21-A-00-00-00-02A-012A-A.xml"
# #amm的dmrl表格，从xxx获得
amm_dmrlTable = dirPath + "副本AMM-TP700004-02-$new$-amm-dmrl20191105.xlsx"

# 初始化content_element，初始化参数start在后面循环生成content时会被覆盖掉
content_element = frame("start")

for xmlPath in os.listdir(filePath):
	# 将fim手册元素化
	fim_arj = etree.parse(filePath + xmlPath)
	arj_task_list = fim_arj.xpath("//task")
	for arj_task in arj_task_list:
		# 获得当前task的taskNum值,通过taskNum在dmrlTable中找到对应的dmrl号
		dmrl = find_dmc(arj_task,dmrl_excel)
		# 获得当前task的faultcode，有些没有faultcode则填入默认值。
		faultcodeARJ = faultcode(arj_task)

		# 初始化默认content框架
		content_element = frame(faultcodeARJ)

		# 添加warning，caution至content中
		warningsAndCautionsRef_insertTo_content(arj_task,caution_xml,warning_xml,content_element)

		# topic下的note转换成notepara
		topicNoteCreat(arj_task,content_element)

		# 生成effect字典
		taskEffect = arj_task.find(".//effect").attrib["label"]
		effect_dic = effect_to_dic(arj_task,taskEffect)		
		# taskEffectId = effect_dic[taskEffect]

		# 将有效性参引写入content中
		if len(effect_dic) != 0:       
			referencedApplicGroupRef = effect_xml(effect_dic,taskEffect)
			content_element.insert(0,referencedApplicGroupRef)	

		# 在content中找到故障隔离主程序的位置
		isolationMainProcedure = content_element.xpath(".//isolationMainProcedure")[0]

		# 将topic中title非相关断路器的分为一类
		arj_topic_list = arj_task.xpath("topic")
		arj_pretopic_list = arj_task.xpath(".//pretopic")
		arj_subtask_list = []

		#生成相关断路器列表
		CBList = cb(arj_topic_list)
		for i in cb(arj_pretopic_list):
			CBList.append(i)


		arj_topicCause = []
		for topic in arj_topic_list:
			if "原因" in (topic.find("title").text):
				arj_topicCause.append(topic)

		for topic in arj_topic_list:
			if (topic.find("title").text)!="相关断路器" and (topic.find("title").text)!="初步评估" and (topic.find("title").text) !="故障修复确认" and (topic.find("title").text) !="修理确认" and "原因" not in (topic.find("title").text):
				arj_subtask_list.append(topic)		

		ie = 1
		for topicNotCB in arj_subtask_list:		
			# 有些subtask没有"list1/l1item/para"，则使用"topic/title"作为isolationProcedureEnd_title
			if topicNotCB.find("title") != None:
				arj_topicTitle = topicNotCB.xpath("title")[0].text
				# 根据subtask的数量，循环添加进故障隔离主程序中
			arj_subtaskNotCB_list = topicNotCB.findall("subtask")
			for i in range(len(arj_subtaskNotCB_list)):
				isolationProcedureEndAlts_XML = etree.SubElement(isolationMainProcedure,"isolationProcedureEndAlts")
				isolationProcedureEndAlts_XML.set("id", "iealts0" + str(ie))
				# 生成id流水号
				id_para = "ie0" + str(ie)


				# 生成对应的subtask的xml树
				subtask_XML = subtask_merge(arj_subtaskNotCB_list[i],effect_dic,id_para,arj_topicTitle,dmrl,taskEffect)
				# 将subtask的xml树依次添加进isolationMainProcedure下
				isolationProcedureEndAlts_XML.insert(i,subtask_XML)
				ie = ie + 1

		#生成可能的原因
		possibleCause_creat(arj_task,content_element)
		if len(arj_topicCause) == 1:
			topicCauseCreat(arj_topicCause[0],effect_dic,taskEffect,content_element)

		# commonInfo，遍历老树，生成新树。
		commonInfo_creat(arj_task,content_element)

		#初步评估
		# 遍历老树，生成新树。
		cbpg = cbpgCreat(arj_task,content_element,effect_dic,taskEffect)
		if cbpg != None:
			isolationMainProcedure.insert(0,cbpg)

		stepEndList = []
		for topic in arj_topic_list:
			if (topic.find("title").text) =="故障修复确认" or (topic.find("title").text) =="修理确认":
				stepEndList.append(topic)
		for topicEnd in stepEndList:
			topicEnd_xml = stepEndCreat(topicEnd,effect_dic,taskEffect,ie)
			isolationMainProcedure.append(topicEnd_xml)			

		# 生成ident的xml树
		head = headxml(arj_task,dmrl_excel,taskEffect,issueNumber,date)

		# 故障描述（由title前半部分转化）,也是head中的techName，
		descr_creat(head,arj_task,content_element)

		# 写xml头，并添加head部分和content部分
		root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/fault.xsd"></dmodule>')
		root.append(head)
		root.append(content_element)

		for i in root.xpath(".//para"):
			if i.text != None:
				if  "相关断路器中所有断路器" in i.text:
					for cbi in CBList:                   
						replaceXml = etree.Element("circuitBreakerRef")
						replaceXml.set("circuitBreakerNumber", cbi)
						#i为para元素
						i.append(replaceXml)
		for i in root.xpath(".//action"):
			if i.text != None:
				if  "相关断路器中所有断路器" in i.text:
					for cbi in CBList:                   
						replaceXml = etree.Element("circuitBreakerRef")
						replaceXml.set("circuitBreakerNumber", cbi)
						#i为para元素
						i.append(replaceXml)
		etree.ElementTree(root).write(resPath + '/DMC-' + dmrl + '_'+issueNumber+'-00_ZH-CN.XML',xml_declaration=True,pretty_print=True,encoding="utf-8")


# 替换手册中出现的amm，fim任务参引
print("dmrlRef_modify")
dmrlRef_modify(resPath)

#修改断路器，表格
print("table_modify")
cbExcel = "ARJ断路器清单梳理-2019年9月版-1108.xlsx"
table_modify(resPath,cbExcel)

#将多余的标签删除,将缺少的标签补齐
print("blankTag")
blankTag(resPath)

#新增xml文件的<?xml version='1.0' encoding='UTF-8'?>
print("addxml")
addxml(resPath)

#删除多余任务字样
strDelete(resPath)