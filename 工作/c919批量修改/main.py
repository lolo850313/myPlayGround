from lxml import etree
import xlrd
import os

path = "D:\\测试\\C919批量更改\\导出XML\\"
# path = "D:\\测试\\C919批量更改\\test\\"
resPath = "D:\\测试\\C919批量更改\\导出xml结果\\"
excelPath = "D:\\测试\\C919批量更改\\c919批量修改.xlsx"
#根据输入修改ref
changeDic = {}
shet = xlrd.open_workbook(excelPath).sheets()[0]
row = shet.nrows
for i in range(1,row):
    changeDic[shet.cell_value(i,0)] = shet.cell_value(i,1)

for filename in os.listdir(path):
    file = path + filename
    root = etree.parse(file)
    # print(filename)

    #处理commonInfo
    sequentialList = root.findall(".//commonInfoDescrPara/para/sequentialList")
    for seq in (sequentialList):
        paraArr = seq.findall("listItem/para")
        commonInfoDescrPara_parent = seq.getparent().getparent().getparent()
        for i in paraArr:
            alts = etree.SubElement(commonInfoDescrPara_parent,"commonInfoDescrParaAlts")
            commonInfoDescrPara = etree.SubElement(alts,"commonInfoDescrPara")
            commonInfoDescrPara.append(i)
        
        commonInfoDescrPara_old = seq.getparent().getparent()
        commonInfoDescrPara_parent.remove(commonInfoDescrPara_old)
    

    #处理step
    isolationMainProcedure = root.find(".//isolationMainProcedure")
    if isolationMainProcedure != None:
        for step in isolationMainProcedure:
            if step.tag == "isolationProcedureEnd":
                stepId = step.attrib["id"]
                stepAlts = etree.Element("isolationProcedureEndAlts")
                stepAlts.set("id", stepId)
                step.set("id", stepId + "-1")
                stepAlts.append(step)
                # isolationMainProcedure.remove(step)
                isolationMainProcedure.append(stepAlts)
            if step.tag == "isolationStep":
                stepId = step.attrib["id"]
                stepAlts = etree.Element("isolationStepAlts")
                stepAlts.set("id", stepId)
                step.set("id", stepId + "-1")
                stepAlts.append(step)
                isolationMainProcedure.append(stepAlts)

        #根据输入修改ref
        dmcodeArr = root.findall(".//dmCode")
        for code in dmcodeArr:
            dmrl = code.attrib["modelIdentCode"]  + "-" + code.attrib["systemDiffCode"]  + "-"\
                + code.attrib["systemCode"]  + "-" +code.attrib["subSystemCode"]  +\
                code.attrib["subSubSystemCode"]  + "-" +code.attrib["assyCode"]  + "-"\
                + code.attrib["disassyCode"] +code.attrib["disassyCodeVariant"]  + "-"\
                + code.attrib["infoCode"] +code.attrib["infoCodeVariant"]\
                + "-" +code.attrib["itemLocationCode"]
            if dmrl in changeDic:
                dmrlTo = changeDic[dmrl]
                code.attrib["modelIdentCode"] = dmrlTo[0:4]
                code.attrib["systemDiffCode"] = dmrlTo[5]
                code.attrib["systemCode"] = dmrlTo[7:9]
                code.attrib["subSystemCode"] = dmrlTo[10]
                code.attrib["subSubSystemCode"] = dmrlTo[11]
                code.attrib["assyCode"] = dmrlTo[13:15]
                code.attrib["disassyCode"] = dmrlTo[16:18]
                code.attrib["disassyCodeVariant"] = dmrlTo[18]
                code.attrib["infoCode"] = dmrlTo[20:23]
                code.attrib["infoCodeVariant"] = dmrlTo[23]
                code.attrib["itemLocationCode"] = dmrlTo[25]
                dmrl = code.attrib["modelIdentCode"]  + "-" + code.attrib["systemDiffCode"]  + "-"\
                + code.attrib["systemCode"]  + "-" +code.attrib["subSystemCode"]  +\
                code.attrib["subSubSystemCode"]  + "-" +code.attrib["assyCode"]  + "-"\
                + code.attrib["disassyCode"] +code.attrib["disassyCodeVariant"]  + "-"\
                + code.attrib["infoCode"] +code.attrib["infoCodeVariant"]\
                + "-" +code.attrib["itemLocationCode"]

        #处理表格
        tableArr = root.findall(".//table")
        for table in tableArr:
            if table is not None:
                action = table.getprevious()
                
                # 表格是否需要处理
                tableHasIrrt = False
                rowArr = table.findall(".//row")
                internalRefArr = table.findall(".//internalRef")
                for internalRef in internalRefArr:
                    if (internalRef.attrib["internalRefTargetType"]) == "irtt56":
                        tableHasIrrt = True
                        # 需要添加到internalRef中的para标签
                        internalRef_Para = internalRef.getparent().getparent().getnext()[0]
                        quantityValue = internalRef_Para.find(".//quantityValue")
                        if quantityValue is not None:
                            quantityValue_text = quantityValue.text
                            if "quantityUnitOfMeasure" not in quantityValue.attrib:
                                print(filename)
                                internalRef_Para_text = "需要手动添加"
                            else:
                                quantityUnitOfMeasure = quantityValue.attrib["quantityUnitOfMeasure"]
                                internalRef_Para_text = quantityValue.text + " " +quantityUnitOfMeasure
                        else:
                            internalRef_Para_text = internalRef_Para.text

                        internalRef_Para_id = internalRef.attrib["internalRefId"]

                        internalRef_insert = etree.Element("internalRef")
                        internalRef_insert.attrib["internalRefId"] = internalRef_Para_id
                        internalRef_insert.attrib["internalRefTargetType"] = "irtt56"
                        internalRef_insert.text = internalRef_Para_text
                        action.append(internalRef_insert)

                if tableHasIrrt == True:
                    table.getparent().remove(table)

                        
        root.write(resPath + filename,xml_declaration=True,pretty_print=True,encoding="utf-8")