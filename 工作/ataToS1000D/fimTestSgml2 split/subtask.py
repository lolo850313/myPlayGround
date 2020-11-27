def subtask_merge(subtaskARJ,effect_dic,id_para,arj_topicTitle,dmrl,taskEffect):
    from lxml import etree

    #根据信息生成isolationProcedureEnd子树
    isolationProcedureEnd_XML = etree.Element("isolationProcedureEnd")
    
    isolationProcedureEnd_XML.set("id",id_para)

    #如果本subtask有effect标签，则从effect_dic中找出对应的id
    if "label" in subtaskARJ.xpath(".//effect")[0].attrib:
        subtask_effect = subtaskARJ.xpath(".//effect")[0].attrib["label"]
        if subtask_effect != taskEffect:
            applicRefId = effect_dic[subtask_effect]
            isolationProcedureEnd_XML.set("applicRefId",applicRefId)
        

    #得到isolationProcedureEnd/title的值
    # 第一个para转换为title，其他转换到randomlist下？
    list1_l1item_para = subtaskARJ.xpath("list1/l1item/para")    
    if len(list1_l1item_para) == 1:
        isolationProcedureEnd_title = list1_l1item_para[0].text
    elif len(list1_l1item_para) > 1:
        isolationProcedureEnd_title = list1_l1item_para[0].text
    else:
        isolationProcedureEnd_title = arj_topicTitle

    
    

    #生成title
    title_XML = etree.SubElement(isolationProcedureEnd_XML, 'title')
    title_XML.text = isolationProcedureEnd_title
    
    #多余的list1_l1item_para放入action中
    l1item_list = subtaskARJ.xpath(".//l1item")[0]
    tmp = 0
    for subOfL1item in l1item_list:        
        if (subOfL1item.tag) == "para":                
            if not subOfL1item.xpath("refext"):
                if tmp == 1:
                    listItem1_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')
                    listItem1_XML.text = subOfL1item.text
                else:
                    tmp = 1
        elif (subOfL1item.tag) == "table":
            if isolationProcedureEnd_XML.find("action") is None:
                listItem1_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')
                listItem1_XML.append(subOfL1item)
            else:
                listItem1_XML.append(subOfL1item)
        elif (subOfL1item.tag) == "note":
            noteText = subOfL1item.xpath("string()").strip()
            note_XML = etree.SubElement(isolationProcedureEnd_XML, 'note')
            notePara_XML = etree.SubElement(note_XML, 'notePara')
            notePara_XML.text = noteText

    tmp = 0    

    #l2item转化为listItem
    l2item_list = subtaskARJ.xpath(".//l2item")

    #根据arj中的生成多个listItem
    for l2item in l2item_list:                  
        for subOfL2item in l2item:
            if (subOfL2item.tag) == "para":
                listItem2_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')
                if not subOfL2item.xpath("refext"):
                    listItem2_XML.text = subOfL2item.text
            elif (subOfL2item.tag) == "note":
                noteText = subOfL2item.xpath("string()").strip()
                note_XML = etree.SubElement(isolationProcedureEnd_XML, 'note')
                notePara_XML = etree.SubElement(note_XML, 'notePara')
                notePara_XML.text = noteText
            elif (subOfL2item.tag) == "table":
                listItem2_XML.append(subOfL2item)
            else :
                if (subOfL2item.tag) != "list3":
                    print(subOfL2item.tag + " get subOfL2item @subtask.py" )
                else:
                    randomList_XML = etree.SubElement(listItem2_XML, 'randomList')
                    #l3item_list
                    l3item_list = subOfL2item.xpath(".//l3item")        
                    for l3item in l3item_list:        
                        listItem3_XML = etree.SubElement(randomList_XML, 'listItem')
                        for subOfL3item in l3item:
                            if (subOfL3item.tag) == "para":
                                if not subOfL3item.xpath("refext"):
                                    para3_XML = etree.SubElement(listItem3_XML, 'para')
                                    para3_XML.text = subOfL3item.text
                            elif (subOfL3item.tag) == "note":
                                noteText = subOfL3item.xpath("string()").strip()
                                note_XML = etree.SubElement(listItem3_XML, 'note')
                                notePara_XML = etree.SubElement(note_XML, 'notePara')
                                notePara_XML.text = noteText
                            elif (subOfL3item.tag) == "table":
                                if listItem3_XML.find("para") is not None:
                                    para3_XML.append(subOfL3item)
                                else:
                                    para3_XML = etree.SubElement(listItem3_XML, 'para')
                                    para3_XML.append(subOfL3item)
                            else:
                                if (subOfL3item.tag) != "list4":
                                    print(subOfL3item.tag + " subOfL3item get @subtask.py")
                                else:
                                    randomList4_XML = etree.SubElement(para3_XML, 'sequentialList')
                                    #l3item_list
                                    l4item_list = subOfL3item.xpath(".//l4item")    
                                    for l4item in l4item_list:        
                                        listItem4_XML = etree.SubElement(randomList4_XML, 'listItem')
                                        for subOfL4item in l4item:
                                            if (subOfL4item.tag) == "para":
                                                if not subOfL4item.xpath("refext"):
                                                    para4_XML = etree.SubElement(listItem4_XML, 'para')
                                                    para4_XML.text = subOfL4item.text
                                            elif (subOfL4item.tag) == "note":
                                                noteText = subOfL4item.xpath("string()").strip()
                                                note_XML = etree.SubElement(listItem4_XML, 'note')
                                                notePara_XML = etree.SubElement(note_XML, 'notePara')
                                                notePara_XML.text = noteText
                                            elif (subOfL4item.tag) == "table":
                                                if listItem4_XML.find("para") is not None:
                                                    para4_XML.append(subOfL4item)
                                                else:
                                                    para4_XML = etree.SubElement(listItem4_XML, 'para')
                                                    para4_XML.append(subOfL4item)
                                            else:
                                                if (subOfL4item.tag) != "list5":
                                                    print(subOfL4item.tag + " subOfL4item get @subtask.py")
                                                else:                                                    
                                                    randomList5_XML = etree.SubElement(para4_XML, 'sequentialList')
                                                    #l3item_list
                                                    l5item_list = subOfL4item.xpath(".//l5item")  
                                                    for l5item in l5item_list:        
                                                        listItem5_XML = etree.SubElement(randomList5_XML, 'listItem')
                                                        for subOfL5item in l5item:
                                                            if (subOfL5item.tag) == "para":
                                                                if not subOfL5item.xpath("refext"):
                                                                    para5_XML = etree.SubElement(listItem5_XML, 'para')
                                                                    para5_XML.text = subOfL5item.text
                                                            elif (subOfL5item.tag) == "note":
                                                                noteText = subOfL5item.xpath("string()").strip()
                                                                note_XML = etree.SubElement(listItem5_XML, 'note')
                                                                notePara_XML = etree.SubElement(note_XML, 'notePara')
                                                                notePara_XML.text = noteText
                                                            elif (subOfL5item.tag) == "table":                                                        
                                                                if listItem5_XML.find("para") is not None:                                                    
                                                                    para5_XML.append(subOfL5item)
                                                                else:
                                                                    para5_XML = etree.SubElement(listItem5_XML, 'para')
                                                                    para5_XML.append(subOfL5item)
                                                            else:
                                                                if (subOfL5item.tag) != "list6":
                                                                    print(subOfL5item.tag + " subOfL5item get @subtask.py")
                                                                else:                                                                    
                                                                    randomList6_XML = etree.SubElement(para5_XML, 'sequentialList')
                                                                    l6item_list = subOfL5item.xpath(".//l6item")    
                                                                    for l6item in l6item_list:        
                                                                        listItem6_XML = etree.SubElement(randomList6_XML, 'listItem')
                                                                        for subOfL6item in l6item:
                                                                            if (subOfL6item.tag) == "para":
                                                                                if not subOfL6item.xpath("refext"):
                                                                                    para6_XML = etree.SubElement(listItem6_XML, 'para')
                                                                                    para6_XML.text = subOfL6item.text
                                                                            elif (subOfL6item.tag) == "note":
                                                                                noteText = subOfL6item.xpath("string()").strip()
                                                                                note_XML = etree.SubElement(listItem6_XML, 'note')
                                                                                notePara_XML = etree.SubElement(note_XML, 'notePara')
                                                                                notePara_XML.text = noteText
                                                                            elif (subOfL6item.tag) == "table":                                                                                
                                                                                if listItem6_XML.find("para") is not None:                                                                              
                                                                                    para6_XML.append(subOfL6item)
                                                                                else:
                                                                                    para6_XML = etree.SubElement(listItem6_XML, 'para')
                                                                                    para6_XML.append(subOfL6item)
                                                                            else:
                                                                                print(subOfL6item.tag + " subOfL6item @subtask.py")
                                    

    return isolationProcedureEnd_XML
