from lxml import etree
from excel import excelout
##总路径
dirPath = "D:\\测试\\s1000d\\s1000d_awm\\"
##手册xml存放路径
xmlPath = "WM-TP700015-$new$-amm(201906).sgm"

#将fim手册元素化
fim_arj = etree.parse(dirPath + xmlPath)
arj_sheet_list = fim_arj.xpath(".//sheet")
array = []

num = 50000   
for sheet in arj_sheet_list:
    dic = {}
    dic["ata插图编号"] = sheet.attrib["gnbr"]
    prefix = sheet.attrib["gnbr"].lower()
    if prefix[:3] == "wdm":
        dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + sheet.attrib["gnbr"][3:9] + "-A-SVV19-" + str(num).zfill(5)+"-A-001-01"
    elif prefix[:2] == "wm":
        dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + sheet.attrib["gnbr"][2:8] + "-A-SVV19-" + str(num).zfill(5)+"-A-001-01"
    else:
        print(prefix)
    num = num + 1
    array.append(dic)
title=["ata插图编号","S1000D ICN编号"]
filename = "ICN.xls"
excelout(array,title,dirPath,filename)