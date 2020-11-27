def frame(lsheet,ICNpath):
	from lxml import etree	
	from graphic import graphicAdd

	#内容生成
	content_element = etree.Element("content")
	description = etree.SubElement(content_element,"description")

	for graphic in lsheet.xpath("graphic"):
		graphic_title = graphic.find("title").text
		figure = etree.SubElement(description,"figure")
		figure_title = etree.SubElement(figure,"title")
		figure_title.text = graphic_title

		graphic_sheetList = graphic.findall("sheet")
		for sheet in graphic_sheetList:
			graphic_sheet_gnbr = sheet.attrib["gnbr"]
			infoEntityIdent = graphicAdd(ICNpath,graphic_sheet_gnbr)     
			figure_graphic = etree.SubElement(figure,"graphic")
			figure_graphic.set("infoEntityIdent",infoEntityIdent)

	return content_element





