# 提取无须ID判断的数据
def extremeBasic(XMLroot):
	WiresExtremitiesList = XMLroot[0][1][1]
	ExtremeBasicTable=[]
	for i in range(len(WiresExtremitiesList)):
		ExtremeBasicTable.append({"WireTag":WiresExtremitiesList[i].get("WireTag",""),"PinParent":WiresExtremitiesList[i].get("PinParent",""),"Pin":WiresExtremitiesList[i].get("Pin",""),"ID":WiresExtremitiesList[i].get("ID",""),"ContactNumber":WiresExtremitiesList[i].get("ContactNumber",""),"ConnectType":WiresExtremitiesList[i].get("ConnectType","")})
		for j in WiresExtremitiesList[i].iter("PartNumber"):
			ExtremeBasicTable[i].update({"TerminalCode":j.get("TerminalCode","")})
			ExtremeBasicTable[i].update({"PartNumber":j.get("PartNumber","")})
	#<WireExtremity>节点没有子节点<EndFittingPartNumber>，<WireExtremity>属性“ContactNumber”值不为空时，“孔号”属性值置空
		if not WiresExtremitiesList[i].iter("EndFittingPartNumbers") and not ExtremeBasicTable[i]["ContactNumber"]:
			ExtremeBasicTable[i]["Pin"] = ""

	for i in range(len(ExtremeBasicTable)):
		#“PinParent”属性值不含“-22SH”且含有“SM"，孔号为“空”
		if "SM" in ExtremeBasicTable[i]["PinParent"] and "-SH" not in ExtremeBasicTable[i]["PinParent"]:
			ExtremeBasicTable[i]["Pin"] = ""
		#“PinParent”属性值含“-22SH”，以“GS”开头,孔号为“空”
			if ExtremeBasicTable[i]["PinParent"][:2] == "GS":
				ExtremeBasicTable[i]["Pin"] = ""
		#“PinParent”属性值含“-22SH”，不以“GS”开头,“Pin”属性值为“_CNT”时，孔号为“空”
		if "-SH" in ExtremeBasicTable[i]["PinParent"] :
			if ExtremeBasicTable[i]["PinParent"][:2] != "GS" and ExtremeBasicTable[i]["Pin"] == "_CNT":
				ExtremeBasicTable[i]["Pin"] = "BKSH"
			# else:
			# 	print(ExtremeBasicTable[i])
	return ExtremeBasicTable

def CPS(ExtremeBasicTable,WireTable):
	for i in range(len(ExtremeBasicTable)):
		for j in range(len(WireTable)):
			#PinParent含有22SH，则令其terminalcode等于CPSTerminalCode
			if "22SH" in ExtremeBasicTable[i]["PinParent"] :
				if ExtremeBasicTable[i]["PinParent"] == WireTable[j]["Tag"] :
					ExtremeBasicTable[i]["TerminalCode"] = WireTable[j]["CPSTerminalCode"]

# 整理元素中无效信息，按ID大小将从到端合并
def mergeExtreme(ExtremeBasicTable):
	digitIdList = []
	mergerResult = []
	# 去掉wiretag非空的元素，去掉ID不为数字的元素
	for i in ExtremeBasicTable:
		if i['ID'].isdigit():
			if i["WireTag"] != "":
				digitIdList.append(i)
	
	# 按ID大小将wiretag的从到端合并起来
	for i in digitIdList:
		for j in digitIdList:
			if(int(i["ID"])>int(j["ID"])and (i["WireTag"]==j["WireTag"])):
				mergerResult.append({"PartNumberFrom":j.get("PartNumber"),"PinFrom":j.get("Pin"),"PinParentFrom":j.get("PinParent"),"TerminalCodeFrom":j.get("TerminalCode"),"WireTag":i.get("WireTag"),"PinParentTo":i.get("PinParent"),"PinTo":i.get("Pin"),"TerminalCodeTo":i.get("TerminalCode"),"PartNumberTo":j.get("PartNumber")})

	return mergerResult

#将wire中基础信息和从到端信息合并
def mergeWireAndExtreme(WireTable,ExtremeFinalTable):
	for i in WireTable:
		for j in ExtremeFinalTable:
			if i["Tag"] == j["WireTag"]:
				i.update(j)
	return WireTable