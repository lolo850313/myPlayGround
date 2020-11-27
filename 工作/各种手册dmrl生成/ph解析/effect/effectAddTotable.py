#将文件夹名中的有效性添加到excel表中
import xlwt
import os

path = "/Users/Hewenhao/ph_Wire/"

#打开次级文件夹
subDirList = os.listdir(path)
subDirList_withPath = []

#获得次级文件夹的完整路径
for i in subDirList:
    subDirList_withPath.append(path + i + "/")

fileList = []
fileList_withPath = []
for i in subDirList_withPath:
    for j in os.listdir(i):
        for file in os.listdir(i + j):
            print(file)

# data = xlrd.open_workbook('path')
# tabel = data.sheets[0]

# tabel.cell(0,0).value