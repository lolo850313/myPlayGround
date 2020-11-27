def effect_to_dic(arj_task,taskEffect):
    from lxml import etree 

    #将本章节下的有效性提取到列表中
    effectARJ = arj_task.xpath(".//effect")
    effect_list = []
    for i in range(len(effectARJ)):
        if "label" in effectARJ[i].attrib:
            effect_list.append(effectARJ[i].attrib["label"])
        else:
            effect_list.append("101+.")

    #有效性去重
    effect_list = list(set(effect_list))

    effect_dic = {}
    tmpI = 1
    for i in range(len(effect_list)):
        if effect_list[i] != taskEffect:
            effect_dic[effect_list[i]] = "appRef-" + str(tmpI+1).zfill(4)
            tmpI = tmpI + 1
    return effect_dic

#生成referencedApplicGroupRef的xml树，输入是有效性和流水号的字典。
def effect_xml(effect_dic,taskEffect):
    from lxml.builder import ElementMaker
    from lxml import etree
 
    referencedApplicGroupRef = etree.Element("referencedApplicGroupRef")
    for i in effect_dic:
        applicRef_xml = etree.SubElement(referencedApplicGroupRef,"applicRef")
        applicRef_xml.set("applicIdentValue",i)
        applicRef_xml.set("id",effect_dic[i])
    
    return referencedApplicGroupRef

#将effect标签写入content中
def effect_insert_content(arj_task,content_element):
    #生成effect字典
	effect_dic = effect_to_dic(arj_task)

	#将有效性参引写入content中
	referencedApplicGroupRef = effect_xml(effect_dic)
	content_element.insert(0,referencedApplicGroupRef)

def faultcode(arj_task):
    import re

    re_faultCode = r'[0-9]{3}\s[0-9]{3}\s[0-9]{2}'
    re_faultCode2 = r'[A-Z][0-9]{2}\s[0-9]{2}\s[-]{3}'
    #读取pretopic
    pretopicARJ = arj_task.findall(".//pretopic")    

    #有些“概述”是“概述 ”，故通过位置，即第一个pretopic为概述
    if len(pretopicARJ)==0:
        return "此任务没有pretopic"
    pretopic_commonInfo = pretopicARJ[0]
    #从概述对象下所有的para元素中找出符合正则表达式的故障代码    
    faultCodeARJ = pretopic_commonInfo.findall(".//para")
    faultCodeArr = []

    for para in faultCodeARJ:
        faultCode = re.findall(re_faultCode,para.text)
        faultCode2 = re.findall(re_faultCode2,para.text)
        for subTmp in faultCode:
            faultCodeArr.append(subTmp)
        for subTmp in faultCode2:
            faultCodeArr.append(subTmp)
    faultCode = ",".join(faultCodeArr)

    return faultCode