# 提取wire中的相关信息
def wire(XMLroot):
	result = []
	xmlWireTable=XMLroot[0][1][0].findall(".//Wire")
	SegregationTable=[]
	WiringDiagramTable=[]
	CPSTable = []
	WireHarness = XMLroot[0][1].attrib.get("Tag","")
	# 提取<wire>数据
	for i in xmlWireTable:
		result.append({"Type":i.attrib.get("Type",""),"Tag":i.attrib.get("Tag",""),"Color":i.attrib.get("Color",""),"MaterialCode":i.attrib.get("MaterialCode",""),"AWG":i.attrib.get("Gauge",""),"PartNumber":i.attrib.get("PartNumber",""),"Length":i.attrib.get("Length",""),"Segregation":i.attrib.get("Segregation",""),"WiringDiagram":i.attrib.get("WiringDiagram","")})
	
	for i in range (len(xmlWireTable)):
		for j in xmlWireTable[i].iter():
			if (j.attrib.get("AttributeName")=="Segregation"):
				SegregationTable.append({"Segregation":j.get("AttributeValue"),"Tag":xmlWireTable[i].get("Tag")})
	for i in result:
		for j in SegregationTable:
			if (i["Tag"]==j["Tag"]):
				i.update(j)
	for i in range (len(xmlWireTable)):
		for j in xmlWireTable[i].iter():
			if (j.attrib.get("AttributeName")=="WiringDiagram"):
				WiringDiagramTable.append({"WiringDiagram":j.get("AttributeValue")[4:12],"Tag":xmlWireTable[i].get("Tag")})
	for i in result:
		for j in WiringDiagramTable:
			if (i["Tag"]==j["Tag"]):
				i.update(j)

# 将CPSTerminalCode提取出来，作为Terminalcode用，但是发现不是成对出现的，所以没有提取到表中的Terminalcode
	for i in range (len(xmlWireTable)):
		for j in xmlWireTable[i].iter():
			if (j.attrib.get("AttributeName")=="CPSTerminalCode"):
				CPSTable.append({"CPSTerminalCode":j.get("AttributeValue")[4:12],"Tag":xmlWireTable[i].get("Tag")})
	for i in result:
		for j in CPSTable:
			if (i["Tag"]==j["Tag"]):
				i.update(j)

	for i in result:
		i["WireHarness"] = WireHarness

	return result

# 提取wiregroup中的相关信息，然后覆盖到wireTable中属于wiregroup的线束中去
def WireGroup(XMLroot,WireTable):
	WireGroupList=XMLroot[0][1][0].findall(".//WireGroup")
	MaterialCodeList=[]	
	for i in WireGroupList:
		if i.iter("Wire"):
			for j in i.iter("Wire"):	
					MaterialCodeList.append({"Tag":j.attrib["Tag"],"MaterialCode":i.get("MaterialCode"),"AWG":i.get("Gauge"),"PartNumber":i.get("PartNumber"),"Length":i.get("Length")})	
	
	for i in WireTable:
		for j in MaterialCodeList:
			if (i["Tag"]==j["Tag"]):
				i.update(j)
				
	return WireTable

