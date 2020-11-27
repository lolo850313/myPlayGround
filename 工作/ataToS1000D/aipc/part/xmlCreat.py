def partSpecCreat(dic):
    idDic = dic.copy()
    for i in idDic:
        if "/" in idDic[i]:
            idDic[i] = idDic[i].replace("/", "--")
            # print(idDic[i])
        if " " in idDic[i]:
            idDic[i] = idDic[i].replace(" ", "--")
            # print(idDic[i])
    from lxml import etree
    partSpec = etree.Element("partSpec")
    partSpec.set("id","part" + "-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"])
    partIdent = etree.SubElement(partSpec,"partIdent")
    partIdent.set("partNumberValue",dic["pnr"])
    partIdent.set("manufacturerCodeValue",dic["pnrmfr_mfr"])
    itemIdentData = etree.SubElement(partSpec,"itemIdentData")
    descrForPart = etree.SubElement(itemIdentData,"descrForPart")
    descrForPart.text = dic["kwd"]
    specDocumentId = 1
    if dic["lbl"].strip() != "" or dic["tbm"].strip() != "":
        techData = etree.SubElement(partSpec,"techData")
        if dic["lbl"].strip() != "":
            specDocument = etree.SubElement(techData,"specDocument")
            specDocument.set("id", "spd-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"]  + "-" + str(specDocumentId).zfill(3))
            specDocumentId += 1
            refs = etree.SubElement(specDocument,"refs")
            externalPubRef = etree.SubElement(refs,"externalPubRef")
            externalPubRefIdent = etree.SubElement(externalPubRef,"externalPubRefIdent")
            externalPubRef.set("id","ePRef-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-001")
            externalPubCode = etree.SubElement(externalPubRefIdent,"externalPubCode")
            externalPubCode.set("pubCodingScheme",dic["lbl"].split(" ")[0])
            externalPubCode.text = dic["lbl"].split(" ")[1]
            externalPubTitle = etree.SubElement(externalPubRefIdent,"externalPubTitle")
            externalPubTitle.text = dic["lbl"]
        if dic["tbm"].strip() != "":
            tbmList = dic["tbm"].split(",")
            aa = tbmList[0][:tbmList[0].find(" IN")]
            bb = tbmList[1][:tbmList[1].find(" IN")]
            cc = tbmList[2][:tbmList[2].find(" MM.")]
            dd = tbmList[3][:tbmList[3].find(" ")]
            ee = tbmList[3][tbmList[3].find(" "):].strip()

            specDocument1 = etree.SubElement(techData,"specDocument")
            specDocument1.set("specDocumentType", "SPEC")
            specDocument1.set("id", "spd-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-" + str(specDocumentId).zfill(3))
            specDocumentId += 1
            specDocument1.set("specDocumentNumber", dd)
            specDocument2 = etree.SubElement(techData,"specDocument")
            specDocument2.set("id", "spd-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-" + str(specDocumentId).zfill(3))
            specDocumentId += 1
            specDocument2.set("specDocumentType", "MATL")
            specDocument2.set("specDocumentNumber", ee)

            quantity1 = etree.SubElement(techData,"quantity")
            quantity1.set("quantityType","qty56")
            # quantity1.set("id", "qtt-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-001")
            quantityGroup1 = etree.SubElement(quantity1,"quantityGroup")
            quantityValue1 = etree.SubElement(quantityGroup1,"quantityValue")
            quantityValue1.set("quantityUnitOfMeasure","in")
            quantityValue1.text = aa

            quantity2 = etree.SubElement(techData,"quantity")
            quantity2.set("quantityType","qty62")
            # quantity2.set("id", "qtt-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-002")
            quantityGroup2 = etree.SubElement(quantity2,"quantityGroup")
            quantityValue2 = etree.SubElement(quantityGroup2,"quantityValue")
            quantityValue2.set("quantityUnitOfMeasure","in")
            quantityValue2.text = bb

            quantity3 = etree.SubElement(techData,"quantity")
            quantity3.set("quantityType","qty01")
            # quantity3.set("id", "qtt-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-003")
            quantityGroup3 = etree.SubElement(quantity3,"quantityGroup")
            quantityValue3 = etree.SubElement(quantityGroup3,"quantityValue")
            quantityValue3.set("quantityUnitOfMeasure","mm")
            quantityValue3.text = cc

    if dic["opt"].strip() != "" or dic["optmfr_mfr"].strip() != "" or dic["lsp"].strip() != "" or dic["lspmfr_mfr"].strip() != "" or dic["pni"].strip() != "" or dic["pnimfr_mfr"].strip() != "" or dic["lfmmfr_ifm"].strip() != "" or dic["lfmmfr_mfr"].strip() != "":
        partRefGroup = etree.SubElement(partSpec,"partRefGroup") 
        if dic["opt"].strip() != "" or dic["pni"].strip() != "":
            optionalPart = etree.SubElement(partRefGroup,"optionalPart")
            optionalPart.set("id", "opt-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-001")
            if dic["opt"].strip() != "":                
                optList = dic["opt"].split("\n")
                optmfr_mfrList = dic["optmfr_mfr"].split("\n")
                for num in range(len(optList)):
                    if optList[num] != "":
                        partRef = etree.SubElement(optionalPart,"partRef")
                        partRef.set("partNumberValue",optList[num])
                        partRef.set("manufacturerCodeValue",optmfr_mfrList[num])
            if dic["pni"].strip() != "":
                pniList = dic["pni"].split("\n")
                pnimfr_mfrList = dic["pnimfr_mfr"].split("\n")
                for num in range(len(pniList)):
                    if pniList[num] != "":
                        partRef = etree.SubElement(optionalPart,"partRef")
                        partRef.set("partNumberValue",pniList[num])
                        partRef.set("manufacturerCodeValue",pnimfr_mfrList[num])
        if dic["lsp"].strip() != "":
            alteredFromPart = etree.SubElement(partRefGroup,"alteredFromPart")
            alteredFromPart.set("id", "alt-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-001")
            lspList = dic["lsp"].split("\n")
            lspmfr_mfrList = dic["lspmfr_mfr"].split("\n")
            for num in range(len(lspList)):
                if lspList[num] != "":
                    partRef = etree.SubElement(alteredFromPart,"partRef")
                    partRef.set("partNumberValue",lspList[num])
                    partRef.set("manufacturerCodeValue",lspmfr_mfrList[num])
        if dic["lfmmfr_ifm"].strip() != "":
            localFabricationMaterial = etree.SubElement(partRefGroup,"localFabricationMaterial")
            localFabricationMaterial.set("id", "lm-" + idDic["pnr"] + "."+ idDic["pnrmfr_mfr"] + "-001")
            lfmmfr_ifmList = dic["lfmmfr_ifm"].split("\n")
            lfmmfr_mfrList = dic["lfmmfr_mfr"].split("\n")
            for num in range(len(lfmmfr_ifmList)):
                if lfmmfr_ifmList[num] != "":
                    partRef = etree.SubElement(localFabricationMaterial,"partRef")
                    partRef.set("partNumberValue",lfmmfr_ifmList[num])
                    partRef.set("manufacturerCodeValue",lfmmfr_mfrList[num])
    return partSpec


