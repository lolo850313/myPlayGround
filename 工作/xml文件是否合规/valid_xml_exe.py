from lxml import etree
import os

dic = {}

path =  os.path.dirname(os.path.abspath(__file__)) + "\\"
inputTxt = path + "input.txt"
resTxt = path + "output.txt"
f = open(inputTxt,"r",encoding="utf-8")
str = f.read()

errArr = []
for t in os.listdir(str):
    if t[-4:] == ".XML" or t[-4:] == ".xml":
        file = str + "\\" + t
        try:
            root = etree.parse(file)
        except Exception as err:
            errHint = "file: " + t + ",  错误提示： " + repr(err)
            errArr.append(errHint)

if len(errArr) == 0:
    resTxt = path + "xml_pass.txt"
    with open(resTxt, "w") as f:
        f.write("no error")
else:
    with open(resTxt, "w") as f:
        for i in errArr:
            f.write(i)
            f.write("\n")

input("program finished! Press <enter>")
