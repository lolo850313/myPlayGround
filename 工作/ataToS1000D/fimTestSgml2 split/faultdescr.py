#故障描述（由title前半部分转化）

def descr_creat(head,arj_task,content_element):
	from lxml import etree
	faultDescr = content_element.find(".//faultDescr")
	descr_text = (head.find(".//techName").text)
	descr = etree.Element("descr")
	descr.text = descr_text
	faultDescr.append(descr)