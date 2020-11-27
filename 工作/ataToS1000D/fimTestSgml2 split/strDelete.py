#将dmRef中多余文字删除
def strDelete(dirPath):
	import xlwt
	import os
	from lxml import etree
	arr = os.listdir(dirPath)
	for filei in arr:
		filePath = dirPath + filei
		root = etree.parse(filePath)
		for dmRef in root.findall(".//dmRef"):
			if dmRef.find(".//dmCode").attrib["infoCode"] != "051":
				dmRefPa = dmRef.getparent()
				papaText = dmRefPa.text
				if papaText != None:
					if "任务:" in papaText or "任务：" in papaText:
						dmRefPa.text = papaText[:papaText.index("任务") +2]			

		for action in root.findall(".//action"):
			if action.text is not None:
				if "任务:" in action.text or "任务：" in action.text:
					dmRef = action.xpath("randomList/listItem/para/dmRef")
					for i in dmRef:
						if i.find(".//dmCode").attrib["infoCode"] != "051":
							iPapa = i.getparent().text
							if iPapa is not None:
								if "任务:" in iPapa or "任务：" in iPapa:
									i.getparent().text = iPapa[:iPapa.index("任务")+2]
								else:
									i.getparent().text =""

		for action in root.findall(".//para"):
			if action.text != None :
				if "任务:" in action.text or "任务：" in action.text:
					dmRef = action.xpath(".//dmRef")
					for i in dmRef:
						if i.find(".//dmCode").attrib["infoCode"] != "051":
							iPapa = i.getparent().text
							if iPapa is not None:
								if "任务:" in iPapa or "任务：" in iPapa:
									i.getparent().text = iPapa[:iPapa.index("任务")+2]
								else:
									i.getparent().text =""
		
		root.write(filePath, pretty_print=True,encoding="utf-8")	

if __name__ == "__main__":
	strDelete("D:\\测试\\s1000d\\s1000d_fim\\split_To\\")
	