htmlf=open('D:\\pdf结构化\\test.html','r',encoding="utf-8")
htmlcont=htmlf.readlines()
for i in (htmlcont):
    if '©Copyright 2019' in i:
        print(i)