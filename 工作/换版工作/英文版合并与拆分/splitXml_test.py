#批量拆分xml
import os
from lxml import etree

schema = "SSM"
rootPath = "D:\\临时文件\\DDN-ARJ21-07482-SVV19-2020-00034(1)\\"
shema_dir = "C:\\Users\\410684\\Desktop\\小程序\\工作\\shema验证\\S1000D 4.1 Schema\\"
path = rootPath + "合并后\\"
dir = []
res = rootPath + "合并后拆分\\"
initialDir = rootPath + "合并前\\"
for i in os.listdir(path):
    dir.append(path + i)

for f in dir:
    root = etree.parse(f)
    dmoduleArr = root.findall(".//dmodule")
    pre = "DMC-"
    end = ".XML"
    for dmodule in dmoduleArr:
        dmCode = dmodule.find(".//dmCode")
        language = dmodule.find(".//language")
        issueInfo = dmodule.find(".//issueInfo")
        title = pre + dmCode.attrib["modelIdentCode"] + "-" \
        + dmCode.attrib["systemDiffCode"] + "-" \
        +  dmCode.attrib["systemCode"] + "-" \
        + dmCode.attrib["subSystemCode"] \
        + dmCode.attrib["subSubSystemCode"] + "-" \
        + dmCode.attrib["assyCode"] + "-" \
        + dmCode.attrib["disassyCode"] \
        + dmCode.attrib["disassyCodeVariant"] + "-" \
        + dmCode.attrib["infoCode"] \
        + dmCode.attrib["infoCodeVariant"] + "-" \
        + dmCode.attrib["itemLocationCode"] + "_"\
        + issueInfo.attrib["issueNumber"] + "-"\
        + issueInfo.attrib["inWork"] + "_" \
        + language.attrib["languageIsoCode"].upper() + "-" \
        + language.attrib["countryIsoCode"] + end
        etree.ElementTree(dmodule).write(res + title, pretty_print=True,encoding="utf-8")
        file = res + title
        f = open(file, "r", encoding="utf-8")
        line = f.readlines()
        headfile = initialDir + title
        headf = open(headfile, "r", encoding="utf-8")
        headline = headf.readlines()
        add = ""
        for i in headline: 
            if "<dmodule" not in i:
                add = add + is
            else:
                add = add + i[:i.index("<dmodule")]
                break
        line.insert(0,add)
        f.close()
        f = open(file,"w",encoding="utf-8")
        f.writelines(line)
        f.close()
#schema校验
from excel import excelout

xsd_dic = {"SSM":"xml_schema_flat\\descript.xsd"}
shema_file = shema_dir + xsd_dic[schema]
fileList =os.listdir(res)
shema = etree.XMLSchema(etree.parse(shema_file))

list_dic = []
for i in fileList:    
    task = res + i
    data = etree.parse(task)
    shema.validate(data)
    if shema.validate(data) == False:
        for i in (shema.error_log):
            dic = {}
            dic["task"] = i.filename
            dic["path"] = i.path
            dic["message"] = i.message
            list_dic.append(dic)

filename = schema + ".xlsx"
title =["task","path","message"]        
excelout(list_dic,title,rootPath,filename)
