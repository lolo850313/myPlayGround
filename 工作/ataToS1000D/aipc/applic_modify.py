#将文件中的有效性按excel的对应关系替换
import xlrd
from lxml import etree
import os

effDic = {}
effpath = "D:\\测试\\s1000d\\effectContentExcelNEW191210.xls"
dirPath = "D:\\测试\\s1000d\\s1000d_aipc\\aipc_dmrl\\"
sh = xlrd.open_workbook(effpath).sheet_by_index(0)
nrow = sh.nrows
for row in range(nrow):
    eff_from = (sh.cell(row, 2).value)
    eff_to = (sh.cell(row, 3).value)
    effDic[eff_from] = eff_to

for i in os.listdir(dirPath):        
    xmlFile = dirPath + i
    if xmlFile[-4:] == ".xml" or xmlFile[-4:] == ".XML":
        task = etree.parse(xmlFile)
        for applicRef in task.xpath(".//applicRef"):
            applicIdentValue = applicRef.attrib["applicIdentValue"]
            if applicIdentValue in effDic:
                applicRef.attrib["applicIdentValue"] = effDic[applicIdentValue]
            else:
                print(applicIdentValue)
        task.write(xmlFile,xml_declaration=True,pretty_print=True,encoding="utf-8")