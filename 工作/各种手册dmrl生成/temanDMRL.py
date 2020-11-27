# path = "d:\\"
from excel import excelout
from lxml import etree
# pathBefore = "C:\\Users\\410684\\Desktop\\小程序\\工作\\"
pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "各种手册dmrl生成\\201812\\"
manualName ="TEMAN-TP700031-$new$-amm.sgm"
#通过ic编码规则excel文档，找出IC+ICV对应infoname的值
icCode = "icCode.xls"

#生成dmrl相关信息
def dmrltabelCreat(path,manualName,icCode):   
    tree = etree.parse(path + manualName)
    import xlrd
    icCode = path + icCode
    data = xlrd.open_workbook(icCode)
    table = data.sheet_by_index(0)
    ruleDic = {}
    for i in range(table.nrows):
        ruleDic[table.cell(i,0).value.strip()] = table.cell(i,1).value.strip()

    #读取task
    sectionList = tree.xpath("//section")

    arjTask = []
    for section in sectionList:
        sectnbr = section.attrib["sectnbr"]
        dc = 1
        for lsheet in section.xpath(".//tlsheet"):
            lsheetList ={}
            toolnbr = lsheet.attrib["toolnbr"]
            lsheetList["sectnbr"] = sectnbr
            lsheetList["dc"] = str(dc).zfill(2)
            lsheetList["toolnbr"] = toolnbr
            lsheetList["title"] = lsheet.findtext(".//title")
            lsheetList["key"] = lsheet.attrib["key"]
            dc = dc + 1
            arjTask.append(lsheetList)

    result = []

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
        dmrlInfo = {}                
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["sectnbr"] +"_"+arjTask[i]["toolnbr"]
        dmrlInfo["title"] = arjTask[i]["title"]
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = arjTask[i]["sectnbr"][:2]
        dmrlInfo["SUB-SYS"] = arjTask[i]["sectnbr"][2:4]
        dmrlInfo["UNIT"] = arjTask[i]["sectnbr"][-2:]
        dmrlInfo["DC"] = arjTask[i]["dc"]
        dmrlInfo["DCV"] = "A"
        dmrlInfo["IC"] = "066"        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(i+2) + ',"-",E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',J'+ str(i+2) + ',"-",K'+ str(i+2) + ',L'+ str(i+2) + ',"-",M'+ str(i+2) + ')'
        dmrlInfo["techName"] = arjTask[i]["title"]
        ic_add_icv = dmrlInfo["IC"] + dmrlInfo["ICV"]
        if ic_add_icv in ruleDic:
            dmrlInfo["infoName"] = ruleDic[ic_add_icv]
        else:
            print(ic_add_icv)
            dmrlInfo["infoName"] = "please add icCode"
            dmrlInfo["infoName"] = "SDS"
        dmrlInfo["KEY"] = arjTask[i]["key"]
        result.append(dmrlInfo)

    return result


dmrlResult = dmrltabelCreat(path,manualName,icCode)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xlsx"

excelout(dmrlResult,title,path,filename)

