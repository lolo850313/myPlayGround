#用于生成subtask下的断路器表格的excel文件
from lxml import etree 
# tree = etree.parse("D:\\ataToS1000D\\ARJFRMFIM-TP700018A-fim26-$new$-amm.sgm")
path = "D:\\测试\\s1000d\\s1000d_fim\\"
tree = etree.parse("D:\\测试\\s1000d\\s1000d_fim\\ARJFRMFIM-TP700018A-$new$-amm(201909).sgm")

task_list = tree.xpath(".//task")
para_list = []
for i in task_list:
	taskNum = i.attrib["chapnbr"] + "-" + i.attrib["sectnbr"] + "-" + i.attrib["subjnbr"]
	#找到相关断路器的subtask
	topic_list = i.xpath(".//topic")

	for topic in topic_list:
		if topic.find("title").text == "相关断路器":
			for subtask in topic.findall("subtask"):
				if "label" in subtask.find("effect").attrib:
					effect = subtask.find("effect").attrib["label"]
				else:
					effect = "ALL"
				for tbody in subtask.findall(".//tbody"):			
					for row in (tbody.findall("row")):
						rowList=[]
						for para in (row.findall(".//para")):
							rowList.append(para.text)
						rowList.append(effect)
						rowList.append(taskNum)
						if rowList[0].strip() != "行":
							if rowList not in para_list:
								para_list.append(rowList)

cb_title = ["行","列","编号","名称","有效性","任务号"]
path = "D:\\测试\\s1000d\\s1000d_fim\\"
cb_filename = "cbWithEffect.xlsx"

#把列表字典写入excel，每行是列表元素，每列是字典
def excelout(array,title,path,filename):
	import xlwt
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('My Worksheet')
	rowNum = 0
	for i in range(len(title)):
		worksheet.write(0,i,label = title[i])
	#excel_row是excel写入的起始行，row是list数据的每个子列表
	
	for row in range(len(array)):
		rowNum = rowNum + 1
		# print(array[row])
		for col in range(len(array[row])):				
			worksheet.write(rowNum,col,label = array[row][col])

	workbook.save(path + filename)

excelout(para_list,cb_title,path,cb_filename)