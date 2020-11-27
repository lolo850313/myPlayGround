from lxml import etree
from excel import excelout
##总路径
dirPath = "D://测试//s1000d//s1000d_aipc//"
##手册xml存放路径
xmlPath = "AIPC-TP700016-$new$-amm(201912).sgm"

#将fim手册元素化
fim_arj = etree.parse(dirPath + xmlPath)
arj_sheet_list = fim_arj.xpath("//sheet")
array = []

num = 30000   
for sheet in arj_sheet_list:
    if "intro" not in sheet.attrib["gnbr"]:
        dic = {}
        dic["ata插图编号"] = sheet.attrib["gnbr"]
        dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + sheet.attrib["gnbr"][4:10] + "-A-SVV19-" + str(num).zfill(5)+"-A-001-01"
        num = num + 1
        array.append(dic)
    else:
        print(sheet.attrib["gnbr"]) 
title=["ata插图编号","S1000D ICN编号"]
filename = "ICN.xls"
excelout(array,title,dirPath,filename)