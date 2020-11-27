#修改大客xml的issueNumber
from lxml import etree
import os
# 数据文件夹
dir = "D:\\临时文件\\ccom\\12\\"
filePath = dir
# 目标文件夹
resPath = filePath
# resPath = dir + "DDN-C919-07482-SVV19-2019-00270\\"
#增加值
# addValue = 1
# inWork = "01"
# 英文
languageIsoCode = "sx"
countryIsoCode = "US"
title = "SX-US"
# # 中文
# languageIsoCode = "zh"
# countryIsoCode = "CN"
# title = "ZH-CN"

xmlList = []
for i in os.listdir(filePath):
	if i[:3] == "DMC":
		xmlList.append(filePath + i)

for i in xmlList:
	print(i)
	tree = etree.parse(i)
	#读取task
#     issueNumber = tree.find(".//issueInfo").attrib["issueNumber"]
#     newIssueNumber = str(int(issueNumber) + addValue).zfill(3)
#     newFilename = i[-48:-16] + newIssueNumber + "-"+ inWork +"_"+title + ".XML"

	#只修改中英文
	fileNameSplit = i.split("\\")
	newFilename = fileNameSplit[-1][:-9] + title + ".XML"
#     newFilename = i[-48:-16] + newIssueNumber + i[-13:]
#     tree.find(".//issueInfo").attrib["issueNumber"] = newIssueNumber
#     tree.find(".//issueInfo").attrib["inWork"] = inWork
	tree.find(".//language").attrib["countryIsoCode"] = countryIsoCode
	tree.find(".//language").attrib["languageIsoCode"] = languageIsoCode
	print(resPath + newFilename)
	tree.write((resPath + newFilename),pretty_print=True,encoding="utf-8",xml_declaration=True)
	os.remove(i)
#countryIsoCode languageIsoCode inWork 
