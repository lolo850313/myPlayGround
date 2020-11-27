# path = "d:\\"
from excel import excelout
from lxml import etree
pathBefore = "C:\\Users\\410684\\Desktop\\小程序\\工作\\"
# pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "各种手册dmrl生成\\201812\\"
manualName ="MPD-TP700011-$new$-amm.sgm"


def introCreat(path,manualName):
    formuler = 0   
    tree = etree.parse(path + manualName)

    #读取前言
    intro_all_list = tree.xpath(".//intro")
    intro_list = []
    result = []

    for i in intro_all_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["title"] = i.findtext(".//title")
        
            intro_list.append(dic)
    

    for i in range(len(intro_list)):
        #将所有dmrl信息放入临时字典中
        taskTitle = intro_list[i]["title"]    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = "intro"
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = "00"
        dmrlInfo["SUB-SYS"] = "40"
        dmrlInfo["UNIT"] = "02"
        dmrlInfo["DC"] = "00"
        dmrlInfo["DCV"] = "A"
        dmrlInfo["IC"] = "04F"        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(formuler+2) + ',"-",E'+ str(formuler+2) + ',"-",F'+ str(formuler+2) + ',"-",G'+ str(formuler+2) + ',"-",H'+ str(formuler+2) + ',"-",I'+ str(formuler+2) + ',J'+ str(formuler+2) + ',"-",K'+ str(formuler+2) + ',L'+ str(formuler+2) + ',"-",M'+ str(formuler+2) + ')'
        formuler = formuler + 1
        dmrlInfo["techName"] = ""
        dmrlInfo["infoName"] = ""
        dmrlInfo["KEY"] = ""
        result.append(dmrlInfo)

    #读取chapter
    chapter_all_list = tree.xpath(".//chapter")
    chapter_list = []

    for i in chapter_all_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["title"] = i.findtext(".//title")
        
            chapter_list.append(dic)
    

    for i in range(len(chapter_list)):
        #将所有dmrl信息放入临时字典中
        taskTitle = chapter_list[i]["title"]    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = "CHAPTER-" + chapter_list[i]["chapnbr"]
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = "00"
        dmrlInfo["SUB-SYS"] = "40"
        dmrlInfo["UNIT"] = "02"
        dmrlInfo["DC"] = str(chapter_list[i]["chapnbr"]).zfill(2)
        dmrlInfo["DCV"] = "A"
        dmrlInfo["IC"] = "028"        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(formuler+2) + ',"-",E'+ str(formuler+2) + ',"-",F'+ str(formuler+2) + ',"-",G'+ str(formuler+2) + ',"-",H'+ str(formuler+2) + ',"-",I'+ str(formuler+2) + ',J'+ str(formuler+2) + ',"-",K'+ str(formuler+2) + ',L'+ str(formuler+2) + ',"-",M'+ str(formuler+2) + ')'
        formuler = formuler + 1
        dmrlInfo["techName"] = taskTitle
        dmrlInfo["infoName"] = taskTitle
        dmrlInfo["KEY"] = ""
        result.append(dmrlInfo)

    #读取chapter
    appendix_all_list = tree.xpath(".//appendix")
    appendix_list = []

    for i in appendix_all_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["title"] = i.findtext(".//title")
        
            appendix_list.append(dic)    
    

    for i in range(len(appendix_list)):
        #将所有dmrl信息放入临时字典中
        taskTitle = appendix_list[i]["title"]    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = "APPENDIX-" + appendix_list[i]["appnbr"]
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = "00"
        dmrlInfo["SUB-SYS"] = "40"
        dmrlInfo["UNIT"] = "02"
        dmrlInfo["DC"] = str(i+1).zfill(2)
        dmrlInfo["DCV"] = "A"
        dmrlInfo["IC"] = "04F"        
        dmrlInfo["ICV"] = "A" 
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(formuler+2) + ',"-",E'+ str(formuler+2) + ',"-",F'+ str(formuler+2) + ',"-",G'+ str(formuler+2) + ',"-",H'+ str(formuler+2) + ',"-",I'+ str(formuler+2) + ',J'+ str(formuler+2) + ',"-",K'+ str(formuler+2) + ',L'+ str(formuler+2) + ',"-",M'+ str(formuler+2) + ')'
        formuler = formuler + 1
        dmrlInfo["techName"] = taskTitle
        dmrlInfo["infoName"] = taskTitle
        dmrlInfo["KEY"] = ""
        result.append(dmrlInfo)

    return result

introResult = introCreat(path,manualName)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xls"

excelout(introResult,title,path,filename)

