#topic下的note转换到safetyRqmts下的note，跟在para后面的note则原地转换为notepara
def topicNoteCreat(arj_task,content_element):
	from lxml import etree
	topic_note_list = arj_task.xpath("topic/note")

	if len(topic_note_list) > 0:
		#content中没有safetyRqmts标签，则将noSafety标签替换为safetyRqmts标签。
		if (content_element.xpath(".//safetyRqmts")) == []:
			safetyRqmts_xml = etree.Element("safetyRqmts")
			content_element.xpath(".//reqSafety")[0][0] = safetyRqmts_xml
			#将原note标签插入到新的note标签中
			for topic_note in topic_note_list:			
				#替换掉原有noSafety标签			
				note_xml = etree.SubElement(safetyRqmts_xml,"note")
				notePara_xml = etree.SubElement(note_xml,"notePara")
				notePara_xml.text = topic_note[0].text
		else:
			for topic_note in topic_note_list:
				safetyRqmts_xml = content_element.find(".//safetyRqmts")			
				#替换掉原有noSafety标签			
				note_xml = etree.SubElement(safetyRqmts_xml,"note")
				notePara_xml = etree.SubElement(note_xml,"notePara")
				notePara_xml.text = topic_note[0].text

#note在topic，l2item，l3item下都有出现
#note不需要更改safetyRqmts属性，直接将note下的para替换为notePara
def noteChange(content_element):
	from lxml import etree
	note_list = content_element.xpath(".//note")
	for note in note_list:
		for para in note.xpath("para"):
			paraText = "<notePara>"+ para.text+ "</notePara>"
			#将string解析为element或elementTree
			notePara = etree.fromstring(paraText)		
			note.append(notePara)
			#在添加notePara后删掉原有的para标签
			note.remove(para)