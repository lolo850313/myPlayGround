# path = "d:\\"
from excel import excelout
from lxml import etree
pathBefore = "D:\\程序源数据\\手册\\201909\\"
path = pathBefore + "dmrl\\"
res= "dmrlExcel\\"
icCode = "icCode.xls"
manualName ="ARJNDT-TP700014-$new$-amm.sgm"

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
    task_list = tree.xpath("//pgblk")
    arjTask = []
    for i in task_list:
        if i.xpath("DELETED") == []:
            dic = i.attrib
            dic["title"] = i.findtext(".//title")
            arjTask.append(dic)

    result = []

    for i in range(len(arjTask)):
        #将所有dmrl信息放入临时字典中
        chapnbr = str(arjTask[i]["chapnbr"]).strip()
        sectnbr = str(arjTask[i]["sectnbr"]).strip()
        volbnr = str(arjTask[i]["volnbr"]).strip()
        taskTitle = arjTask[i]["title"]    
        dmrlInfo = {}
        dmrlInfo["index"] = i+1
        dmrlInfo["Task NO."] = arjTask[i]["volnbr"] +"-"+ arjTask[i]["chapnbr"] +"-" +arjTask[i]["sectnbr"] +"-"+ arjTask[i]["subjnbr"]
        dmrlInfo["title"] = taskTitle
        dmrlInfo["MI"] = "ARJ21"
        dmrlInfo["SDC"] = "A"
        dmrlInfo["SYS"] = chapnbr
        dmrlInfo["SUB-SYS"] = sectnbr
        dmrlInfo["UNIT"] = arjTask[i]["subjnbr"]
        dmrlInfo["DC"] = "00"
        dmrlInfo["DCV"] = "A"
        
        if volbnr == "1":
            if chapnbr == "51":
                if sectnbr == "90" or sectnbr == "91":
                    ic = "028"
                elif sectnbr == "92":
                    ic = "354"
                elif sectnbr == "93":
                    ic = "357"
                elif sectnbr == "94":
                    ic = "355"
                elif sectnbr == "95":
                    ic = "358"
                elif sectnbr == "96":
                    ic = "353"
                elif sectnbr == "97":
                    ic = "352"
                elif sectnbr == "98":
                    ic = "351"
                elif sectnbr == "99":
                    ic = "359"
                else:
                    print(1)
            else:
                print(2)
        elif volbnr == "2":
            ic = "354"
        elif volbnr == "4":
            ic = "355"
        elif volbnr == "5":
            ic = "358"
        elif volbnr == "6":
            ic = "353"
        elif volbnr == "7":
            ic = "352"
        elif volbnr == "8":
            ic = "351"
        elif volbnr == "9":
            ic = "359"
        else:
            print(3)
        dmrlInfo["IC"] = ic        
        dmrlInfo["ICV"] = "A"
        dmrlInfo["ILC"] = "A"
        dmrlInfo["DMC"] = '=CONCATENATE(D' + str(i+2) + ',"-",E'+ str(i+2) + ',"-",F'+ str(i+2) + ',"-",G'+ str(i+2) + ',"-",H'+ str(i+2) + ',"-",I'+ str(i+2) + ',J'+ str(i+2) + ',"-",K'+ str(i+2) + ',L'+ str(i+2) + ',"-",M'+ str(i+2) + ')'
        dmrlInfo["techName"] = taskTitle
        ic_add_icv = dmrlInfo["IC"] + dmrlInfo["ICV"]
        if ic_add_icv in ruleDic:
            dmrlInfo["infoName"] = ruleDic[ic_add_icv]
        else:
            print(ic_add_icv)
            dmrlInfo["infoName"] = "please add icCode"
            dmrlInfo["infoName"] = ic        
        dmrlInfo["KEY"] = arjTask[i]["key"]
        result.append(dmrlInfo)

    return result

dmrlResult = dmrltabelCreat(path,manualName,icCode)
title = ["index","Task NO.","title","MI","SDC","SYS","SUB-SYS","UNIT","DC","DCV","IC","ICV","ILC","DMC","techName","infoName","KEY"]

filename = manualName[:-4] + "-dmrl.xlsx"

excelout(dmrlResult,title,pathBefore + res,filename)

