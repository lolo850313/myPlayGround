# 用于生成warning，caution的excel文件
#后续应手动将task中含有table的warning删除

from lxml import etree 
from excel import excelout
# tree = etree.parse("D:\\ataToS1000D\\ARJFRMFIM-TP700018A-fim26-$new$-amm.sgm")
tree = etree.parse("D:\\测试\\s1000d\\s1000d_fim\\ARJFRMFIM-TP700018A-$new$-amm(201909).sgm")

#读取task
task_list = tree.xpath("//task")

#targetStr是xpath中warning和caution的变量
def warningOrCaution(task_list,targetStr):  
    #将task中的warning、caution、dmrl值分别输出到字典中
    dic = {}
    for task in task_list:
        # 确定dmrl号
        dmrl = task.attrib["chapnbr"]+"-"+task.attrib["sectnbr"]+"-"+task.attrib["subjnbr"]+"-"+task.attrib["func"]+"-"+task.attrib["seq"]
        for searchTarget in task.findall(".//" + targetStr):
            #只提取warning，caution标签下第一个para标签的文本内容。（以防止提取到table中的内容）
            firstWarning_para = searchTarget.find("para").text
            # warning中的内容不在字典中则以列表元素加入字典中，在则加入对应的列表中
            if firstWarning_para not in dic:
                dic[firstWarning_para] = [dmrl]
            else:
                dic[firstWarning_para].append(dmrl)

    #将字典转换成excel可接受的列表形式
    excel_list = []
    flow = 1
    for i in dic:
        tempDic = {}
        tempDic[targetStr] = i
        taskString = ""
        for j in dic[i]:
            taskString = taskString + j + "   "
        tempDic["task"] = taskString
        #CIR唯一标识，通过流水号自动生成
        if targetStr == "warning":
            num = "W-SVV19-" + str(flow).zfill(4)
        if targetStr == "caution":
            num = "C-SVV19-" + str(flow).zfill(4) 
        tempDic["唯一标示"]=num
        flow = flow + 1
        excel_list.append(tempDic)

    return excel_list

warning_excel = warningOrCaution(task_list,"warning")
caution_excel = warningOrCaution(task_list,"caution")

w_title = ["唯一标示","warning","task"]
c_title = ["唯一标示","caution","task"]
warning_filename = "warningRepository.xls"
caution_filename = "cautionRepository.xls"
# path = "d:\\"
path = "D:\\测试\\s1000d\\s1000d_fim\\"

excelout(warning_excel,w_title,path,warning_filename)
excelout(caution_excel,c_title,path,caution_filename) 
 