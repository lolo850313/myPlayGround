#-*-coding:utf-8-*-
from sgmEffect import effectOut

#从文件夹path中将后缀为suffix的文件的完整路径变成列表输出
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

    #如果文件在二级文件夹下，则需这段
    # for i in range(len(subPath)):
    #      childPath = os.listdir(subPath[i])
    #      for j in childPath:
    #          if j[-4:] == ".sgm" :
    #              suffixPath.append(subPath[i] + "//" +  j)
    # return suffixPath

    return suffixPath


suffix = ".sgm"
path = "/Users/Hewenhao/52AMM"
file_List = fileList(path,suffix)

effectTotal = []
for file in file_List:
    f = open(file,"r",encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        if line.find('<effect label="'):
            for effect in effectOut(line):
                effectTotal.append(effect)

#effect去重
effectTotal = list(set(effectTotal))
effect_file = open("/Users/Hewenhao/effect.txt","w")
for i in effectTotal:
    effect_file.write(i + "\n")
print(effectTotal)



