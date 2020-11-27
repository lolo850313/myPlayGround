#拆分翻译后的xml章节xml
from lxml import etree
import os

path = "D:\\测试\\enToZh\\"
fileArr = os.listdir(path)
print(fileArr)
newPath = path + "new\\"
# os.mkdir(newPath)

for i in fileArr:
    if i[-4:] == ".XML":
        file = path + i
        root = etree.parse(file)
        dmoduleArr = root.findall("dmodule")
        for j in dmoduleArr:
            dmcode = j.find(".//dmCode")
            issueNumber = j.find(".//issueInfo").attrib["issueNumber"]
            inWork = j.find(".//issueInfo").attrib["inWork"]
            title = "DMC-" + dmcode.attrib["modelIdentCode"] + "-" + dmcode.attrib["systemDiffCode"] + "-" + \
            dmcode.attrib["systemCode"] + "-" + dmcode.attrib["subSystemCode"] + dmcode.attrib["subSubSystemCode"] + "-" + \
            dmcode.attrib["assyCode"] + "-" + dmcode.attrib["disassyCode"] + dmcode.attrib["disassyCodeVariant"] + "-" +  \
            dmcode.attrib["infoCode"]+dmcode.attrib["infoCodeVariant"] + "-" + dmcode.attrib["itemLocationCode"] + "_" + \
            issueNumber + "-" + inWork + "_" + "EN-US.XML"
            (root).write(newPath + title, encoding="utf-8")

            # etree.Element(j).write(newPath + )
