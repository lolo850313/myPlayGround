def cmsfile(dirPath,excelPath,issueNumber,date):
	#id中是否添加_来分割。
	import xlrd
	from lxml import etree
	from lxml.builder import ElementMaker
	from help import headxml
	from help import effect_xml


	f = xlrd.open_workbook(excelPath)
	shet = f.sheet_by_index(3)
	nr = shet.nrows
	#表格数据存放
	dic = {}
	#表格有效性存放
	effectDic = {}
	#有效性id流水号
	effIdNum = 1

	#head中的参数
	date = {"day":"25","month":"11","year":"2019"}
	dmCode_para = {"modelIdentCode":"ARJ21",
					"systemDiffCode":"A",
					"systemCode":"00",
					"subSystemCode":"4",
					"subSubSystemCode":"4",
					"assyCode":"07",
					"disassyCode":"01",
					"disassyCodeVariant":"A",                          
					"infoCode":"414",
					"infoCodeVariant":"A",
					"itemLocationCode":"A",
					"techName":"CMS信息",
					"infoName":"关联性故障",
					}

	#获得excel表中信息
	for r in range(2,nr):
		eff = shet.cell_value(r,6)
		if eff not in effectDic and eff != "":
			effectDic[eff] = "appRef-" + str(effIdNum).zfill(3)
			effIdNum += 1
		if shet.cell_value(r,1) not in dic:        
			dic[shet.cell_value(r,1)] = {}
			subDic = {}
			subDic["故障代码"] = shet.cell_value(r,3)
			subDic["CMS LRU"] = shet.cell_value(r,4)
			subDic["CMS信息"] = shet.cell_value(r,5)
			subDic["有效性"] = eff
			subDic["参引DMC"] = shet.cell_value(r,7)
			dic[shet.cell_value(r,1)][shet.cell_value(r,2)] = subDic
		else:
			subDic = {}
			subDic["故障代码"] = shet.cell_value(r,3)
			subDic["CMS LRU"] = shet.cell_value(r,4)
			subDic["CMS信息"] = shet.cell_value(r,5)
			subDic["有效性"] = eff
			subDic["参引DMC"] = shet.cell_value(r,7)
			dic[shet.cell_value(r,1)][shet.cell_value(r,2)] = subDic

	# print(dic["cms26-1500AA0"])

	root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/fault.xsd"></dmodule>')

	head = headxml(dmCode_para,effectDic,issueNumber,date)

	#构造correlatedFaultAlts
	E = ElementMaker()

	correlatedFault = E.correlatedFault
	bassicCorrelatedFaults = E.basicCorrelatedFaults
	assocWaringMalfunction = E.assocWarningMalfunction
	fault = E.fault
	faultDescr = E.faultDescr
	descr = E.descr
	detailedFaultDescr = E.detailedFaultDescr
	faultMessageBody = E.faultMessageBody
	bitMessage = E.bitMessage
	dectionInfo = E.detectionInfo
	faultMessageBody = E.faultMessageBody
	detectedLruItem = E.detectedLruItem
	lru = E.lru
	name = E.name
	faultMessageBody = E.faultMessageBody
	systemName = E.systemName
	dmRef = E.dmRef
	isolateDectedFault = E.isolateDectedFault
	lruItem = E.lruItem
	faultIsolationRef = E.faultIsolationRef
	dmRefIdent = E.dmRefIdent
	dmCode = E.dmCode
	isolateDetectedFault = E.isolateDetectedFault
	faultRef = E.faultRef
	externalPubRef = E.externalPubRef
	externalPubRefIdent = E.externalPubRefIdent
	externalPubCode = E.externalPubCode
	refs = E.refs

	faultReporting = etree.Element("faultReporting")

	#生成correlatedFaultAlts
	for alts in dic:
		correlatedFaultAlts = etree.Element("correlatedFaultAlts")
		correlatedFaultAlts.set("id", alts)
		for item in dic[alts]:
			correlatedFault_ele = correlatedFault(
				bassicCorrelatedFaults,
				isolateDetectedFault,
				applicRefId = effectDic[dic[alts][item]["有效性"]],
				id = item)

			basicCorrelatedFaults_ele = correlatedFault_ele.find("basicCorrelatedFaults")

			bitMessage_ele = bitMessage(
							fault(faultCode = dic[alts][item]["故障代码"]),												
							faultDescr
								(detailedFaultDescr
									(systemName,
									faultMessageBody(dic[alts][item]["CMS信息"])
									)
								),
							dectionInfo
								(detectedLruItem
									(lru
										(name(dic[alts][item]["CMS LRU"]),
										id = item + "_" + dic[alts][item]["故障代码"]
										)
									)
								)
							)
			isolateDetectedFault_ele = correlatedFault_ele.find(".//isolateDetectedFault")

			dmPara = {"modelIdentCode":dic[alts][item]["参引DMC"][0:5],
							"systemDiffCode":dic[alts][item]["参引DMC"][6],
							"systemCode":dic[alts][item]["参引DMC"][8:10],
							"subSystemCode":dic[alts][item]["参引DMC"][11],
							"subSubSystemCode":dic[alts][item]["参引DMC"][12],
							"assyCode":dic[alts][item]["参引DMC"][14:16],
							"disassyCode":dic[alts][item]["参引DMC"][17:19],
							"disassyCodeVariant":dic[alts][item]["参引DMC"][19],
							"infoCode":dic[alts][item]["参引DMC"][21:24],
							"infoCodeVariant":dic[alts][item]["参引DMC"][-3],
							"itemLocationCode":dic[alts][item]["参引DMC"][-1]
						}

			dmRef_ele = faultIsolationRef(
				refs(
					dmRef(
						dmRefIdent
							(dmCode
								(modelIdentCode=dmPara["modelIdentCode"],
								systemDiffCode=dmPara["systemDiffCode"],
								systemCode=dmPara["systemCode"],
								subSystemCode=dmPara["subSystemCode"],
								subSubSystemCode=dmPara["subSubSystemCode"],
								assyCode=dmPara["assyCode"],
								disassyCode=dmPara["disassyCode"],
								disassyCodeVariant=dmPara["disassyCodeVariant"],
								infoCode=dmPara["infoCode"],
								infoCodeVariant=dmPara["infoCodeVariant"],
								itemLocationCode=dmPara["itemLocationCode"]
							)
						),
						id = item + "_" + dic[alts][item]["故障代码"] + "_" + dic[alts][item]["参引DMC"]
					)
				)
			)

			isolateDetectedFault_ele.append(dmRef_ele)

			basicCorrelatedFaults_ele.append(bitMessage_ele)
			correlatedFaultAlts.append(correlatedFault_ele)
		faultReporting.append(correlatedFaultAlts)

	#构造有效性    
	referencedApplicGroupRef = effect_xml(effectDic)

	#构造content
	content = etree.Element("content")

	content.append(referencedApplicGroupRef)
	content.append(faultReporting)

	root.append(head)
	root.append(content)

	etree.ElementTree(root).write(dirPath + '/DMC-ARJ21-A-00-41-07-04A-414A-A.xml',xml_declaration=True,pretty_print=True,encoding="utf-8")

if __name__ == "__main__":
	dirPath = "D:\\测试\\s1000d\\s1000d_fim\\"
	excelPath = dirPath + "ARJFRMFIM-故障代码和维修信息清单-2019.9-转S1000D-20191202.xls"
	issueNumber = "000"
	date = {"day":"25","month":"11","year":"2019"}
	cmsfile(dirPath,excelPath,issueNumber,date)