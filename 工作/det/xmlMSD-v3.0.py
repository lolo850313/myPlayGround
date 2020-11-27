def write_excel(data,outPath):  
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

	for i in range(len(data)):
		# #alertId有可能是字符串，也有可能是列表或者字典。如果是字符串则应该
		# if not isinstance(data[i].get("AlertID"),(str)) and len(data[i].get("AlertID")) > 0:			
		# 	data_sheet.write(row, 0, data[i].get("FIM Code","FIM Code not exist"))
		# 	data_sheet.write(row, 1, data[i].get("Failure Name","Failure Name not exist"))  
		# 	data_sheet.write(row, 2, data[i].get("Failure Message","Failure Message not exist")) 
		# 	data_sheet.write(row, 3, data[i].get("Maintenance Text","Maintenance Text not exist"))  
		# 	data_sheet.write(row, 4, data[i].get("FMES ID","FMES ID not exist"))
		# 	data_sheet.write(row, 5, data[i].get("FR Logic","FR Logic not exist"))
		# 	data_sheet.write(row, 6, data[i].get("Fault Report Name","Fault Report Name not exist"))
		# 	data_sheet.write(row, 7, data[i].get("Fault Report Type","Fault Report Type not exist"))
		# 	if data[i].get("Fault Report Size","Fault Report Size not exist") == True:
		# 		data_sheet.write(row, 8, 1)
		# 	else:
		# 		data_sheet.write(row, 8, 2)
		# 	data_sheet.write(row, 13, data[i].get("Test Name","Test not exist"))
		# 	data_sheet.write(row, 14, data[i].get("TestIdentificationCode","TestIdentificationCode not exist")) 
		# 	data_sheet.write(row, 15, data[i].get("Test Type","Test Type not exist")) 
		# 	InhibitTextList = ""
		# 	for item in data[i].get("InhibitText","InhibitText not exist"):
		# 		InhibitTextList = InhibitTextList + item + "\n"
		# 	data_sheet.write(row, 16, InhibitTextList)
		# 	PreconditionTextsList = ""
		# 	for item in data[i].get("PreconditionTexts","PreconditionTexts not exist"):
		# 		PreconditionTextsList = PreconditionTextsList + item + "\n"
		# 	data_sheet.write(row, 17, PreconditionTextsList)
		# 	data_sheet.write(row, 18, data[i].get("MS ID","MS ID not exist"))
		# 	data_sheet.write(row, 19, data[i].get("MS Name","MS Name not exist")) 
		# 	data_sheet.write(row, 20, data[i].get("ATA","ATA not exist")) 
		# 	data_sheet.write(row, 21, data[i].get("BP","BP not exist"))
		# 	data_sheet.write(row, 22, data[i].get("Date","Date not exist"))
		# 	for q in range(len(data[i].get("AlertID"))):
		# 		# 有些AlertID的列表中的子元素为字符串，所以应将此中子元素排除
		# 		# [{'AlertID': '1359', 'FaultCode': '1359', 'FDEClass': 'caution',
		# 		# 'FDEText': 'DOOR NOT CLSD'}, {'AlertID': '1360', 'FaultCode': '1360', 'FDEClass': 'caution', 'FDEText': 'DOOR DISARMED'}, '1361', '1362', '1363', '1364', '1365', '1366', '1367', '1368', '1369', '1370', '
		# 		# 1372', '1373', {'AlertID': '1374', 'FaultCode': '1374', 'FDEClass': 'advisory', 'FDEText': 'REFUEL DOOR NOT CLSD'}, '1375', {'AlertID': '1371', 'FaultCode': '1371', 'FDEClass': 'advisory', 'FDEText': 'FL
		# 		# IGHT LOCK FAULT'}]

		# 		for sub_aid in range(len())
		# 		if not isinstance(data[i].get("AlertID")[q],(str)): 
		# 			data_sheet.write(row, 9, data[i].get("AlertID")[q].get("FaultCode","FaultCode not exist")) 
		# 			data_sheet.write(row, 10, data[i].get("AlertID")[q].get("AlertID","AlertID not exist")) 
		# 			data_sheet.write(row, 11, data[i].get("AlertID")[q].get("FDEText","FDEText not exist"))
		# 			data_sheet.write(row, 12, data[i].get("AlertID")[q].get("FDEClass","FDEClass not exist"))
		# 		else:
		# 			data_sheet.write(row, 10, data[i].get("AlertID")[q])
		# 		row = row + 1			
		# else:
		
		data_sheet.write(row, 0, data[i].get("FIM Code","FIM Code not exist"))
		data_sheet.write(row, 1, data[i].get("Failure Name","Failure Name not exist"))  
		data_sheet.write(row, 2, data[i].get("Failure Message","Failure Message not exist")) 
		data_sheet.write(row, 3, data[i].get("Maintenance Text","Maintenance Text not exist"))  
		data_sheet.write(row, 4, data[i].get("FMES ID","FMES ID not exist"))
		data_sheet.write(row, 5, data[i].get("FR Logic","FR Logic not exist"))
		data_sheet.write(row, 6, data[i].get("Fault Report Name","Fault Report Name not exist"))
		data_sheet.write(row, 7, data[i].get("Fault Report Type","Fault Report Type not exist"))
		data_sheet.write(row, 8, data[i].get("Fault Report Size","Fault Report Size not exist")) 
		data_sheet.write(row, 9, data[i].get("AlertID","AlertID not exist")) 
		data_sheet.write(row, 10, " ") 
		data_sheet.write(row, 11, " ")
		data_sheet.write(row, 12, " ")
		data_sheet.write(row, 13, data[i].get("Test Name","Test not exist"))
		data_sheet.write(row, 14, data[i].get("TestIdentificationCode","TestIdentificationCode not exist")) 
		data_sheet.write(row, 15, data[i].get("Test Type","Test Type not exist")) 
		InhibitTextList = ""
		for item in data[i].get("InhibitText","InhibitText not exist"):
			InhibitTextList = InhibitTextList + item + "@@@"
		data_sheet.write(row, 16, data[i].get(InhibitTextList,"InhibitText not exist"))
		PreconditionTextsList = ""
		for item in data[i].get("PreconditionTexts","PreconditionTexts not exist"):
			PreconditionTextsList = PreconditionTextsList + item + "@@@\n"
		data_sheet.write(row, 17, data[i].get(PreconditionTextsList,"PreconditionTexts not exist"))
		data_sheet.write(row, 18, data[i].get("MS ID","MS ID not exist"))
		data_sheet.write(row, 19, data[i].get("MS Name","MS Name not exist")) 
		data_sheet.write(row, 20, data[i].get("ATA","ATA not exist")) 
		data_sheet.write(row, 21, data[i].get("BP","BP not exist"))
		data_sheet.write(row, 22, data[i].get("Date","Date not exist"))
		row = row + 1

	
	workbook.save(outPath)
	return row

#<FaultReportName> 对应的<FaultReportingData ID>，该 ID 是唯一识别 Fault Report 的标识，还可以读取<CorrelatedFDEFaultCode>
def FailureData_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//FailureData")
	dic = []
	for i in dataTree:
		data = {}
		data["FIM Code"] = i.attrib.get("FIMCode", "FIMCode not exist")
		data["Failure Name"] = i.attrib.get("FailureName","FailureName not exist")  
		data["Failure Message"] = i.attrib.get("FailureMessage","FailureMessage not exist")       
		data["Maintenance Text"] = i.attrib.get("MaintenanceText","MaintenanceText not exist")
		data["FMES ID"] = i.attrib.get("FMESFailureIdentifier","FMESFailureIdentifier not exist")
		data["FR Logic"] = i.attrib.get("FRLogic","FRLogic not exist")
		data["Id"] = []
		FaultReporting_arr = i.findall(".//FaultReporting")
		for ele in FaultReporting_arr:
			data["Id"].append(ele.attrib.get("Id"))

				
		# if len(data["Id"]) > 1:
		# 	print(path)
		# 	print(data["Id"])
		dic.append(data)
	return dic

# 通过<FaultReportingData ID>，可以在 XML 文件可以读取到其相关的Id,FaultReportName,CorrelatedFDEFaultCode信息
def FaultReportingData_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//FaultReportingData")                                                                                               
	dic = []
	for i in dataTree:
		data = {}
		data["Id"] = i.attrib.get("Id","Id not exist")
		data["Fault Report Name"] = i.attrib.get("FaultReportName","FaultRepotName not exist")
		data["Fault Report Type"] = i.attrib.get("FaultReportType","FaultRepotType not exist")
		data["Fault Report Size"] = i.attrib.get("FaultReportParameterSize","FaultRepotSize not exist")
		data["AlertID"] = []
		for j in i:
			if j.tag == "CorrelatedFDEFaultCode":
				data["AlertID"].append(j.text)

		dic.append(data)
	# for i in dic:
	# 	print(i)
	return dic

#<CorrelatedFDEFaultCode>对应的<AlertID>、<FDEClass>和<FDE text>信息   ("D:\\01A OMS\\46-10_10_HF_GIPC_A429_CH_INSTANCES_BP423.msd")
def FDEtext_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//FlightDeckEffectsType")
	dic = []
	for i in dataTree:
		data = {}
		data["AlertID"] = i.attrib.get("AlertID","AlertID not exist")
		data["FaultCode"] = i.attrib.get("FaultCode","FaultCode not exist")
		
		if len(data["AlertID"]) == 0 :
			print(path,i)
		data["FDEClass"] = i.attrib.get("FDEClass","FDEClass not exist")
		for j in i:
			if j.tag == "FDEText":
				data["FDEText"]=j.text
		dic.append(data)
	return dic



def initiatedTestData_Tree(path):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path)
	XMLroot = tree.getroot()
	dataTree = XMLroot.findall(".//InitiatedTestData")
	dic = []
	for i in dataTree:
		data = {}
		data["Id"] = i.attrib.get("Id","Id not exist")
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

		data["FailingFaults"] = []
		for j in i:
			if j.tag == "FailingFaults":
				data["FailingFaults"].append(j.attrib.get("Id","FailingFaults Id not exist"))
		dic.append(data)
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
	if len(FaultReportingData) != 0 :
		for i in failureData:
			for j in FaultReportingData:
				if j.get("Id") in i.get("Id"):
					if "Fault Report Type" not in i.get("Id"):
						i["Fault Report Type"] = [j["Fault Report Type"]]
						i["Fault Report Size"] = [j["Fault Report Size"]]
						i["AlertID"] = [j["AlertID"]]
					else:
						i["Fault Report Type"].append(j["Fault Report Type"])
						i["Fault Report Size"].append(j["Fault Report Size"])
						i["AlertID"].append(j["AlertID"])
					

	# for i in (failureData):
	# 	print(i)
	return failureData

def mergeFDE(a,b):    
	for i in a:
		if "AlertID" in i :
			if len(i["AlertID"]) != 0:
				for j in range(len(i["AlertID"])):
					for qq in b:
						if i["AlertID"][j] == qq["AlertID"]:
							i["AlertID"][j] = qq
			else:
				i["AlertID"] = [{"AlertID":"AlertID not exist","FaultCode":"FaultCode  not exist","FDEClass":"FDEText  not exist","FDEClass":"FDEText  not exist"}]
		else:
			#否则alertID会是str，然后进入到if len(data[i].get("AlertID")) > 0下进行打印而报错。
			i["AlertID"] = [{"AlertID":"AlertID not exist","FaultCode":"FaultCode  not exist","FDEClass":"FDEText  not exist","FDEClass":"FDEText  not exist"}]    
	return a
				
def mergeInit(main,initiatedTestData):
	for item_main in main:
		for item_ini in initiatedTestData:
			#34-11_34103_ADS 3_.msd中有些FailureData下没有FaultReporting Id。
			if "Id" in item_main:
				if item_main["Id"] in item_ini["FailingFaults"]:
					item_main["InhibitText"] = item_ini["InhibitText"]
					item_main["PreconditionTexts"] = item_ini["PreconditionTexts"]
					item_main["Test Type"] = item_ini["Test Type"]
					item_main["TestIdentificationCode"] = item_ini["TestIdentificationCode"]
					item_main["Test Name"] = item_ini["Test Name"]

	return main

def merge_head(main,head):
	for i in main:
		i.update(head)

	return main


import os
dir = "D:\\程序源数据\\det\\"
dir = "C:\\Users\\lolobook\\Desktop\\工作相关\\det\\"
path = dir + "test\\"
resultPath = dir + "testResult\\"
total = 0
for i in os.listdir(path):	
	if i[-3:] == "msd":
		FaultReportingData = FaultReportingData_Tree(path + i)  

		failureData = FailureData_Tree(path + i)    
		fde = FDEtext_Tree(path + i)
		head = headInfo_Tree(path + i)
		initiatedTestData = initiatedTestData_Tree(path + i)

		merge_fimcode = mergeFaultReportingData(failureData,FaultReportingData)
		merge_fde = mergeFDE(merge_fimcode,fde)
		merge_init = mergeInit(merge_fde,initiatedTestData)
		result = merge_head(merge_init,head)
		total = total + write_excel(result,resultPath + i[:-3] + "xls")

print(total)



