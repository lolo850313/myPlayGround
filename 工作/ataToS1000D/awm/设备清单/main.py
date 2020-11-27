#按设备号前缀，生成各个dmrl
from effect_to_dic import effectToDic
from lxml import etree
from head import headxml
from wiringData import contentFrame
import xlrd

#输入路径
path = "D://测试//s1000d//s1000d_awm//equipment//"
#设备号相关信息
filePath = path + "BB_251_全机汇总设备目录-新中英文对照-20191223.xlsx"
#通过TaskNo找到对应的dmc参数
dmrlFile = path + "WM-TP700015-$new$-amm-eqip-dmrl.xlsx"

resTitle = ["设备号","设备名称（中文）","设备名称（英文）","标准零件号","供应商零件号","供应商","安装位置","设备安装图号","线路图ATA","有效性"]
#版本号
issueNumber = "002"
time = {"day":"20","month":"12","year":"2019"}

#将taskNo与dmc的对应关系提取到taskNO_dmrl字典中
dmrlFile_sheet = xlrd.open_workbook(dmrlFile).sheet_by_index(0)
dmrlFile_rows = dmrlFile_sheet.nrows
taskNo_dmrl = {}
for row in range(1,dmrlFile_rows):    
    k = dmrlFile_sheet.cell(row,1).value
    taskNo_dmrl[k] = {}
    taskNo_dmrl[k]["title"] = dmrlFile_sheet.cell(row,2).value
    taskNo_dmrl[k]["title"] = dmrlFile_sheet.cell(row,2).value
    taskNo_dmrl[k]["modelIdentCode"] = dmrlFile_sheet.cell(row,3).value
    taskNo_dmrl[k]["systemDiffCode"] = dmrlFile_sheet.cell(row,4).value
    taskNo_dmrl[k]["systemCode"] = dmrlFile_sheet.cell(row,5).value
    taskNo_dmrl[k]["subSystemCode"] = str(dmrlFile_sheet.cell(row,6).value)[0]
    taskNo_dmrl[k]["subSubSystemCode"] = str(dmrlFile_sheet.cell(row,6).value)[1]
    taskNo_dmrl[k]["assyCode"] = dmrlFile_sheet.cell(row,7).value
    taskNo_dmrl[k]["disassyCode"] = dmrlFile_sheet.cell(row,8).value
    taskNo_dmrl[k]["disassyCodeVariant"] = dmrlFile_sheet.cell(row,9).value
    taskNo_dmrl[k]["infoCode"] = dmrlFile_sheet.cell(row,10).value
    taskNo_dmrl[k]["infoCodeVariant"] = dmrlFile_sheet.cell(row,11).value
    taskNo_dmrl[k]["itemLocationCode"] = dmrlFile_sheet.cell(row,12).value
    taskNo_dmrl[k]["DMC"] = dmrlFile_sheet.cell(row,13).value
    taskNo_dmrl[k]["techName"] = dmrlFile_sheet.cell(row,14).value
    taskNo_dmrl[k]["infoName"] = dmrlFile_sheet.cell(row,15).value
    taskNo_dmrl[k]["KEY"] = dmrlFile_sheet.cell(row,16).value
# print(taskNo_dmrl)
#按taskNo_dmrl中的taskNo将BB251中的设备号分别生成drml
filePath_sheet = xlrd.open_workbook(filePath).sheet_by_index(0)
filePath_rows = filePath_sheet.nrows

wireGroup = {}
for row in range(1,filePath_rows):
    taskNo = filePath_sheet.cell(row,0).value
    group = taskNo[:2]
    wireDic = {"设备号":taskNo,"设备名称(中文)":filePath_sheet.cell(row,1).value,
    "设备名称(英文)":filePath_sheet.cell(row,2).value,
    "标准零件号":filePath_sheet.cell(row,3).value,
    "供应商零件号":filePath_sheet.cell(row,4).value,
    "供应商":filePath_sheet.cell(row,5).value,
    "供应商（英文）":filePath_sheet.cell(row,6).value,
    "安装位置":filePath_sheet.cell(row,7).value,
    "安装位置（英文）":filePath_sheet.cell(row,8).value,
    "设备安装图号":filePath_sheet.cell(row,9).value,
    "线路图ATA号":filePath_sheet.cell(row,10).value,
    "有效性":filePath_sheet.cell(row,11).value}
    if group in wireGroup:
        if wireDic["设备号"] in wireGroup[group]:
            wireGroup[group][wireDic["设备号"]].append(wireDic)
        else:
            wireGroup[group][wireDic["设备号"]] = [wireDic]
    else:
        wireGroup[group] = {wireDic["设备号"]:[wireDic]}

for row in wireGroup:    
    dmCodeRef = {"assyCode":"00","disassyCode":"00","disassyCodeVariant":"A","infoCode":"051","infoCodeVariant":"A","itemLocationCode":"A","modelIdentCode":"ARJ21","subSubSystemCode":"0","subSystemCode":"2","systemCode":"21","systemDiffCode":"A"}
    
    taskHead = row 
    if taskHead in taskNo_dmrl:
        dmCode = taskNo_dmrl[taskHead]
        dmrl = dmCode["DMC"]
    else:
        print(taskHead + " @ not in equip-dmrl")
    wireList = wireGroup[row]

    root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/wrngdata.xsd"></dmodule>')	
    headXML = headxml(dmCode,time, issueNumber)

    effList = []
    for wire in wireList:
        for i in wireList[wire]:
            if i["有效性"] not in effList:
                effList.append(i["有效性"])  

    #得到当前dmrl的有效性字典
    effectDic = effectToDic(effList)
    contentXML = contentFrame(dmCodeRef,effectDic,wireList,row)
    root.append(headXML)
    root.append(contentXML)
    etree.ElementTree(root).write(path + "\\output\\DMC-" + dmrl + '_'+ str(issueNumber) +'-00_ZH-CN.XML',xml_declaration=True,pretty_print=True,encoding="utf-8")

    
    


