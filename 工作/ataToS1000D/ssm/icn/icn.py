from lxml import etree
from excel import excelout
##总路径
dirPath = "D:\\测试\\s1000d\\s1000d_ssm\\"
##手册xml存放路径
xmlPath = "SSM-TP700029-$new$-amm(201906).sgm"

#将fim手册元素化
fim_arj = etree.parse(dirPath + xmlPath)
arj_sheet_list = fim_arj.xpath(".//sheet")
arj_grsymbol_list = fim_arj.xpath(".//grsymbol")
array = []

for sheet in arj_sheet_list:
    dic = {}
    dic["ata插图编号"] = sheet.attrib["gnbr"]
    prefix = sheet.attrib["gnbr"].lower()
    if prefix[:3] == "ssm":
        dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + prefix[3:9] + "-A-SVV19-" + "4" + prefix[-4:] +"-A-001-01"
        dic["tag"] = "sheet"
    # elif prefix[:2] == "wm":
    #     dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + prefix[2:8] + "-A-SVV19-" + "4" + prefix[-4:] +"-A-001-01"
    else:
        print(prefix)
    array.append(dic)

for sheet in arj_grsymbol_list:
    dic = {}
    dic["ata插图编号"] = sheet.attrib["gnbr"]
    prefix = sheet.attrib["gnbr"].lower()
    if prefix[:3] == "ssm":
        dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + prefix[3:9] + "-A-SVV19-" + "4" + prefix[-4:] +"-A-001-01"
        dic["tag"] = "grsymbol"
    # elif prefix[:2] == "wm":
    #     dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + prefix[2:8] + "-A-SVV19-" + "4" + prefix[-4:] +"-A-001-01"
    else:
        print(prefix)
    array.append(dic)

title=["ata插图编号","S1000D ICN编号","tag"]
filename = "ICN.xls"
excelout(array,title,dirPath,filename)