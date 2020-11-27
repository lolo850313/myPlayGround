
def fileList(path,suffix):
    import os
    subPath = os.listdir(path)
    suffixPath = []
    for i in range(len(subPath)):
        #windows
        # subPath[i] = path + "//" + subPath[i]
        #mac下
        subPath[i] = path + "/" + subPath[i]

    for i in subPath:
        if i[-4:] == suffix:
            suffixPath.append(i)

    return suffixPath


def mainReplace(file,old,new):
    f = open(file,"r",encoding="utf-8")
    lines = f.readlines()
    change = 0       
    for i in range(len(lines)):
        if lines[i].find(old) != -1:
            lines[i] = lines[i].replace(old,new)
            change = 1
    f.close()
    if change == 1:
        f = open(file,"w",encoding="utf-8")
        f.writelines(lines)
        f.close()

suffix = ".sgm"
path = "/Users/Hewenhao/52AMM"
file_List = fileList(path,suffix)
for i in file_List:
    mainReplace(i,'<effect label="ALL">','<effect label="105-109,111+.">')
    mainReplace(i,'<effect label="105+.">','<effect label="105-109,111+.">')





    