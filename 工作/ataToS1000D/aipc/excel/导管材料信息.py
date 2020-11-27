from lxml import etree
from excel import excelout
##总路径
dirPath = "/Users/hewenhao/OneDrive/工作/ATA2S1000D/aipc/"
##手册xml存放路径
xmlPath = "AIPC-TP700016-$new$-amm(201909).sgm"

#将fim手册元素化
fim_arj = etree.parse(dirPath + xmlPath)
arj_sheet_list = fim_arj.xpath("//sheet")
array = []
 
for sheet in arj_sheet_list:
    if "intro" not in sheet.attrib["gnbr"]:
        dic = {}
        dic["ata插图编号"] = sheet.attrib["gnbr"]
        dic["S1000D ICN编号"] = "ICN-ARJ21-A-" + sheet.attrib["gnbr"][4:10] + "-A-SVV19-" + str(num).zfill(5)+"-A-001-01"
        num = num + 1
        array.append(dic)

title=["导管材料信息","管径","壁厚","管长","材料规范","材料牌号-热处理"]
filename = "导管材料信息.xls"
excelout(array,title,dirPath,filename)