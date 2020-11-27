#aipc名称无法从xml中得到
import os
from lxml import etree
#把列表字典写入excel，每行是列表元素，每列是字典
def excelout(list_dic,title,path,resPath,filename):
	from xlwt import Workbook
	workbook = Workbook()
	worksheet = workbook.add_sheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for row in range(len(list_dic)):
		for col in range(len(title)):				
			worksheet.write(row+1,col,list_dic[row][title[col]])

	workbook.save(resPath + filename)

#在当前文件夹下设置输入文件夹input，并将输入文件放入其中
filePath = __file__[:-13] + "input/"
resPath = __file__[:-13]
# filePath = "D://测试//PDF_PMC-C919-SVV19-SCYZ0-00_001-00_ZH-CN_MASTER_FULL//"
fileList_origin = os.listdir(filePath)

dataDic2 = []
for i in fileList_origin:
	if i[-3:].lower() == "xml":
		root = etree.parse(filePath + i)
		print(i)
		spareDescr_list = root.findall(".//preliminaryRqmts/reqSpares/spareDescrGroup/spareDescr")		
		for spares in spareDescr_list:
			dic = {}
			
			dmCode = root.find(".//dmCode")
			dic["章节"] = dmCode.attrib["systemCode"]
			# DMC-ARJ21-S-21-22-03-00B-720A-A_001-00_ZH-CN.xml
			dic["DMC"] = i[4:-17]
			dic["中文名称/英文名称"] = root.find(".//techName").text + " / " +  root.find(".//infoName").text         
			sparesname = spares.find(".//name")
			dic["备件名称"] = "无"
			dic["备件热点"] = "无"
			dic["AIPC参引"] = "无"
			dic["图号"] = "无"
			dic["备件项目号"] = "无"
			if sparesname is not None:
				dic["备件名称"] = sparesname.text
			shortname = spares.find(".//shortName")
			if shortname is not None:
				dic["备件热点"] = shortname.text
			catalogSeqNumber = spares.find(".//catalogSeqNumberRef")			
			if catalogSeqNumber is not None:
				dic["图号"] = catalogSeqNumber.attrib["item"]
				dic["备件项目号"] = catalogSeqNumber.attrib["figureNumber"]
				dmCode = catalogSeqNumber.find(".//dmCode")
				if dmCode is not None:
					dic["AIPC参引"] = dmCode.attrib["modelIdentCode"] + "-" + dmCode.attrib["systemDiffCode"] + "-" + dmCode.attrib["systemCode"] + "-" + dmCode.attrib["subSystemCode"] + dmCode.attrib["subSubSystemCode"] + "-" + dmCode.attrib["assyCode"] + "-" +dmCode.attrib["disassyCode"] + dmCode.attrib["disassyCodeVariant"] + "-" + dmCode.attrib["infoCode"] + dmCode.attrib["infoCodeVariant"] + "-" + dmCode.attrib["itemLocationCode"]
				
			
			
			dataDic2.append(dic)

title2 = ["章节","DMC","中文名称/英文名称","备件名称","备件热点","图号","备件项目号","AIPC参引"]

excelout(dataDic2,title2,filePath,resPath,"备件信息表.xlsx")