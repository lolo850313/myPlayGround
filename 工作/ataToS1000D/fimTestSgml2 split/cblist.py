def cb(arj_pretopic_list):
	CBList = []
	for topic in arj_pretopic_list:
		if (topic.find("title").text)=="相关断路器":
			for row in topic.xpath(".//tbody/row"):
				paraList = row.xpath(".//para")
				if len(paraList) == 4:
					cbtext = paraList[2].text
					if cbtext != "编号":
						CBList.append(cbtext)
				elif len(paraList) == 2:
					cbtext = paraList[0].text
					if cbtext != "编号":
						CBList.append(cbtext)
				else:
					print("table row length != 4 or != 2")
	return CBList