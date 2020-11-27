def graphicAdd(ICNpath,arj_figure,content_element,dmc):
	import xlrd
	from lxml import etree
	#读取ICN关系表
	data = xlrd.open_workbook(ICNpath)
	icnTable = data.sheets()[0]
	row = icnTable.nrows
	icnDic = {}
	for i in range(row):
		gnbrExcel = icnTable.cell(i,0).value
		gnbrExcel = gnbrExcel.split("_")[0]
		icnExcel = icnTable.cell(i,1).value
		icnDic[gnbrExcel] = icnExcel

	#infoEntityIdent通过ICN的excel得到,并添加到content_element下
	figure_XML = content_element.find(".//figure")
	
	#figure下的graphic
	sheetList = arj_figure.findall("graphic/sheet")
	idNum = 1
	for i in sheetList:
		gnbr = i.attrib["gnbr"]
		infoEntityIdent = icnDic[gnbr]
		graphic_XML = etree.Element("graphic")
		graphic_XML.set("infoEntityIdent",infoEntityIdent)
		graphic_XML.set("id","gra-" + dmc + str(idNum).zfill(3))
		idNum += 1
		figure_XML.append(graphic_XML)
	
	return content_element