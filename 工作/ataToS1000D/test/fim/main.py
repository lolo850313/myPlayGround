# cautionRef未测试正确
# isolationProcedureEnd下的table可以放action后
# applicIdentValue的值需要更新？？
#
# #转换后会出现多余的action标签。可以通过批量读取dmc后使用删除操作。
# DMC-ARJ21-A-26-00-00-04A-421D-A_001-00_ZH-CN 中相关断路器未录入
# DMC-ARJ21-A-26-00-00-04A-421D-A_001-00_ZH-CN 中 欧姆符号Ω不能正常显示
# 29-12-00-810-829故障隔离程序不在topic/subtask下，而在pretopic下用item的层级来写，无法转换
# table有多余属性id
# 有几个topic 生成几个isolationprocedureEndAlts
# 一些参引未转换：AMM 49-15-01-200-801
# 	DMC-ARJ21-A-49-10-00-09A-421A-A_001-00_ZH-CN中AMM TASK 49-10-00-860-801
# 	DMC-ARJ21-A-29-14-00-02A-421A-A_001-00_ZH-CN AMM TASK 29-14-00-720-801
#
# 以下情况打算靠人为解决
# DMC-ARJ21-A-26-00-00-04A-421D-A_001-00_ZH-CN 中“取下C.相关断路器中”，转换后没有此topic，导致表述有误
# DMC-ARJ21-A-26-00-00-04A-421D-A_001-00_ZH-CN 中“执行F.故障修复确认程序”，转换后没有此topic，导致表述有误
# 描述类数据建议手动转换
#
# 需与杨洋确认
# 初步评估l1item下的的para是否是转换到action中
# l2item下的para是否是转入randomList/listItem/para下
# l3item下的para是否是转入randomList/listItem/para/squentialList/listItem/para下

from mainFrame import frame
from lxml import etree
from subtask import subtask_merge
from effect import effect_to_dic,effect_xml,faultcode
from head import headxml,findDmCode,find_dmc
from warningAndCaution import warningRefCreat,cautionRefCreat,cirList,warningsAndCautionsRef_insertTo_content
from possibleCause import possibleCause_creat
from faultdescr import descr_creat
from pretopic import commonInfo_creat,cbpgCreat
from ref_replace import dmrlRef_modify
from note import topicNoteCreat,noteChange
from table import table_modify

##总路径
dirPath = "/Users/hewenhao/测试/"
# 手册xml存放路径
xmlPath = "ARJFRMFIM-TP700018A-$new$-amm(201903).sgm"

# dmrl转换规则存放路径，从fimDMRL获得
dmrl_excel = dirPath + "ARJFRMFIM-TP700018A-DMRL-2019.3-合稿-柯倩云-20190603-修订.xlsx"

# 警告库，从warningXML获得
warning_xml = dirPath + "ARJ21-A-00-00-00-01A-012A-A.xml"
# 警戒库，从cautionXML获得
caution_xml = dirPath + "ARJ21-A-00-00-00-02A-012A-A.xml"
# #amm的dmrl表格，从xxx获得
# amm_dmrlTable = dirPath + "amm-dmrlTable.xls"

# 初始化content_element，初始化参数start在后面循环生成content时会被覆盖掉
content_element = frame("start")

# 将fim手册元素化
fim_arj = etree.parse(dirPath + xmlPath)
arj_task_list = fim_arj.xpath("//task")

for arj_task in arj_task_list:
	# 获得当前task的taskNum值,通过taskNum在dmrlTable中找到对应的dmrl号
	dmrl = find_dmc(arj_task,dmrl_excel)
	# 获得当前task的faultcode，有些没有faultcode则填入默认值。
	faultcodeARJ = faultcode(arj_task)

	# 初始化默认content框架
	content_element = frame(faultcodeARJ)

	# 添加warning，caution至content中
	warningsAndCautionsRef_insertTo_content(arj_task,caution_xml,warning_xml,content_element)

	# topic下的note转换成notepara
	topicNoteCreat(arj_task,content_element)

	# 生成effect字典
	effect_dic = effect_to_dic(arj_task)

	# 将有效性参引写入content中
	referencedApplicGroupRef = effect_xml(effect_dic)
	content_element.insert(0,referencedApplicGroupRef)

	# 在content中找到故障隔离主程序的位置
	isolationMainProcedure = content_element.xpath(".//isolationMainProcedure")[0]

	# 将topic中title非相关断路器的分为一类
	arj_topic_list = arj_task.xpath("topic")
	arj_topicNotCB_list = []

	for topic in arj_topic_list:
		if (topic.find("title").text)!="相关断路器" and (topic.find("title").text)!="初步评估":
			arj_topicNotCB_list.append(topic)

	for topicNotCB in arj_topicNotCB_list:
		isolationProcedureEndAlts_XML = etree.SubElement(isolationMainProcedure,"isolationProcedureEndAlts")
		# 有些subtask没有"list1/l1item/para"，则使用"topic/title"作为isolationProcedureEnd_title
		if topicNotCB.find("title") != None:
			arj_topicTitle = topicNotCB.xpath("title")[0].text
			# 根据subtask的数量，循环添加进故障隔离主程序中
		arj_subtaskNotCB_list = topicNotCB.findall("subtask")
		for i in range(len(arj_subtaskNotCB_list)):
			# 生成id流水号
			id_para = "e0" + str(i + 1 )

			# 生成对应的subtask的xml树
			subtask_XML = subtask_merge(arj_subtaskNotCB_list[i],effect_dic,id_para,arj_topicTitle,dmrl)
			# 将subtask的xml树依次添加进isolationMainProcedure下
			isolationProcedureEndAlts_XML.insert(i,subtask_XML)

	#生成可能的原因
	possibleCause_creat(arj_task,content_element)

	# commonInfo，遍历老树，生成新树。
	commonInfo_creat(arj_task,content_element)

	#初步评估
	# commonInfo，遍历老树，生成新树。
	cbpg = cbpgCreat(arj_task,content_element,effect_dic)
	if cbpg != None:
		isolationMainProcedure.insert(0,cbpg)

	# 生成ident的xml树
	head = headxml(arj_task,dmrl_excel,effect_dic)

	# 故障描述（由title前半部分转化）,也是head中的techName，
	descr_creat(head,arj_task,content_element)

	# 写xml头，并添加head部分和content部分
	root = etree.XML('<dmodule xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_4-1/xml_schema_flat/fault.xsd"></dmodule>')
	root.append(head)
	root.append(content_element)

	etree.ElementTree(root).write(dirPath + '/s1000dFim/' + dmrl + '_001-00_ZH-CN.XML',pretty_print=True,encoding="utf-8")

dmrlRef_modify(dirPath+"s1000dFim/")
table_modify("/Users/hewenhao/测试")
