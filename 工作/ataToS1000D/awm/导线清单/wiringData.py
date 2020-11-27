#effectDic是由接线清单表中提取的字典，键为有效性，值为流水号，比如a001、a002等
#通过effectDic生成content中有效性的部分。

def contentFrame(dmCodeRef,effectDic,wireList,row,ata_dmrl):
	from lxml import etree
	from excel_to_dic import excelToDic
	from lxml.builder import ElementMaker

	E = ElementMaker()
	wire_xml = E.wire
	wireIdent_xml = E.wireIdent
	wireNumber_xml = E.wireNumber
	wireConnection_xml = E.wireConnection
	fromEquip_xml = E.fromEquip
	functionalItemRef_xml = E.functionalItemRef
	contactInfo_xml = E.contactInfo
	contact_xml = E.contact
	wireConnectionCode_xml = E.wireConnectionCode
	specialConnection_xml = E.specialConnection
	electricalPotential_xml = E.electricalPotential
	toEquip_xml = E.toEquip
	wireInfo_xml = E.wireInfo
	wireCode_xml = E.wireCode
	wireType_xml = E.wireType
	wireGauge_xml = E.wireGauge
	harnessIdent_xml = E.harnessIdent
	length_xml = E.length
	wireRoute_xml = E.wireRoute
	functionalDescrRef_xml = E.functionalDescrRef
	refs_xml = E.refs
	dmRef_xml = E.dmRef
	dmRefIdent_xml = E.dmRefIdent
	dmCode_xml = E.dmCode

	#生成content框架
	content = etree.Element("content")
	referencedApplicGroupRef = etree.SubElement(content,"referencedApplicGroupRef")
	wiringData = etree.SubElement(content,"wiringData")
	wiringGroup = etree.SubElement(wiringData,"wireGroup")

	#将有效性及其对应的id添加进referencedApplicGroupRef
	for i in effectDic:
		applicRef = etree.SubElement(referencedApplicGroupRef,"applicRef")
		applicRef.set("applicIdentValue",i)
		applicRef.set("id",effectDic[i])
	
	for wire in wireList:
		wiringAlts = etree.SubElement(wiringGroup,"wireAlts")
		if isinstance(wire,float):
			wireId = str(int(wire))
			if "/" in wireId:
				wireId = wireId.replace("/", "_")
			wiringAlts.set("id", "w"+wireId)
		else:
			wireId = wire
			if "/" in wire:
				wireId = wire.replace("/", "_")
			wiringAlts.set("id", "w"+wireId)	
		for excelInfo in wireList[wire]:		
			if isinstance(excelInfo["孔号(从)"],str):
				excelInfo["孔号(从)"] = excelInfo["孔号(从)"].strip()
			if isinstance(excelInfo["孔号(到)"],str):
				excelInfo["孔号(到)"] = excelInfo["孔号(到)"].strip()
			if isinstance(excelInfo["端接代号(从)"],float):
				excelInfo["端接代号(从)"] = str(int(excelInfo["端接代号(从)"]))
			if isinstance(excelInfo["端接代号(到)"],float):
				excelInfo["端接代号(到)"] = str(int(excelInfo["端接代号(到)"]))
			if isinstance(excelInfo["导线材料"],float):
				excelInfo["导线材料"] = str(int(excelInfo["导线材料"]))
			if isinstance(excelInfo["AWG"],float):
				excelInfo["AWG"] = str(int(excelInfo["AWG"]))
			if isinstance(excelInfo["孔号(从)"],float):
				excelInfo["孔号(从)"] = str(int(excelInfo["孔号(从)"]))
			if isinstance(excelInfo["孔号(到)"],float):
				excelInfo["孔号(到)"] = str(int(excelInfo["孔号(到)"]))
			if isinstance(excelInfo["长度"],float):
				excelInfo["长度"] = str(int(excelInfo["长度"]))
			if isinstance(excelInfo["导线号"],float):
				excelInfo["导线号"] = str(int(excelInfo["导线号"]))
			if excelInfo["ATA编号"] in ata_dmrl:
				dmCodeRef = ata_dmrl[excelInfo["ATA编号"]]
			else:
				#如果搜不到，暂定dmCodeRef
				dmCodeRef = False
			if excelInfo["孔号(从)"] != "C+S" and excelInfo["孔号(从)"] != "C+S":
									
				wire_element = wire_xml(							
					wireIdent_xml(wireNumber_xml(excelInfo["导线号"])),
					wireConnection_xml(
						fromEquip_xml(
							functionalItemRef_xml(functionalItemNumber = excelInfo["设备号(从)"]),
							contactInfo_xml(
								contact_xml(contactIdent = excelInfo["孔号(从)"]),
									wireConnectionCode_xml(
									specialConnection_xml(excelInfo["端接代号(从)"]),
									electricalPotential_xml
									)
								),							
							),
						toEquip_xml(
							functionalItemRef_xml(functionalItemNumber = excelInfo["设备号(到)"]),
							contactInfo_xml(
								contact_xml(contactIdent = excelInfo["孔号(到)"]),
									wireConnectionCode_xml(
									specialConnection_xml(excelInfo["端接代号(到)"]),
									electricalPotential_xml
									)
								),
							
							),
					),
					wireInfo_xml(
						wireCode_xml(
							wireType_xml(excelInfo["导线材料"]),
							wireGauge_xml(
								excelInfo["AWG"],
								wireGaugeType = "awg"
								)),
							harnessIdent_xml(excelInfo["线束号"]),
							length_xml(excelInfo["长度"],unitOfMeasure = "mm",wireLengthType = "estimated"),
							wireRoute_xml(excelInfo["敷设字母"])
					),			
					applicRefId = effectDic[excelInfo["有效性"]],
					wireState = "active"
					)
				if dmCodeRef != False:
					f = functionalDescrRef_xml(refs_xml(dmRef_xml(dmRefIdent_xml(dmCode_xml(
						assyCode = dmCodeRef["assyCode"],
						disassyCode = dmCodeRef["disassyCode"],
						disassyCodeVariant = dmCodeRef["disassyCodeVariant"],
						infoCode = dmCodeRef["infoCode"],
						infoCodeVariant = dmCodeRef["infoCodeVariant"],
						itemLocationCode = dmCodeRef["itemLocationCode"],
						modelIdentCode = dmCodeRef["modelIdentCode"],
						subSystemCode = dmCodeRef["subSystemCode"],
						subSubSystemCode = dmCodeRef["subSubSystemCode"],
						systemCode = dmCodeRef["systemCode"],
						systemDiffCode = dmCodeRef["systemDiffCode"]
					)))))
					wire_element.find(".//wireInfo").append(f)
				wiringAlts.append(wire_element)
			else:
				wire_element = wire_xml(							
					wireIdent_xml(wireNumber_xml(excelInfo["导线号"])),
					wireConnection_xml(
						fromEquip_xml(
							functionalItemRef_xml(functionalItemNumber = excelInfo["设备号(从)"]),
							contactInfo_xml(
								contact_xml(contactIdent = excelInfo["孔号(从)"]),
									wireConnectionCode_xml(
									specialConnection_xml(excelInfo["端接代号(从)"]),
									electricalPotential_xml
									)
								),
							
							),
						toEquip_xml(
							functionalItemRef_xml(functionalItemNumber = excelInfo["设备号(到)"]),
							contactInfo_xml(
								contact_xml(contactIdent = excelInfo["孔号(到)"]),
									wireConnectionCode_xml(
									specialConnection_xml(excelInfo["端接代号(到)"]),
									electricalPotential_xml
									)
								),							
							),
					),
					wireInfo_xml(
						wireCode_xml(
							wireType_xml(excelInfo["导线材料"]),
							wireGauge_xml(
								excelInfo["AWG"],
								wireGaugeType = "awg"
								)),
							harnessIdent_xml(excelInfo["线束号"]),
							length_xml(excelInfo["长度"],unitOfMeasure = "mm",wireLengthType = "estimated"),
							wireRoute_xml(excelInfo["敷设字母"])
					),			
					applicRefId = effectDic[excelInfo["有效性"]],
					wireState = "notactiv"
					)	
				wiringGroup.append(wire_element)

				
	waList = content.findall(".//wireAlts")
	for w in waList:
		if w.getchildren() == []:
			w.getparent().remove(w)
	return content







