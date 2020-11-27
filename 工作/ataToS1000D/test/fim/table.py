#将转换后的dm中的table进行修改
#如果是断路器，则提取表格中断路器信息到CIR中，如果不是则执行下面
#thead，tgroup，tbody，entry等元素的align，valign属性又大写转为小写。
#row元素的属性rowsep非0，则首先转为1。
def table_modify(dirPath):
    def tmodi(xmlFile):
        from lxml import etree
        task = etree.parse(xmlFile)
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
            
        

    import os
    dirPath = dirPath + "/dmrl/"
    for i in os.listdir(dirPath):
        xmlFile = dirPath + i
        if xmlFile[-4:] == ".XML":     
            tmodi(xmlFile)

if __name__ == "__main__":
    table_modify("/Users/hewenhao/测试")
