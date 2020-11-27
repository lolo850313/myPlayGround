#将pm树xml文件中的pm标题提取到excel中。
from lxml import etree
import os

#将列表写入excel第一列
def excelout(arr,title,path,filename):
	import xlsxwriter
	workbook = xlsxwriter.Workbook(path + filename)
	worksheet = workbook.add_worksheet('My Worksheet')

	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for row in range(len(arr)):	
		worksheet.write(row,0,arr[row])

	workbook.close()

dir = "D:\\程序源数据\\手册\\pm树\\"
fileArr = os.listdir(dir)
pmTreeArr = []
for i in fileArr:
	if i[-4:] != ".xls":
		file = dir + i
		tree = etree.parse(file)
		root = tree.getroot()
		titleList = root.findall(".//pmEntryTitle")
		for i in titleList:
			pmTreeArr.append(i.text)

filename="ssm.xls"
path = dir
title = "pm数中文"
excelout(pmTreeArr,title,path,filename)


