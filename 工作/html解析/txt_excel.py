def excelout(arr,title,path,filename):
	from xlwt import Workbook
	workbook = Workbook()
	worksheet = workbook.add_sheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for row in range(len(arr)):	
		for col in range(len(arr[row])):
			worksheet.write(row+1,col,arr[row][col])

	workbook.save(path + filename)

import os

path = "D:\\file\\res\\"
title = ["所属文件夹", "task", "关键词", "para"]
fileArr = os.listdir(path)
for i in range(len(fileArr)):
	fileArr[i] = path +  fileArr[i]

for file in fileArr:
	with open(file, encoding="gb18030") as f:    #打开文件
		totalString = ""
		data = f.readlines()   #读取文件
		for sdata in data:
			totalString += sdata

		tmpArr = totalString.split("@@@")
		for i in range(len(tmpArr)):
			tmpArr[i] = tmpArr[i].split("@")
		
		excelName = (file.split("\\")[-1][:-4] + ".xlsx")
		excelout(tmpArr,title,path,excelName)