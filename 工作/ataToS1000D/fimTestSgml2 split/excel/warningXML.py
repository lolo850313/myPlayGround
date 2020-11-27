# 用于生成warning的xml文件
def warningCreat(warningPath):
	from lxml import etree
	from lxml.builder import ElementMaker
	import xlrd

	#生成content框架
	E = ElementMaker()
	content_xml = E.content
	commonRepository_xml = E.commonRepository
	warningRepository_xml = E.warningRepository
	content_element = content_xml(
		commonRepository_xml(
            warningRepository_xml
        )
    )

	# 扫描excel中数据，
	workbook = xlrd.open_workbook(warningPath)
	sheet = workbook.sheet_by_index(0)
	array = []
	for i in range(1,sheet.nrows):
		array.append([sheet.cell(i,0).value,sheet.cell(i,1).value])

	#依次生成warningSpec子树后添加到warningRepository下
	warningSpec_xml = content_element[0][0]
	for i in array:
		warningSpec = etree.Element('warningSpec')
		warningIdent = etree.SubElement(warningSpec,'warningIdent')
		warningIdent.set("warningIdentNumber",i[0])
		warningAndCautionPara = etree.SubElement(warningSpec,'warningAndCautionPara')
		warningSpec_xml.append(warningSpec)
		warningAndCautionPara.text = i[1]

	#输出ddn文档
	etree.ElementTree(content_element).write(warningPath[:-21] + 'ARJ21-A-00-00-00-01A-012A-A.xml',pretty_print=True,encoding="utf-8",xml_declaration=True)

path = "D:\\测试\\s1000d\\s1000d_fim\\"
warningCreat(path + "warningRepository.xls")