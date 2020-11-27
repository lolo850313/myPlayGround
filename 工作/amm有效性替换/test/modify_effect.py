
def fileList(path,suffix):
    import os
    subPath = os.listdir(path)
    suffixPath = []
    for i in range(len(subPath)):
        #windows
        # subPath[i] = path + "//" + subPath[i]
        #mac下
        subPath[i] = path + "/" + subPath[i]
    return subPath


def mainReplace(file,old,new):
    f = open(file,"r",encoding = "utf-8")
    lines = f.readlines()
    change = 0       
    for line in lines:
        if line.find(old) != -1:
            line = line.replace(old,new)
            change = 1
    f.close()
    if change == 1:
        f = open(file,"w",encoding ="utf-8")
        f.writelines(lines)
        f.close()

suffix = ".sgm"
path = "/Users/Hewenhao/52AMM"
file_List = fileList(path,suffix)

old = '<effect label="ALL">'
new = '<effect label="105-109,111+.">'
for file in file_List:
    f = open(file,"r",encoding = "utf-8")
    lines = f.readlines()
    change = 0       
    for line in lines:
        if line.find(old) != -1:
            line = line.replace(old,new)
            change = 1
    f.close()
    if change == 1:
        f = open(file,"w",encoding ="utf-8")
        f.writelines(lines)
        f.close()




    