#用于批量处理英文xml中错误str。
import os
dir = "E:\\手册发布a\\fim201909\\FIM-2019年9月版（已提交）\\"
# dir = "C:\\Users\\410684\\Desktop\\手册发布\\AWM-2019年3月版\\"
arr = []
for i in os.listdir(dir):
	if i[-4:] == ".xml" or i[-4:] == ".XML":
		arr.append(dir+i)

strReplace = []

def alter(file, old_str, new_str):
	fileDate = ""
	with open(file,"r", encoding="utf-8") as f1:
		for line in f1:
			if old_str in line:
				line = line.replace(old_str , new_str)
			fileDate += line 
	with open(file,"w", encoding="utf-8") as f2:
		f2.write(fileDate)
		
for i in arr:
	print(i)
	if i[-4:] == ".XML" or 	i[-4:] == ".xml":
		alter(i ,"&minus;", "-")
		alter(i ,"&deg;", "°")
		alter(i ,"&ndash;", "-")
		alter(i ,"&horbar;", "—")
		alter(i ,"&mgr;", "μ")
		alter(i ,"&OHgr;", "Ω")
		alter(i ,"&square;", "□")
		alter(i ,"&ordm;", "º")
		alter(i ,"&uarr;", "↑")
		alter(i ,"&darr;", "↓")
		alter(i ,"&utri;", "▵")
		alter(i ,"&times;", "×")