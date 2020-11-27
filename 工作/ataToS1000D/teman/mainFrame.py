def frame(lsheet,ICNpath):
	from lxml import etree
	
	from graphic import graphicAdd

	#lsheet中的数据提取
	toolnbr = lsheet.attrib["toolnbr"]
	#内容生成
	content_element = etree.Element("content")
	description = etree.SubElement(content_element,"description")

	#toolnbr生成第一个levelledPara
	levelledPara_1 = etree.SubElement(description,"levelledPara")
	levelledPara_1_title = etree.SubElement(levelledPara_1,"title")
	levelledPara_1_title.text = "PART NUMBER"
	levelledPara_1_para = etree.SubElement(levelledPara_1,"para")
	levelledPara_1_para.set("id","par-PN")
	levelledPara_1_para.text = toolnbr
	
	#tlsect
	for tlsect in lsheet.xpath("tlsect"):       
		if "othtype" in tlsect.attrib:
			if tlsect.attrib["othtype"] == "SPC":
				tlsectParaText = tlsect.find("para").text            
				levelledPara_SPC = etree.SubElement(description,"levelledPara")
				levelledPara_SPC_title = etree.SubElement(levelledPara_SPC,"title")
				levelledPara_SPC_title.text = "SUPPLIER"
				levelledPara_SPC_para = etree.SubElement(levelledPara_SPC,"para")
				levelledPara_SPC_para.text = tlsectParaText                
				levelledPara_SPC_para.set("id","par-SPP")                                   
			elif tlsect.attrib["othtype"] == "AMM":
				tlsectParaText = tlsect.find("para").text            
				levelledPara_AMM = etree.SubElement(description,"levelledPara")
				levelledPara_AMM_title = etree.SubElement(levelledPara_AMM,"title")
				levelledPara_AMM_title.text = "MAINTENANCE TASK"
				levelledPara_AMM_para = etree.SubElement(levelledPara_AMM,"para")
				levelledPara_AMM_para.text = tlsectParaText                
				levelledPara_AMM_para.set("id","par-MT")
			elif tlsect.attrib["othtype"] == "NTE":
				tlsectParaText = tlsect.find("para").text            
				levelledPara_AMM = etree.SubElement(description,"levelledPara")
				levelledPara_AMM_note = etree.SubElement(levelledPara_AMM,"note")
				levelledPara_AMM_notePara = etree.SubElement(levelledPara_AMM_note,"notePara")
				levelledPara_AMM_notePara.text = tlsectParaText
		else:
			if "type" in tlsect.attrib:
				if tlsect.attrib["type"] == "DES":
					tlsectParaText = tlsect.find("para").text
					levelledPara_2 = etree.SubElement(description,"levelledPara")
					levelledPara_2_title = etree.SubElement(levelledPara_2,"title")
					levelledPara_2_para = etree.SubElement(levelledPara_2,"para")
					levelledPara_2_para.text = tlsectParaText                
					levelledPara_2_title.text = "FUNCTION AND USAGE"
				if tlsect.attrib["type"] == "DIM":
					tlsectParaText = tlsect.find("para").text
					levelledPara_2 = etree.SubElement(description,"levelledPara")
					levelledPara_2_title = etree.SubElement(levelledPara_2,"title")
					levelledPara_2_para = etree.SubElement(levelledPara_2,"para")
					levelledPara_2_para.text = tlsectParaText
					
					levelledPara_2_title.text = "DIMENTIONS"
				if tlsect.attrib["type"] == "WGT":
					tlsectParaText = tlsect.find("para").text
					levelledPara_2 = etree.SubElement(description,"levelledPara")
					levelledPara_2_title = etree.SubElement(levelledPara_2,"title")
					levelledPara_2_para = etree.SubElement(levelledPara_2,"para")
					levelledPara_2_para.text = tlsectParaText                
					levelledPara_2_title.text = "MASS"
				if tlsect.attrib["type"] == "OTH":
					if tlsect.find("para") != None:
						paraList = tlsect.findall("para")
						levelledPara_2 = etree.SubElement(description,"levelledPara")
						for i in paraList:
							tlsectParaText = i.text                            
							levelledPara_2_para = etree.SubElement(levelledPara_2,"para")
							levelledPara_2_para.text = tlsectParaText

					else:
						tlsectParaText = ""
						levelledPara_2 = etree.SubElement(description,"levelledPara")
						levelledPara_2_para = etree.SubElement(levelledPara_2,"para")
						levelledPara_2_para.text = tlsectParaText
				if tlsect.attrib["type"] == "PLI":
					oldRowList = tlsect.findall(".//tbody/row")
					from lxml.builder import ElementMaker
					E = ElementMaker()
					paraOfrow1 =[]
					for para in oldRowList[0].findall(".//para"):                  
						paraOfrow1.append(para.text)
					if (len(paraOfrow1)) == 6:
						if paraOfrow1[1] == None:
							paraOfrow1.pop(1)
						else:
							paraOfrow1[0] = paraOfrow1[0] + paraOfrow1[1]
							paraOfrow1.pop(1)
					paraOfrow1_1=[]
					for i in paraOfrow1:
						if i != None:
							paraOfrow1_1.append(i)
						else:
							paraOfrow1_1.append("")
					while len(paraOfrow1_1)<5:
						paraOfrow1_1.append("")
					#TEMAN32507,ITEM091000G05
					table_xml = E.table
					tgroup_xml = E.tgroup
					colspec_xml = E.colspec
					thead_xml = E.thead
					row_xml = E.row
					entry_xml = E.entry
					para_xml = E.para
					tbody_xml = E.tbody
					table_element = table_xml(
						tgroup_xml(
							colspec_xml(colname = "col0"),
							colspec_xml(colname = "col1"),
							colspec_xml(colname = "col2"),
							colspec_xml(colname = "col3"),
							colspec_xml(colname = "col4"),
							thead_xml(
								row_xml(
									entry_xml(
										para_xml("图-项目号"),
										align = "center",
										valign = "middle"
									),
									entry_xml(
										para_xml("零件号"),
										align = "center",
										valign = "middle"
									),
									entry_xml(
										para_xml("说明"),
										align = "center",
										valign = "middle"
									),
									entry_xml(
										para_xml("有效性"),
										align = "center",
										valign = "middle"
									),
									entry_xml(
										para_xml("件数"),
										align = "center",
										valign = "middle"
									), 
								)
							),
							tbody_xml(
								row_xml(
									entry_xml(
										para_xml(paraOfrow1_1[0])                                        
									),
									entry_xml(
										para_xml(paraOfrow1_1[1]),
										align = "center"
									),
									entry_xml(
										para_xml(paraOfrow1_1[2]),
										align = "center",
									),
									entry_xml(
										para_xml(paraOfrow1_1[3]),
										align = "center",
									),
									entry_xml(
										para_xml(paraOfrow1_1[4]),
										align = "center",
									), 
								)
							),
							cols = "5")
						)

					#将tbody下的第二行以后的数据录入table_element中
					paraOfTbody_not1 = []
					for i in range(1,len(oldRowList)):
						tmpEntryList = oldRowList[i].findall(".//entry")
						tmpRow=[]
						for i in tmpEntryList:
							if i.find("para")== None:
								tmpRow.append("")
							else:
								if i.find("para").text==None:
									tmpRow.append("")
								else:
									tmpRow.append(i.find("para").text)
						paraOfTbody_not1.append(tmpRow)
					for i in paraOfTbody_not1:
						i[0] = i[0] + i[1]
						i.pop(1)
					for i in paraOfTbody_not1:
						tmpRow_xml = etree.Element("row")
						tmpEntry_xml1 = etree.SubElement(tmpRow_xml,"entry")
						tmpEntry_xml1.set("align","right")
						tmpPara_xml = etree.SubElement(tmpEntry_xml1,"para")
						tmpPara_xml.text = i[0]
						tmpEntry_xml2 = etree.SubElement(tmpRow_xml,"entry")
						tmpEntry_xml2.set("align","center")
						tmpPara_xml = etree.SubElement(tmpEntry_xml2,"para")
						tmpPara_xml.text = i[1]
						tmpEntry_xml3 = etree.SubElement(tmpRow_xml,"entry")
						tmpPara_xml = etree.SubElement(tmpEntry_xml3,"para")
						tmpPara_xml.text = i[2]
						tmpEntry_xml4 = etree.SubElement(tmpRow_xml,"entry")
						tmpPara_xml = etree.SubElement(tmpEntry_xml4,"para")
						tmpPara_xml.text = i[3]
						tmpEntry_xml5 = etree.SubElement(tmpRow_xml,"entry")
						tmpEntry_xml5.set("align","center")
						tmpPara_xml = etree.SubElement(tmpEntry_xml5,"para")
						tmpPara_xml.text = i[4]
						table_element.find(".//tbody").append(tmpRow_xml)			
					description.append(table_element)
	
	for graphic in lsheet.xpath("graphic"):
		graphic_title = graphic.find("title").text
		figure = etree.SubElement(description,"figure")
		figure_title = etree.SubElement(figure,"title")
		figure_title.text = graphic_title

		graphic_sheetList = graphic.findall("sheet")
		for sheet in graphic_sheetList:
			graphic_sheet_gnbr = sheet.attrib["gnbr"]
			infoEntityIdent = graphicAdd(ICNpath,graphic_sheet_gnbr)     
			figure_graphic = etree.SubElement(figure,"graphic")
			figure_graphic.set("infoEntityIdent",infoEntityIdent)

	return content_element





