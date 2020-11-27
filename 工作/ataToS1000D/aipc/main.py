#ARJ21-A-21-00-01-01A-941A-A adt未赋值，但有pnrmfr_pnr + " " + adt
from mainFrame import frame
from lxml import etree
from effect import effect_to_dic,effect_xml
from head import headxml,findDmCode,find_dmrl
# from subtask import prtlistMerge
import re
from graphic import graphicAdd
from entityAdd import entityStr
from excel import excelout
from tbmExcelpy import tbmExcel
from lblExcelpy import lblExcel

def prtlistMerge(item,effect_dic,dmrl_excel,graphicId,dmCode_para,dmc):
	from excel import excelout
	from lxml import etree
	from lxml.builder import ElementMaker
	from head import findDmCode
	import re

	global dic

	itemSeqNumberValue_para = "000"
	#提取item中的数据    
	fignbr = item.attrib["fignbr"]
	figureNumber = fignbr[:2]


	#itemnbr
	itemnbr = item.attrib["itemnbr"]


	indent = item.attrib["indent"]

	attach = item.attrib["attach"]
	if item.find("effect")!=None:
		itemEffect = item.find("effect").attrib["label"]
		itemEffect = effect_dic[itemEffect]
	else:
		itemEffect = "ALL"
	# print(effect_dic)
	#将effect转换为参引
	
	kwd = item.find("pnrmfr").attrib["kwd"]
	pnrmfr_pnr = item.find("pnrmfr/pnr").text
	pnrmfr_mfr = item.find("pnrmfr/mfr").text
	if pnrmfr_mfr == "NONE":
		pnrmfr_mfr = "blank"
	upa = item.find("upa").text
	if item.find("adt")!=None:
		adt = item.find("adt").text
	else:
		adt = "no adt"
		# print(dmCode_para)

	E = ElementMaker()
	catalogSeqNumber_XML = E.catalogSeqNumber
	itemSeqNumber_XML = E.itemSeqNumber
	accessPointRef_XML = E.accessPointRef
	quantityPerNextHigherAssy_XML = E.quantityPerNextHigherAssy    
	partRef_XML = E.partRef
	partSegment_XML = E.partSegment
	techData_XML = E.techData
	partRefGroup_XML = E.partRefGroup
	itemIdentData_XML = E.itemIdentData
	descrForPart_XML = E.descrForPart
	partLocationSegment_XML = E.partLocationSegment
	attachStoreShipPart_XML = E.attachStoreShipPart
	changeAuthority_XML = E.changeAuthority
	changeAuthorityData_XML = E.changeAuthorityData
	genericPartDataGroup_XML = E.genericPartDataGroup
	notillustrated_XML = E.notIllustrated

	#框架
	catalogSeqNumber_element = catalogSeqNumber_XML(                 
		itemSeqNumber_XML
			(
				quantityPerNextHigherAssy_XML(upa),
				partRef_XML(manufacturerCodeValue = pnrmfr_mfr,
					partNumberValue = pnrmfr_pnr),
				partSegment_XML(
					itemIdentData_XML(descrForPart_XML),
					techData_XML(
					),
					partRefGroup_XML,
				),
				partLocationSegment_XML(
					attachStoreShipPart_XML(attachStoreShipPartCode = attach),
					notillustrated_XML,

				),
				applicRefIds=itemEffect, 
				itemSeqNumberValue=itemSeqNumberValue_para,         
			),
		figureNumber=figureNumber,
		indenture=str(int(indent)+1),
		item = itemnbr[:3],       
	)  

	cataID = "csn-" + graphicId[4:] + "-" + itemnbr[:3]
	catalogSeqNumber_element.set("id",cataID)

	figureNumberVariant = dmCode_para["disassyCodeVariant"]
	catalogSeqNumber_element.set("figureNumberVariant",figureNumberVariant)


	if len(itemnbr) > 4:
		print("catalogSeqNumber itemVariant.length more than 4")
	#pan
	if item.find("pan")!=None:
		pan = item.find("pan").text
		accessPointRef_XML = etree.Element("accessPointRef")
		catalogSeqNumber_element.insert(0,accessPointRef_XML)        
		accessPointRef_XML.set("accessPointNumber",pan)
		accessPointRef_XML.set("id","acp-" + dmc + "-" + str(dic["acp"]).zfill(3))
		dic["acp"] += 1

	#sfn空标签
	itemSeqNumber_element = catalogSeqNumber_element.find(".//itemSeqNumber")

	if len(itemnbr) == 4:
		itemVariant = itemnbr[3].upper()
		if ord(itemVariant) <= 72:
			itemSeqNumberValue_para = "00" + itemVariant
		elif ord(itemVariant) > 72 and ord(itemVariant) <= 77:            
			itemVariant = chr(ord(itemVariant) + 1)
			itemSeqNumberValue_para = "00" + itemVariant
		elif ord(itemVariant) > 77 and ord(itemVariant) < 89:            
			itemVariant = chr(ord(itemVariant) + 2)
			itemSeqNumberValue_para = "00" + itemVariant
		elif ord(itemVariant) == 89:            
			itemSeqNumberValue_para = "0AA"
		elif ord(itemVariant) == 90:            
			itemSeqNumberValue_para = "0AB"
		if itemVariant == "I":
			print(itemVariant + " 72+ itemVariant")
		if itemVariant == "O":
			print(itemVariant + " 72+ itemVariant")
		itemSeqNumber_element.set("itemSeqNumberValue",itemSeqNumberValue_para)

	itemSeqNumber_element.set("id","isn-" + graphicId[4:] + "-" + itemnbr[:3] +"-" +itemSeqNumberValue_para)
	if item.find("sfn")!=None:
		if item.find("sfn").text == None:
			itemSeqNumber_element.set("partStatus","pst03")

	# #多余标签的删除
	# content_element.remove(content_element.find("accessPointRef"))
	if attach == "0":
		catalogSeqNumber_element.find(".//partLocationSegment").remove(catalogSeqNumber_element.find(".//attachStoreShipPart")) 

	#sbcdata/sbc
	if len(item.findall("sbcdata")) != 0:
		for item_sbcdata in item.findall("sbcdata"):
			chgcond = item_sbcdata.find("sbc").attrib["chgcond"]
			chgnbr = item_sbcdata.find("sbc").attrib["chgnbr"]
			chgtype = item_sbcdata.find("sbc").attrib["chgtype"]
			if chgcond == "S1":
				chgcond="PRE"
			elif chgcond == "S2":
				chgcond="POST"
			elif chgcond == "S6":
				chgcond="RWK"
			changeAuthorityData_element = etree.Element("changeAuthorityData")
			itemSeqNumber_element.append(changeAuthorityData_element)
			changeAuthorityData_element.set("condValue", chgcond)
			changeAuthorityData_element.set("id", "chaData-" + dmc + "-" + str(dic["chaData"]).zfill(3))
			dic["chaData"] += 1
			changeAuthority_element = etree.SubElement(changeAuthorityData_element,"changeAuthority")
			changeAuthority_element.set("condNumber", chgnbr)
			changeAuthority_element.set("condTypeName", chgtype)

	if len(item.findall("lbl")) != 0:
		for item_lbl in item.findall("lbl"):
			lbl = item_lbl.text              
			if lbl[:2] == "CR":
				changeAuthorityData_element = etree.Element("changeAuthorityData")
				changeAuthorityData_element.set("id", "chaData-" + dmc + "-" + str(dic["chaData"]).zfill(3))
				dic["chaData"] += 1
				itemSeqNumber_element.append(changeAuthorityData_element)
				chgtype = "CONC"
				chgcond = lbl.strip()
				chgnbr = lbl.strip()
				changeAuthorityData_element.set("condValue", chgcond)
				changeAuthority_element = etree.SubElement(changeAuthorityData_element,"changeAuthority")
				changeAuthority_element.set("condNumber", chgnbr)
				changeAuthority_element.set("condTypeName", chgtype)
			elif lbl[:3] == "FRR":
				changeAuthorityData_element = etree.Element("changeAuthorityData")
				changeAuthorityData_element.set("id", "chaData-" + dmc + "-" + str(dic["chaData"]).zfill(3))
				dic["chaData"] += 1
				itemSeqNumber_element.append(changeAuthorityData_element)
				chgtype = "FRR"
				chgcond = lbl.strip()
				chgnbr = lbl[3:].strip()
				changeAuthorityData_element.set("condValue", chgcond)
				changeAuthority_element = etree.SubElement(changeAuthorityData_element,"changeAuthority")
				changeAuthority_element.set("condNumber", chgnbr)
				changeAuthority_element.set("condTypeName", chgtype)
			elif lbl[:2] == "R-":
				changeAuthorityData_element = etree.Element("changeAuthorityData")
				changeAuthorityData_element.set("id", "chaData-" + dmc + "-" + str(dic["chaData"]).zfill(3))
				dic["chaData"] += 1
				itemSeqNumber_element.append(changeAuthorityData_element)
				chgtype = "FRR"
				chgcond = lbl.strip()
				chgnbr = lbl.strip()
				changeAuthorityData_element.set("condValue", chgcond)
				changeAuthority_element = etree.SubElement(changeAuthorityData_element,"changeAuthority")
				changeAuthority_element.set("condNumber", chgnbr)
				changeAuthority_element.set("condTypeName", chgtype)
			elif lbl[:4] == "EIPC":
				techData_ = catalogSeqNumber_element.find(".//techData")
				specDocument_XML = etree.SubElement(techData_ , "specDocument")
				refs_XML = etree.SubElement(specDocument_XML,"refs")
				externalPubRef_XML = etree.SubElement(refs_XML,"externalPubRef")
				externalPubRef_XML.set("id","ePRef-" + dmc + "-" + str(dic["epr"]).zfill(3))
				dic["epr"] += 1
				externalPubRefIdent_XML = etree.SubElement(externalPubRef_XML,"externalPubRefIdent")
				externalPubCode_XML = etree.SubElement(externalPubRefIdent_XML,"externalPubCode")
				externalPubTitle_XML = etree.SubElement(externalPubRefIdent_XML,"externalPubTitle") 
				externalPubCode_XML.set("pubCodingScheme","EIPC")
				externalPubCode_XML.text = lbl[4:].strip()
				externalPubTitle_XML.text = lbl
			elif lbl[:3] == "CMM" or lbl[:3] == "DWG":
				pass
			else:
				changeAuthorityData_element = etree.Element("changeAuthorityData")
				changeAuthorityData_element.set("id", "chaData-" + dmc + "-" + str(dic["chaData"]).zfill(3))
				dic["chaData"] += 1
				itemSeqNumber_element.append(changeAuthorityData_element)
				chgtype = "QT"
				chgcond = lbl.strip()
				chgnbr = lbl.strip()
				changeAuthorityData_element.set("condValue", chgcond)
				changeAuthority_element = etree.SubElement(changeAuthorityData_element,"changeAuthority")
				changeAuthority_element.set("condNumber", chgnbr)
				changeAuthority_element.set("condTypeName", chgtype)

	#genericPartDataGroup
		#adt,sfn,msc如果存在则在itemSeqNumber/genericPartDataGroup/genericPartData/genericPartDataValue下新增元素
	if item.find("sfn")!=None or item.find("msc")!=None:
		genericPartDataGroup_XML = etree.Element("genericPartDataGroup")
		itemSeqNumber_element.append(genericPartDataGroup_XML)

		# gpDataNum = 1
		sfn = item.find("sfn")
		if sfn !=None:			
			sfnText = sfn.text
			if sfnText != None:
				genericPartData_XML = etree.SubElement(genericPartDataGroup_XML,"genericPartData")
				genericPartData_XML.set("genericPartDataName", "SFN")
				# # genericPartData_XML.set("id", "gpData-" + dmc + "-" + str(gpDataNum).zfill(3))
				# gpDataNum += 1
				genericPartDataValue_XML = etree.SubElement(genericPartData_XML,"genericPartDataValue")
				genericPartDataValue_XML.text = sfnText
		if len(item.findall("msc")) != 0:
			for item_msc in item.findall("msc"):
				msc = item_msc.text
				genericPartData_XML = etree.SubElement(genericPartDataGroup_XML,"genericPartData")
				genericPartData_XML.set("genericPartDataName", "Miscellaneous Text")
				# genericPartData_XML.set("id", "gpData-" + dmc + "-" + str(gpDataNum).zfill(3))
				# gpDataNum += 1
				genericPartDataValue_XML = etree.SubElement(genericPartData_XML,"genericPartDataValue")
				genericPartDataValue_XML.text = msc

	

	if item.find("intw")!=None or item.find("intwadt")!=None or item.find("lid")!=None or item.find("uoamfr")!=None or item.find("rplby")!=None or item.find("rplbyadt")!=None or item.find("uwpmfr")!=None:                        
		partRefGroup_element = catalogSeqNumber_element.find(".//partRefGroup")
		if len(item.findall("intw")) != 0:
			for item_intw in item.findall("intw"):
				intw_pnrmfr_mfr = item_intw.find("mfr").text
				intw_pnrmfr_pnr = item_intw.find("pnr").text
				if intw_pnrmfr_mfr == "NONE":
					# print("intw none" + intw_pnrmfr_mfr)
					intw_pnrmfr_mfr = "blank"
					# print("intw none" + intw_pnrmfr_mfr)
					
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","INTW")
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",intw_pnrmfr_mfr)
				replacedBy_partRef_XML.set("partNumberValue",intw_pnrmfr_pnr)
		if len(item.findall("intwadt")) != 0:
			for item_intwadt in item.findall("intwadt"):
				intwadt = item_intwadt.text
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","INTW")
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",pnrmfr_mfr)
				replacedBy_partRef_XML.set("partNumberValue",pnrmfr_pnr + " " + intwadt)
				# replacementCond_XML = etree.SubElement(replacedBy_XML,"replacementCond")
				# replacementCond_XML.text = intwadt
		if len(item.findall("lid")) != 0:
			for item_lid in item.findall("lid"):
				lid = item_lid.text
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",pnrmfr_mfr)
				# replacedBy_partRef_XML.set("partNumberValue",pnrmfr_pnr)
				replacedBy_partRef_XML.set("partNumberValue",pnrmfr_pnr + " " + adt)
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","LID")
				replacementCond_XML = etree.SubElement(replacedBy_XML,"replacementCond")
				replacementCond_XML.text = lid
		if len(item.findall("uoamfr")) != 0:
			for item_uoamfr in item.findall("uoamfr"):
				uoamfr_uoa = item_uoamfr.find("uoa").text
				uoamfr_mfr = item_uoamfr.find("mfr").text
				if uoamfr_mfr == "NONE":
					uoamfr_mfr = "blank"
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","UOA")
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",uoamfr_mfr)
				replacedBy_partRef_XML.set("partNumberValue",uoamfr_uoa)

		if len(item.findall("uwpmfr")) != 0:
			for item_uwpmfr in item.findall("uwpmfr"):
				uwpmfr_uwp = item_uwpmfr.find("uwp").text
				uwpmfr_mfr  = item_uwpmfr.find("mfr").text
				if uwpmfr_mfr == "NONE":
					uwpmfr_mfr = "blank"
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","UWP")
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",uwpmfr_mfr)
				replacedBy_partRef_XML.set("partNumberValue",uwpmfr_uwp)

		if len(item.findall("rplby")) != 0:
			for item_rplby in item.findall("rplby"):
				rplby_pnr = item_rplby.find("pnr").text
				rplby_mfr = item_rplby.find("mfr").text
				if rplby_mfr == "NONE":
					rplby_mfr = "blank"
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","REPLBY")
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",rplby_mfr)
				replacedBy_partRef_XML.set("partNumberValue",rplby_pnr)
		if len(item.findall("rplbyadt")) != 0:
			for rplbyadt_item in item.findall("rplbyadt"):
				rplbyadt = rplbyadt_item.text
				replacedBy_XML = etree.Element("replacedBy")
				replacedBy_XML.set("id","rpb-" + dmc + "-" + str(dic["rpb"]).zfill(3))
				dic["rpb"] += 1
				partRefGroup_element.append(replacedBy_XML)
				replacedBy_XML.set("replacementCode","REPLBY")
				replacedBy_partRef_XML = etree.SubElement(replacedBy_XML,"partRef")
				replacedBy_partRef_XML.set("manufacturerCodeValue",pnrmfr_mfr)
				pnrmfr_pnr_new = pnrmfr_pnr + " " + rplbyadt
				replacedBy_partRef_XML.set("partNumberValue",pnrmfr_pnr_new)
		 
	#partLocationSegment
	reDmCode = r'^[0-9]{2}[-][0-9]{2}[-][0-9]{2}[-][0-9]{2}[A-Z]{0,1}$'
	rft = 1
	#未做 可通过dmrl清单对应到具体的dm，则将对应的dmc导入到dmRef下的工作
	if len(item.findall("nha")) != 0:
		for item_nha in item.findall("nha"):
			nha = item_nha.text
			partLocationSegment_element = catalogSeqNumber_element.find(".//partLocationSegment")
			referTo_XML = etree.SubElement(partLocationSegment_element,"referTo")
			referTo_XML.set("refType","rft01")
			referTo_XML.set("id","rft-" + dmc + "-" + str(dic["rf"]).zfill(3))
			dic["rf"] += 1
			refs_XML = etree.SubElement(referTo_XML,"refs")
			dmRef_XML = etree.SubElement(refs_XML,"dmRef")
			dmRefIdent_XML = etree.SubElement(dmRef_XML,"dmRefIdent")
			dmCode_XML = etree.SubElement(dmRefIdent_XML,"dmCode")        
			nhaDmCode = findDmCode(dmrl_excel,1,nha)
			if nhaDmCode == None:
				print("nha "+ nha)
				dmCode_XML.set("modelIdentCode","nha")
				dmCode_XML.set("systemDiffCode","nha")
				dmCode_XML.set("systemCode","nha")                
				dmCode_XML.set("subSystemCode","nha")
				dmCode_XML.set("subSubSystemCode","nha")
				dmCode_XML.set("assyCode","nha")
				dmCode_XML.set("disassyCode","nha")
				dmCode_XML.set("disassyCodeVariant","nha")
				dmCode_XML.set("infoCode","nha")
				dmCode_XML.set("infoCodeVariant","nha")
				dmCode_XML.set("itemLocationCode","nha") 
			else:
				dmCode_XML.set("modelIdentCode",nhaDmCode["modelIdentCode"])
				dmCode_XML.set("systemDiffCode",nhaDmCode["systemDiffCode"])
				dmCode_XML.set("systemCode",nhaDmCode["systemCode"])                
				dmCode_XML.set("subSystemCode",nhaDmCode["subSystemCode"])
				dmCode_XML.set("subSubSystemCode",nhaDmCode["subSubSystemCode"])
				dmCode_XML.set("assyCode",nhaDmCode["assyCode"])
				dmCode_XML.set("disassyCode",nhaDmCode["disassyCode"])
				dmCode_XML.set("disassyCodeVariant",nhaDmCode["disassyCodeVariant"])
				dmCode_XML.set("infoCode",nhaDmCode["infoCode"])
				dmCode_XML.set("infoCodeVariant",nhaDmCode["infoCodeVariant"])
				dmCode_XML.set("itemLocationCode",nhaDmCode["itemLocationCode"])                
	if len(item.findall("det")) != 0:
		for item_det in item.findall("det"):
			det = item_det.text
			partLocationSegment_element = catalogSeqNumber_element.find(".//partLocationSegment")
			referTo_XML = etree.SubElement(partLocationSegment_element,"referTo")
			referTo_XML.set("refType","rft02")
			referTo_XML.set("id","rft-" + dmc + "-" + str(dic["rf"]).zfill(3))
			dic["rf"] += 1
			refs_XML = etree.SubElement(referTo_XML,"refs")
			dmRef_XML = etree.SubElement(refs_XML,"dmRef")
			dmRefIdent_XML = etree.SubElement(dmRef_XML,"dmRefIdent")
			dmCode_XML = etree.SubElement(dmRefIdent_XML,"dmCode")
			detDmCode = findDmCode(dmrl_excel,1,det)
			if detDmCode == None:
				print("det "+ det)
				dmCode_XML.set("modelIdentCode","det")
				dmCode_XML.set("systemDiffCode","det")
				dmCode_XML.set("systemCode","det")                
				dmCode_XML.set("subSystemCode","det")
				dmCode_XML.set("subSubSystemCode","det")
				dmCode_XML.set("assyCode","det")
				dmCode_XML.set("disassyCode","det")
				dmCode_XML.set("disassyCodeVariant","det")
				dmCode_XML.set("infoCode","det")
				dmCode_XML.set("infoCodeVariant","det")
				dmCode_XML.set("itemLocationCode","det")
			else: 
				dmCode_XML.set("modelIdentCode",detDmCode["modelIdentCode"])
				dmCode_XML.set("systemDiffCode",detDmCode["systemDiffCode"])
				dmCode_XML.set("systemCode",detDmCode["systemCode"])                
				dmCode_XML.set("subSystemCode",detDmCode["subSystemCode"])
				dmCode_XML.set("subSubSystemCode",detDmCode["subSubSystemCode"])
				dmCode_XML.set("assyCode",detDmCode["assyCode"])
				dmCode_XML.set("disassyCode",detDmCode["disassyCode"])
				dmCode_XML.set("disassyCodeVariant",detDmCode["disassyCodeVariant"])
				dmCode_XML.set("infoCode",detDmCode["infoCode"])
				dmCode_XML.set("infoCodeVariant",detDmCode["infoCodeVariant"])
				dmCode_XML.set("itemLocationCode",detDmCode["itemLocationCode"]) 
	
	if len(item.findall("refint")) != 0:
		for item_refint in item.findall("refint"):
			refint = item_refint.attrib["refid"]
			partLocationSegment_element = catalogSeqNumber_element.find(".//partLocationSegment")
			referTo_XML = etree.SubElement(partLocationSegment_element,"referTo")
			referTo_XML.set("refType","rft57")
			referTo_XML.set("id","rft-" + dmc + "-" + str(dic["rf"]).zfill(3))
			dic["rf"] += 1
			refs_XML = etree.SubElement(referTo_XML,"refs")
			dmRef_XML = etree.SubElement(refs_XML,"dmRef")
			dmRefIdent_XML = etree.SubElement(dmRef_XML,"dmRefIdent")
			dmCode_XML = etree.SubElement(dmRefIdent_XML,"dmCode")
			refintDmCode = findDmCode(dmrl_excel,16,refint)
			if refintDmCode != None:
				dmCode_XML.set("modelIdentCode",refintDmCode["modelIdentCode"])
				dmCode_XML.set("systemDiffCode",refintDmCode["systemDiffCode"])
				dmCode_XML.set("systemCode",refintDmCode["systemCode"])                
				dmCode_XML.set("subSystemCode",refintDmCode["subSystemCode"])
				dmCode_XML.set("subSubSystemCode",refintDmCode["subSubSystemCode"])
				dmCode_XML.set("assyCode",refintDmCode["assyCode"])
				dmCode_XML.set("disassyCode",refintDmCode["disassyCode"])
				dmCode_XML.set("disassyCodeVariant",refintDmCode["disassyCodeVariant"])
				dmCode_XML.set("infoCode",refintDmCode["infoCode"])
				dmCode_XML.set("infoCodeVariant",refintDmCode["infoCodeVariant"])
				dmCode_XML.set("itemLocationCode",refintDmCode["itemLocationCode"]) 
			else:
				print(refint + " refint not in dmrl")
	if len(item.findall("pld")) != 0:
		for item_pld in item.findall("pld"):
			pld = item_pld.text
			partLocationSegment_element = catalogSeqNumber_element.find(".//partLocationSegment")
			descrForLocation_XML = etree.SubElement(partLocationSegment_element,"descrForLocation")
			descrForLocation_XML.text = pld

	if item.find("adt")!=None:
		adt = item.find("adt").text
		catalogSeqNumber_element.find(".//itemSeqNumber/partRef").attrib["partNumberValue"] = pnrmfr_pnr + " " + adt

	illusind = item.attrib["illusind"]
	if illusind == "1":
		catalogSeqNumber_element.find(".//partLocationSegment").remove(catalogSeqNumber_element.find(".//notIllustrated"))

	#如果有空标签的情况，需要将空标签删除
	if len(catalogSeqNumber_element.find(".//partLocationSegment")) == 0:
		itemSeqNumber_element.remove(catalogSeqNumber_element.find(".//partLocationSegment"))

	#如果有空标签的情况，需要将空标签删除
	if len(catalogSeqNumber_element.find(".//techData")) == 0:
		catalogSeqNumber_element.find(".//partSegment").remove(catalogSeqNumber_element.find(".//techData"))
	if len(catalogSeqNumber_element.find(".//partRefGroup")) == 0:
		catalogSeqNumber_element.find(".//partSegment").remove(catalogSeqNumber_element.find(".//partRefGroup"))
	
	#如果partSegment仅又一个元素itemIdentData，则将partSegment删除
	if len(catalogSeqNumber_element.find(".//partSegment")) == 1:
		itemSeqNumber_element.remove(catalogSeqNumber_element.find(".//partSegment"))

	#如果partSegment仅又一个元素itemIdentData，则将partSegment删除
	genericPartData_list = catalogSeqNumber_element.findall(".//genericPartData")
	genericPartDataGroup_list = catalogSeqNumber_element.findall(".//genericPartDataGroup")
	genericPartDataValue_list = catalogSeqNumber_element.findall(".//genericPartDataValue")
	for gen in genericPartDataValue_list:
		if gen != None:
			if gen.text == None:
				print(2222)
				gen.getparent().remove(gen)
		else:
			print("None")
	for gen in genericPartData_list:
		if gen != None:
			# print(genericPartData_ele)
			if len(gen) == 0:
				gen.getparent().remove(gen)
	for gen in genericPartDataGroup_list:
		if gen != None:
			# print(genericPartData_ele)
			if len(gen) == 0:
				gen.getparent().remove(gen)
	# if genericPartData_ele != None:
	# 	if len(genericPartData_ele) == 1:
	# 		genericPartDataGroup_ele.remove(genericPartData_ele)
	# if genericPartDataGroup_ele != None:
	# 	if len(genericPartDataGroup_ele) == 1:
	# 		genericPartDataGroup_ele.remove(genericPartData_ele)
	
	return catalogSeqNumber_element

# 版本号
issueNumber = "002"
##总路径
dirPath = "D://测试//s1000d//s1000d_aipc//"

issueDatePara = {"day":"20","month":"12","year":"2019"}
##手册xml存放路径
xmlPath = "AIPC-TP700016-$new$-amm(201912).sgm"
#dmrl对应关系表
# dmrl_excel = dirPath + "AIPC-TP700016-$new$-amm-dmrl.xls"
#测试用dmrl对应关系表
dmrl_excel = dirPath + "AIPC-TP700016-$new$-aipc(201912)-dmrl-确认后.xls"
#ICN对应关系表
ICNpath = dirPath +"AIPC图(201912)_tICN-确认后.xls"	


# 结果存放位置
resPath = "D://测试//s1000d//s1000d_aipc//aipc_dmrl//"
#导管材料信息
tbmExcelPath = resPath + "tbmExcel.xls"

#初始化content_element，初始化参数start在后面循环生成content时会被覆盖掉
arjTitle = "arjTitle"
graphicId = "fig-0001"
content_element = frame(arjTitle,graphicId)

#将fim手册元素化
fim_arj = etree.parse(dirPath + xmlPath)
arj_figure_list = fim_arj.xpath("//figure")

#输出tbm表格
tbmDicList = []
tbmTitle = "tbm.xls"

#输出lbl表格
lblDicList = []
lblTitle = "lbl.xls"

for arj_figure in arj_figure_list:
	#获得dmrl号
	dmrl = find_dmrl(arj_figure,dmrl_excel)
	print(dmrl)
	taskDic = arj_figure.attrib
	taskNum = taskDic["chapnbr"] + "-" +  taskDic["sectnbr"] + "-" + taskDic["unitnbr"]  + "-" + taskDic["fignbr"]
	dmCode_para = findDmCode(dmrl_excel,1,taskNum)

	dmc = dmCode_para["systemCode"] + dmCode_para["subSystemCode"] + dmCode_para["subSubSystemCode"] + dmCode_para["assyCode"] + dmCode_para["disassyCode"]+ dmCode_para["disassyCodeVariant"]
	graphicId = "fig-" + dmc
	arjTitle = arj_figure.xpath(".//title")[0].text	
	if arjTitle == None:
		arjTitle = ""
	#初始化默认content框架
	content_element = frame(arjTitle,graphicId)

	# 生成effect字典
	effect_dic = effect_to_dic(arj_figure,dmc)

	#figure的有效性
	if arj_figure.find("effect") == None:
		print(taskNum + "@main effect is none") 
		figure_effect = "105+."
	else:
		figure_effect = arj_figure.find("effect").attrib["label"]
		
	#将graphic元素添加到figure下
	graphicAdd(ICNpath,arj_figure,content_element,dmc)

	#将有效性参引写入content中
	referencedApplicGroupRef = effect_xml(effect_dic)
	content_element.insert(0,referencedApplicGroupRef)	
	illustratedPartsCatalog_XML = content_element.find("illustratedPartsCatalog")
	#根据catalog的数量，循环添加进故障隔离主程序中
	item_list = arj_figure.xpath(".//item")
	
	arjDMC = arj_figure.attrib["key"]
	dic = {"dpd":0,"acp":0,"rf":0,"epr":0,"rpb":0,"chaData":0}
	for item in item_list:
		#将cata的id提取出来，然后将新的cata并入具有相同id的cata
		idList = []
		if illustratedPartsCatalog_XML.findall(".//catalogSeqNumber"):
			for i in illustratedPartsCatalog_XML.findall(".//catalogSeqNumber"):
				idList.append(i.attrib["id"])

		catalogSeqNumber=prtlistMerge(item,effect_dic,dmrl_excel,graphicId,dmCode_para,dmc)
		if catalogSeqNumber.attrib["id"] in idList:
			id_index = (idList.index(catalogSeqNumber.attrib["id"]))
			cata_index = illustratedPartsCatalog_XML.findall(".//catalogSeqNumber")[id_index]
			itemSeqNumber = (catalogSeqNumber.find("itemSeqNumber"))
			cata_index.append(itemSeqNumber)
		else:
			illustratedPartsCatalog_XML.append(catalogSeqNumber)
	
	#生成ident的xml树
	head = headxml(issueNumber,dmCode_para,figure_effect,issueDatePara,effect_dic)	

	#entityString
	entityString = entityStr(content_element)

	#写xml头，并添加head部分和content部分
	root = etree.XML(entityString + '<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/ipd.xsd"></dmodule>')
	root.append(head)
	root.append(content_element)
		
	
	#输出大客文档
	etree.ElementTree(root).write(resPath +'/DMC-'+ dmrl + '_'+issueNumber+'-00_ZH-CN.XML',xml_declaration=True,pretty_print=True,encoding="utf-8")
# excelout(tbmDicList,dirPath,"tbm.xls")
# excelout(lblDicList,dirPath,"lbl.xls")

#因为图没在文件夹中，所以不能打DDN包
# ddnCreat(resPath,issueNumber)