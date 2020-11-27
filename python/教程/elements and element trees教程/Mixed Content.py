#混合文本。将一个xml元素插入文本中。
from lxml import etree
html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

dmcString = "<externalPubRef><externalPubRefIndent><externalPubCode>AMM</externalPubCode><externalPubTitle>AAA</externalPubTitle></externalPubRefIndent></externalPubRef>"
replaceString =etree.fromstring(dmcString)
body.append(replaceString)

replaceString.tail = "TAIL"
print(etree.tostring(html,pretty_print=True))