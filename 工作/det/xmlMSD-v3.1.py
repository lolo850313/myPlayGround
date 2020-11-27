#initiatedTestData无法与FailureData_Tree找到对应关系

def write_excel(data,head,outPath): 
	import xlwt  
	workbook = xlwt.Workbook(encoding='utf-8')    
	data_sheet = workbook.add_sheet('demo')    
	row = 1
	data_sheet.write(0, 0, "FIM Code")
	data_sheet.write(0, 1, "Failure Name")  
	data_sheet.write(0, 2, "Failure Message") 
	data_sheet.write(0, 3, "Maintainace Text")  
	data_sheet.write(0, 4, "FMES ID")
	data_sheet.write(0, 5, "FR Logic")
	data_sheet.write(0, 6, "Fault Report Name")
	data_sheet.write(0, 7, "Fault Report Type")
	data_sheet.write(0, 8, "Fault Report Size")
	data_sheet.write(0, 9, "Fault Code")
	data_sheet.write(0, 10, "AlertID")
	data_sheet.write(0, 11, "FDE text")
	data_sheet.write(0, 12, "FDE Class")
	data_sheet.write(0, 13, "Test Name")
	data_sheet.write(0, 14, "Test ID")
	data_sheet.write(0, 15, "Test Type")
	data_sheet.write(0, 16, "Inhibit Conditions")
	data_sheet.write(0, 17, "Precondition Texts")
	data_sheet.write(0, 18, "MS ID")
	data_sheet.write(0, 19, "MS Name")
	data_sheet.write(0, 20, "ATA")
	data_sheet.write(0, 21, "BP")
	data_sheet.write(0, 22, "Date")

	for i in data:
		for sub in data[i]["fde_info"]:		
			data_sheet.write(row, 0, data[i].get("FIM Code","FIM Code not exist"))
			data_sheet.write(row, 1, data[i].get("Failure Name","Failure Name not exist"))  
			data_sheet.write(row, 2, data[i].get("Failure Message","Failure Message not exist")) 
			data_sheet.write(row, 3, data[i].get("Maintenance Text","Maintenance Text not exist"))  
			data_sheet.write(row, 4, data[i].get("FMES ID","FMES ID not exist"))
			data_sheet.write(row, 5, data[i].get("FR Logic","FR Logic not exist"))
			
			data_sheet.write(row, 6, data[i].get("Fault Report Name","Fault Report Name not exist"))
			data_sheet.write(row, 7, data[i].get("Fault Report Type","Fault Report Type not exist"))
			if data[i].get("Fault Report Size","Fault Report Size not exist") == True:
				data_sheet.write(row, 8, 1)
			else:
				data_sheet.write(row, 8, 2)

			data_sheet.write(row, 9, sub[0]) 
			data_sheet.write(row, 10, sub[1]) 
			data_sheet.write(row, 11, sub[2])
			data_sheet.write(row, 12, sub[3])

			data_sheet.write(row, 13, data[i].get("Test Name","Test not exist"))
			data_sheet.write(row, 14, data[i].get("TestIdentificationCode","TestIdentificationCode not exist")) 
			data_sheet.write(row, 15, data[i].get("Test Type","Test Type not exist")) 
			InhibitTextList = ""
			for item in data[i].get("InhibitText","InhibitText not exist"):
				InhibitTextList = InhibitTextList + item + "\n"
			data_sheet.write(row, 16, InhibitTextList)
			PreconditionTextsList = ""
			for item in data[i].get("PreconditionTexts","PreconditionTexts not exist"):
				PreconditionTextsList = PreconditionTextsList + item + "\n"
			data_sheet.write(row, 17, PreconditionTextsList)
			data_sheet.write(row, 18, head["MS ID"])
			data_sheet.write(row, 19, head["MS Name"]) 
			data_sheet.write(row, 20, head["ATA"]) 
			data_sheet.write(row, 21, head["BP"])
			data_sheet.write(row, 22, head["Date"])

			row = row + 1		
	
	workbook.save(outPath)
	return row

#<FaultReportName> 对应的<FaultReportingData ID>，该 ID 是唯一识别 Fault Report 的标识，还可以读取<CorrelatedFDEFaultCode>
def FailureData_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//FailureData")
	dic = {}
	for i in dataTree:
		FaultReporting_arr = i.findall(".//FaultReporting")
		if FaultReporting_arr == None:
			print(path + " FailureData 下没有 FaultReporting")
		for ele in FaultReporting_arr:
			data = {}
			dic[ele.attrib.get("Id")] = data
			data["FIM Code"] = i.attrib.get("FIMCode", "FIMCode not exist")
			data["Failure Name"] = i.attrib.get("FailureName","FailureName not exist")  
			data["Failure Message"] = i.attrib.get("FailureMessage","FailureMessage not exist")       
			data["Maintenance Text"] = i.attrib.get("MaintenanceText","MaintenanceText not exist")
			data["FMES ID"] = i.attrib.get("FMESFailureIdentifier","FMESFailureIdentifier not exist")
			data["FR Logic"] = i.attrib.get("FRLogic","FRLogic not exist")
	return dic

# 通过<FaultReportingData ID>，可以在 XML 文件可以读取到其相关的Id,FaultReportName,CorrelatedFDEFaultCode信息
def FaultReportingData_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//FaultReportingData")                                                                                               
	dic = {}
	for i in dataTree:
		data = {}
		dic[i.attrib["Id"]] = data
		data["Fault Report Name"] = i.attrib.get("FaultReportName","FaultRepotName not exist")
		data["Fault Report Type"] = i.attrib.get("FaultReportType","FaultRepotType not exist")
		data["Fault Report Size"] = i.attrib.get("FaultReportParameterSize","FaultRepotSize not exist")
		data["AlertID"] = []
		for j in i:
			if j.tag == "CorrelatedFDEFaultCode":
				data["AlertID"].append(j.text)

	return dic

#<CorrelatedFDEFaultCode>对应的<AlertID>、<FDEClass>和<FDE text>信息   ("D:\\01A OMS\\46-10_10_HF_GIPC_A429_CH_INSTANCES_BP423.msd")
def AlertID_info(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//FlightDeckEffectsType")
	dic = {}
	for i in dataTree:
		data = {}
		dic[i.attrib["AlertID"]] = data
		data["FaultCode"] = i.attrib.get("FaultCode","FaultCode not exist")
		data["FDEClass"] = i.attrib.get("FDEClass","FDEClass not exist")
		for j in i:
			if j.tag == "FDEText":
				data["FDEText"]=j.text

	return dic



def initiatedTestData_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//InitiatedTestData")
	dic = {}
	for i in dataTree:
		for j in i:
			if j.tag == "FailingFaults":
				data = {}
				dic[j.attrib["Id"]] = data
				data["Test Name"] = i.attrib.get("Name","Test not exist")
				data["TestIdentificationCode"] = i.attrib.get("TestIdentificationCode","TestIdentificationCode not exist")
				data["Test Type"] = i.attrib.get("TestType","TestType not exist")
				data["PreconditionTexts"] = []
				for j in i:
					if j.tag == "PreconditionTexts":
						data["PreconditionTexts"].append(j.text)
				data["InhibitText"] = []
				for j in i:
					if j.tag == "InhibitConditions":
						data["InhibitText"].append(j.attrib.get("InhibitText","InhibitText Id not exist"))
	return dic

# 头信息
def headInfo_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	icd = XMLroot.findall(".//Icd")
	data = {}
	data["BP"] = icd[0].attrib.get("IcdBaseline","IcdBaseline not exist")
	data["Date"] = icd[0].attrib.get("DateProduced","DateProduced not exist")
	MemberSystemModelingData = XMLroot.findall(".//MemberSystemModelingData")
	data["MS Name"] = MemberSystemModelingData[0].attrib.get("Name","Name not exist")
	data["MS ID"] = MemberSystemModelingData[0].attrib.get("MemberSystemId","MemberSystemId not exist")
	data["ATA"] = MemberSystemModelingData[0].attrib.get("AtaSystem","AtaSystem not exist")
	return data

#融合failureData,FaultReportingData
def mergeFaultReportingData(failureData,FaultReportingData):
	for i in failureData:
		if i in FaultReportingData:
			failureData[i].update(FaultReportingData[i])
					
	return failureData

def mergeFDE(merge_fimcode,AlertID_dic):    
	for i in merge_fimcode:
		if len(merge_fimcode[i]["AlertID"]) != 0:
			merge_fimcode[i]["fde_info"] = []
			for j in merge_fimcode[i]["AlertID"]:
				if j in AlertID_dic:
					tmpJ = [j,AlertID_dic[j]["FaultCode"] ,AlertID_dic[j]["FDEText"] ,AlertID_dic[j]["FDEClass"]]
					merge_fimcode[i]["fde_info"].append(tmpJ)
				else:
					print(file + " " + i + "alerdId "+ str(j) + "problem")
		else:
			merge_fimcode[i]["fde_info"] = [["AlertID not exist","FaultCode  not exist","FDEText  not exist","FDEClass  not exist"]]
	return merge_fimcode
				
def mergeInit(main,initiatedTestData):
	for item_main in main:
		if item_main in initiatedTestData:
			main[item_main].update(initiatedTestData[item_main])
		
	return main

# def merge_head(main,head):
# 	for i in main:
# 		i.update(head)

# 	return main


import os
dir = "D:\\程序源数据\\det\\"
dir = "C:\\Users\\lolobook\\Desktop\\工作相关\\det\\"
path = dir + "det-BP6(2).1G\\"
resultPath = dir + "testResult\\"
total = 0
for i in os.listdir(path):	
	if i[-3:] == "msd":
		file = path + i
		fileName = i[:-4]
		FaultReportingData = FaultReportingData_Tree(file)  
		failureData = FailureData_Tree(file)   
		AlertID_dic = AlertID_info(file)
		head = headInfo_Tree(file)

		initiatedTestData = initiatedTestData_Tree(file)
		merge_init = mergeInit(failureData,initiatedTestData)
		merge_fimcode = mergeFaultReportingData(failureData,FaultReportingData)
		merge_fde = mergeFDE(merge_fimcode,AlertID_dic)
		
		write_excel(merge_fde,head,resultPath + fileName + ".xls")



