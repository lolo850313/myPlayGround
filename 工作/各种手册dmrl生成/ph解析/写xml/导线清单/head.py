def headxml(path):    
    from lxml import etree
    from lxml.builder import ElementMaker 
    from excelRead import dmCodeDic

    #通过excel文件获取dmcode信息
    dmCode = dmCodeDic(path)

    #确定线束号
    harnessName ="-W" + dmCode["subSystemCode"] + dmCode["subSubSystemCode"] + dmCode["disassyCode"]

    #相关初始参数
    #日期 需要修改
    para = {"techName":"WIRE LIST" + harnessName,"infoName":"Wiring diagram",
            "countryIsoCode":"US","languageIsoCode":"sx",
            "inWork":"00","issueNumber":"001",
            "issueType":"new","day":"10",
            "month":"10","year":"2018",
            "securityClassification":"01","enterpriseCode":"SVV19",
            "applicIdentValue":"appsp-model-C919"
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
                    (assyCode = dmCode["assyCode"],
                    disassyCode = dmCode["disassyCode"],
                    disassyCodeVariant = dmCode["disassyCodeVariant"],
                    infoCode = dmCode["infoCode"],
                    infoCodeVariant = dmCode["infoCodeVariant"],
                    itemLocationCode = dmCode["itemLocationCode"],
                    modelIdentCode = dmCode["modelIdentCode"],
                    subSubSystemCode = dmCode["subSubSystemCode"],
                    subSystemCode = dmCode["subSystemCode"],
                    systemCode = dmCode["systemCode"],
                    systemDiffCode = dmCode["systemDiffCode"]
                    ),
                language_xml(
                    countryIsoCode=para["countryIsoCode"],languageIsoCode=para["languageIsoCode"]
                ),
                issueInfo_xml(
                    inWork=para["inWork"],issueNumber=para["issueNumber"]
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
                            (assyCode = dmCode["assyCode"],
                            disassyCode = dmCode["disassyCode"],
                            disassyCodeVariant = dmCode["disassyCodeVariant"],
                            infoCode = dmCode["infoCode"],
                            infoCodeVariant = dmCode["infoCodeVariant"],
                            itemLocationCode = dmCode["itemLocationCode"],
                            modelIdentCode = dmCode["modelIdentCode"],
                            subSubSystemCode = dmCode["subSubSystemCode"],
                            subSystemCode = dmCode["subSystemCode"],
                            systemCode = dmCode["systemCode"],
                            systemDiffCode = dmCode["systemDiffCode"]
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
