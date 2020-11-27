def subtask_merge(subtaskARJ,effect_dic,id_para,arj_topicTitle,dmrl):
    from lxml import etree

    #如果本subtask有effect标签，则从effect_dic中找出对应的id
    if "label" in subtaskARJ.xpath(".//effect")[0].attrib:
        subtask_effect = subtaskARJ.xpath(".//effect")[0].attrib["label"]
    else:
        subtask_effect = "101+."
    applicRefId = effect_dic[subtask_effect]
    id = id_para

    #得到isolationProcedureEnd/title的值
    # 第一个para转换为title，其他转换到randomlist下？
    list1_l1item_para = subtaskARJ.xpath("list1/l1item/para")    
    if len(list1_l1item_para) == 1:
        isolationProcedureEnd_title = list1_l1item_para[0].text
    elif len(list1_l1item_para) > 1:
        isolationProcedureEnd_title = list1_l1item_para[0].text
        print(dmrl)
    else:
        isolationProcedureEnd_title = arj_topicTitle

    
    #根据信息生成isolationProcedureEnd子树
    isolationProcedureEnd_XML = etree.Element("isolationProcedureEnd")
    isolationProcedureEnd_XML.set("applicRefId",applicRefId)
    isolationProcedureEnd_XML.set("id",id)

    #生成title
    title_XML = etree.SubElement(isolationProcedureEnd_XML, 'title')
    title_XML.text = isolationProcedureEnd_title

    #如果l1item下有note，则转换后添加到isolationProcedureEnd_XML下
    l1Note= subtaskARJ.xpath(".//l1item/note")
    if l1Note != []:
        l1NoteText = l1Note[0].xpath("string()").strip()
        l1Note_XML = etree.SubElement(isolationProcedureEnd_XML, 'notePara')
        l1Note_XML.text = l1NoteText


    
    #多余的list1_l1item_para放入randomlist中
    for kk in range(1,len(list1_l1item_para)):
        if list1_l1item_para[kk].text.strip() != "":
            print(dmrl + " kk")
            action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')
            randomList_spec_XML = etree.SubElement(action_XML, 'randomList')
            print(list1_l1item_para[kk].text)
            randomList_spec_XML.text = list1_l1item_para[kk].text
    

    #l2item转化为listItem
    l2item_list = subtaskARJ.xpath(".//l2item")
    #生成action，randomlist，
    if l2item_list != []:
        if isolationProcedureEnd_XML.xpath("action") == []:
            action_XML = etree.SubElement(isolationProcedureEnd_XML, 'action')
        randomList_XML = etree.SubElement(action_XML, 'randomList')
    #根据arj中的生成多个listItem
    for l2item in l2item_list:          
        listItem2_XML = etree.SubElement(randomList_XML, 'listItem')
        for subOfL2item in l2item:
            if (subOfL2item.tag) == "para":
                if not subOfL2item.xpath("refext"):
                    para2_XML = etree.SubElement(listItem2_XML, 'para')
                    para2_XML.text = subOfL2item.text
            elif (subOfL2item.tag) == "note":
                noteText = subOfL2item.xpath("string()").strip()
                note_XML = etree.SubElement(listItem2_XML, 'note')
                notePara_XML = etree.SubElement(note_XML, 'notePara')
                notePara_XML.text = noteText
            elif (subOfL2item.tag) == "table":
                #将表直接拷贝                       
                isolationProcedureEnd_XML.append(subOfL2item)
            else :
                if (subOfL2item.tag) != "list3":
                    print(subOfL2item.tag + " get subOfL2item subtask " )
                else:
                    sequentialList_XML = etree.SubElement(para2_XML, 'sequentialList')
                    #l3item_list
                    l3item_list = subOfL2item.xpath(".//l3item")        
                    for l3item in l3item_list:        
                        listItem3_XML = etree.SubElement(sequentialList_XML, 'listItem')
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
                                #将表直接拷贝                        
                                isolationProcedureEnd_XML.append(subOfL3item)
                            else:
                                if (subOfL3item.tag) != "list4":
                                    print(subOfL3item.tag + " subOfL3item get subtask")
                                else:
                                    randomList4_XML = etree.SubElement(para3_XML, 'randomList')
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
                                                #将表直接拷贝                        
                                                isolationProcedureEnd_XML.append(subOfL4item)
                                            else:
                                                if (subOfL4item.tag) != "list5":
                                                    print(subOfL4item.tag + " subOfL4item get subtask")
                                                else:
                                                    randomList5_XML = etree.SubElement(para4_XML, 'randomList')
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
                                                                #将表直接拷贝                        
                                                                isolationProcedureEnd_XML.append(subOfL5item)
                                                            else:
                                                                if (subOfL5item.tag) != "list6":
                                                                    print(subOfL5item.tag + " subOfL5item get subtask")
                                                                else:
                                                                    randomList6_XML = etree.SubElement(para5_XML, 'randomList')
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
                                                                                #将表直接拷贝                         
                                                                                isolationProcedureEnd_XML.append(subOfL6item)
                                                                            else:
                                                                                print(subOfL6item.tag + " subOfL6item subtask")
                                    

    return isolationProcedureEnd_XML
