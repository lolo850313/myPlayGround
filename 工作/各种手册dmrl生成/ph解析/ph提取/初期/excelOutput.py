def excelOutput(xmlpath,WireTable):		
	import xlwt
	excelList=[]
	

	rowTitle=["WireHarness","PinParentFrom","PinFrom","TerminalCodeFrom","Tag","MaterialCode","AWG","Length","PinParentTo","PinTo","TerminalCodeTo","Segregation","WiringDiagram","PartNumberFrom","PartNumberTo","Color"]
	for i in WireTable:
		excelList.append([i.get("WireHarness",""),i.get("PinParentFrom",""),i.get("PinFrom",""),i.get("TerminalCodeFrom",""),i.get("Tag",""),i.get("MaterialCode",""),i.get("AWG",""),i.get("Length",""),i.get("PinParentTo",""),i.get("PinTo",""),i.get("TerminalCodeTo",""),i.get("Segregation",""),i.get("WiringDiagram",""),i.get("PartNumberFrom",""),i.get("PartNumberTo",""),i.get("Color","")])
	
	workbook = xlwt.Workbook(encoding='utf-8')
	data_sheet = workbook.add_sheet("demo")
	for i in range(0,len(rowTitle)):
		data_sheet.write(0,i,rowTitle[i])
		
	for i in range(len(excelList)):
		for j in range(len(excelList[i])):
			data_sheet.write(i+1,j,excelList[i][j])
	
	savePath="d:/PHexcel"+xmlpath[5:-2]+"ls"
	workbook.save(savePath)