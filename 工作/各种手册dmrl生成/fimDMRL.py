# path = "d:\\"
from excel import excelout
from lxml import etree
# pathBefore = "C:\\Users\\410684\\Desktop\\小程序\\工作\\"
pathBefore = "/Users/hewenhao/测试/"
path = pathBefore
manualName ="ARJFRMFIM-TP700018A-$new$-amm(201903).sgm"
#通过ic编码规则excel文档，找出IC+ICV对应infoname的值
icCode = "icCode.xls"

#生成dmrl相关信息
def dmrltabelCreat(path,manualName,icCode):   
    tree = etree.parse(path + manualName)

    #读取task
    task_list = tree.xpath("//task")
    arjTask = []

    import xlrd
    icCode = path + icCode
    data = xlrd.open_workbook(icCode)
    table = data.sheet_by_index(0)
    ruleDic = {}
    for i in range(table.nrows):
        ruleDic[table.cell(i,0).value.strip()] = table.cell(i,1).value.strip()
    #将task的title录入字典
    for i in task_list:
        #避免有些task被删除，没有title,导致dic的title为none
        if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["title"] = i.findtext(".//title")
            arjTask.append(dic)

    result = []

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
        taskTitle = arjTask[i]["title"]
        if "—" in taskTitle:
            techName = taskTitle.split("—")[0]
        if arjTask[i]["pgblknbr"]=="2":
            infoName = "故障隔离程序"
        else:
            infoName = "任务支持"
    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["chapnbr"] +"-"+arjTask[i]["sectnbr"] +"-"+ arjTask[i]["subjnbr"] + "-"+arjTask[i]["func"] + "-"+arjTask[i]["seq"]
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = arjTask[i]["chapnbr"]
        dmrlInfo["S-SYS"] = arjTask[i]["sectnbr"]
        dmrlInfo["SUB"] = arjTask[i]["subjnbr"]
        dmrlInfo["DC"] = "dc"
        if "confltr" in arjTask[i]:
            dmrlInfo["DCV"] = (arjTask[i]["confltr"])
        else:
            dmrlInfo["DCV"] = "A"
        if arjTask[i]["pgblknbr"] == "2":
            dmrlInfo["IC"] = "421"
        else:
            dmrlInfo["IC"] = "430"        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        #dmc的值写成vb公式
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(i+2) + ',"-",E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',J'+ str(i+2) + ',"-",K'+ str(i+2) + ',L'+ str(i+2) + ',"-",M'+ str(i+2) + ')'
        dmrlInfo["techName"] = techName
        ic_add_icv = dmrlInfo["IC"] + dmrlInfo["ICV"]
        if ic_add_icv in ruleDic:
            dmrlInfo["infoName"] = ruleDic[ic_add_icv]
        else:
            print(ic_add_icv)
            dmrlInfo["infoName"] = "please add icCode"
            dmrlInfo["infoName"] = "SDS"
        dmrlInfo["KEY"] = arjTask[i]["key"]

        result.append(dmrlInfo)

    #修改dc号，当s-sys值不等于当前s-sys值时，dc流水号重置为0，等于时dc流水号递增。
    tmpSSYS = ""
    dcNum = 1
    for i in result:
        if tmpSSYS != i["S-SYS"]:
            tmpSSYS = i["S-SYS"]
            dcNum = 1
            #dc流水号补全两位
            i["DC"] = str(dcNum).zfill(2)
        else:
            dcNum = dcNum + 1
            i["DC"] = str(dcNum).zfill(2)
    return result

dmrlResult = dmrltabelCreat(path,manualName,icCode)
title = ["index","Task NO.","title","MI","SDC","SYS","S-SYS","SUB","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xlsx"

excelout(dmrlResult,title,path,filename)

