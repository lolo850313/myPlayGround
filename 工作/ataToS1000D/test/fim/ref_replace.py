#AWM未处理
#将任务参引替换掉919能识别的tag，AMM，FIM，AWM。不能识别的使用	
# <externalPubRef><externalPubRefIdent><externalPubCode>"***"</externalPubCode><externalPubTitle>"***"</externalPubTitle></externalPubRefIdent></externalPubRef>
def dmrlRef_modify(dirPath):
    def amm_dmref(xmlFile,amm_dmrlTable):
        import xlrd
        from lxml import etree
        import re

        book = xlrd.open_workbook(amm_dmrlTable)
        sheet = book.sheet_by_index(0)
        nrow = sheet.nrows
        task = etree.parse(xmlFile)
        strRe = r'AMM\s{1}TASK\s{1}[0-9]{2}[-][0-9]{2}[-][0-9]{2}[-][0-9]{3}[-][0-9]{3}'
        
        for i in task.xpath(".//para"):
            if i.text != None:
                for ammtask in (re.findall(strRe,i.text)):
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>AMM</externalPubCode><externalPubTitle>"+ ammtask[9:] + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    for row in range(nrow):
                        if sheet.cell(row,1).value == ammtask[9:]:
                            modelIdentCode = (sheet.cell(row,13).value)[:5]
                            systemDiffCode = (sheet.cell(row,13).value)[6]
                            systemCode = (sheet.cell(row,13).value)[8:10]
                            subSystemCode = (sheet.cell(row,13).value)[11]
                            subSubSystemCode = (sheet.cell(row,13).value)[12]
                            assyCode = (sheet.cell(row,13).value)[14:16]
                            disassyCode= (sheet.cell(row,13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row,13).value)[-8]
                            infoCode = (sheet.cell(row,13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row,13).value)[-3]
                            itemLocationCode = (sheet.cell(row,13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="'+modelIdentCode+'" systemDiffCode="'+systemDiffCode+'" systemCode="'+systemCode+'" subSystemCode="'+subSystemCode+'" subSubSystemCode="'+subSubSystemCode+'" assyCode="'+assyCode+'" disassyCode="'+disassyCode+'" disassyCodeVariant="'+disassyCodeVariant+'" infoCode="'+infoCode+'" infoCodeVariant="'+infoCodeVariant+'" itemLocationCode="'+itemLocationCode+'"/></dmRefIdent></dmRef>'
                    replaceString =etree.fromstring(dmcString)
                    textBefore = i.text.find(ammtask)
                    textTail = i.text[textBefore + len(ammtask):]                    
                    i.text = i.text[:textBefore]
                    i.append(replaceString)
                    replaceString.tail = textTail

        #task本身就是elementtree，可以使用write方法写入xml文件。
        #而etree.ElementTree(something)是将something转换为elementtree后，变可以写入xml文件。
        task.write(xmlFile,pretty_print=True,encoding="utf-8")

    def fim_dmref(xmlFile,fim_dmrlTable):
        import xlrd
        from lxml import etree
        import re

        book = xlrd.open_workbook(fim_dmrlTable)
        sheet = book.sheet_by_index(0)
        nrow = sheet.nrows
        task = etree.parse(xmlFile)
        strRe = r'FIM\s{1}TASK\s{1}[0-9]{2}[-][0-9]{2}[-][0-9]{2}[-][0-9]{3}[-][0-9]{3}'

        for i in task.xpath(".//para"):
            if i.text != None:
                for fim in (re.findall(strRe,i.text)):
                    dmcString = "<externalPubRef><externalPubRefIdent><externalPubCode>FIM</externalPubCode><externalPubTitle>"+ fim[9:] + "</externalPubTitle></externalPubRefIdent></externalPubRef>"
                    #遍历amm表格，如果表格
                    for row in range(nrow):
                        if fim[9:] == sheet.cell(row,1).value:
                            modelIdentCode = (sheet.cell(row,13).value)[:5]
                            systemDiffCode = (sheet.cell(row,13).value)[6]
                            systemCode = (sheet.cell(row,13).value)[8:10]
                            subSystemCode = (sheet.cell(row,13).value)[11]
                            subSubSystemCode = (sheet.cell(row,13).value)[12]
                            assyCode = (sheet.cell(row,13).value)[14:16]
                            disassyCode= (sheet.cell(row,13).value)[17:19]
                            disassyCodeVariant = (sheet.cell(row,13).value)[-8]
                            infoCode = (sheet.cell(row,13).value)[-6:-3]
                            infoCodeVariant = (sheet.cell(row,13).value)[-3]
                            itemLocationCode = (sheet.cell(row,13).value)[-1]
                            dmcString = '<dmRef><dmRefIdent><dmCode modelIdentCode="'+modelIdentCode+'" systemDiffCode="'+systemDiffCode+'" systemCode="'+systemCode+'" subSystemCode="'+subSystemCode+'" subSubSystemCode="'+subSubSystemCode+'" assyCode="'+assyCode+'" disassyCode="'+disassyCode+'" disassyCodeVariant="'+disassyCodeVariant+'" infoCode="'+infoCode+'" infoCodeVariant="'+infoCodeVariant+'" itemLocationCode="'+itemLocationCode+'"/></dmRefIdent></dmRef>'
                    replaceString =etree.fromstring(dmcString)
                    textBefore = i.text.find(fim)
                    textTail = i.text[textBefore + len(fim):]
                    i.text = i.text[:textBefore]
                    i.append(replaceString)
                    replaceString.tail = textTail

        task.write(xmlFile,pretty_print=True,encoding="utf-8")

    import os

    amm_dmrlTable = dirPath[:-10] + "amm-dmrlTable.xls"
    fim_dmrlTable = dirPath[:-10] + "ARJFRMFIM_TSN20-dmrl.xls"
    for i in os.listdir(dirPath):
        xmlFile = dirPath + i
        if xmlFile[-4:] == ".XML":       
            amm_dmref(xmlFile,amm_dmrlTable)
            fim_dmref(xmlFile,fim_dmrlTable)

if __name__ == "__main__":
    dmrlRef_modify("/Users/hewenhao/测试")