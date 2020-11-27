import os
from lxml import etree
from excel import excelout
resPath = "D:\\测试\\s1000d\\s1000d_aipc\\"

aipcFilePath = "D:\\测试\\s1000d\\s1000d_aipc\\aipc_dmrl\\"
shema_file = "D:\\测试\\s1000d\\S1000D 4.1 Schema\\xml_schema_flat\\ipd.xsd"
fileList =os.listdir(aipcFilePath)
shema = etree.XMLSchema(etree.parse(shema_file))
list_dic = []   
for i in fileList:    
    task = aipcFilePath + i
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

filename = "aipc_schemaTest.xlsx"
title =["task","path","message"]        
excelout(list_dic,title,resPath,filename)
