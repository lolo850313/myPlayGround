# 提取connectDevice中的PinParent的值
def connectDevice(XMLroot):
	xmlConnectDevice = XMLroot[0][0]
	connectList=[]
	for i in xmlConnectDevice:
		connectList.append({"Tag":i.get("Tag",""),"PartNumber":i.get("PartNumber","")})
	return connectList

def connectNumberToPartNumber(connectList, ExtremeBasicTable):
	# 处理Pin含有.时的PartNumber
	for i in ExtremeBasicTable:
		for j in ExtremeBasicTable:
			if "." in i["Pin"] and i["PinParent"] == j["WireTag"][:11] + "-.SH":
				i["PartNumber"] = j["PartNumber"] 


	#处理PartNumber以下3种情况：contactNumber为空，GS开头，非GS开头
	for i in ExtremeBasicTable:
		for j in connectList:
			# ContactNumber是否为空
			if i["ContactNumber"] == "":
				# 当i与j的PinParent一致时，令i与j的partnumber一致。
				if i["PinParent"] ==  j["Tag"]:
					i['PartNumber'] = j["PartNumber"]
			else:
				if i["PinParent"][:2] == ["GS"]:
					if i["PinParent"]+"-"+i["ContactNumber"] == j["Tag"]:
						i['PartNumber'] = j["PartNumber"]
				else:
					if i["PinParent"]+"-"+i["Pin"] +"-" +i["ContactNumber"] == j["Tag"]:
						i['PartNumber'] = j["PartNumber"]
	
	return ExtremeBasicTable
			
			