# #将转换文件名录入列表中
# import os
# txtFile = os.listdir("d:/txt/")

# #读取文件
# file = open("d:/txt/"+txtFile[0],"r")
file = open("d:/txt/26-01-00-810-816-APU灭火瓶低压离散信号线失效-20180712.txt","r")
#将file中的语句录入列表中
textList=[]
for i in file:
    textList.append(i)

#将段落位置录入sectionLocation
# sectionLocation = []

# for i in range(len(textList)):
#     if (textList[i].strip()[-5:])==".  概述":
#         sectionLocation.append({"概述":i})
#     if (textList[i].strip()[-8:])==".  可能的原因":
#         sectionLocation.append({"可能的原因":i})
#     if (textList[i].strip()[-8:])==".  相关断路器":
#         sectionLocation.append({"相关断路器":i})
#     if (textList[i].strip()[-7:])==".  初始评估":
#         sectionLocation.append({"初始评估":i})
#     if (textList[i].strip()[-9:])==".  故障隔离程序":
#         sectionLocation.append({"故障隔离程序":i})
#     if (textList[i].strip()[-4:])=="任务结束":
#         sectionLocation.append({"任务结束":i}) 

sectionLocation = {}

for i in range(len(textList)):
    if (textList[i].strip()[-5:])==".  概述":
        sectionLocation["概述"]=i
    if (textList[i].strip()[-8:])==".  可能的原因":
        sectionLocation["可能的原因"]=i
    if (textList[i].strip()[-8:])==".  相关断路器":
        sectionLocation["相关断路器"]=i
    if (textList[i].strip()[-7:])==".  初始评估":
        sectionLocation["初始评估"]=i
    if (textList[i].strip()[-9:])==".  故障隔离程序":
        sectionLocation["故障隔离程序"]=i
    if (textList[i].strip()[-9:])==".  故障修复确认":
        sectionLocation["故障修复确认"]=i
    if (textList[i].strip()[-4:])=="任务结束":
        sectionLocation["任务结束"]=i   


from xml.dom.minidom import Document
doc = Document()
task = doc.createElement("task")
tfmatr = doc.createElement("tfmatr")
task.appendChild(tfmatr)

#doc在tfmatr下生成pretopic标签，使其有title标签，且title为string
def tfmatrAddPretopic(pretopicX,titleX,title_textX,string):
    pretopicX = doc.createElement("pretopic")
    tfmatr.appendChild(pretopicX)
    titleX = doc.createElement("title")
    pretopicX. appendChild(titleX)
    title_textX = doc.createTextNode(string) 
    titleX.appendChild(title_textX) 

pretopic1=0
title1=0
title_text1=0
pretopic2=0
title2=0
title_text2=0
pretopic3=0
title3=0
title_text3=0
pretopic4=0
title4=0
title_text4=0

if ("概述" ) in sectionLocation:
    tfmatrAddPretopic(pretopic1,title1,title_text1,'概述')
if ("可能的原因" ) in sectionLocation:
    tfmatrAddPretopic(pretopic2,title2,title_text2,'可能的原因')
if ("相关断路器" ) in sectionLocation:
    tfmatrAddPretopic(pretopic3,title3,title_text3,'相关断路器')
if ("初始评估" ) in sectionLocation:
    tfmatrAddPretopic(pretopic4,title4,title_text4,'初始评估')


#写入topic,subtask标签及其标题
if ("故障隔离程序" ) in sectionLocation:
    topic = doc.createElement("topic")
    task.appendChild(topic)
    title_topic = doc.createElement("title")
    topic.appendChild(title_topic)
    title_text_topic = doc.createTextNode("故障隔离程序") 
    title_topic.appendChild(title_text_topic)
    subtask = doc.createElement("subtask")
    topic.appendChild(subtask)

if ("故障修复确认" ) in sectionLocation:
    topicEnd = doc.createElement("topic")
    task.appendChild(topicEnd)
    title_topicEnd = doc.createElement("title")
    topicEnd.appendChild(title_topicEnd)
    title_text_topicEnd = doc.createTextNode("故障修复确认") 
    title_topicEnd.appendChild(title_text_topicEnd)
    subtaskEnd = doc.createElement("subtask")
    topicEnd.appendChild(subtaskEnd)

#根据sectionLocation将textList分段
sec = 0
masterSecLoc = []
secList = []
for i in sectionLocation.values():
    masterSecLoc.append(i)
while sec<len(masterSecLoc)-1:
    secList.append(textList[masterSecLoc[sec]:masterSecLoc[sec+1]])
    sec = sec + 1


re_dig = r'[0-9]{1,2}'
re_lower = r'[a-z]{1}'
re_upper = r'[A-Z]{1}'
#根据段落标志生成{层级：内容}字典
import re
def paraDic(list):
    dic ={}
    for i in list:
        if i[0] == "(" and i[2] == ")":
            if re.match(re_dig,i[1]):
                if "item1" in dic:
                    dic["item1"].append(i)                    
                else:
                    dic["item1"]=[]
                    dic["item1"].append(i) 
            if re.match(re_lower,i[1]):
                if "item2" in dic:
                    dic["item2"].append(i)                    
                else:
                    dic["item2"]=[]
                    dic["item2"].append(i) 
        else:
            if re.match(re_lower,i[0]):
                if "item3" in dic:
                    dic["item3"].append(i)                    
                else:
                    dic["item3"]=[]
                    dic["item3"].append(i) 
    return dic

secDicList = []
for i in secList:
    secDicList.append(paraDic(i))

#按照{层级：内容}字典使用DOM生成xml

#实现树
# myTree = ['a',   #root
#       ['b',  #left subtree
#        ['d' [], []],
#        ['e' [], []] ],
#       ['c',  #right subtree
#        ['f' [], []],
#        [] ]
#      ]

#使用python实现 多叉树。有一串数据abcd abe abcf，insert("abcd",1)便可实现最左边的插入，
# serch("ABE")，便可返回Node，获得值30
class node:
 
    def __init__(self, data):
        self._data = data
        self._children = []
 
    def getdata(self):
        return self._data
 
    def getchildren(self):
        return self._children
 
    def add(self, node):
        self._children.append(node)
 
    def go(self, data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None
 
class tree:
 
    def __init__(self):
        self._head = node('header')
 
    def linktohead(self, node):
        self._head.add(node)
 
    def insert(self, path, data):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return False
            else:
                cur = cur.go(step)
        cur.add(node(data))
        return True
 
    def search(self, path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return None
            else:
                cur = cur.go(step)
        return cur
                   


title = doc.createElement("title")
title_text = doc.createTextNode('概述') 
pretopic.appendChild(title)
title.appendChild(title_text)

list1 = doc.createElement("list1")
pretopic.appendChild(list1)

l1item = doc.createElement("l1item")
list1.appendChild(l1item)

para = doc.createElement("para")
list1.appendChild(para)

list2 = doc.createElement("list2")
list1.appendChild(list2)

l2item = doc.createElement("l2item")
list2.appendChild(para)

f = open("d:/tel.xml","w",encoding="utf-8")

doc.writexml(f)

f.close()