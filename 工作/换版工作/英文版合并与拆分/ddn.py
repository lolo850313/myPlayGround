def ddnCreat(xml_dir,date,ddnCode_para):
	from lxml import etree
	from headCreat import headxml
	from ddnContentCreat import ddnContent
	#写xml头
	root = etree.XML('<ddn xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/ddn.xsd"></ddn>')
	# #生成ident的xml树
	head = headxml(date,ddnCode_para)
	root.append(head)
	
	Content = ddnContent(xml_dir)

	root.append(Content)

	#输出ddn文档
	fileName = "DDN-" + ddnCode_para["modelIdentCode"] + "-" +  ddnCode_para["receiverIdent"] + "-" + ddnCode_para["senderIdent"] + "-" + ddnCode_para["yearOfDataIssue"] + "-" + ddnCode_para["seqNumber"] + ".XML"
	etree.ElementTree(root).write(xml_dir + fileName,pretty_print=True,encoding="utf-8",xml_declaration=True)
	# etree.ElementTree(content_element).write('d:/homemade/'+ dmrl + '.xml',pretty_print=True,encoding="utf-8")


