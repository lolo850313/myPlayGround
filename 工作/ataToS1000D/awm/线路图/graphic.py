def graphicAdd(ICNpath,gnbr):
	import xlrd
	from lxml import etree
	#读取ICN关系表
	data = xlrd.open_workbook(ICNpath)
	icnTable = data.sheets()[0]
	row = icnTable.nrows
	icnDic = {}
	for i in range(row):
		gnbrExcel = icnTable.cell(i,0).value
		icnExcel = icnTable.cell(i,1).value
		icnDic[gnbrExcel] = icnExcel

	#infoEntityIdent通过ICN的excel得到,并添加到content_element下
	if gnbr in icnDic:
		infoEntityIdent = icnDic[gnbr]
	else:
		print(gnbr + " @not in ICNexcel")	
	
	return infoEntityIdent