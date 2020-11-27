#将任务参引替换掉919能识别的tag，AMM，FIM，AWM。不能识别的使用	

def dmrlRef_modify(dirPath):
    def amm_dmref(xmlFile,amm_dmrlTable):
        def dashModify(dmcString):
            dmcString = dmcString.replace("−","-")
            dmcString = dmcString.replace("–","-")
            return dmcString

        import xlrd
        from lxml import etree
        import re

        book = xlrd.open_workbook(amm_dmrlTable)
        sheet = book.sheet_by_index(0)
        nrow = sheet.nrows
        task = etree.parse(xmlFile)
        strRe = r'AMM\s{0,1}[TtAaSsKk]{0,4}[：:]{0,1}\s{0,2}[0-9]{2}[−–-][0-9]{2}[−–-][0-9]{2}[−–-][0-9]{3}[−–-][0-9]{3}'
        
        for i in task.xpath(".//para"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AMM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//action"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AMM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//title"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AMM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//notePara"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AMM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]
        #task本身就是elementtree，可以使用write方法写入xml文件。
        #而etree.ElementTree(something)是将something转换为elementtree后，变可以写入xml文件。
        task.write(xmlFile,xml_declaration=True,pretty_print=True,encoding="utf-8")

    def fim_dmref(xmlFile,fim_dmrlTable):
        import xlrd
        from lxml import etree
        import re

        book = xlrd.open_workbook(fim_dmrlTable)
        sheet = book.sheet_by_index(0)
        nrow = sheet.nrows
        task = etree.parse(xmlFile)
        strRe = r'FIM\s{0,1}[TtAaSsKk]{0,4}[：:]{0,1}\s{0,2}[0-9]{2}[−–-][0-9]{2}[−–-][0-9]{2}[−–-][0-9]{3}[−–-][0-9]{3}'

        for i in task.xpath(".//para"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>FIM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 3).value)
                            systemDiffCode = (sheet.cell(row, 4).value)
                            systemCode = (sheet.cell(row, 5).value)
                            subSystemCode = (sheet.cell(row, 6).value)[0]
                            subSubSystemCode = (sheet.cell(row, 6).value)[1]
                            assyCode = (sheet.cell(row, 7).value)
                            disassyCode = (sheet.cell(row, 8).value)
                            disassyCodeVariant = (sheet.cell(row, 9).value)
                            infoCode = (sheet.cell(row, 10).value)
                            infoCodeVariant = (sheet.cell(row, 11).value)
                            itemLocationCode = (sheet.cell(row, 12).value)
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//action"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>FIM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//title"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>FIM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//notePara"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>FIM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 13).value)[:5]
                            systemDiffCode = (sheet.cell(row, 13).value)[6]
                            systemCode = (sheet.cell(row, 13).value)[8:10]
                            subSystemCode = (sheet.cell(row, 13).value)[11]
                            subSubSystemCode = (sheet.cell(row, 13).value)[12]
                            assyCode = (sheet.cell(row, 13).value)[14:16]
                            disassyCode = (sheet.cell(row, 13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row, 13).value)[-8]
                            infoCode = (sheet.cell(row, 13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row, 13).value)[-3]
                            itemLocationCode = (sheet.cell(row, 13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        task.write(xmlFile,xml_declaration=True,pretty_print=True,encoding="utf-8")


    def awm_dmref(xmlFile,awm_dmrlTable):
        import xlrd
        from lxml import etree
        import re

        book = xlrd.open_workbook(awm_dmrlTable)
        sheet = book.sheet_by_index(0)
        nrow = sheet.nrows
        task = etree.parse(xmlFile)
        strRe = r'AWM\s{0,2}[0-9]{2}[−–-][0-9]{2}[−–-][0-9]{2}'

        for i in task.xpath(".//para"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-8:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AWM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 3).value)
                            systemDiffCode = (sheet.cell(row, 4).value)
                            systemCode = (sheet.cell(row, 5).value)
                            subSystemCode = (sheet.cell(row, 6).value)[0]
                            subSubSystemCode = (sheet.cell(row, 6).value)[1]
                            assyCode = (sheet.cell(row, 7).value)
                            disassyCode = (sheet.cell(row, 8).value)
                            disassyCodeVariant = (sheet.cell(row, 9).value)
                            infoCode = (sheet.cell(row, 10).value)
                            infoCodeVariant = (sheet.cell(row, 11).value)
                            itemLocationCode = (sheet.cell(row, 12).value)
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//action"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-8:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AWM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 3).value)
                            systemDiffCode = (sheet.cell(row, 4).value)
                            systemCode = (sheet.cell(row, 5).value)
                            subSystemCode = (sheet.cell(row, 6).value)[0]
                            subSubSystemCode = (sheet.cell(row, 6).value)[1]
                            assyCode = (sheet.cell(row, 7).value)
                            disassyCode = (sheet.cell(row, 8).value)
                            disassyCodeVariant = (sheet.cell(row, 9).value)
                            infoCode = (sheet.cell(row, 10).value)
                            infoCodeVariant = (sheet.cell(row, 11).value)
                            itemLocationCode = (sheet.cell(row, 12).value)
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//title"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-8:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AWM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 3).value)
                            systemDiffCode = (sheet.cell(row, 4).value)
                            systemCode = (sheet.cell(row, 5).value)
                            subSystemCode = (sheet.cell(row, 6).value)[0]
                            subSubSystemCode = (sheet.cell(row, 6).value)[1]
                            assyCode = (sheet.cell(row, 7).value)
                            disassyCode = (sheet.cell(row, 8).value)
                            disassyCodeVariant = (sheet.cell(row, 9).value)
                            infoCode = (sheet.cell(row, 10).value)
                            infoCodeVariant = (sheet.cell(row, 11).value)
                            itemLocationCode = (sheet.cell(row, 12).value)
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        for i in task.xpath(".//notePara"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-8:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AWM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 3).value)
                            systemDiffCode = (sheet.cell(row, 4).value)
                            systemCode = (sheet.cell(row, 5).value)
                            subSystemCode = (sheet.cell(row, 6).value)[0]
                            subSubSystemCode = (sheet.cell(row, 6).value)[1]
                            assyCode = (sheet.cell(row, 7).value)
                            disassyCode = (sheet.cell(row, 8).value)
                            disassyCodeVariant = (sheet.cell(row, 9).value)
                            infoCode = (sheet.cell(row, 10).value)
                            infoCodeVariant = (sheet.cell(row, 11).value)
                            itemLocationCode = (sheet.cell(row, 12).value)
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]

        task.write(xmlFile,xml_declaration=True,pretty_print=True,encoding="utf-8")
    
    #替换断路器文字为标签
    def cb_dmref(xmlFile):
        from lxml import etree
        import re

        task = etree.parse(xmlFile)
        strRe = r'[B][1][−–-][0-9]{4}'

        for i in task.xpath(".//para"):
            if i.text is not None:
                if  "断开断路器" in i.text or "取下断路器" in i.text or "重置断路器" in i.text or "闭合断路器" in i.text or "确认断路器" in i.text:
                    xmlList = []
                    itext = i.text
                    for cbText in (re.findall(strRe, itext)):
                        xmlList.append(cbText)
                    if len(xmlList)!=0:
                        cur = xmlList.pop(-1)
                        xmlList.insert(0,cur)
                        for num in range(len(xmlList)):                   
                            replaceXml = etree.Element("circuitBreakerRef")
                            replaceXml.set("circuitBreakerNumber", xmlList[num])
                            # print(xmlList[num])
                            #i为para元素,为了使circuitBreakerNumber后置，
                            i.insert(-1, replaceXml)

        for i in task.xpath(".//action"):
            if i.text is not None:
                if  "断开断路器" in i.text or "取下断路器" in i.text or "重置断路器" in i.text or "闭合断路器" in i.text or "确认断路器" in i.text:
                    xmlList = []
                    itext = i.text
                    for cbText in (re.findall(strRe, itext)):
                        xmlList.append(cbText)
                    if len(xmlList)!=0:
                        cur = xmlList.pop(-1)
                        xmlList.insert(0,cur)
                        for num in range(len(xmlList)):                   
                            replaceXml = etree.Element("circuitBreakerRef")
                            replaceXml.set("circuitBreakerNumber", xmlList[num])
                            # print(xmlList[num])
                            #i为para元素,为了使circuitBreakerNumber后置，
                            i.insert(-1, replaceXml)
        
        task.write(xmlFile,xml_declaration=True,pretty_print=True,encoding="utf-8")

    
    def fimInTable_dmref(xmlFile,fim_dmrlTable):
        import xlrd
        from lxml import etree
        import re

        book = xlrd.open_workbook(fim_dmrlTable)
        sheet = book.sheet_by_index(0)
        nrow = sheet.nrows
        task = etree.parse(xmlFile)
        strRe = r'[0-9]{2}[−–-][0-9]{2}[−–-][0-9]{2}[−–-][0-9]{3}[−–-][0-9]{3}'

        for i in task.xpath(".//entry/para"):
            if i.text != None:
                xmlList = []
                strList = []
                itext = i.text
                for ammtask in (re.findall(strRe, itext)):
                    xmlList.append(ammtask)

                for curRef in xmlList:
                    curIndex = itext.index(curRef)
                    strList.append(itext[:curIndex])
                    itext = itext[(curIndex + len(curRef)):]
                strList.append(itext)
                i.text = strList[0]
                for num in range(len(xmlList)):
                    taskNo = xmlList[num][-16:].replace("−","-").replace("–","-").strip()
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>FIM</externalPubCode><externalPubTitle>" + taskNo + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row, 1).value == taskNo:
                            modelIdentCode = (sheet.cell(row, 3).value)
                            systemDiffCode = (sheet.cell(row, 4).value)
                            systemCode = (sheet.cell(row, 5).value)
                            subSystemCode = (sheet.cell(row, 6).value)[0]
                            subSubSystemCode = (sheet.cell(row, 6).value)[1]
                            assyCode = (sheet.cell(row, 7).value)
                            disassyCode = (sheet.cell(row, 8).value)
                            disassyCodeVariant = (sheet.cell(row, 9).value)
                            infoCode = (sheet.cell(row, 10).value)
                            infoCodeVariant = (sheet.cell(row, 11).value)
                            itemLocationCode = (sheet.cell(row, 12).value)
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="' + modelIdentCode + '" systemDiffCode="' + systemDiffCode + '" systemCode="' + systemCode + '" subSystemCode="' + subSystemCode + '" subSubSystemCode="' + subSubSystemCode + '" assyCode="' + assyCode + '" disassyCode="' + disassyCode + '" disassyCodeVariant="' + disassyCodeVariant + '" infoCode="' + infoCode + '" infoCodeVariant="' + infoCodeVariant + '" itemLocationCode="' + itemLocationCode + '"/></dmRefIdent></dmRef>'
                    replaceXml = etree.fromstring(dmcString)
                    i.insert(-1,replaceXml)
                    replaceXml.tail = strList[num + 1]


        task.write(xmlFile,xml_declaration=True,pretty_print=True,encoding="utf-8")
    
    import os
    exPath = "D:/测试/s1000d/s1000d_fim/"
    amm_dmrlTable = exPath + "副本AMM-TP700004-02-$new$-amm-dmrl20191101.xlsx"
    fim_dmrlTable = exPath + "ARJFRMFIM-TP700018A-DMRL-2019.9-汇总.xlsx"
    awm_dmrlTable = exPath + "WM-TP700015-$new$-amm-dmrl.xlsx"
    for i in os.listdir(dirPath):
        
        xmlFile = dirPath + i
        if xmlFile[-4:] == ".xml" or xmlFile[-4:] == ".XML":      
            amm_dmref(xmlFile,amm_dmrlTable)
            fim_dmref(xmlFile,fim_dmrlTable)
            awm_dmref(xmlFile,awm_dmrlTable)
            fimInTable_dmref(xmlFile,fim_dmrlTable)
            cb_dmref(xmlFile)



if __name__ == "__main__":
    dmrlRef_modify("D:\\测试\\s1000d\\s1000d_fim\\split_To\\")
    print("refReplace finish")