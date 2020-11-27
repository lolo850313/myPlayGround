#从dmrl的excel表中找出taskNum所在的行，将此行D列至M列的信息依次提取，输出dmCode字典。
def findDmCode(dmrlPath,location,taskNum):	
	import xlrd

	book = xlrd.open_workbook(dmrlPath)
	sh = book.sheet_by_index(0)

	rowNumber = sh.nrows
	colNumber = sh.ncols
	for i in range(rowNumber):
		for j in range(colNumber):
			if sh.cell_value(i, location) == taskNum :
				result = {"modelIdentCode":sh.cell_value(i, 3),
							"systemDiffCode":sh.cell_value(i, 4),
							"systemCode":sh.cell_value(i, 5),
							"subSystemCode":sh.cell_value(i, 6)[0],
							"subSubSystemCode":sh.cell_value(i, 6)[1],
							"assyCode":sh.cell_value(i, 7),
							"disassyCode":sh.cell_value(i, 8),
							"disassyCodeVariant":sh.cell_value(i,9),                            
							#读出来会是浮点数421.0，则先转换为int，再转换为字符串
							"infoCode":str(int(sh.cell_value(i, 10))),
							"infoCodeVariant":sh.cell_value(i, 11),
							"itemLocationCode":sh.cell_value(i, 12),
							"techName":sh.cell_value(i, 14),
							"infoName":sh.cell_value(i, 15),}
				return result 
				
#获得当前task的taskNum值,通过taskNum在dmrlTable中找到对应的dmrl号  
def find_dmrl(arj_task,dmrl_excel) :
	taskDic = arj_task.attrib
	taskNum = taskDic["chapnbr"] + "-" +  taskDic["sectnbr"] + "-" + taskDic["unitnbr"]  + "-" + taskDic["fignbr"]
	dmCode_para = findDmCode(dmrl_excel,1,taskNum)
	if(dmCode_para ==None):
		print(taskNum + "@head dmcode is None")
	return dmCode_para["modelIdentCode"] + "-" + dmCode_para["systemDiffCode"] + "-" + dmCode_para["systemCode"] + "-"+ dmCode_para["subSystemCode"] +  dmCode_para["subSubSystemCode"] + "-"+ dmCode_para["assyCode"] + "-"+ dmCode_para["disassyCode"] +  dmCode_para["disassyCodeVariant"] + "-"+ dmCode_para["infoCode"] + dmCode_para["infoCodeVariant"]  + "-"+dmCode_para["itemLocationCode"]


def headxml(issueNumberPara,dmCode_para,effect,issueDatePara,effect_dic):    
	from lxml import etree
	from lxml.builder import ElementMaker 

	para = {"techName":"ARJ21飞机","infoName":"零件公用信息库",
			"countryIsoCode":"CN","languageIsoCode":"zh",
			"inWork":"00","issueNumber":issueNumberPara,
			"issueType":"new","day":issueDatePara["day"],
			"month":issueDatePara["month"],"year":issueDatePara["year"],
			"securityClassification":"01","enterpriseCode":"SVV19",
			"applicIdentValue":effect
			}

	brex_para = {"modelIdentCode":"ARJ21","systemDiffCode":"A",
			"systemCode":"00","subSystemCode":"0",
			"subSubSystemCode":"0","assyCode":"00",
			"disassyCode":"00","disassyCodeVariant":"A",
			"infoCode":"022","infoCodeVariant":"A",
			"itemLocationCode":"D"
	}

	
	#构建相关E对象
	E = ElementMaker()
	identAndStatusSection_xml = E.identAndStatusSection
	dmAddress_xml = E.dmAddress
	dmStatus_xml = E.dmStatus
	dmIdent_xml = E.dmIdent
	dmAddressItems_xml = E.dmAddressItems
	dmCode_xml = E.dmCode
	language_xml = E.language
	issueInfo_xml = E.issueInfo
	issueDate_xml = E.issueDate
	dmTitle_xml = E.dmTitle
	techName_xml = E.techName
	infoName_xml = E.infoName

	security_xml = E.security
	responsiblePartnerCompany_xml = E.responsiblePartnerCompany
	enterpriseName_xml = E.enterpriseName
	originator_xml = E.originator
	applicRef_xml = E.applicRef
	reasonForUpdate_xml = E.reasonForUpdate

	displayText_xml = E.displayText
	simplePara_xml = E.simplePara
	brexDmRef_xml = E.brexDmRef
	dmRef_xml = E.dmRef
	dmRefIdent_xml = E.dmRefIdent

	qualityAssurance_xml = E.qualityAssurance
	unverified_xml = E.unverified

	#利用E对象创建ident_element树
	ident_element = identAndStatusSection_xml(
		dmAddress_xml(
			dmIdent_xml(
				dmCode_xml
					# #从dmrl的excel表中D列到M列依次填入                    
					(modelIdentCode = dmCode_para["modelIdentCode"],
					systemDiffCode = dmCode_para["systemDiffCode"],
					systemCode = dmCode_para["systemCode"],
					subSystemCode = dmCode_para["subSystemCode"],
					subSubSystemCode = dmCode_para["subSubSystemCode"],
					assyCode = dmCode_para["assyCode"],
					disassyCode = dmCode_para["disassyCode"],
					disassyCodeVariant = dmCode_para["disassyCodeVariant"],
					infoCode = dmCode_para["infoCode"],
					infoCodeVariant = dmCode_para["infoCodeVariant"],
					itemLocationCode = dmCode_para["itemLocationCode"],
					),
				language_xml(
					countryIsoCode=para["countryIsoCode"],languageIsoCode=para["languageIsoCode"]
				),
				issueInfo_xml(
					issueNumber=para["issueNumber"],inWork=para["inWork"]
				)   
			),
			dmAddressItems_xml(
				issueDate_xml(
					day=para["day"], month=para["month"], year=para["year"]
				),
				dmTitle_xml(
					techName_xml(dmCode_para["techName"]),
					infoName_xml(dmCode_para["infoName"])
				)
			)
		),
		dmStatus_xml(
			security_xml(securityClassification=para["securityClassification"]),
			responsiblePartnerCompany_xml(
				enterpriseName_xml("COMAC"),
				enterpriseCode = para["enterpriseCode"]
			),
			originator_xml(
				enterpriseName_xml("COMAC"),
				enterpriseCode = para["enterpriseCode"]
			),
			applicRef_xml(
				applicIdentValue = effect,
				# id = effect_dic[effect]
			),
			brexDmRef_xml(
				dmRef_xml
					(dmRefIdent_xml
						(dmCode_xml
							(modelIdentCode = brex_para["modelIdentCode"],
							systemDiffCode = brex_para["systemDiffCode"],
							systemCode = brex_para["systemCode"],
							subSystemCode = brex_para["subSystemCode"],
							subSubSystemCode = brex_para["subSubSystemCode"],
							assyCode = brex_para["assyCode"],
							disassyCode = brex_para["disassyCode"],
							disassyCodeVariant = brex_para["disassyCodeVariant"],
							infoCode = brex_para["infoCode"],
							infoCodeVariant = brex_para["infoCodeVariant"],
							itemLocationCode = brex_para["itemLocationCode"]              
							)
						)
					)
			),
			qualityAssurance_xml(
				unverified_xml
			),
			issueType = para["issueType"],
		)
	)

	return ident_element
