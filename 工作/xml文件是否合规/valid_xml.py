from lxml import etree
import os

dic = {}
path = "E:\\手册发布a\\fim201909\\FIM-2019年9月版（已提交）\\"
for t in os.listdir(path):
    if t[-4:] == ".XML" or t[-4:] == ".xml":
        file = path + t
        try:
            root = etree.parse(file)
        except Exception as err:
            print(err)
            dic["file"] = t
            dic ["error info"] = err