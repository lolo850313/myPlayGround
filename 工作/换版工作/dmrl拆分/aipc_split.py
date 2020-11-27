# path = "d:\\"
from lxml import etree
path = "D:\\程序源数据\\手册\\201912\\"
manualName ="AIPC-TP700016-$new$-amm(201912)"
result = "\\dmrlSplit\\aipc\\"

#生成dmrl相关信息
def dmrl_split(path,manualName):   
    tree = etree.parse(path + "dmrl\\" + manualName)

    #读取task
    task_list = tree.xpath("//figure")
    for i in task_list:
        pgblk = i.attrib
        title = pgblk["chapnbr"] +"-"+  pgblk["sectnbr"] +"-"+ pgblk["unitnbr"] +"-"+ pgblk["fignbr"]
        etree.ElementTree(i).write(path + result + title + ".xml",pretty_print=True,xml_declaration=True,encoding="utf-8")
        # etree.ElementTree(i).write(path + "\\dtd拆分\\" + title + ".xml",pretty_print=True,encoding="utf-8")

dmrl_split(path,manualName)