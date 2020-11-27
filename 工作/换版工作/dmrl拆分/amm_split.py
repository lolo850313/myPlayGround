# 运行此程序可使用快捷键shift+Enter
from lxml import etree
#xml文件放置路径
path = "D:\\程序源数据\\手册\\201909\\"
manualName ="AMM-TP700004-02-$new$-amm.sgm"
#拆分后的结果路径为path+result
result = "\\dmrlSplit\\amm\\"

#生成dmrl相关信息
def dmrl_split(path,manualName):   
    tree = etree.parse(path + "dmrl\\" +manualName)

    #读取task
    task_list = tree.xpath("//task")
    for i in task_list:
        pgblk = i.attrib
        title = pgblk["chapnbr"] +"-"+  pgblk["sectnbr"] +"-"+ pgblk["subjnbr"] +"-"+ pgblk["func"] +"-"+ pgblk["seq"]
        if "confltr" in pgblk:
            title = title +"-"+ pgblk["confltr"]
        if "varnbr" in pgblk:
            title = title +"-"+ pgblk["varnbr"]
        etree.ElementTree(i).write(path + result + title + ".xml",pretty_print=True,xml_declaration=True,encoding="utf-8")
        # etree.ElementTree(i).write(path + "\\dtd拆分\\" + title + ".xml",pretty_print=True,encoding="utf-8")

dmrl_split(path,manualName)