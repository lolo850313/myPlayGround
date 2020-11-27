# path = "d:\\"
from excel import excelout
from lxml import etree
pathBefore = "D:\\程序源数据\\手册\\201912\\"
# pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "dmrl\\"
res= "dmrlExcel\\"
manualName ="AIPC-TP700016-$new$-amm(201912).sgm"

#生成dmrl相关信息
def dmrltabelCreat(path,manualName):   
    tree = etree.parse(path + manualName)

    #读取task
    task_list = tree.xpath("//figure")
    arjTask = []
    for i in task_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["title"] = i.findtext(".//title")
            arjTask.append(dic)

    result = []

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
        taskTitle = arjTask[i]["title"]    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["chapnbr"] +"-"+arjTask[i]["sectnbr"] +"-"+ arjTask[i]["unitnbr"] + "-"+arjTask[i]["fignbr"]
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = arjTask[i]["chapnbr"]
        dmrlInfo["SUB-SYS"] = arjTask[i]["sectnbr"]
        dmrlInfo["UNIT"] = arjTask[i]["unitnbr"]
        dmrlInfo["DC"] = arjTask[i]["fignbr"][:2]
        if len(arjTask[i]["fignbr"]) > 2:
            rule = {"a":"B","A":"B","B":"C","C":"D","D":"E","E":"F","F":"G","G":"H","H":"I","I":"J","J":"K","K":"L"}
            if arjTask[i]["fignbr"][2] in rule:
                dmrlInfo["DCV"] =rule[arjTask[i]["fignbr"][2]]
            else:
                print(arjTask[i])
                print(arjTask[i]["fignbr"][2])
        else:
            dmrlInfo["DCV"] = "A"
        dmrlInfo["IC"] = "941"        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(i+2) + ',"-",E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',J'+ str(i+2) + ',"-",K'+ str(i+2) + ',L'+ str(i+2) + ',"-",M'+ str(i+2) + ')'
        dmrlInfo["techName"] = taskTitle
        dmrlInfo["infoName"] = "图解零件目录"
        dmrlInfo["KEY"] = arjTask[i]["key"]
        result.append(dmrlInfo)
    return result

dmrlResult = dmrltabelCreat(path,manualName)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xls"

excelout(dmrlResult,title,pathBefore + res,filename)

