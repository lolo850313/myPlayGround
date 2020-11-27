#effectDic是由接线清单表中提取的字典，键为有效性，值为流水号，比如a001、a002等
#通过effectDic生成content中有效性的部分。

def contentFrame(dmCodeRef,effectDic,wireList,row):
	from lxml import etree
	from excel_to_dic import excelToDic
	from lxml.builder import ElementMaker

	E = ElementMaker()

	#生成content框架
	content = etree.Element("content")

	#将有效性及其对应的id添加进referencedApplicGroupRef
	referencedApplicGroupRef = etree.SubElement(content,"referencedApplicGroupRef")
	for i in effectDic:
		applicRef = etree.SubElement(referencedApplicGroupRef,"applicRef")
		applicRef.set("applicIdentValue",i)
		applicRef.set("id",effectDic[i])

	wiringData = etree.SubElement(content,"wiringData")
	electricalEquipGroup = etree.SubElement(wiringData,"electricalEquipGroup")
	
	

	for wire in wireList:
		electricalEquip_xml = E.electricalEquip
		functionalItemRef_xml = E.functionalItemRef
		partNumber_xml = E.partNumber
		equipName_xml = E.equipName
		installationInfo_xml = E.installationInfo
		installationLocation_xml = E.installationLocation
		dmCode_xml = E.dmCode
		functionalDescrRef_xml = E.functionalDescrRef
		refs_xml = E.refs
		dmRef_xml = E.dmRef
		dmRefIdent_xml = E.dmRefIdent
		responsiblePartnerCompany_xml = E.responsiblePartnerCompany
		altIdentGroup = E.altIdentGroup
		altIdent = E.altIdent
		manufactureCode = E.manufacturerCode
		assyInstruction = E.assyInstruction
		connectionListClass = E.connectionListClass

		electricalEquipAlts = etree.Element("electricalEquipAlts")
		electricalEquipAlts.set("id", wire)		

		#将列表字典中的元素依次生成xml对象添加至xml树中
		for excelInfo in wireList[wire]:
			if isinstance((excelInfo["标准零件号"]),float):
				excelInfo["标准零件号"] = str(int(excelInfo["标准零件号"]))
			if isinstance((excelInfo["供应商零件号"]),float):
				excelInfo["供应商零件号"] = str(int(excelInfo["供应商零件号"]))
			if isinstance(excelInfo["安装位置"],float):
				excelInfo["安装位置"] = str(int(excelInfo["安装位置"]))		
			if len(excelInfo["线路图ATA号"]) != 8:
				euip_element = electricalEquip_xml(							
				functionalItemRef_xml(functionalItemNumber=excelInfo["设备号"]),
				partNumber_xml(excelInfo["标准零件号"]),
				altIdentGroup(altIdent(
					partNumber_xml(excelInfo["供应商零件号"]),
					manufactureCode(excelInfo["供应商"])
				)),
				assyInstruction,
				connectionListClass(row),
				# responsiblePartnerCompany_xml(enterpriseCode=excelInfo["供应商"]),
				equipName_xml(excelInfo["设备名称(中文)"]),
				installationInfo_xml(installationLocation_xml(excelInfo["安装位置"])),
				applicRefId = effectDic[excelInfo["有效性"]],
				equipState = "active"
				)
			else:
				euip_element = electricalEquip_xml(							
				functionalItemRef_xml(functionalItemNumber=excelInfo["设备号"]),
				partNumber_xml(excelInfo["标准零件号"]),
				altIdentGroup(altIdent(
					partNumber_xml(excelInfo["供应商零件号"]),
					manufactureCode(excelInfo["供应商"])
				)),
				assyInstruction,
				connectionListClass(row),
				# responsiblePartnerCompany_xml(enterpriseCode=excelInfo["供应商"]),
				equipName_xml(excelInfo["设备名称(中文)"]),
				installationInfo_xml(installationLocation_xml(excelInfo["安装位置"])),
				functionalDescrRef_xml(refs_xml(dmRef_xml(dmRefIdent_xml(dmCode_xml(modelIdentCode = "ARJ21",
									systemDiffCode = "A",
									systemCode = excelInfo["线路图ATA号"][:2],
									subSystemCode = excelInfo["线路图ATA号"][3],
									subSubSystemCode = excelInfo["线路图ATA号"][4],
									assyCode = "00",
									disassyCode = excelInfo["线路图ATA号"][-2:],
									disassyCodeVariant = "A",
									infoCode = "051",
									infoCodeVariant = "A",
									itemLocationCode = "A"
									))))),			
				applicRefId = effectDic[excelInfo["有效性"]],
				equipState = "active"
				)
			
			electricalEquipAlts.append(euip_element)
			assyInstruction_XML = euip_element.find("assyInstruction")
			installationInfo_List = excelInfo["设备安装图号"].split(",")
			# if len(installationInfo_List) > 1:
			# 	print(installationInfo_List)
			for assy in installationInfo_List:
				assy_XML = etree.SubElement(assyInstruction_XML,"assy")
				instructionIdent_XML = etree.SubElement(assy_XML,"instructionIdent")
				instructionIdent_XML.text = assy
			# if delRef:
			# 	dmRefIdent_xml = euip_element.find(".//dmRefIdent")
				
			# 	dmRefIdent_xml.remove(dmRefIdent_xml.find("dmCode"))

		electricalEquipGroup.append(electricalEquipAlts)			
	return content







