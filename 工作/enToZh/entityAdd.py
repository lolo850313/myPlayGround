#将xml_declaration的单引号改为双引号
import os
old = "D:\\测试\\enToZh\\old\\"
new = "D:\\测试\\enToZh\\new\\"
for i in os.listdir(old):
    #获得entity
    f = open(old + i, "r", encoding="utf-8")
    line = f.readlines()
    entityIndex = 0
    for j in range(len(line)):
        if "<dmodule" in line[j]:
            entityIndex = j
    head = line[:entityIndex]
    f.close()

    #翻译后的正文
    f = open(new + i, "r", encoding="utf-8")
    line = f.readlines()
    f.close()

    #写成文件
    f = open(new + i, "w", encoding="utf-8")
    line = head + line
    f.writelines(line)
    f.close()
# f.writelines(line)
# f.close()