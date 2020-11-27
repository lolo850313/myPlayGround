#对xml文件增加xml_declaration
def addxml(dirpath):
    import os
    for i in os.listdir(dirpath):
        path = dirpath + i
        f = open(path,"r",encoding="utf-8")
        line = f.readlines()
        add = '<?xml version="1.0" encoding="UTF-8"?>'
        line.insert(0,add)
        
        f.close()
        f = open(path,"w",encoding="utf-8")
        f.writelines(line)
        f.close()

if __name__ == "__main__":
    dirpath = "D:\\测试\\s1000d\\s1000d_fim\\split_To\\"
    addxml(dirpath)