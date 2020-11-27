import os
root = "D:\\程序源数据\\手册\\201909\\"
confirmPath = root + "compare\\"
dmrlPath = root + "dmrlExcel\\"
comparePath = root + "compareResult\\"

def dmrlCompare(confirmFile,dmrlFile,resultFile):
	import xlrd
	import xlwt

	confirmFileDic = {}
	confirmtable = xlrd.open_workbook(confirmFile).sheets()[0]
	rowlength1 = confirmtable.nrows
	for row in range(1,rowlength1):
		confirmFileDic[confirmtable.cell(row,1).value] = [confirmtable.cell(row,0).value,confirmtable.cell(row,2).value,confirmtable.cell(row,3).value,confirmtable.cell(row,4).value,confirmtable.cell(row,5).value,confirmtable.cell(row,6).value,confirmtable.cell(row,7).value,confirmtable.cell(row,8).value,confirmtable.cell(row,9).value,confirmtable.cell(row,10).value,confirmtable.cell(row,11).value,confirmtable.cell(row,12).value,confirmtable.cell(row,13).value,confirmtable.cell(row,14).value,confirmtable.cell(row,15).value,confirmtable.cell(row,16).value]
	dmrlFileDic = {}
	dmrltable = xlrd.open_workbook(dmrlFile).sheets()[0]
	rowlength2 = dmrltable.nrows
	for row in range(1,rowlength2):
		dmrlFileDic[dmrltable.cell(row,1).value] = [dmrltable.cell(row,0).value,dmrltable.cell(row,2).value,dmrltable.cell(row,3).value,dmrltable.cell(row,4).value,dmrltable.cell(row,5).value,dmrltable.cell(row,6).value,dmrltable.cell(row,7).value,dmrltable.cell(row,8).value,dmrltable.cell(row,9).value,dmrltable.cell(row,10).value,dmrltable.cell(row,11).value,dmrltable.cell(row,12).value,dmrltable.cell(row,13).value,dmrltable.cell(row,14).value,dmrltable.cell(row,15).value,dmrltable.cell(row,16).value]
	
	line = 1
	for i in dmrlFileDic:
		if i in confirmFileDic:
			for j in range(11):                
				dmrlFileDic[i][j] = confirmFileDic[i][j]
			for j in range(13,16):
				dmrlFileDic[i][j] = confirmFileDic[i][j]
			dmrlFileDic[i][12] = '=CONCATENATE(D' + str(line+1) + ',"-",E'+ str(line+1) + ',"-",F'+ str(line+1) + ',"-",G'+ str(line+1) + ',"-",H'+ str(line+1) + ',"-",I'+ str(line+1) + ',J'+ str(line+1) + ',"-",K'+ str(line+1) + ',L'+ str(line+1) + ',"-",M'+ str(line+1) + ')'
		else:
			dmrlFileDic[i][12] = '=CONCATENATE(D' + str(line+1) + ',"-",E'+ str(line+1) + ',"-",F'+ str(line+1) + ',"-",G'+ str(line+1) + ',"-",H'+ str(line+1) + ',"-",I'+ str(line+1) + ',J'+ str(line+1) + ',"-",K'+ str(line+1) + ',L'+ str(line+1) + ',"-",M'+ str(line+1) + ')'
			dmrlFileDic[i].append("new data")
		line = line + 1
	for i in confirmFileDic:
		if i not in dmrlFileDic:
			dmrlFileDic[i] = confirmFileDic[i]
			dmrlFileDic[i].append("deleted")
	
	import xlsxwriter
	resultbook = xlsxwriter.Workbook(resultFile)
	resultSheet = resultbook.add_worksheet('My Worksheet')

	k = 1
	resultSheet.write(0,0,"index")
	resultSheet.write(0,1,"Task NO.")
	resultSheet.write(0,2,"title")
	resultSheet.write(0,3,"MI")
	resultSheet.write(0,4,"SDC")
	resultSheet.write(0,5,"SYS")
	resultSheet.write(0,6,"SUB-SYS")
	resultSheet.write(0,7,"UNIT")
	resultSheet.write(0,8,"DC")
	resultSheet.write(0,9,"DCV")
	resultSheet.write(0,10,"IC")
	resultSheet.write(0,11,"ICV")
	resultSheet.write(0,12,"ILC")
	resultSheet.write(0,13,"DMC")
	resultSheet.write(0,14,"techName")
	resultSheet.write(0,15,"infoName")
	resultSheet.write(0,16,"key")
	resultSheet.write(0,17,"与主编确认后表格对比")
	for i in dmrlFileDic:
		resultSheet.write(k,0,dmrlFileDic[i][0])
		resultSheet.write(k,1,i)
		for j in range(1,len(dmrlFileDic[i])):
			resultSheet.write(k,j+1,dmrlFileDic[i][j])
		k = k + 1

	resultbook.close()

	
		
	
	#如果完全一致，则不输出结果文件
	
def dmrlCompare_SDS(confirmFile,dmrlFile,resultFile):
	import xlrd
	import xlwt

	confirmFileDic = {}
	confirmtable = xlrd.open_workbook(confirmFile).sheets()[0]
	rowlength1 = confirmtable.nrows
	for row in range(1,rowlength1):
		confirmFileDic[confirmtable.cell(row,1).value] = [confirmtable.cell(row,0).value,confirmtable.cell(row,2).value,confirmtable.cell(row,3).value,confirmtable.cell(row,4).value,confirmtable.cell(row,5).value,confirmtable.cell(row,6).value,confirmtable.cell(row,7).value,confirmtable.cell(row,8).value,confirmtable.cell(row,9).value,confirmtable.cell(row,10).value,confirmtable.cell(row,11).value,confirmtable.cell(row,12).value,confirmtable.cell(row,13).value,confirmtable.cell(row,14).value,confirmtable.cell(row,15).value,confirmtable.cell(row,16).value,confirmtable.cell(row,17).value]
	dmrlFileDic = {}
	dmrltable = xlrd.open_workbook(dmrlFile).sheets()[0]
	rowlength2 = dmrltable.nrows
	for row in range(1,rowlength2):
		dmrlFileDic[dmrltable.cell(row,1).value] = [dmrltable.cell(row,0).value,dmrltable.cell(row,2).value,dmrltable.cell(row,3).value,dmrltable.cell(row,4).value,dmrltable.cell(row,5).value,dmrltable.cell(row,6).value,dmrltable.cell(row,7).value,dmrltable.cell(row,8).value,dmrltable.cell(row,9).value,dmrltable.cell(row,10).value,dmrltable.cell(row,11).value,dmrltable.cell(row,12).value,dmrltable.cell(row,13).value,dmrltable.cell(row,14).value,dmrltable.cell(row,15).value,dmrltable.cell(row,16).value,dmrltable.cell(row,17).value]
	
	line = 1
	for i in dmrlFileDic:
		if i in confirmFileDic:
			for j in range(12):                
				dmrlFileDic[i][j] = confirmFileDic[i][j]
			for j in range(14,17):
				dmrlFileDic[i][j] = confirmFileDic[i][j]
			dmrlFileDic[i][13] = '=CONCATENATE(E' + str(line+1) + ',"-",F'+ str(line+1) + ',"-",G'+ str(line+1) + ',"-",H'+ str(line+1) + ',"-",I'+ str(line+1) + ',"-",J'+ str(line+1) + ',K'+ str(line+1) + ',"-",L'+ str(line+1) + ',M'+ str(line+1) + ',"-",N'+ str(line+1) + ')'
		else:
			dmrlFileDic[i][13] = '=CONCATENATE(E' + str(line+1) + ',"-",F'+ str(line+1) + ',"-",G'+ str(line+1) + ',"-",H'+ str(line+1) + ',"-",I'+ str(line+1) + ',"-",J'+ str(line+1) + ',K'+ str(line+1) + ',"-",L'+ str(line+1) + ',M'+ str(line+1) + ',"-",N'+ str(line+1) + ')'
			dmrlFileDic[i].append("new data")
		line = line + 1
	for i in confirmFileDic:
		if i not in dmrlFileDic:
			dmrlFileDic[i] = confirmFileDic[i]
			dmrlFileDic[i].append("deleted")
	
	import xlsxwriter
	resultbook = xlsxwriter.Workbook(resultFile)
	resultSheet = resultbook.add_worksheet('My Worksheet')

	k = 1
	resultSheet.write(0,0,"index")
	resultSheet.write(0,1,"Task NO.")
	resultSheet.write(0,2,"title")
	resultSheet.write(0,3,"title2")
	resultSheet.write(0,4,"MI")
	resultSheet.write(0,5,"SDC")
	resultSheet.write(0,6,"SYS")
	resultSheet.write(0,7,"SUB-SYS")
	resultSheet.write(0,8,"UNIT")
	resultSheet.write(0,9,"DC")
	resultSheet.write(0,10,"DCV")
	resultSheet.write(0,11,"IC")
	resultSheet.write(0,12,"ICV")
	resultSheet.write(0,13,"ILC")
	resultSheet.write(0,14,"DMC")
	resultSheet.write(0,15,"techName")
	resultSheet.write(0,16,"infoName")
	resultSheet.write(0,17,"key")
	resultSheet.write(0,18,"与主编确认后表格对比")
	for i in dmrlFileDic:
		resultSheet.write(k,0,dmrlFileDic[i][0])
		resultSheet.write(k,1,i)
		for j in range(1,len(dmrlFileDic[i])):
			resultSheet.write(k,j+1,dmrlFileDic[i][j])
		k = k + 1

	resultbook.close()	


comfirmList= os.listdir(confirmPath)
dmrlPathList= os.listdir(dmrlPath)
for i in comfirmList:
	if i in dmrlPathList:
		if i[:3] != "SDS":
			dmrlCompare(confirmPath + i,dmrlPath + i,comparePath + i)
		else:
			dmrlCompare_SDS(confirmPath + i,dmrlPath + i,comparePath + i)
# ii = "SDS-TP700004-01-$new$-amm-dmrl.xlsx"
# dmrlCompare(confirmPath + ii,dmrlPath + ii,comparePath + ii)	