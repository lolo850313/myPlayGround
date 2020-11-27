# 用于生成caution表格的xml文件
def cautionCreat(cirPath):
	from lxml import etree
	from lxml.builder import ElementMaker
	import xlrd

	#生成content框架
	E = ElementMaker()
	content_xml = E.content
	commonRepository_xml = E.commonRepository
	cautionRepository_xml = E.cautionRepository
	content_element = content_xml(
		commonRepository_xml(
            cautionRepository_xml
        )
    )

	# 扫描excel中数据，
	workbook = xlrd.open_workbook(cirPath)
	sheet = workbook.sheet_by_index(0)
	array = []
	for i in range(1,sheet.nrows):
		array.append([sheet.cell(i,0).value,sheet.cell(i,1).value])

	#依次生成warningSpec子树后添加到warningRepository下
	cautionSpec_xml = content_element[0][0]
	for i in array:
		cautionSpec = etree.Element('cautionSpec')
		cautionIdent = etree.SubElement(cautionSpec,'cautionIdent')
		cautionIdent.set("cautionIdentNumber",i[0])
		warningAndCautionPara = etree.SubElement(cautionSpec,'warningAndCautionPara')
		cautionSpec_xml.append(cautionSpec)
		warningAndCautionPara.text = i[1]

	#输出ddn文档
	etree.ElementTree(content_element).write(cirPath[:-21] + 'ARJ21-A-00-00-00-02A-012A-A.xml',pretty_print=True,encoding="utf-8",xml_declaration=True)

path = "D:\\测试\\s1000d\\s1000d_fim\\"
cautionCreat(path + "cautionRepository.xls")