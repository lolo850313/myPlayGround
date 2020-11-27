#生成导线清单
from excel import excelout
from lxml import etree
# pathBefore = "C:\\Users\\410684\\Desktop\\小程序\\工作\\"
pathBefore = "C:\\Users\\lolo\\Desktop\\工作\\"
path = pathBefore + "各种手册dmrl生成\\201812\\"
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
    task_list = tree.xpath("//extwlist")
    arjTask = []
    for i in task_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            arjTask.append(dic)

    result = []

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
         
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["extwnbr"]
        if arjTask[i]["extwnbr"] in wmRuleDic:
            taskTitle = wmRuleDic[arjTask[i]["extwnbr"]]
        else:
            taskTitle = "###"
         
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = "91"
        dmrlInfo["SUB-SYS"] = arjTask[i]["extwnbr"][:2]
        dmrlInfo["UNIT"] = arjTask[i]["extwnbr"][3:5]
        dmrlInfo["DC"] = arjTask[i]["extwnbr"][5:7]
        dmrlInfo["DCV"] = "A"        
        dmrlInfo["IC"] = "057"        
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

    #修改dc号，当s-sys值不等于当前s-sys值时，dc流水号重置为0，等于时dc流水号递增。
    return result

dmrlResult = dmrltabelCreat(path,manualName,wmRule,icCode)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-extw-dmrl.xlsx"

excelout(dmrlResult,title,path,filename)

