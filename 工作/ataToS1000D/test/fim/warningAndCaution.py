#用于生成task中warning，caution的列表
#生成思路是：先将所有的warning，caution的标签提取出来，然后在warningsAndCautionsRef和safetyRqmts中生成相应的标签。
def cirList(arj_task,cirTag):
	cir_list = []	
	for i in arj_task.xpath(cirTag):
		cir_list.append(i.find("para").text)
	
	# 去重
	result = []
	for i in cir_list:
		if i not in result:
			result.append(i)
	return result

#根据arj_warning搜索warning_xml中的对应的warningIdentNum后，生成warningRef_xml树
def warningRefCreat(warning_xml,arj_warning,warId):
	from lxml import etree
	#搜索warningxml中对应arj_warning的warningIdentNum值
	warningSpec_list = etree.parse(warning_xml).findall(".//warningSpec")
	for warning in warningSpec_list:
		if warning[1].text == arj_warning:
			warningIdentNum = (warning[0].attrib["warningIdentNumber"])
	##根据warningIdentNumber生成warningsAndCautionsRef_xml树
	#id流水号，自动补齐3位
	warId = "War-" + str(warId).zfill(3)
	warningRef_xml = etree.Element("warningRef")
	warningRef_xml.set("id",warId)
	warningRef_xml.set("warningIdentNumber",warningIdentNum)    
	return warningRef_xml

#根据arj_caution搜索caution_xml中的对应的cautionIdentNum后，生成caution_xml树
def cautionRefCreat(caution_xml,arj_caution,cauId):
	from lxml import etree
	#搜索cautionxml中对应arj_caution的cautionIdentNum值
	cautionSpec_list = etree.parse(caution_xml).findall(".//cautionSpec")
	for caution in cautionSpec_list:
		if caution[1].text == arj_caution:
			cautionIdentNum = (caution[0].attrib["cautionIdentNumber"])
	#根据cautionIdentNumber生成warningsAndCautionsRef_xml树
	cautionRef_xml = etree.Element("cautionRef")
	cauId = "Cau-" + str(cauId).zfill(3)
	cautionRef_xml.set("id",cauId)
	cautionRef_xml.set("cautionIdentNumber",cautionIdentNum)    
	return cautionRef_xml

#将构造的warningsAndCautionsRef_xml添加到content_element
def warningsAndCautionsRef_insertTo_content(arj_task,caution_xml,warning_xml,content_element):
	from lxml import etree
	#搜索task中的warning，caution标签
	arj_warning_list = cirList(arj_task,".//warning")
	arj_caution_list = cirList(arj_task,".//caution")

	#caution和warning不未空
	if arj_warning_list != [] or arj_caution_list!= []:
		warningsAndCautionsRef_xml = etree.Element('warningsAndCautionsRef')
		warId = 1
		cauId = 1
		for arj_warning in arj_warning_list:
			print(arj_warning)
			#生成warningsAndCautionsRef_xml
			warningRef_xml = warningRefCreat(warning_xml,arj_warning,warId)
			warningsAndCautionsRef_xml.insert(0,warningRef_xml)
			#生成id流水号
			warId = warId + 1
		for arj_caution in arj_caution_list:
			#生成warningsAndCautionsRef_xml
			cautionRef_xml = cautionRefCreat(caution_xml,arj_caution,cauId)
			warningsAndCautionsRef_xml.insert(1,cautionRef_xml)
			cauId = cauId + 1
		content_element.insert(0,warningsAndCautionsRef_xml)
		
		#如果task中有warning和caution的标签，则对reqSafety进行修正。
		safetyRqmts_xml = etree.Element("safetyRqmts")
		#合并后的war-001,war-002等
		warId_merged = ""
		#warNum表示task中有几个war参引,warNum从1开始
		if warId > 1:
			for warNum in range(1,warId):
				warId_merged = warId_merged + "War-"+str(warNum).zfill(3) + " "
			#去掉末尾的空格
			warId_merged = warId_merged.strip()
			safetyRqmts_xml.set("warningRefs",warId_merged)

		if cauId > 1:
			#合并后的war-001,war-002等
			cauId_merged = ""
			#warNum表示task中有几个war参引,cauNum从1开始
			for cauNum in range(1,cauId):
				cauId_merged = cauId_merged + "Cau-"+str(cauNum).zfill(3) + " "
			#去掉末尾的空格
			cauId_merged = cauId_merged.strip()
			safetyRqmts_xml.set("cautionRefs",cauId_merged)

		#替换掉原有noSafety标签
		content_element.xpath(".//reqSafety")[0][0] = safetyRqmts_xml



