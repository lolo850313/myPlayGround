#将每个line中的有效性提取出来
#将每个line中，前面是<effect label="，后面是"></effect>，的字符串提取出来
def effectOut(string):
    effectList = []
    end = 0
    while string.find('<effect label="') != -1:
        start = string.find('<effect label="')-15
        end = start + string[start : ].find('"></effect>') + 2
        effect = string[start + 15 : end]
        effectList.append(effect)
        string = string[end :]

    return effectList

# def effectOut(string):
#     effectList = []
#     end = 0
#     while string.find('<effect label="') != -1:
#         start = string.find('<effect label="')-15
#         end = start + string[start : ].find('"></effect>') + 2
#         effect = string[start + 15 : end]
#         effectList.append(effect)
#         string = string[end :]

#     return effectList

# #将路径path中文件的旧字符串old替换为新字符串new
# def mainReplace(path,old,new):
#     f = open(path,"r",encoding="utf-8")
#     line = f.readlines()
#     change = 0
#     for i in range(len(line)):
#         if line[i].find(old) != -1:
#             line[i] = line[i].replace(old,new)
#             change = 1
#     f.close()
#     if change == 1:
#         f = open(path,"w",encoding="utf-8")
#         f.writelines(line)
#         f.close()

