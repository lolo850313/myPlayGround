#将多余标签删除,将所有title中的。号删除
def blankTag(file_path):
	import os
	from lxml import etree
	
	file_path = file_path
	for i in os.listdir(file_path):
		xmlFile = file_path + i
		task = etree.parse(xmlFile)
		# 将没有子元素的标签删除
		for sequentialList in task.findall(".//sequentialList"):
			if sequentialList.getchildren() == []:
				sequentialList.getparent().remove(sequentialList)
		for commonInfoDescrParaAlts in task.findall(".//commonInfoDescrParaAlts"):
			if commonInfoDescrParaAlts.getchildren() == []:
				commonInfoDescrParaAlts.getparent().remove(commonInfoDescrParaAlts)
		for commonInfo in task.findall(".//commonInfo"):
			if commonInfo.getchildren() == []:
				commonInfo.getparent().remove(commonInfo)
		for possibleCauseGroup in task.findall(".//possibleCauseGroup"):
			if possibleCauseGroup.getchildren() == []:
				possibleCauseGroup.getparent().remove(possibleCauseGroup)	
		for listItem in task.findall(".//listItem"):
			if listItem.getchildren() == []:
				listItem.getparent().remove(listItem)
		for randomList in task.findall(".//randomList"):
			if randomList.getchildren() == []:
				randomList.getparent().remove(randomList)
		for actionlList in task.findall(".//action"):
			if (actionlList.text) == None and actionlList.getchildren() == []:
				actionlList.getparent().remove(actionlList)
		# 将没有子元素的isolationMainProcedure标签补充相关必要标签
		for isolationMainProcedure in task.findall(".//isolationMainProcedure"):
			if isolationMainProcedure.getchildren() == []:
				isolationProcedureEndAlts = etree.Element("isolationProcedureEndAlts")
				isolationProcedureEnd = etree.SubElement(isolationProcedureEndAlts,"isolationProcedureEnd")
				isolationProcedureEnd.set("applicRefId" ,"a001")
				isolationProcedureEnd.set("id" ,"ie01")
				isolationMainProcedure.append(isolationProcedureEndAlts)
		
		#将所有title中的。号删除
		for title in task.findall(".//title"):
			if "。" in (title.text):
				title.text = title.text.strip("。")
			# if title.text == []:
			# 	sequentialList.getparent().remove(sequentialList)

		task.write(xmlFile,pretty_print=True,encoding="utf-8")
		
if __name__ == "__main__":
	dirPath = "D:\\测试\\s1000d\\s1000d_fim\\split_To\\"
	blankTag(dirPath)