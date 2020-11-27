from lxml import etree
xmlFile = 'd://homemade.xml'
task = etree.parse(xmlFile)
head_list = task.xpath(".//link")

def cirXml(circuitBreakerNumber):
            from lxml import etree
            circuitBreakerDescrGroup = etree.Element("circuitBreakerDescrGroup")
            circuitBreakerDescrSubGroup = etree.SubElement(circuitBreakerDescrGroup,"circuitBreakerDescrSubGroup")
            circuitBreakerDescr = etree.SubElement(circuitBreakerDescrSubGroup,"circuitBreakerDescr")
            circuitBreakerRef = etree.SubElement(circuitBreakerDescr,"circuitBreakerRef")
            circuitBreakerRef.set("circuitBreakerNumber",circuitBreakerNumber)
            return circuitBreakerDescrGroup


for i in head_list:
    i.attrib["herf"] = "qq"
print(etree.tostring(task,pretty_print=True))
task.write(xmlFile,pretty_print=True,encoding="utf-8")
# etree.ElementTree(page).write('/Users/hewenhao/dmrl/homemade.xml',pretty_print=True,encoding="utf-8")