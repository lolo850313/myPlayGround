def excelToDic(filePath):
	import xlrd
	sheet = xlrd.open_workbook(filePath).sheet_by_index(0)
	row = sheet.nrows
	col = sheet.ncols
	equipList = []
	title = []
	for i in range(col):
		title.append(sheet.cell(0,i).value)

	for i in range(1,row):
		dic = {}
		for j in range(col):			
			dic[title[j]] = sheet.cell(i,j).value
		equipList.append(dic)

	return equipList