#将item中lbl转换前和转换后的数据写入字典中
def lblExcel(item):
	from lxml import etree
	if len(item.findall("lbl")) != 0:
		lbl_list = []
		for item_lbl in item.findall("lbl"):
			lbl = item_lbl.text
			if lbl[:3] == "CMM":
			    pubCodingSheme = "@@@"
			    externalPubCodeText = "@@@"                
			elif lbl[:2] == "CR":
				pubCodingSheme = "CONC"
				externalPubCodeText = lbl
			elif lbl[:3] == "FRR":
				pubCodingSheme = "FRR"
				externalPubCodeText = lbl[3:].strip()
			elif lbl[:2] == "R-":
				pubCodingSheme = "FRR"
				externalPubCodeText = lbl
			elif lbl[:4] == "EIPC":
			    pubCodingSheme = "@@@"
			    externalPubCodeText = "@@@"
			else:
				pubCodingSheme = "QT"
				externalPubCodeText = lbl

			lbl_list.append({"lbl":lbl,"condTypeName":pubCodingSheme,"condValue":lbl,"condNumber":externalPubCodeText})
		return lbl_list


	




