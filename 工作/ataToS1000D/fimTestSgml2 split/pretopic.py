def commonInfo_creat(arj_task,content_element):
	import re
	from lxml import etree
	#commonInfo，遍历老树，生成新树。
	arj_pretopic_commonInfo = ""
	for i in arj_task.findall(".//pretopic"):
		if "概述" in i.find("title").text:
			arj_pretopic_commonInfo = i
	
	#如果没找到概述部分则直接return
	if arj_pretopic_commonInfo == "":
		return

	#遍历老树，生成新树
	arj_pretopic_l1item = arj_pretopic_commonInfo.xpath(".//l1item")

	#将概述下不含故障代码的liitem放入l1item_list中
	# re_faultCode = r'[0-9]{3}\s[0-9]{3}\s[0-9]{2}'
	l1item_list = []	
	for i in (arj_pretopic_l1item):
		l1item_list.append(i)

	#找到conten中commonInfo的位置
	ata_commonInfo = content_element.find("faultIsolation/commonInfo")	
	#以word文档为准的树形结构 commonInfo/para/commonInfoDescrPara/para/commonInfoDescrPara/para
	for level1 in l1item_list:
		commonInfoDescrParaAlts = etree.SubElement(ata_commonInfo,"commonInfoDescrParaAlts")		
		commonInfoDescrPara_0 = etree.SubElement(commonInfoDescrParaAlts,"commonInfoDescrPara")
		para_0 = etree.SubElement(commonInfoDescrPara_0,"para")
		para_0.text = level1[0].text
		if level1.findall(".//l2item") != None:
			commonInfoDescrPara_1 = etree.SubElement(para_0,"sequentialList")			
			for level2 in level1.findall(".//l2item"):
				listItem_1 = etree.SubElement(commonInfoDescrPara_1,"listItem")				
				para_1 = etree.SubElement(listItem_1,"para")
				para_1.text = level2[0].text
				if level2.findall(".//l3item") != None:
					commonInfoDescrPara_2 = etree.SubElement(para_1,"sequentialList")
					for level3 in level2.findall(".//l3item"):
						listItem_2 = etree.SubElement(commonInfoDescrPara_2,"listItem")	
						para_2 = etree.SubElement(listItem_2,"para")
						para_2.text = level3[0].text
						if level3.findall(".//l4item") != None:
							for level4 in level2.findall(".//l4item"):
								commonInfoDescrPara_3 = etree.SubElement(para_2,"sequentialList")
								para_3 = etree.SubElement(commonInfoDescrPara_3,"para")
								para_3.text = level4[0].text
								print("message Lose : pretopic has level4")

#初步评估,可由topic或pretopic中解析出,warning和caution，note
#commonInfo，遍历老树，生成新树。
def cbpgCreat(arj_task,content_element,effect_dic,taskEffectId):
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
		cbpgAttrib = arj_pretopic_cbpg.xpath(".//effect")[0].attrib
		if "label" in cbpgAttrib:
			cbpg_effect = cbpgAttrib["label"]
			if cbpg_effect != taskEffectId:		
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
		#有些情况 note会在para前出现，所以暂时先生成action_XML，以便note能添加到action_XML下。			
		
		#l1item下的节点为list2，para，note，table等		
		for subl1item in l1item:
			# #有些情况 note会在para前出现，所以暂时先生成action_XML，以便note能添加到action_XML下。			
			# action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')			
			if subl1item.tag == "para":
				if len(subl1item.text.strip())>0:
					action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')				
					action_XML.text = subl1item.text
			#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
			elif subl1item.tag == "note":
				noteText = subl1item.xpath("string()").strip()
				note_XML = etree.SubElement(isolationProcedureEnd_XML, 'note')
				notePara_XML = etree.SubElement(note_XML, 'notePara')
				notePara_XML.text = noteText
			elif subl1item.tag == "table":
				#action下的table直接放在isolationProcedureEnd_XML下，但如果转换为cbRef后放置位置会出错！！            
				action_XML.append(subl1item)
			#循环遍历时，如果subl1item时list2，则直接生成action的子元素
			elif subl1item.tag == "list2":
				randomList_XML = etree.SubElement(action_XML, 'randomList')
				l2item_list = subl1item.xpath("l2item")
				#对此subl1item下的元素l2item进行提取
				for l2item in l2item_list:
					listItem_XML = etree.SubElement(randomList_XML, 'listItem')					
					for subl2item in l2item:						
						if subl2item.tag == "para":							
							para_XML2 = etree.SubElement(listItem_XML, 'para')
							para_XML2.text = subl2item.text
						#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
						elif subl2item.tag == "note":
							noteText = subl2item.xpath("string()").strip()
							note_XML = etree.SubElement(listItem_XML, 'note')
							notePara_XML = etree.SubElement(note_XML, 'notePara')
							notePara_XML.text = noteText
						elif subl2item.tag == "table":						                        
							para_XML2.append(subl2item)
						#循环遍历时，如果subl1item时list2，则直接生成action的子元素
						elif subl2item.tag == "list3":
							sequentialList_XML = etree.SubElement(para_XML2, 'sequentialList')							
							l3item_list = subl2item.xpath("l3item")
							#对此subl2item下的元素l3item进行提取
							for l3item in l3item_list:
								l3listItem_XML = etree.SubElement(sequentialList_XML, 'listItem')
								for subl3item in l3item:
									if subl3item.tag == "para":
										para_XML3 = etree.SubElement(l3listItem_XML, 'para')
										para_XML3.text = subl3item.text
									#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
									elif subl3item.tag == "note":
										noteText = subl3item.xpath("string()").strip()
										note_XML = etree.SubElement(l3listItem_XML, 'note')
										notePara_XML = etree.SubElement(note_XML, 'notePara')
										notePara_XML.text = noteText
									elif subl3item.tag == "table":										                        
										para_XML3.append(subl3item)
									#循环遍历时，如果subl1item时list2，则直接生成action的子元素
									elif subl3item.tag == "list4":
										sequentialList_XML = etree.SubElement(para_XML3, 'sequentialList')										
										l4item_list = subl3item.xpath("l4item")
										#对此subl2item下的元素l3item进行提取
										for l4item in l4item_list:
											l4listItem_XML = etree.SubElement(sequentialList_XML, 'listItem')
											for subl4item in l4item:
												if subl4item.tag == "para":
													para_XML4 = etree.SubElement(l4listItem_XML, 'para')
													para_XML4.text = subl4item.text
												#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
												elif subl4item.tag == "note":
													noteText = subl4item.xpath("string()").strip()
													note_XML = etree.SubElement(l4listItem_XML, 'note')
													notePara_XML = etree.SubElement(note_XML, 'notePara')
													notePara_XML.text = noteText
												elif subl4item.tag == "table":										                        
													para_XML4.append(subl4item)
												#循环遍历时，如果subl1item时list2，则直接生成action的子元素
												elif subl4item.tag == "list5":
													print("message Lose :  get list5 pretopic")												
				
	return isolationProcedureEndAlts_XML

def stepEndCreat(topic,effect_dic,taskEffectId,ie):
	from lxml import etree

	isolationProcedureEndAlts_XML = etree.Element("isolationProcedureEndAlts") 
	isolationProcedureEndAlts_XML.set("id","iealts0" + str(ie))
	isolationProcedureEnd_XML = etree.SubElement(isolationProcedureEndAlts_XML,"isolationProcedureEnd")    
	isolationProcedureEnd_XML.set("id","ie0" + str(ie))
	#如果是topic下的初步评估则需要添加有效性标签。
	cbpgAttrib = topic.find(".//effect").attrib
	if "label" in cbpgAttrib:
		cbpg_effect = cbpgAttrib["label"]
		if cbpg_effect != taskEffectId:
			applicRefId = effect_dic[cbpg_effect]		
			isolationProcedureEnd_XML.set("applicRefId",applicRefId)	

	#title值
	title = etree.SubElement(isolationProcedureEnd_XML,"title")
	title.text = "故障修复确认"

	#l1item转化为action
	l1item_list = topic.xpath(".//l1item")

	# #生成action，randomlist，	
	#根据arj中的生成多个listItem
	for l1item in l1item_list:		
		#l1item下的节点为list2，para，note，table等		
		for subl1item in l1item:
			# #有些情况 note会在para前出现，所以暂时先生成action_XML，以便note能添加到action_XML下。			
			# action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')			
			if subl1item.tag == "para":
				if len(subl1item.text.strip())>0:
					action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')				
					action_XML.text = subl1item.text
			#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
			elif subl1item.tag == "note":
				noteText = subl1item.xpath("string()").strip()
				note_XML = etree.SubElement(isolationProcedureEnd_XML, 'note')
				notePara_XML = etree.SubElement(note_XML, 'notePara')
				notePara_XML.text = noteText
			elif subl1item.tag == "table":
				#action下的table直接放在isolationProcedureEnd_XML下，但如果转换为cbRef后放置位置会出错！！            
				action_XML.append(subl1item)
			#循环遍历时，如果subl1item时list2，则直接生成action的子元素
			elif subl1item.tag == "list2":
				randomList_XML = etree.SubElement(action_XML, 'randomList')
				l2item_list = subl1item.xpath("l2item")
				#对此subl1item下的元素l2item进行提取
				for l2item in l2item_list:
					for subl2item in l2item:
						if subl2item.tag == "para":
							listItem_XML = etree.SubElement(randomList_XML, 'listItem')
							para_XML2 = etree.SubElement(listItem_XML, 'para')
							para_XML2.text = subl2item.text
						#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
						elif subl2item.tag == "note":
							noteText = subl2item.xpath("string()").strip()
							note_XML = etree.SubElement(listItem_XML, 'note')
							notePara_XML = etree.SubElement(note_XML, 'notePara')
							notePara_XML.text = noteText
						elif subl2item.tag == "table":						                        
							para_XML2.append(subl2item)
						#循环遍历时，如果subl1item时list2，则直接生成action的子元素
						elif subl2item.tag == "list3":
							sequentialList_XML = etree.SubElement(para_XML2, 'sequentialList')
							l3listItem_XML = etree.SubElement(sequentialList_XML, 'listItem')
							l3item_list = subl2item.xpath("l3item")
							#对此subl2item下的元素l3item进行提取
							for l3item in l3item_list:
								for subl3item in l3item:
									if subl3item.tag == "para":
										para_XML3 = etree.SubElement(l3listItem_XML, 'para')
										para_XML3.text = subl3item.text
									#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
									elif subl3item.tag == "note":
										noteText = subl3item.xpath("string()").strip()
										note_XML = etree.SubElement(l3listItem_XML, 'note')
										notePara_XML = etree.SubElement(note_XML, 'notePara')
										notePara_XML.text = noteText
									elif subl3item.tag == "table":										                        
										para_XML3.append(subl3item)
									#循环遍历时，如果subl1item时list2，则直接生成action的子元素
									elif subl3item.tag == "list4":
										sequentialList_XML = etree.SubElement(para_XML3, 'sequentialList')
										l4listItem_XML = etree.SubElement(sequentialList_XML, 'listItem')
										l4item_list = subl3item.xpath("l4item")
										#对此subl2item下的元素l3item进行提取
										for l4item in l4item_list:
											for subl4item in l4item:
												if subl4item.tag == "para":
													para_XML4 = etree.SubElement(l4listItem_XML, 'para')
													para_XML4.text = subl4item.text
												#如果subl1item是note，则直接将整个subl1item添加到action树下，然后被notechange函数做进一步的调整。
												elif subl4item.tag == "note":
													noteText = subl4item.xpath("string()").strip()
													note_XML = etree.SubElement(l4listItem_XML, 'note')
													notePara_XML = etree.SubElement(note_XML, 'notePara')
													notePara_XML.text = noteText
												elif subl4item.tag == "table":										                        
													para_XML4.append(subl4item)
												#循环遍历时，如果subl1item时list2，则直接生成action的子元素
												elif subl4item.tag == "list5":
													print("message Lose :  get list5 pretopic")												
				
	return isolationProcedureEndAlts_XML