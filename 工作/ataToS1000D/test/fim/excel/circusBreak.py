#用于生成断路器表格的excel文件
from lxml import etree 
# tree = etree.parse("D:\\ataToS1000D\\ARJFRMFIM-TP700018A-fim26-$new$-amm.sgm")
path = "/Users/hewenhao/测试/"
tree = etree.parse("/Users/hewenhao/测试/ARJFRMFIM-TP700018A-$new$-amm(201903).sgm")

#读取tgroup
tbodylist = tree.xpath("//tbody")

para_list = []
cb_list = []
awm_list = []

#按照tbody提取带有行列信息的para
for tbody in tbodylist:
	tbody_list=[]
	for row in (tbody.findall("row")):
		rowList=[]
		for para in (row.findall(".//para")):
			rowList.append(para.text)
		tbody_list.append(rowList)
	para_list.append(tbody_list)
#只将首行首列是“行”的表格放入断路器excel中
for table in para_list:
	if table[0][0] == "行":     
		for rowNum in range(1,len(table)):
			row_list = []
			row_list.append(table[rowNum][0])
			row_list.append(table[rowNum][1])
			row_list.append(table[rowNum][2])
			row_list.append(table[rowNum][3])
			# print(rowList)
		cb_list.append(row_list)
# 数据要去重，然后赋予唯一参引号
cb_list_final = []
for i in cb_list:
	if i not in cb_list_final:
		cb_list_final.append(i)
		
for i in cb_list_final:
	print(i)

cb_title = ["行","列","编号","名称"]
path = "/Users/hewenhao/测试/"
cb_filename = "cb.xls"

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
		for col in range(len(array[row])):				
			worksheet.write(rowNum,col,label = array[row][col])

	workbook.save(path + filename)

excelout(cb_list_final,cb_title,path,cb_filename)