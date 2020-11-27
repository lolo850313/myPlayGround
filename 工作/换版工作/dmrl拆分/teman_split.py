# path = "d:\\"
from lxml import etree
path = "D:\\程序源数据\\手册\\201909\\"
manualName ="TEMAN-TP700031-$new$-amm - 副本.sgm"
result = "\\dmrlSplit\\teman\\"

#生成dmrl相关信息
def dmrl_split(path,manualName,result):   
	tree = etree.parse(path + "dmrl\\" +manualName)
	#读取task
	sectionList = tree.xpath("//section")
	for section in sectionList:
		sectnbr = section.attrib["sectnbr"]
		for lsheet in section.xpath(".//tlsheet"):
			toolnbr = lsheet.attrib["toolnbr"]
			title = sectnbr +"-"+ toolnbr
			if "/" in title:
				titleList = title.split("/")
				title = '@'.join(title.split("/")) + "（请将@替换为斜杠）"
				print(title)
			etree.ElementTree(lsheet).write(path + result + title + ".xml",pretty_print=True,xml_declaration=True,encoding="utf-8")
	# etree.ElementTree(i).write(path + "\\dtd拆分\\" + title + ".xml",pretty_print=True,encoding="utf-8")

dmrl_split(path,manualName,result)