#xml生成程序
#excel 不同有效性合并 （G20 G21 G22等）
#使用合并有效性后的excel 生成xml

from lxml import etree
from wiringData import wiring_frame
from excelRead import readExcel

#从excel所在的文件夹名中提取
effectARJ = "10101"

#从excel文件中提取线束信息字典excelInfo_list
# excelInfo = {"线束号":"线束号","导线号":"导线号","从端端接代号":"从端端接代号","到端端接代号":"到端端接代号","从端孔号":"从端孔号","到端孔号":"到端孔号","导线材料":"导线材料","AWG":"导线线规","导线长度":"导线长度","敷设字母":"敷设字母"}
path = "d:/WB_8810C01000G20_A_5d45349d-3509-4e41-adb2-c6f54952d96c (1).xls"
excelInfo_list = readExcel(path)

#生成content头
content = etree.Element('content')

for i in excelInfo_list:
    #从文件名中提取
    dmCode = {"assyCode":"00","disassyCode":"00","disassyCodeVariant":"A","infoCode":"051","infoCodeVariant":"A","itemLocationCode":"A","modelIdentCode":"C919","subSubSystemCode":"1","subSystemCode":"2","systemCode":"21","systemDiffCode":"A"}
    
    #从ph中提取wireColor，contactPartNumberARJ，partNumber，暂设默认
    phInfo = {"接触件件号" : "接触件件号","导线零件号" : "导线零件号","导线颜色" : "导线颜色"}

    #从文件名中提取
    dmCode = {"assyCode":"00","disassyCode":"00","disassyCodeVariant":"A","infoCode":"051","infoCodeVariant":"A","itemLocationCode":"A","modelIdentCode":"C919","subSubSystemCode":"1","subSystemCode":"2","systemCode":"21","systemDiffCode":"A"}

    excelInfo = i

    wiring_xml = wiring_frame(effectARJ,dmCode,excelInfo,phInfo)

    #将wiring添加到content中
    content.append(wiring_xml)


# etree.ElementTree(content).write('/Users/Hewenhao/wiring.xml',pretty_print=True,encoding="utf-8")
etree.ElementTree(content).write('d:/wiring.xml',pretty_print=True,encoding="utf-8")
