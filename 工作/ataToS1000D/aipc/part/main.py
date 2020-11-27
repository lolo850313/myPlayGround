from lxml import etree
import xlrd
from xmlCreat import partSpecCreat
from head import headxml

dirPath = "D://测试//s1000d//s1000d_aipc//"
partExcel = "part-cir-v2.xlsx"
data = xlrd.open_workbook(dirPath + partExcel)
fileEffect = "appsp-asn-ALL"
#创建head部分
issueNumberPara = "002"
time = {"year":"2019","month":"12","day":"20"}
head = headxml(issueNumberPara,time,fileEffect)

#创建了content
content = etree.Element("content")
commonRepository = etree.SubElement(content,"commonRepository")
partRepository = etree.SubElement(commonRepository,"partRepository")

#转换excel中的数据
table = data.sheets()[0]
rows = table.nrows
part_date = []
for i in range(1,rows):
    dic = {}
    if isinstance(table.cell_value(i,0),float):
        dic["pnr"] = str(int(table.cell_value(i,0)))
    else:
        dic["pnr"] = table.cell_value(i,0)
    dic["kwd"] = table.cell_value(i,1)
    if isinstance(table.cell_value(i,2),float):
        dic["pnrmfr_mfr"] = str(int(table.cell_value(i,2)))
    elif isinstance(table.cell_value(i,2),str):
        dic["pnrmfr_mfr"] = table.cell_value(i,2)
    elif isinstance(table.cell_value(i,2),int):
        dic["pnrmfr_mfr"] = str(table.cell_value(i,2))
    dic["lbl"] = table.cell_value(i,3)
    dic["opt"] = table.cell_value(i,4)
    dic["optmfr_mfr"] = table.cell_value(i,5) 
    dic["lsp"] = table.cell_value(i,6)
    dic["lspmfr_mfr"] = table.cell_value(i,7)
    dic["pni"] = table.cell_value(i,8)
    dic["pnimfr_mfr"] = table.cell_value(i,9)
    dic["tbm"] = table.cell_value(i,12)
    dic["lfmmfr_ifm"] = table.cell_value(i,10)
    dic["lfmmfr_mfr"] = table.cell_value(i,11)
    part_date.append(dic)

#将excel的数据转换为partSpec
for part in part_date:
    subPart = partSpecCreat(part)
    partRepository.append(subPart)

#写xml头，并添加head部分和content部分
root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/comrep.xsd"></dmodule>')
root.append(head)
root.append(content)
dmrl = "ARJ21-A-00-00-00-00A-00GA-A"
etree.ElementTree(root).write(dirPath +'/DMC-'+ dmrl + '_'+issueNumberPara+'-00_ZH-CN.XML',xml_declaration=True,pretty_print=True,encoding="utf-8")