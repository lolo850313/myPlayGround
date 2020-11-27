def commonInfo_creat(arj_task,content_element):
	import re
	from lxml import etree
	#commonInfo，遍历老树，生成新树。
	arj_pretopic_commonInfo = ""
	for i in arj_task.findall(".//pretopic"):
		if (i.find("title").text)=="概述":
			arj_pretopic_commonInfo = i
	
	#如果没找到概述部分则直接return
	if arj_pretopic_commonInfo == "":
		return

	#遍历老树，生成新树
	arj_pretopic_l1item = arj_pretopic_commonInfo.xpath(".//l1item")

	#将概述下不含故障代码的liitem放入l1item_list中
	re_faultCode = r'[0-9]{3}\s[0-9]{3}\s[0-9]{2}'
	l1item_list = []	
	for i in (arj_pretopic_l1item):
		if re.findall(re_faultCode,i[0].text) == []:
			l1item_list.append(i)

	#找到conten中commonInfo的位置
	ata_commonInfo = content_element.find("faultIsolation/commonInfo")
	#以word文档为准的树形结构 commonInfo/para/commonInfoDescrPara/para/commonInfoDescrPara/para
	for level1 in l1item_list:
		para_0 = etree.SubElement(ata_commonInfo,"para")
		para_0.text = level1[0].text
		if level1.findall(".//l2item") != None:
			for level2 in level1.findall(".//l2item"):
				commonInfoDescrPara_1 = etree.SubElement(ata_commonInfo,"commonInfoDescrPara")
				para_1 = etree.SubElement(commonInfoDescrPara_1,"para")
				para_1.text = level2[0].text
				if level2.findall(".//l3item") != None:
					for level3 in level2.findall(".//l3item"):
						para_2 = etree.SubElement(commonInfoDescrPara_1,"para")
						para_2.text = level3[0].text
						if level3.findall(".//l4item") != None:
							for level4 in level2.findall(".//l4item"):
								commonInfoDescrPara_2 = etree.SubElement(commonInfoDescrPara_1,"commonInfoDescrPara")
								para_3 = etree.SubElement(commonInfoDescrPara_2,"para")
								para_3.text = level4[0].text
								print("pretopic has level4")

#初步评估,可由topic或pretopic中解析出,warning和caution，note
#commonInfo，遍历老树，生成新树。
def cbpgCreat(arj_task,content_element,effect_dic):
	from lxml import etree
	id = "cbpg"
	#初步评估可能在pretopic中也有可能在topic中
	arj_pretopic_cbpg = ""
	for i in arj_task.findall(".//pretopic"):
		if (i.find("title").text)=="初步评估" or (i.find("title").text)=="初始评估":
			arj_pretopic_cbpg = i

	for i in arj_task.findall(".//topic"):
		if (i.find("title").text)=="初步评估":
			arj_pretopic_cbpg = i
	
	#如果没找到概述部分则直接return
	if arj_pretopic_cbpg == "":
		return	

	isolationProcedureEndAlts_XML = etree.Element("isolationProcedureEndAlts") 
	isolationProcedureEnd_XML = etree.SubElement(isolationProcedureEndAlts_XML,"isolationProcedureEnd")    
	isolationProcedureEnd_XML.set("id",id)
	#如果是topic下的初步评估则需要添加有效性标签。
	if (arj_pretopic_cbpg.tag) == "topic":
		cbpg_effect = arj_pretopic_cbpg.xpath(".//effect")[0].attrib["label"]
		applicRefId = effect_dic[cbpg_effect]
		isolationProcedureEnd_XML.set("applicRefId",applicRefId)

	#title值
	title = etree.SubElement(isolationProcedureEnd_XML,"title")
	title.text = "初步评估"

	#l1item转化为action
	l1item_list = arj_pretopic_cbpg.xpath(".//l1item")

	# #生成action，randomlist，	
	#根据arj中的生成多个listItem
	for l1item in l1item_list:
		#l1item下的节点为list2，para，note，table等		
		for subl1item in l1item:
			#有些情况 note会在para前出现，所以暂时先生成action_XML，以便note能添加到action_XML下。			
			action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')			
			if subl1item.tag == "para":
				if len(subl1item.text.strip())>0:				
					action_XML.text = subl1item.text
					tmp = action_XML
				else:
					print("pretopic l1item get refex")
					action_XML.tag = "xxx"
			#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
			elif subl1item.tag == "note":
				noteText = subl1item.xpath("string()").strip()
				note_XML = etree.SubElement(action_XML, 'note')
				notePara_XML = etree.SubElement(note_XML, 'notePara')
				notePara_XML.text = noteText
			elif subl1item.tag == "table":                  
				isolationProcedureEnd_XML.append(subl1item)
			#循环遍历时，如果subl1item时list2，则直接生成action的子元素
			elif subl1item.tag == "list2":
				randomList_XML = etree.SubElement(action_XML, 'randomList')
				l2item_list = subl1item.xpath("l2item")
				#对此subl1item下的元素l2item进行提取
				for l2item in l2item_list:
					for subl2item in l2item:
						if subl2item.tag == "para":
							listItem_XML = etree.SubElement(randomList_XML, 'listItem')
							para_XML = etree.SubElement(listItem_XML, 'para')
							para_XML.text = subl2item.text
						#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
						elif subl2item.tag == "note":
							noteText = subl2item.xpath("string()").strip()
							note_XML = etree.SubElement(listItem_XML, 'note')
							notePara_XML = etree.SubElement(note_XML, 'notePara')
							notePara_XML.text = noteText
						elif subl2item.tag == "table":						                        
							isolationProcedureEnd_XML.append(subl2item)
						#循环遍历时，如果subl1item时list2，则直接生成action的子元素
						elif subl2item.tag == "list3":
							sequentialList_XML = etree.SubElement(para_XML, 'sequentialList')
							l3listItem_XML = etree.SubElement(sequentialList_XML, 'listItem')
							l3item_list = subl1item.xpath("l3item")
							#对此subl1item下的元素l2item进行提取
							for l3item in l3item_list:
								for subl3item in l3item:
									if subl3item.tag == "para":
										para_XML = etree.SubElement(l3listItem_XML, 'para')
										para_XML.text = subl3item.text
									#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
									elif subl3item.tag == "note":
										noteText = subl3item.xpath("string()").strip()
										note_XML = etree.SubElement(l3listItem_XML, 'note')
										notePara_XML = etree.SubElement(note_XML, 'notePara')
										notePara_XML.text = noteText
									elif subl3item.tag == "table":										                        
										isolationProcedureEnd_XML.append(subl3item)
									#循环遍历时，如果subl1item时list2，则直接生成action的子元素
									elif subl3item.tag == "list4":
										print(" get list4 pretopic")										
				
	return isolationProcedureEndAlts_XML