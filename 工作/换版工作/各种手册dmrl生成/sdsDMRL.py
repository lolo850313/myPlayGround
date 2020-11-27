# path = "d:\\"
from excel import excelout
from lxml import etree
pathBefore = "C:\\Users\\410684\\Desktop\\小程序\\工作\\"
# pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "各种手册dmrl生成\\201903\\"
#通过ic编码规则excel文档，找出IC+ICV对应infoname的值
icCode = "icCode.xls"
manualName ="SDS-TP700004-01-$new$-amm.sgm"

#生成dmrl相关信息
def dmrltabelCreat(path,manualName,icCode):
    import xlrd
    icCode = path + icCode
    data = xlrd.open_workbook(icCode)
    table = data.sheet_by_index(0)
    ruleDic = {}
    for i in range(table.nrows):
        ruleDic[table.cell(i,0).value.strip()] = table.cell(i,1).value.strip()

    tree = etree.parse(path + manualName)

    #读取task
    task_list = tree.xpath(".//subject")
    arjTask = []
    for subj in task_list:        
        subjTitle = subj.findtext(".//title")
        for i in subj.xpath(".//pageset"):
            # if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["subjTitle"] = subjTitle
            dic["title"] = i.findtext(".//title")
            arjTask.append(dic)

    result = []

    icCodeDic = {"介绍":"040","一般说明":"040",
    "控制与显示":"110","指示":"110","EICAS显示":"110","简图页显示":"110",
    "系统总线接口":"03B","总线接口":"03B","接口":"03B","功能描述":"042","部件位置":"04A","电源":"04B","操作":"04C",
    "BIT测试":"04D","测试":"04D","上电机内自检测":"04D","初始化自检测调整":"04D","液压通电自检测":"04D",}

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
        taskTitle = arjTask[i]["title"]    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["chapnbr"] +"-"+arjTask[i]["sectnbr"] +"-"+ arjTask[i]["subjnbr"] + "-"+arjTask[i]["pgsetnbr"]
        dmrlInfo["title1"] = arjTask[i]["subjTitle"] + "-" + taskTitle
        dmrlInfo["title2"] = taskTitle        
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = arjTask[i]["chapnbr"]
        dmrlInfo["SUB-SYS"] = arjTask[i]["sectnbr"]
        dmrlInfo["UNIT"] = arjTask[i]["subjnbr"]
        dmrlInfo["DC"] = str(int(arjTask[i]["pgsetnbr"][-2:])-1).zfill(2)
        dmrlInfo["DCV"] = "A"
        if "-" in taskTitle:
            icCode_initial = taskTitle.split("-")[-1].strip()
            if icCode_initial in icCodeDic:
                icCode_final = icCodeDic[icCode_initial]
            else:
                icCode_final = ""
        elif "－" in taskTitle:
            icCode_initial = taskTitle.split("－")[-1].strip()
            if icCode_initial in icCodeDic:
                icCode_final = icCodeDic[icCode_initial]
            else:
                icCode_final = ""
        elif "—" in taskTitle:
            icCode_initial = taskTitle.split("—")[-1].strip()
            if icCode_initial in icCodeDic:
                icCode_final = icCodeDic[icCode_initial]
            else:
                icCode_final = ""
        elif "–" in taskTitle:
            icCode_initial = taskTitle.split("–")[-1].strip()
            if icCode_initial in icCodeDic:
                icCode_final = icCodeDic[icCode_initial]
            else:
                icCode_final = ""
        else:
            icCode_initial = taskTitle.strip()
            if icCode_initial in icCodeDic:
                icCode_final = icCodeDic[icCode_initial]
            else:
                icCode_final = ""
        dmrlInfo["IC"] = icCode_final        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',"-",J'+ str(i+2) + ',K'+ str(i+2) + ',"-",L'+ str(i+2) + ',M'+ str(i+2) + ',"-",N'+ str(i+2)+')'
        if "—" in taskTitle:
            techName = taskTitle.split("—")[:-1][0].strip()
        elif "-" in taskTitle:
            techName = taskTitle.split("-")[:-1][0].strip()
        elif "－" in taskTitle:
            techName = taskTitle.split("－")[:-1][0].strip()
        elif "–" in taskTitle:
            techName = taskTitle.split("–")[:-1][0].strip()
        else:
            techName = taskTitle.strip()
        dmrlInfo["techName"] = techName
        ic_add_icv = dmrlInfo["IC"] + dmrlInfo["ICV"]
        if ic_add_icv in ruleDic:
            dmrlInfo["infoName"] = ruleDic[ic_add_icv]
        else:
            dmrlInfo["infoName"] = "please add icCode"
            dmrlInfo["infoName"] = "SDS"
        dmrlInfo["KEY"] = arjTask[i]["key"]
        result.append(dmrlInfo)

    for i in result:
        #生成DMC
        for j in i:
            if type(i[j])== int:
                i[j] = str(i[j])
    return result

dmrlResult = dmrltabelCreat(path,manualName,icCode)
title = ["index","Task NO.","title1","title2","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xlsx"

excelout(dmrlResult,title,path,filename)

