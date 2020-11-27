#将转换后的dm中的table进行修改
#如果是断路器，则提取表格中断路器信息到CIR中，如果不是则执行下面
#thead，tgroup，tbody，entry等元素的align，valign属性又大写转为小写。
#row元素的属性rowsep非0，则首先转为1。
# 断路器转换后的模板
def table_modify(dirPath,cbExcel):
    #将断路器字符串转为断路器标签
    def cirXml(circuitBreakerNumber):
            from lxml import etree
            circuitBreakerRef = etree.Element("circuitBreakerRef")
            circuitBreakerRef.set("circuitBreakerNumber",circuitBreakerNumber)
            return circuitBreakerRef

    #修改table位置到isolationProcedureEnd节点下
    def tableLocation(xmlFile):
        import xlrd
        from lxml import etree
        task = etree.parse(xmlFile)
        isolationProcedureEnd_list = task.xpath(".//isolationProcedureEnd")
        t = 1
        for iso in isolationProcedureEnd_list:
            for act in iso.findall("action"):
                if act.findall(".//table") is not None:
                    actIndex = iso.getchildren().index(act)
                    for table in act.findall(".//table"):
                        tBaba = table.getparent()
                        applicRefId = "t" + str(t).zfill(3)                        
                        internalRef = etree.Element("internalRef")
                        internalRef.set("internalRefId",applicRefId)
                        internalRef.set("internalRefTargetType","irtt62")                        
                        tBaba.remove(table)
                        # tBaba.insert(-1,internalRef)
                        tBaba.append(internalRef)

                        table.set("id",applicRefId)
                        # iso.insert(actIndex + 1,table)
                        iso.append(table)
                        t = t + 1
                

        task.write(xmlFile,pretty_print=True,encoding="utf-8")
    # 修改table的属性大小写
    def tmodi(xmlFile):
        import xlrd
        from lxml import etree
        task = etree.parse(xmlFile)
        table_list = task.xpath(".//table")
        for table in table_list:
            for attr in table.attrib:                
                table.attrib[attr] = table.attrib[attr].lower()
        tgroup_list = task.xpath(".//tgroup")
        for tgroup in tgroup_list:
            for attr in tgroup.attrib:                
                tgroup.attrib[attr] = tgroup.attrib[attr].lower()

        colspec_list = task.xpath(".//colspec")
        for colspec in colspec_list:
            for attr in colspec.attrib:
                colspec.attrib[attr] = colspec.attrib[attr].lower()
        thead_list = task.xpath(".//thead")
        for thead in thead_list:
            for attr in thead.attrib:
                thead.attrib[attr] = thead.attrib[attr].lower()

        tbody_list = task.xpath(".//tbody")
        for tbody in tbody_list:
            for attr in tbody.attrib:
                tbody.attrib[attr] = tbody.attrib[attr].lower()

        entry_list = task.xpath(".//entry")
        for entry in entry_list:
            for attr in entry.attrib:            
                entry.attrib[attr] = entry.attrib[attr].lower()

        task.write(xmlFile,pretty_print=True,encoding="utf-8")
            
    #表格转断路器
    def tableToCir(xmlFile,dirPath,cbExcel):      
        import xlrd
        from lxml import etree      

        # 读取excel
        cbTable = xlrd.open_workbook(dirPath + cbExcel).sheets()[0]
        cbRow = cbTable.nrows
        # cbDic = {}
        # for i in range(cbRow):
        #     cbDic[cbTable.cell_value(i,2)] = [cbTable.cell_value(i,0),cbTable.cell_value(i,1),cbTable.cell_value(i,3)]

        cbDic = []
        for i in range(cbRow):
            cbDic.append(cbTable.cell_value(i,1))

        task = etree.parse(xmlFile)
        table_list = task.xpath(".//table")
        for table in table_list:
            colsAttrib = table.find("tgroup").attrib["cols"]
            pNode = table.getparent()
            if colsAttrib == "4":
                row_list = table.findall(".//row")
                hang = row_list[0].findall(".//para")[0].text
                lie = row_list[0].findall(".//para")[1].text
                if hang == "行" and lie == "列":
                    for cb in range(1,len(row_list)):
                        cbName = row_list[cb].findall(".//para")[2].text.strip()
                        if cbName in cbDic:                            
                            if pNode is not None :
                                pNode.append(cirXml(cbName))                    
                        else:
                            # 断路器库中不存在的断路器名称
                            print(xmlFile)
                            print(cbName + " @@@@")
                    pNode.remove(table)
              
        task.write(xmlFile,pretty_print=True,encoding="utf-8")   
                
                    
        

    import os
    cbPath = "D:\\测试\\s1000d\\s1000d_fim\\"
    for i in os.listdir(dirPath):
        xmlFile = dirPath + i
        if xmlFile[-4:] == ".XML":
            tableToCir(xmlFile,cbPath,cbExcel)   
            tmodi(xmlFile)            
            tableLocation(xmlFile)
    
if __name__ == "__main__":
    table_modify("D:\\测试\\s1000d\\s1000d_fim\\split_To\\","ARJ断路器清单梳理-2019年9月版-1029.xlsx")
    # tableLocation("D:\\测试\\s1000d\\s1000d_fim\\ARJ21-A-78-32-00-BBA-421A-A_001-00_ZH-CN.XML")