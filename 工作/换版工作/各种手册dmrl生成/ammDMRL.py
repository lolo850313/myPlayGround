#IC规则可能有问题，应该是最后横线后的部分

# path = "d:\\"
from excel import excelout
from lxml import etree
pathBefore = "D:\\程序源数据\\手册\\201909\\"
# pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "dmrl\\"
res= "dmrlExcel\\"
icCode = "icCode.xls"
mppRule = "mppRule.xlsx"
manualName ="AMM-TP700004-02-$new$-amm.sgm"

#生成dmrl相关信息
def dmrltabelCreat(path,manualName,icCode,mppRule):
    import xlrd
    icCode = path + icCode
    data = xlrd.open_workbook(icCode)
    table = data.sheet_by_index(0)
    ruleDic = {}
    for i in range(table.nrows):
        ruleDic[table.cell(i,0).value.strip()] = table.cell(i,1).value.strip()

    mppIcCode = path + mppRule
    mppdata = xlrd.open_workbook(mppIcCode)
    mpptable = mppdata.sheet_by_index(0)
    mppruleDic = {}
    for i in range(mpptable.nrows):
        mppruleDic[mpptable.cell(i,0).value.strip()] = mpptable.cell(i,1).value.strip()

    tree = etree.parse(path + manualName)

    #读取task
    task_list = tree.xpath(".//task")
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
        dmrlInfo["Task NO."] = arjTask[i]["chapnbr"] +"-"+arjTask[i]["sectnbr"] +"-"+ arjTask[i]["subjnbr"] + "-"+arjTask[i]["func"]+ "-"+arjTask[i]["seq"]
        if "confltr" in arjTask[i]:
            if arjTask[i]["confltr"] != "":
                dmrlInfo["Task NO."] = dmrlInfo["Task NO."] +"-"+arjTask[i]["confltr"]
        if "varnbr" in arjTask[i]:
            if arjTask[i]["varnbr"] != "":
                dmrlInfo["Task NO."] = dmrlInfo["Task NO."] +"-"+arjTask[i]["varnbr"]
        dmrlInfo["title"] = taskTitle        
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = arjTask[i]["chapnbr"]
        dmrlInfo["SUB-SYS"] = arjTask[i]["sectnbr"]
        dmrlInfo["UNIT"] = arjTask[i]["subjnbr"]
        dmrlInfo["DC"] = str(int(arjTask[i]["seq"][-2:])-1).zfill(2)
        dmrlInfo["DCV"] = "A"
        #取的前面的部分，会出现标题误删除的情况，需要章节人员自行检查修改
        func = arjTask[i]["func"]
        if func in mppruleDic:
            icCode_final = mppruleDic[func].strip()
            if icCode_final != "":
                dmrlInfo["IC"] = icCode_final[:-1]    
                dmrlInfo["ICV"] = icCode_final[-1]
            else:
                dmrlInfo["IC"] = ""       
                dmrlInfo["ICV"] = ""            
        else:
            dmrlInfo["IC"] = ""       
            dmrlInfo["ICV"] = ""           
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(i+2) + ',"-",E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',J'+ str(i+2) + ',"-",K'+ str(i+2) + ',L'+ str(i+2) + ',"-",M'+ str(i+2) + ')'
        if "的" in taskTitle:
            techName = "的".join(taskTitle.split("的")[:-1]).strip()
        else:
            techName = taskTitle.strip()
        dmrlInfo["techName"] = techName
        # print(dmrlInfo["ICV"])
        # print(type(dmrlInfo["ICV"]))
        ic_add_icv = dmrlInfo["IC"] + dmrlInfo["ICV"]
        if ic_add_icv in ruleDic:
            dmrlInfo["infoName"] = ruleDic[ic_add_icv]
        else:
            dmrlInfo["infoName"] = "MPP"
        dmrlInfo["KEY"] = arjTask[i]["key"]
        result.append(dmrlInfo)

    for i in result:
        #生成DMC
        for j in i:
            if type(i[j])== int:
                i[j] = str(i[j])
    return result

dmrlResult = dmrltabelCreat(path,manualName,icCode,mppRule)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xlsx"

excelout(dmrlResult,title,pathBefore + res,filename)

