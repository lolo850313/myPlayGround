def headxml():    
    from lxml import etree
    from lxml.builder import ElementMaker 
    

    #相关初始参数
    #日期 需要修改
    ddnCode_para = {"modelIdentCode":"ARJ21","receiverIdent":"SVV19",
            "senderIdent":"SVV19","seqNumber":"00001","yearOfDataIssue":"2018"}
    para = {"day":"25","month":"06",
            "year":"2019","securityClassification":"01",
            "enterpriseName":"COMAC"}
    dmCode_para = {"modelIdentCode":"ARJ21",
                    "systemDiffCode":"A",
                    "systemCode":"00",
                    "subSystemCode":"0",
                    "subSubSystemCode":"0",
                    "assyCode":"00",
                    "disassyCode":"00",
                    "disassyCodeVariant":"A",                            
                    "infoCode":"022",
                    "infoCodeVariant":"A",
                    "itemLocationCode":"D"}

    
    #构建相关E对象
    E = ElementMaker()
    identAndStatusSection_xml = E.identAndStatusSection
    ddnAddress_xml = E.ddnAddress
    ddnStatus_xml = E.ddnStatus
    ddnIdent_xml = E.ddnIdent
    ddnAddressItems_xml = E.ddnAddressItems
    ddnCode_xml = E.ddnCode
    issueDate_xml = E.issueDate
    dispatchTo_xml = E.dispatchTo
    dispatchAddress_xml = E.dispatchAddress
    enterprise_xml = E.enterprise
    enterpriseName_xml = E.enterpriseName
    address_xml = E.address
    department_xml = E.department
    street_xml = E.street
    city_xml = E.city
    country_xml = E.country
    dispatchFrom_xml = E.dispatchFrom
    ddnStatus_xml = E.ddnStatus
    authorization_xml = E.authorization
    dmCode_xml = E.dmCode
    security_xml = E.security
    brexDmRef_xml = E.brexDmRef
    dmRef_xml = E.dmRef
    dmRefIdent_xml = E.dmRefIdent
    

    #利用E对象创建ident_element树
    ident_element = identAndStatusSection_xml(
        ddnAddress_xml(
            ddnIdent_xml(
                ddnCode_xml                  
                    (modelIdentCode = ddnCode_para["modelIdentCode"],
                    receiverIdent = ddnCode_para["receiverIdent"],
                    senderIdent = ddnCode_para["senderIdent"],
                    seqNumber = ddnCode_para["seqNumber"],
                    yearOfDataIssue = ddnCode_para["yearOfDataIssue"],
                    ) 
            ),
            ddnAddressItems_xml(
                issueDate_xml(
                    day=para["day"], month=para["month"], year=para["year"]
                ),
                dispatchTo_xml(
                    dispatchAddress_xml(
                        enterprise_xml(
                            enterpriseName_xml(para["enterpriseName"])
                        ),
                        address_xml(
                            department_xml,
                            street_xml,
                            city_xml,
                            country_xml
                        )
                    ),
                ),
                dispatchFrom_xml(
                    dispatchAddress_xml(
                        enterprise_xml(
                            enterpriseName_xml("COMAC")
                        ),
                        address_xml(
                            department_xml,
                            street_xml,
                            city_xml,
                            country_xml
                        )
                    ),
                ),
            )
        ),
        ddnStatus_xml(
            security_xml(securityClassification=para["securityClassification"]),
            authorization_xml,
            brexDmRef_xml(
                dmRef_xml
                    (dmRefIdent_xml
                        (dmCode_xml
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
                            itemLocationCode = dmCode_para["itemLocationCode"])
                        )
                    )
            )
        )
    )

    return ident_element
