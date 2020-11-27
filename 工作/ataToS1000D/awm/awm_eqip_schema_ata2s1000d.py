import os
from lxml import etree
from excel import excelout
resPath = "D:\\测试\\s1000d\\s1000d_awm\\equipment\\"

ammFilePath = "D:\\测试\\s1000d\\s1000d_awm\\equipment\\extw-output\\"
shema_file = "D:\\测试\\s1000d\\S1000D 4.1 Schema\\xml_schema_flat\\wrngdata.xsd"
fileList =os.listdir(ammFilePath)
shema = etree.XMLSchema(etree.parse(shema_file))
list_dic = []   
for i in fileList:    
    task = ammFilePath + i
    data = etree.parse(task)
    shema.validate(data)
    if shema.validate(data) == False:
        for i in (shema.error_log):
            dic = {}
            dic["task"] = i.filename[-48:]
            # dic["task"] = i.filename[-15:]
            dic["path"] = i.path
            dic["message"] = i.message
            list_dic.append(dic)
# print(list_dic)
filename = "equipSchemaTest.xlsx"
title =["task","path","message"]        
excelout(list_dic,title,resPath,filename)
