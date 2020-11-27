def headxml(dmCode_para,effect_dic,issueNumber,date):    
	from lxml import etree
	from lxml.builder import ElementMaker 

	#相关初始参数
	#日期 需要修改
	para = {"techName":dmCode_para["techName"],"infoName":dmCode_para["infoName"],
			"countryIsoCode":"CN","languageIsoCode":"zh",
			"inWork":"01","issueNumber":issueNumber,
			"issueType":"new","day":date["day"],
			"month":date["month"],"year":date["year"],
			"securityClassification":"01","enterpriseCode":"SVV19",
			"applicIdentValue":"appsp-asn1-101~999"
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

def effect_xml(effect_dic):
    from lxml.builder import ElementMaker
    from lxml import etree
 
    referencedApplicGroupRef = etree.Element("referencedApplicGroupRef")
    for i in effect_dic:
        applicRef_xml = etree.SubElement(referencedApplicGroupRef,"applicRef")
        applicRef_xml.set("applicIdentValue",i)
        applicRef_xml.set("id",effect_dic[i])
    
    return referencedApplicGroupRef