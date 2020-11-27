from lxml import etree
from excel import excelout
import os
##总路径
dirPath = "D:\\测试\\s1000d\\s1000d_teman\\"
filePath = dirPath + "teman\\"

#将fim手册元素化
array = []
num = 90000

for i in os.listdir(filePath):
	#将arj_sect_list手册元素化
	teman_arj = etree.parse(filePath + i)
	arj_sheet_list = teman_arj.xpath("//sheet")
	for sheet in arj_sheet_list:
		if sheet.attrib["gnbr"][:4] == "item":
			dic = {}
			dic["ata插图编号"] = sheet.attrib["gnbr"]
			dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + sheet.attrib["gnbr"][4:10] + "-A-SVV19-" + str(num).zfill(5)+"-A-001-01"
			num = num + 1
			array.append(dic)
		elif sheet.attrib["gnbr"][:5] == "ITEM-":
			dic = {}
			dic["ata插图编号"] = sheet.attrib["gnbr"]
			dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + sheet.attrib["gnbr"][5:11] + "-A-SVV19-" + str(num).zfill(5)+"-A-001-01"
			num = num + 1
			array.append(dic)
		else:
			print(sheet.attrib["gnbr"]) 
			
title=["ata插图编号","S1000D ICN编号"]
filename = "ICN.xls"
excelout(array,title,dirPath,filename)