def entityStr(content_element):
    from lxml import etree
    infoEntityIdentList = []
    entityString = '<!DOCTYPE dmodule['
    graphicList = content_element.xpath(".//figure/graphic")
    for i in graphicList:
        infoEntityIdentString = i.attrib["infoEntityIdent"]
        entityString = entityString + '<!ENTITY ' + infoEntityIdentString + ' SYSTEM ' + '\"'+ infoEntityIdentString +'.CGM\" NDATA CGM>'
        
    entityString = entityString + ']>'
    return entityString