# path = "d:\\"
from lxml import etree
path = "D:\\程序源数据\\手册\\201909\\"
manualName ="SDS-TP700004-01-$new$-amm.sgm"
res = "\\dmrlSplit\\ndt\\"

#生成dmrl相关信息
def dmrl_split(path,manualName):   
    tree = etree.parse(path + "dmrl\\" +manualName)

    #读取task
    task_list = tree.xpath("//pageset")
    for i in task_list:
        pgblk = i.attrib
        title = pgblk["chapnbr"] +"-"+  pgblk["sectnbr"] +"-"+ pgblk["subjnbr"] +"-"+ pgblk["pgsetnbr"]
        etree.ElementTree(i).write(path + res + title + ".xml",pretty_print=True,xml_declaration=True,encoding="utf-8")
        # etree.ElementTree(i).write(path + "\\dtd拆分\\" + title + ".xml",pretty_print=True,encoding="utf-8")

dmrl_split(path,manualName)