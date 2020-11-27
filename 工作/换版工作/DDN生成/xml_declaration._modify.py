import os
path = "D:\\临时文件\\ccom\\12\\"
for i in os.listdir(path):
    if i[-4:] == ".XML" or i[-4:] == ".xml":
        file = path + i
        f = open(file, "r", encoding="utf-8")
        line = f.readlines()
        line[0] = '<?xml version="1.0" encoding="UTF-8"?>'
        f.close()
        f = open(file,"w",encoding="utf-8")
        f.writelines(line)
        f.close()