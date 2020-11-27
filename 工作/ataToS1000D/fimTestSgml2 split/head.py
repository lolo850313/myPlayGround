#从task中读取相关信息，以供构成S1000D的头信息
def titleInfo(arj_task):
	from lxml import etree

	headDic = {}
	title = arj_task.xpath(".//title")[0].text 
	taskDic = arj_task.attrib
	return title

#从arj_task树中提取task
def taskNumber(arj_task):
	from lxml import etree
 
	taskDic = arj_task.attrib
	taskNum = taskDic["chapnbr"] + "-" +  taskDic["sectnbr"] + "-" + taskDic["subjnbr"] +  "-" + taskDic["func"]  + "-" + taskDic["seq"]
	if "confltr" in taskDic:
		taskNum = taskNum + "-" +  taskDic["confltr"]
	return taskNum

# 从dmrl的excel表中找出taskNum所在的行，将此行D列至M列的信息依次提取，输出dmCode字典。
def findDmCode(dmrlPath,taskNum):
	import xlrd

	book = xlrd.open_workbook(dmrlPath)
	sh = book.sheet_by_index(0)

	rowNumber = sh.nrows
	colNumber = sh.ncols
	for i in range(rowNumber):
		for j in range(colNumber):
			if sh.cell_value(i, 1 ) == taskNum :
				if isinstance(sh.cell_value(i, 8),str):
					result = {"modelIdentCode":str(sh.cell_value(i, 3)),
								"systemDiffCode":str(sh.cell_value(i, 4)),
								"systemCode":str(int(sh.cell_value(i, 5))).zfill(2),
								"subSystemCode":str(sh.cell_value(i, 6))[0],
								"subSubSystemCode":str(sh.cell_value(i, 6))[1],
								"assyCode":str(sh.cell_value(i, 7)),
								"disassyCode":sh.cell_value(i, 8),
								"disassyCodeVariant":str(sh.cell_value(i,9)),
								# 读出来会是浮点数421.0，则先转换为int，再转换为字符串
								"infoCode":str(int(sh.cell_value(i, 10))),
								"infoCodeVariant":str(sh.cell_value(i, 11)),
								"itemLocationCode":str(sh.cell_value(i, 12)),
							  	"DMC":sh.cell_value(i, 13),
							  	"techName":sh.cell_value(i, 14),
							  	"infoName":sh.cell_value(i, 15)
							  }
				else:
					result = {"modelIdentCode": str(sh.cell_value(i, 3)),
							  "systemDiffCode": str(sh.cell_value(i, 4)),
							  "systemCode": str(int(sh.cell_value(i, 5))),
							  "subSystemCode": str(sh.cell_value(i, 6))[0],
							  "subSubSystemCode": str(sh.cell_value(i, 6))[1],
							  "assyCode": str(sh.cell_value(i, 7)),
							  "disassyCode": str(int(sh.cell_value(i, 8))),
							  "disassyCodeVariant": str(sh.cell_value(i, 9)),
							  # 读出来会是浮点数421.0，则先转换为int，再转换为字符串
							  "infoCode": str(int(sh.cell_value(i, 10))),
							  "infoCodeVariant": str(sh.cell_value(i, 11)),
							  "itemLocationCode": str(sh.cell_value(i, 12)),
							  "DMC": sh.cell_value(i, 13),
							  "techName": sh.cell_value(i, 14),
							  "infoName": sh.cell_value(i, 15)
							  }
				return result
				
#获得当前task的taskNum值,通过taskNum在dmrlTable中找到对应的dmrl号  
def find_dmc(arj_task,dmrl_excel) :
	
	taskNum = taskNumber(arj_task)
	dmCode_para = findDmCode(dmrl_excel,taskNum)
	return dmCode_para["DMC"]

def headxml(arj_task,dmrl_excel,effect_dic,issueNumber,date):    
	from lxml import etree
	from lxml.builder import ElementMaker 

	taskNum = taskNumber(arj_task)

	taskEffect = arj_task.find("effect").attrib["label"]
	#通过taskNum在dmrl_excel中找到对应的dmcode信息
	dmCode_para = findDmCode(dmrl_excel,taskNum)
	#将title分隔成techName和infoName
	technamePara = dmCode_para["techName"]
	infonamePara = dmCode_para["infoName"]

	#相关初始参数
	#日期 需要修改
	para = {"techName":technamePara,"infoName":infonamePara,
			"countryIsoCode":"CN","languageIsoCode":"zh",
			"inWork":"00","issueNumber":issueNumber,
			"issueType":"new","day":date["day"],
			"month":date["month"],"year":date["year"],
			"securityClassification":"01","enterpriseCode":"SVV19",
			"applicIdentValue":taskEffect
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
					techName_xml(para["techName"]),
					infoName_xml(para["infoName"])
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
				applicIdentValue = para["applicIdentValue"]
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
			reasonForUpdate_xml(
				simplePara_xml("升版")
			),
			issueType = para["issueType"],
		)
	)

	return ident_element
