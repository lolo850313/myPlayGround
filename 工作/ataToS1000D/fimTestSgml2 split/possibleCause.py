#可能的原因，将可能的原因添加到possibleCauseGroup中
def possibleCause_creat(arj_task,content_element):
    from lxml import etree
    pretopic_list = arj_task.xpath(".//pretopic")
    possibleCause = []
    for i in pretopic_list:
        if i.find("title").text:
            if "原因" in i.find("title").text:
                for j in i.xpath(".//para"):
                    possibleCause.append(j.text)

    possibleCauseGroup = content_element.find(".//possibleCauseGroup")
    if len(possibleCause) > 0:
        for i in possibleCause:
            otherPossibleCause = etree.Element("otherPossibleCause")
            otherPossibleCause.text = i
            possibleCauseGroup.append(otherPossibleCause)

def topicCauseCreat(topic,effect_dic,taskEffect,content_element):
    from lxml import etree
    subtaskList = topic.findall(".//subtask")
    possibleCauseGroup = content_element.find(".//possibleCauseGroup")
    for subtask in subtaskList:
        subEffect = subtask.find("effect").attrib["label"]
        para = subtask.find(".//para").text
        otherPossibleCause = etree.SubElement(possibleCauseGroup, "otherPossibleCause")
        otherPossibleCause.text = para
        if subEffect != taskEffect:
            otherPossibleCause.set("applicRefId", effect_dic[subEffect])