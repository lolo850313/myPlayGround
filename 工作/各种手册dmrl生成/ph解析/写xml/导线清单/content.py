def contentxml(path):
    from lxml.builder import ElementMaker 
    from lxml import etree
    from wiringData import wiring_frame
    from excelRead import wireDic,dmCodeDic

    #从excel所在的文件夹名中提取，如果有效性在列表中，则应该把此参数放于excelread文件中
    effectARJ = "10101"

    #从excel中提取线束信息
    excelInfo_list = wireDic(path)

    #从excel中提取dmCode信息
    dmCode = dmCodeDic(path)

    #生成content头
    content = etree.Element("content")
    wiringData_XML = etree.SubElement(content, "wiringData")
    wireGroup_XML = etree.SubElement(wiringData_XML, "wireGroup")
    wireAlts_XML = etree.SubElement(wireGroup_XML, "wireAlts")


    #循环生成线束xml，并添加至wirealts元素下
    for i in excelInfo_list:
        #从ph中提取wireColor，contactPartNumberARJ，partNumber，暂设默认
        phInfo = {"接触件件号" : "接触件件号","导线零件号" : "导线零件号","导线颜色" : "导线颜色"}   

        excelInfo = i

        wiring_xml = wiring_frame(effectARJ,dmCode,excelInfo,phInfo)

        #将wiring添加到content中
        wireAlts_XML.append(wiring_xml)

    return content


