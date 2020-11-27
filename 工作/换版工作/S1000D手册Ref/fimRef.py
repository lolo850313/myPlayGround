from lxml import etree
import os

def excelout(list_dic,title,path,filename):
	import xlsxwriter
	workbook = xlsxwriter.Workbook(path + filename)
	worksheet = workbook.add_worksheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	#excel_row是excel写入的起始行，row是list数据的每个子列表
	row = 1
	for key in list_dic:
		for sub in list_dic[key]:
			worksheet.write(row,0,key)
			worksheet.write(row,1,sub)
			row = row + 1

	workbook.close()

pathBefore = "D:\\程序源数据\\手册\\201912\\dmrl\\"
# pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "fim\\"

refDic = {}
xmlDic = os.listdir(path)
for i in xmlDic:
	if i[-23:-19] != "414A":
		doc = path + i
		refDic[i] = []
		tree = etree.parse(doc)
		content = tree.find(".//content")
		if content is not None:
			dmrefArr = content.xpath(".//dmCode")
			for dmCode in dmrefArr:
				dmCode_para = dmCode.attrib
				ref = dmCode_para["modelIdentCode"] \
				+ "-" + dmCode_para["systemDiffCode"] \
				+ "-" +dmCode_para["systemCode"] \
				+ "-" + dmCode_para["subSystemCode"] + dmCode_para["subSubSystemCode"] \
				+ "-" + dmCode_para["assyCode"] \
				+ "-" + dmCode_para["disassyCode"] + dmCode_para["disassyCodeVariant"] \
				+ "-" + dmCode_para["infoCode"] + dmCode_para["infoCodeVariant"] \
				+ "-" + dmCode_para["itemLocationCode"]
				refDic[i].append(ref)

		
			externalPubCodeArr = tree.xpath(".//externalPubCode")
			for j in externalPubCodeArr:
				refDic[i].append(j.text)
title = ["dmrl", "ref"]
filename = "fimRef.xls"
excelout(refDic,title,path,filename)
	

