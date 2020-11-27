#一览表新增一列，当前dm参引的其他dm
#新增参引关系表， 表头：被参引的DMC，参引的DMC
#aipc名称无法从xml中得到
import os
from lxml import etree
from excel import excelout,excelout2,excelout3
#在当前文件夹下设置输入文件夹input，并将输入文件放入其中
# filePath = __file__[:-21] + "input/"
# print(filePath)
filePath = "D:\\测试\\PDF_PMC-ARJ21-SVV19-20001-02_002-00_ZH-CN_MASTER_FULL\\"
# filePath = "D://测试//PDF_PMC-C919-SVV19-SCYZ0-00_001-00_ZH-CN_MASTER_FULL//"
fileList_origin = os.listdir(filePath)

for i in fileList_origin:
    if i[-5:] == ".xlsx":
        os.remove(filePath + i)
#941文件列表
fileList_origin = os.listdir(filePath)
file941List = []
for i in fileList_origin:
    if i[-3:].lower() == "xml":
        if i.split("-")[-4] == "941A":
            file941List.append(i)

#总表
dataDic2 = []
for fileName in fileList_origin:  
    if fileName[-3:].lower() == "xml" and fileName[:3] == "DMC" and fileName.split("-")[-4] != "941A":
        print(fileName)
        dic = {}
        dic["章节"] = (fileName.split("-")[3])
        dic["DMC"] = fileName[4:34]
        root = etree.parse(filePath + fileName)
        dic["中文名称/英文名称"] = root.find(".//techName").text + " / " +  root.find(".//infoName").text
        # print(dic["中文名称/英文名称"])
        dic["参引层级"] = ""
        dic["被参引次数"] = "1"
        if root.find(".//issueInfo").attrib["inWork"] == "00":
            dic["DM到位状态"] = "ISSUED"
        else:
            dic["DM到位状态"] = "DM未到位"

        dic["对应AIPC模块编码"] =[]
        dic["对应AIPC名称"] = []
        if root.find(".//catalogSeqNumberRef") is not None:
            for i in root.findall(".//catalogSeqNumberRef"):
                if i.attrib["item"] not in dic["对应AIPC名称"]:
                    dic["对应AIPC名称"].append(i.attrib["item"])
        else:
            dic["对应AIPC名称"].append("NA")
            dic["对应AIPC模块编码"].append("NA")
            

            
        dmref_list = root.findall(".//catalogSeqNumberRef/refs/dmRef/dmRefIdent/dmCode")
                
        for j in dmref_list:
            if j.attrib["infoCode"] == "941":
                tmpDmCode = j.attrib["modelIdentCode"] + "-" + j.attrib["systemDiffCode"] + "-" + j.attrib["systemCode"] + "-" + j.attrib["subSystemCode"] + j.attrib["subSubSystemCode"] + "-" + j.attrib["assyCode"] + "-" +j.attrib["disassyCode"] + j.attrib["disassyCodeVariant"] + "-" + j.attrib["infoCode"] + j.attrib["infoCodeVariant"] + "-" + j.attrib["itemLocationCode"]
                if tmpDmCode not in dic["对应AIPC模块编码"]:
                    dic["对应AIPC模块编码"].append(tmpDmCode)
        aipcFilePath = "无法搜到对应的941参引"
        for aipcRef in dic["对应AIPC模块编码"]:
            for file9 in file941List:
                if aipcRef in file9:
                    aipcFilePath = filePath + file9
        dic["备件件号"] = []
        dic["备件件名"] = []
        dic["备件数量"] = []
        if aipcFilePath != "无法搜到对应的941参引":
            root941 = etree.parse(aipcFilePath)     
                
            #备件件号，备件件名，备件数量
            cata_list = root941.findall(".//content/illustratedPartsCatalog/catalogSeqNumber")

            for item in dic["对应AIPC名称"]:
                for cata in cata_list:
                    if cata.attrib["item"] == item:
                        sparesNo_list = cata.findall(".//itemSeqNumber/partRef")
                        for i in (sparesNo_list):
                            dic["备件件号"].append(i.attrib["partNumberValue"])            
                        sparesName_list = cata.findall(".//itemSeqNumber/partSegment/itemIdentData/descrForPart")
                        for i in (sparesName_list):
                            dic["备件件名"].append(i.text)
                        sparesQuantity_list = cata.findall(".//itemSeqNumber/quantityPerNextHigherAssy")
                        for i in (sparesQuantity_list):
                            dic["备件数量"].append(i.text)
            
        dic["单位"] = ""
        dic["备件是否到位"] = ""
        dic["库存状态"] = ""

        #耗材项目号
        supplyRqmtNumber_list = root.findall(".//reqSupplies/supplyDescrGroup/supplyDescr/supplyRqmtRef")
        dic["耗材项目号"] = []
        for i in (supplyRqmtNumber_list):
            dic["耗材项目号"].append(i.attrib["supplyRqmtNumber"])
        #耗材名称
        supplyName_list = root.findall(".//reqSupplies/supplyDescrGroup/supplyDescr/supplyRqmtRef/supplyRqmtSpec/supplyRqmtAlts/supplyRqmt/supplySetGroup/supplySpec/name")
        dic["耗材名称"] = []
        for i in (supplyName_list):
            dic["耗材名称"].append(i.text)
        #耗材规范号
        supplySpecDocument_list = root.findall(".//reqSupplies/supplyDescrGroup/supplyDescr/supplyRqmtRef/supplyRqmtSpec/supplyRqmtAlts/supplyRqmt/specGroup/specDocument")
        dic["耗材规范号"] = []
        for i in (supplySpecDocument_list):
            dic["耗材规范号"].append(i.attrib["specDocumentNumber"])
        #耗材牌号
        supplyIdent_list = root.findall(".//reqSupplies/supplyDescrGroup/supplyDescr/supplyRqmtRef/supplyRqmtSpec/supplyRqmtAlts/supplyRqmt/supplySetGroup/supplySpec/supplyIdent")
        dic["耗材牌号"] = []
        for i in (supplyIdent_list):
            dic["耗材牌号"].append(i.attrib["supplyNumber"])
        dic["耗材库存状态"] = ""
        dic["耗材是否到位"] = ""
        
        #GSE件号
        gseToolNumber_list = root.findall(".//reqSupportEquips/supportEquipDescrGroup/supportEquipDescr/toolSpec/toolIdent")
        dic["GSE件号"] = []
        for i in (gseToolNumber_list):
            dic["GSE件号"].append(i.attrib["toolNumber"])
        #GSE名称
        gseName_list = root.findall(".//reqSupportEquips/supportEquipDescrGroup/supportEquipDescr/toolSpec/itemIdentData/descrForPart")
        dic["GSE名称"] = []
        for i in (gseName_list):
            dic["GSE名称"].append(i.text)
        dic["GSE是否到位"] = ""
        dic["替代GSE件号"] = ""
        dic["替代GSE件名"] = ""
        dic["替代评估表编号"] = ""

        dic["参引"] = []
        contentXml = root.find(".//content")

        #口盖
        accessPointRef_list = root.findall(".//preliminaryRqmts/productionMaintData/workAreaLocationGroup/accessPointRef")
        dic["口盖号"] = []
        dic["口盖名称"] = []
        for i in accessPointRef_list:
            if "changeType" in i.attrib:
                if i.attrib["changeType"] != "delete":
                    dic["口盖号"].append(i.attrib["accessPointNumber"])
                    accessPointName = i.find(".//name").text
                    print(accessPointName)
                    dic["口盖名称"].append(accessPointName)

        #参引dmc
        ref_list = contentXml.findall(".//dmCode")
        #去掉refs
        for dmcode in ref_list:
            changeType = False
            for an in dmcode.iterancestors():
                if "changeType" in an.attrib:
                    if an.attrib["changeType"] == "delete":
                        changeType = True
            if changeType == False:
                dmtitle = dmcode.attrib["modelIdentCode"] + "-" + dmcode.attrib["systemDiffCode"] + "-" + \
                    dmcode.attrib["systemCode"] + "-" + dmcode.attrib["subSystemCode"] + dmcode.attrib["subSubSystemCode"] + "-" + \
                    dmcode.attrib["assyCode"] + "-" + dmcode.attrib["disassyCode"] + dmcode.attrib["disassyCodeVariant"] + "-" +  \
                    dmcode.attrib["infoCode"]+dmcode.attrib["infoCodeVariant"] + "-" + dmcode.attrib["itemLocationCode"]
                dic["参引"].append(dmtitle)
            else:
                dmtitle = dmcode.attrib["modelIdentCode"] + "-" + dmcode.attrib["systemDiffCode"] + "-" + \
                    dmcode.attrib["systemCode"] + "-" + dmcode.attrib["subSystemCode"] + dmcode.attrib["subSubSystemCode"] + "-" + \
                    dmcode.attrib["assyCode"] + "-" + dmcode.attrib["disassyCode"] + dmcode.attrib["disassyCodeVariant"] + "-" +  \
                    dmcode.attrib["infoCode"]+dmcode.attrib["infoCodeVariant"] + "-" + dmcode.attrib["itemLocationCode"]

    
        dataDic2.append(dic)

title2 = ["章节","DMC","中文名称/英文名称","参引层级","被参引次数","DM到位状态","对应AIPC模块编码","对应AIPC名称","备件件号","备件件名","备件数量","单位","备件是否到位","耗材项目号","耗材名称","耗材规范号","耗材牌号","耗材库存状态","耗材是否到位","GSE件号","GSE名称","GSE是否到位","替代GSE件号","替代GSE件名","替代评估表编号","参引","口盖号","口盖名称"]

#耗材表
title3 = ["耗材规范号","耗材库存状态","耗材是否到位","DMC","DM到位状态"]
dataDic3 = {}
for i in dataDic2:
    for j in i["耗材规范号"]:
        if j not in dataDic3:
            dataDic3[j] = {"耗材规范号":i["耗材规范号"],"耗材库存状态":i["耗材库存状态"],"耗材是否到位":i["耗材是否到位"],"DMC":[i["DMC"]],"DM到位状态":[i["DM到位状态"]]}
        else:
            dataDic3[j]["DMC"].append(i["DMC"])
            dataDic3[j]["DM到位状态"].append(i["DM到位状态"])

#备件表
title4 = ["备件件号","备件件名","备件数量","单位","库存状态","DMC","DM到位状态"]
dataDic4 = {}
for i in dataDic2:
    for j in i["备件件号"]:
        if j not in dataDic4:
            dataDic4[j] = {"备件件号":j,"备件件名":i["备件件名"][i["备件件号"].index(j)],"备件数量":i["备件数量"][i["备件件号"].index(j)],"单位":i["单位"],"库存状态":i["库存状态"],"DMC":[i["DMC"]],"DM到位状态":[i["DM到位状态"]]}
        else:
            dataDic4[j]["DMC"].append(i["DMC"])
            dataDic4[j]["DM到位状态"].append(i["DM到位状态"])

#GSE表
title5 = ["GSE件号","GSE名称","GSE是否到位","替代GSE件号","替代GSE件名","替代评估表编号","DMC","DM到位状态"]
dataDic5 = {}
for i in dataDic2:
    for j in i["GSE件号"]:
        if j not in dataDic5:
            dataDic5[j] = {"GSE件号":j,"GSE名称":i["GSE名称"][i["GSE件号"].index(j)],"GSE是否到位":i["GSE是否到位"],"替代GSE件号":i["替代GSE件号"],"替代GSE件名":i["替代GSE件名"],"替代评估表编号":i["替代评估表编号"],"DMC":[i["DMC"]],"DM到位状态":[i["DM到位状态"]]}
        else:
            dataDic5[j]["DMC"].append(i["DMC"])
            dataDic5[j]["DM到位状态"].append(i["DM到位状态"])

#参引关系表
title6 = ["被参引的DMC","参引的DMC"]
dataDic6 = {}
for i in dataDic2:
    for j in i["参引"]:
        if j not in dataDic6:
            dataDic6[j] = {"被参引的DMC" : j, "参引的DMC" : [i["DMC"]]}
        else:
            if i["DMC"] not in dataDic6[j]["参引的DMC"]:
                if len(dataDic6[j]["参引的DMC"]) <= 220:
                    dataDic6[j]["参引的DMC"].append(i["DMC"])
        
#口盖表
title7 = ["口盖号", "口盖名称", "参引的DMC"]
dataDic7 = {}
for i in dataDic2:
    for j in range(len(i["口盖号"])):
        if i["口盖号"][j] not in dataDic7:
            dataDic7[i["口盖号"][j]] = {"口盖号" : i["口盖号"][j], "口盖名称" : i["口盖名称"][j], "参引的DMC":[i["DMC"]]}
        else:
            if i["DMC"] not in dataDic7[i["口盖号"][j]]["参引的DMC"]:
                dataDic7[i["口盖号"][j]]["参引的DMC"].append(i["DMC"])

excelout(dataDic2,title2,filePath,"前置条件一览表.xlsx")
excelout2(dataDic3,title3,filePath,"消耗品信息反馈表.xlsx")
excelout2(dataDic4,title4,filePath,"备件状态反馈表.xlsx")
excelout2(dataDic5,title5,filePath,"GSE信息反馈表.xlsx")
excelout2(dataDic6,title6,filePath,"参引关系表.xlsx")
excelout2(dataDic7,title7,filePath,"口盖参引关系表.xlsx")