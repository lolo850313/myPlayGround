#生成导线清单
from excel import excelout
from lxml import etree
pathBefore = "D:\\程序源数据\\手册\\201909\\dmrl\\"
# pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore
manualName ="WM-TP700015-$new$-amm.sgm"
wmRule = "wmRule.xlsx"
#通过ic编码规则excel文档，找出IC+ICV对应infoname的值
icCode = "icCode.xls"

#生成dmrl相关信息
def dmrltabelCreat(path,manualName,wmRule,icCode):
    import xlrd
    wmRule = path + wmRule
    data = xlrd.open_workbook(wmRule)
    table = data.sheet_by_index(0)
    wmRuleDic = {}
    for i in range(table.nrows):
        for j in range(table.ncols):
            wmRuleDic[table.cell(i,1).value] = table.cell(i,2).value

    icCode = path + icCode
    data = xlrd.open_workbook(icCode)
    table = data.sheet_by_index(0)
    icRuleDic = {}
    for i in range(table.nrows):
        icRuleDic[table.cell(i,0).value.strip()] = table.cell(i,1).value.strip()   
    tree = etree.parse(path + manualName)

    #读取task
    task_list = tree.xpath("//eqiplist")
    arjTask = []
    for i in task_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            arjTask.append(dic)

    result = []

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
        taskTitle = "##"  
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["eqipwnbr"]
        if arjTask[i]["eqipwnbr"] in wmRuleDic:
            taskTitle = wmRuleDic[arjTask[i]["eqipwnbr"]]
        else:
            taskTitle = "###"
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = "91"
        dmrlInfo["SUB-SYS"] = "21"
        dmrlInfo["UNIT"] = "13"
        dmrlInfo["DC"] = arjTask[i]["eqipwnbr"]
        dmrlInfo["DCV"] = "A"        
        dmrlInfo["IC"] = "056"        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(i+2) + ',"-",E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',J'+ str(i+2) + ',"-",K'+ str(i+2) + ',L'+ str(i+2) + ',"-",M'+ str(i+2) + ')'
        dmrlInfo["techName"] = taskTitle
        ic_add_icv = dmrlInfo["IC"] + dmrlInfo["ICV"]
        if ic_add_icv in icRuleDic:
            dmrlInfo["infoName"] = icRuleDic[ic_add_icv]
        else:
            print(ic_add_icv)
            dmrlInfo["infoName"] = "please add icCode"
            dmrlInfo["infoName"] = "SDS"
        dmrlInfo["KEY"] = arjTask[i]["key"]
        result.append(dmrlInfo)

    return result

dmrlResult = dmrltabelCreat(path,manualName,wmRule,icCode)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-eqip-dmrl.xlsx"

excelout(dmrlResult,title,path,filename)

