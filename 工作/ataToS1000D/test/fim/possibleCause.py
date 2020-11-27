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
        else:
            possibleCause.append("No possibleCause")
    possibleCauseGroup = content_element.find(".//possibleCauseGroup")
    for i in possibleCause:
        otherPossibleCause = etree.Element("otherPossibleCause")
        otherPossibleCause.text = i
        possibleCauseGroup.append(otherPossibleCause)