from lxml import etree
from os import listdir
from excel import excelout
path =  __file__[:-7] + "input/"
res = __file__[:-7]

dataList = []
fileList = listdir(path)
for i in fileList:
    filePath = path + i
    root = etree.parse(filePath)

    #获得关联元素
    refId = root.xpath("//*[@reasonForUpdateRefIds]")    
    data2 = {}
    for k in refId:        
        for rs in k.attrib["reasonForUpdateRefIds"].split():
            data2[rs] = {}
            data2[rs]["元素id值"] = k.attrib["id"]
            if "changeType" in k.attrib:
                data2[rs]["changeType"] = k.attrib["changeType"]
            else:
                data2[rs]["changeType"] = ""
            data2[rs]["reasonForUpdateRefIds"] = rs
            data2[rs]["元素完整路径"] = root.getpath(k)
            data2[rs]["带changeMark属性的子元素"] = ""
            changeMarkList = k.xpath("//*[@changeMark]")
            for cc in changeMarkList:
                data2[rs]["带changeMark属性的子元素"] = cc.tag+","+data2[rs]["带changeMark属性的子元素"]
    

    simpleParaList = root.findall(".//reasonForUpdate")
    for j in simpleParaList:
        data = {"DMC":i}
        data["./@updateReasonType"] = j.attrib["updateReasonType"]
        data["./simplePara"] = j.xpath("./simplePara")[0].text
        if "id" in j.attrib:
            data["id"] = j.attrib["id"]
            tmpId = data["id"]
            data["元素id值"] = data2[tmpId]["元素id值"]
            data["changeType"] = data2[tmpId]["changeType"]
            data["元素完整路径"] = data2[tmpId]["元素完整路径"]
            data["带changeMark属性的子元素"] = data2[tmpId]["带changeMark属性的子元素"]
        else:
            data["id"] = ""
            data["元素id值"] = ""
            data["changeType"] = ""
            data["元素完整路径"] = ""
            data["带changeMark属性的子元素"] = ""
        dataList.append(data)
title = ["DMC","./simplePara","./@updateReasonType","id","元素完整路径","changeType","带changeMark属性的子元素"]
filename = "reasonForUpDate.xls"
excelout(dataList,title,res,filename)
    