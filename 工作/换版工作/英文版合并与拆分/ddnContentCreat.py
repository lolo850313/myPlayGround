def ddnContent(xml_dir):
    from lxml import etree 
    from lxml.builder import ElementMaker 
    import os

    ddnContent_xml = etree.Element("ddnContent")
    deliveryList_xml = etree.SubElement(ddnContent_xml,"deliveryList")

    for i in os.listdir(xml_dir):
        if i[-3:] == "XML" : 
            deliveryListItem_XML = etree.SubElement(deliveryList_xml, 'deliveryListItem')
            dispatchFileName_XML = etree.SubElement(deliveryListItem_XML, 'dispatchFileName')
            dispatchFileName_XML.text = i
            issueInfo_XML = etree.SubElement(deliveryListItem_XML, 'issueInfo')
            print(i)
            issueNumber = i.split("_")[1][:3]
            inWork = i.split("_")[1][4:6]
            issueInfo_XML.set("inWork",inWork)
            issueInfo_XML.set("issueNumber",issueNumber)
        if i[-3:] == "xml" : 
            deliveryListItem_XML = etree.SubElement(deliveryList_xml, 'deliveryListItem')
            dispatchFileName_XML = etree.SubElement(deliveryListItem_XML, 'dispatchFileName')
            dispatchFileName_XML.text = i
            issueInfo_XML = etree.SubElement(deliveryListItem_XML, 'issueInfo')
            issueNumber = i.split("_")[1][:3]
            inWork = i.split("_")[1][4:6]
            issueInfo_XML.set("inWork",inWork)
            issueInfo_XML.set("issueNumber",issueNumber)
        if i[-3:] == "cgm" : 
            deliveryListItem_XML = etree.SubElement(deliveryList_xml, 'deliveryListItem')
            dispatchFileName_XML = etree.SubElement(deliveryListItem_XML, 'dispatchFileName')
            dispatchFileName_XML.text = i
        if i[-3:] == "CGM" : 
            deliveryListItem_XML = etree.SubElement(deliveryList_xml, 'deliveryListItem')
            dispatchFileName_XML = etree.SubElement(deliveryListItem_XML, 'dispatchFileName')
            dispatchFileName_XML.text = i
        if i[-3:] == "tif" : 
            deliveryListItem_XML = etree.SubElement(deliveryList_xml, 'deliveryListItem')
            dispatchFileName_XML = etree.SubElement(deliveryListItem_XML, 'dispatchFileName')
            dispatchFileName_XML.text = i
        if i[-3:] == "jpg" : 
            deliveryListItem_XML = etree.SubElement(deliveryList_xml, 'deliveryListItem')
            dispatchFileName_XML = etree.SubElement(deliveryListItem_XML, 'dispatchFileName')
            dispatchFileName_XML.text = i               

    return ddnContent_xml





