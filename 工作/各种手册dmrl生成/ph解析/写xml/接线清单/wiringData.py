def contentFrame(effectARJ,contactIdentARJ,contactPartNumberARJ,dmCode,wireInfo):
    from lxml import etree
    from lxml.builder import ElementMaker    

    E = ElementMaker()

    #************************初始化相关E工厂对象，形成基本树（即不管arj项目如何构成，都需要的基本子元素）
    content_XML = E.content
    wiringData_XML = E.wiringData
    wireGroup_XML = E.wireGroup
    wireAlts_XML = E.wireAlts
    wire_XML = E.wire
    wireIdent_XML = E.wireIdent
    wireNumber_XML = E.wireNumber
    wireConnection_XML = E.wireConnection
    fromEquip_XML = E.fromEquip
    contactInfo_XML = E.contactInfo
    wireConnectionCode_XML = E.wireConnectionCode
    contact_XML = E.contact
    specialConnection_XML = E.specialConnection
    toEquip_XML = E.toEquip
    wireInfo_XML = E.wireInfo
    wireCode_XML = E.wireCode
    wireType_XML = E.wireType
    wireGauge_XML = E.wireGauge
    partNumber_XML = E.partNumber
    harnessIdent_XML = E.harnessIdent
    length_XML = E.length
    wireColor_XML = E.wireColor
    wireRoute_XML = E.wireRoute
    functionalDescrRef_XML = E.functionalDescrRef
    refs_XML = E.refs
    dmRef_XML = E.dmRef
    dmRefIdent_XML = E.dmRefIdent
    electricalEquipGroup_XML = E.electricalEquipGroup
    electricalEquip_XML = E.electricalEquip
    equipName_XML = E.equipName
    dmCode_XML = E.dmCode
   
    wiringData_element = wiringData_XML(
            wireGroup_XML(
                wireAlts_XML(
                    wire_XML(
                        wireIdent_XML
                            (wireNumber_XML(wireInfo["wireNumber"])),
                        wireConnection_XML
                            (fromEquip_XML
                                (contactInfo_XML
                                    (contact_XML(contactIdent=contactIdentARJ,contactPartNumber=contactPartNumberARJ),
                                    wireConnectionCode_XML(specialConnection_XML(wireInfo["specialConnectionFrom"]))
                                    )
                                ),
                            toEquip_XML
                                (contactInfo_XML
                                    (contact_XML(contactIdent=contactIdentARJ,contactPartNumber=contactPartNumberARJ),
                                    wireConnectionCode_XML(specialConnection_XML(wireInfo["specialConnectionTo"]))
                                    )
                                )
                            ),
                        wireInfo_XML
                            (wireCode_XML
                                (
                                    wireType_XML(wireInfo["wireType"]),
                                    wireGauge_XML(wireInfo["wireGauge"])
                                ),
                            partNumber_XML(wireInfo["partNumber"]),
                            harnessIdent_XML(wireInfo["harnessIdent"]),
                            length_XML(wireInfo["length"]),
                            wireColor_XML(wireInfo["wireColor"]),
                            wireRoute_XML(wireInfo["wireRoute"]),
                            functionalDescrRef_XML
                                (refs_XML
                                    (dmRef_XML
                                        (dmRefIdent_XML
                                            (dmCode_XML
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
                                    )
                                )
                            ),
                        applicRefId = effectARJ
                    )
                )
            ),
            #接线设备清单，暂不做
            # electricalEquipGroup_XML
            #     (electricalEquip_XML
            #         (
            #         partNumber_XML(wireInfo["partNumber"]),
            #         equipName_XML(wireInfo["equipName"]),
            #         functionalDescrRef_XML
            #             (refs_XML
            #                 (dmRef_XML
            #                     (dmRefIdent_XML
            #                         (dmCode_XML
            #                             (assyCode = dmCode["assyCode"],
            #                             disassyCode = dmCode["disassyCode"],
            #                             disassyCodeVariant = dmCode["disassyCodeVariant"],
            #                             infoCode = dmCode["infoCode"],
            #                             infoCodeVariant = dmCode["infoCodeVariant"],
            #                             itemLocationCode = dmCode["itemLocationCode"],
            #                             modelIdentCode = dmCode["modelIdentCode"],
            #                             subSubSystemCode = dmCode["subSubSystemCode"],
            #                             subSystemCode = dmCode["subSystemCode"],
            #                             systemCode = dmCode["systemCode"],
            #                             systemDiffCode = dmCode["systemDiffCode"]
            #                             )
            #                         )
            #                     )
            #                 )
            #             )
            #         )
            #     )        
        )

    return wiringData_element






