#将xml_declaration的单引号改为双引号
path = "D://测试//s1000d//s1000d_fim//dmrl//DMC-ARJ21-A-05-51-00-A3A-421A-A_001-00_ZH-CN.XML"
f = open(path,"r",encoding="utf-8")
line = f.readlines()
line[0] = '<?xml version="1.0" encoding="UTF-8"?>'
f.close()
f = open(path,"w",encoding="utf-8")
f.writelines(line)
f.close()