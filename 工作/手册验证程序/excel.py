#把列表字典写入excel，每行是列表元素，每列是字典
def excelout(list_dic,title,path,filename):
	from xlwt import Workbook
	workbook = Workbook()
	worksheet = workbook.add_sheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for row in range(len(list_dic)):	
		for col in range(len(title)):
				if	isinstance(list_dic[row][title[col]],str):
					worksheet.write(row+1,col,list_dic[row][title[col]])
				else:
					tmp = ""
					for i in  list_dic[row][title[col]]:
						# 有时候i会是空列表
						if i != None:
							tmp = i + ";" + tmp
					worksheet.write(row+1,col,tmp)

	workbook.save(path + filename)

#把字典写入excel，数据依次放入
def excelout2(dic,title,path,filename):
	import xlwt
	workbook = xlwt.Workbook()
	worksheet = workbook.add_sheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	row = 1
	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for i in dic:
		worksheet.write(row,0,i)
		for indexT in range(1,len(title)):
			if isinstance(dic[i][title[indexT]],list):
				tmpStr = ""
				for j in dic[i][title[indexT]]:
					if j == None:
						tmpStr = "None ;" + tmpStr
					else:
						tmpStr =  j + ";" + tmpStr
				worksheet.write(row,indexT,tmpStr)
			else:
				worksheet.write(row,indexT,dic[i][title[indexT]])
		row = row + 1
	
	workbook.save(path + filename)

def excelout3(dic,title,path,filename):
	import xlwt
	workbook = xlwt.Workbook()
	worksheet = workbook.add_sheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	row = 1
	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for i in dic:
		worksheet.write(row,0,i)
		if isinstance(dic[i]["参引的DMC"],list):
			for sub in range(len(dic[i]["参引的DMC"])):
				worksheet.write(row,sub+1,dic[i]["参引的DMC"][sub])
		else:
			worksheet.write(row,indexT,dic[i]["参引的DMC"])
		row = row + 1
	
	workbook.save(path + filename)