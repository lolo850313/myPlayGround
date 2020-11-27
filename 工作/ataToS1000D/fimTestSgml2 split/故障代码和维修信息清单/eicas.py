def eicasfile(dirPath,excelPath,issueNumber,date):
	import xlrd
	from lxml import etree
	from lxml.builder import ElementMaker
	from help import headxml
	from help import effect_xml

	f = xlrd.open_workbook(excelPath)
	shet = f.sheet_by_index(0)
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
					"subSubSystemCode":"1",
					"assyCode":"07",
					"disassyCode":"01",
					"disassyCodeVariant":"A",                          
					"infoCode":"414",
					"infoCodeVariant":"A",
					"itemLocationCode":"A",
					"techName":"EICAS信息",
					"infoName":"关联性故障",
					}

	#获得excel表中信息
	for r in range(2,nr):
		eff = shet.cell_value(r,8)
		if eff not in effectDic and eff != "":
			effectDic[eff] = "appRef-" + str(effIdNum).zfill(3)
			effIdNum += 1
		if shet.cell_value(r,1) not in dic:        
			dic[shet.cell_value(r,1)] = {}
			dic[shet.cell_value(r,1)][shet.cell_value(r,2)] = {}
			subDic = {}
			subDic["故障类型"] = shet.cell_value(r,3)
			subDic["故障等级"] = shet.cell_value(r,4)
			subDic["故障代码"] = shet.cell_value(r,5)
			subDic["故障名称"] = shet.cell_value(r,6)
			subDic["故障描述"] = shet.cell_value(r,7)
			subDic["有效性"] = eff
			subDic["CMS relate"] = [{"CMS ID" : shet.cell_value(r,9),
				"关联的CMS LRU" : shet.cell_value(r,10),
				"关联的CMS信息" : shet.cell_value(r,11),
				"参引的DMC" :shet.cell_value(r,12)}]
			dic[shet.cell_value(r,1)][shet.cell_value(r,2)] = [subDic]
		else:
			if shet.cell_value(r,2) in dic[shet.cell_value(r,1)]:
				if shet.cell_value(r,3) != "":
					subDic = {}
					subDic["故障类型"] = shet.cell_value(r,3)
					subDic["故障等级"] = shet.cell_value(r,4)
					subDic["故障代码"] = shet.cell_value(r,5)
					subDic["故障名称"] = shet.cell_value(r,6)
					subDic["故障描述"] = shet.cell_value(r,7)
					subDic["有效性"] = eff
					subDic["CMS relate"] = [{"CMS ID" : shet.cell_value(r,9),
						"关联的CMS LRU" : shet.cell_value(r,10),
						"关联的CMS信息" : shet.cell_value(r,11),
						"参引的DMC" :shet.cell_value(r,12)}]
					dic[shet.cell_value(r,1)][shet.cell_value(r,2)].append(subDic)
				else:
					cmsDic = {"CMS ID" : shet.cell_value(r,9),
						"关联的CMS LRU" : shet.cell_value(r,10),
						"关联的CMS信息" : shet.cell_value(r,11),
						"参引的DMC" :shet.cell_value(r,12)}
					dic[shet.cell_value(r,1)][shet.cell_value(r,2)][0]["CMS relate"].append(cmsDic)
			else:
				subDic = {}
				subDic["故障类型"] = shet.cell_value(r,3)
				subDic["故障等级"] = shet.cell_value(r,4)
				subDic["故障代码"] = shet.cell_value(r,5)
				subDic["故障名称"] = shet.cell_value(r,6)
				subDic["故障描述"] = shet.cell_value(r,7)
				subDic["有效性"] = eff
				subDic["CMS relate"] = [{"CMS ID" : shet.cell_value(r,9),
				"关联的CMS LRU" : shet.cell_value(r,10),
				"关联的CMS信息" : shet.cell_value(r,11),
				"参引的DMC" :shet.cell_value(r,12)}]
				dic[shet.cell_value(r,1)][shet.cell_value(r,2)] = [subDic]



	root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/fault.xsd"></dmodule>')

	head = headxml(dmCode_para,effectDic,issueNumber,date)

	#构造correlatedFaultAlts
	#help里的reasonForUpdate
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
	refs = E.refs
	isolateDectedFault = E.isolateDectedFault
	lruItem = E.lruItem
	faultIsolationRef = E.faultIsolationRef
	dmRefIdent = E.dmRefIdent
	dmCode = E.dmCode
	isolateDetectedFault = E.isolateDetectedFault

	faultReporting = etree.Element("faultReporting")

	#生成correlatedFaultAlts
	for alts in dic:
		correlatedFaultAlts = etree.Element("correlatedFaultAlts")
		correlatedFaultAlts.set("id", alts)
		for item in dic[alts]:
			# print(dic[alts][item][0]["有效性"])
			lruKey = 0
			correlatedFault_ele = correlatedFault(
				bassicCorrelatedFaults(
					assocWaringMalfunction(                    
						fault(faultCode = dic[alts][item][0]["故障代码"]),
						faultDescr(
							descr(dic[alts][item][0]["故障描述"]),
							detailedFaultDescr(
								systemName,
								faultMessageBody(dic[alts][item][0]["故障名称"])
								)
							),
						faultPartCategory = dic[alts][item][0]["故障类型"],
						subCategory = dic[alts][item][0]["故障等级"],
					)
				),
				isolateDetectedFault,
				applicRefId = effectDic[dic[alts][item][0]["有效性"]],
				id = item)

			basicCorrelatedFaults_ele = correlatedFault_ele.find("basicCorrelatedFaults")
			
			for cmsRelate in dic[alts][item][0]["CMS relate"]:
				dmPara = {"modelIdentCode":cmsRelate["参引的DMC"][0:5],
									"systemDiffCode":cmsRelate["参引的DMC"][6],
									"systemCode":cmsRelate["参引的DMC"][8:10],
									"subSystemCode":cmsRelate["参引的DMC"][11],
									"subSubSystemCode":cmsRelate["参引的DMC"][12],
									"assyCode":cmsRelate["参引的DMC"][14:16],
									"disassyCode":cmsRelate["参引的DMC"][17:19],
									"disassyCodeVariant":cmsRelate["参引的DMC"][19],
									"infoCode":cmsRelate["参引的DMC"][21:24],
									"infoCodeVariant":cmsRelate["参引的DMC"][-3],
									"itemLocationCode":cmsRelate["参引的DMC"][-1]
								}
				if cmsRelate["CMS ID"] != "None":
					lruKey = 1
					# print(lruKey)
					bitMessage_ele = bitMessage(
							fault(faultCode = cmsRelate["CMS ID"]),	
							dmRef(
									dmRefIdent(
										dmCode(
											modelIdentCode=dmPara["modelIdentCode"],
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
									id = item + "_" + cmsRelate["CMS ID"] + "_" + cmsRelate["参引的DMC"]
								),												
							faultDescr
								(detailedFaultDescr
									(systemName,
									faultMessageBody(cmsRelate["关联的CMS信息"])
									)
								),
							dectionInfo
								(detectedLruItem
									(lru
										(name(cmsRelate["关联的CMS LRU"]),
										id = item + "_" + cmsRelate["CMS ID"]
										)
									)
								)
							)

					
					basicCorrelatedFaults_ele.append(bitMessage_ele)
				else:
					bitMessage_ele = etree.Element("bitMessage")
					dmRef_ele =faultIsolationRef(refs(
						dmRef(
									dmRefIdent
										(dmCode(
											modelIdentCode=dmPara["modelIdentCode"],
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
									id = item + "_" + cmsRelate["CMS ID"] + "_" + cmsRelate["参引的DMC"]
									)

					)) 
					

					isolateDetectedFault_ele = correlatedFault_ele.find(".//isolateDetectedFault")
					isolateDetectedFault_ele.append(dmRef_ele)
					# basicCorrelatedFaults_ele.append(bitMessage_ele)
				
			if lruKey == 1:
				lruItem_ele = lruItem(lru)
				isolateDetectedFault_ele = correlatedFault_ele.find(".//isolateDetectedFault")
				if (isolateDetectedFault_ele.find("faultIsolationRef")) == None:
					isolateDetectedFault_ele.append(lruItem_ele)

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

	etree.ElementTree(root).write(dirPath + '/DMC-ARJ21-A-00-41-07-01A-414A-A.xml',xml_declaration=True,pretty_print=True,encoding="utf-8")

if __name__ == "__main__":
	dirPath = "D:\\测试\\s1000d\\s1000d_fim\\"
	excelPath = dirPath + "ARJFRMFIM-故障代码和维修信息清单-2019.9-转S1000D-20191202.xls"
	issueNumber = "000"
	date = {"day":"25","month":"11","year":"2019"}
	eicasfile(dirPath,excelPath,issueNumber,date)