def effect_to_dic(arj_task):
	from lxml import etree 

	#将本章节下的有效性提取到列表中
	effectARJ = arj_task.xpath(".//effect")
	effect_list = []
	for i in range(len(effectARJ)):
		if "label" in effectARJ[i].attrib:
			effect_list.append(effectARJ[i].attrib["label"])
		else:
			effect_list.append("101+.")

	#有效性去重
	effect_list = list(set(effect_list))

	effect_dic = {}
	for i in range(len(effect_list)):
		effect_dic[effect_list[i]] = "appRef-" + str(i+1).zfill(4)

 
	return effect_dic

#生成referencedApplicGroupRef的xml树，输入是有效性和流水号的字典。
def effect_xml(effect_dic):
	from lxml.builder import ElementMaker
	from lxml import etree

	referencedApplicGroupRef = etree.Element("referencedApplicGroupRef")
	for i in effect_dic:
		applicRef_xml = etree.SubElement(referencedApplicGroupRef,"applicRef")
		applicRef_xml.set("applicIdentValue",i)
		applicRef_xml.set("id",effect_dic[i])
	return referencedApplicGroupRef

#将effect标签写入content中
def effect_insert_content(arj_task,content_element):
	effect_dic = effect_to_dic(arj_task)
	#将有效性参引写入content中
	referencedApplicGroupRef = effect_xml(effect_dic)
	content_element.insert(0,referencedApplicGroupRef)