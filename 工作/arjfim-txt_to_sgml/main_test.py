file = open("d:/txt/26-01-00-810-816-APU灭火瓶低压离散信号线失效-20180712.txt","r")

textList=[]
for i in file:
    textList.append(i)

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
    if (textList[i].strip()[-4:])=="任务结束":
        sectionLocation["任务结束"]=i   

#dom初始化操作
from xml.dom.minidom import Document
doc = Document()
task = doc.createElement("task")
tfmatr = doc.createElement("tfmatr")
doc.appendChild(task)
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

 

f = open("d:/tel.xml","w",encoding="utf-8")

doc.writexml(f)

f.close()