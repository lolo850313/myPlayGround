from fileList import filelist
from xmlWire import wire,WireGroup
from excelOutput import excelOutput
from xmlExtreme import extremeBasic,mergeExtreme,mergeWireAndExtreme
from partNumber import connectDevice,connectNumberToPartNumber

file = filelist("d:/ph103+./")

for	i in file:
	WireTable=[]
	extremeBasicList = []
	#第二部分 
	
	import xml.etree.ElementTree as ET
	tree = ET.parse(i)	
	XMLroot = tree.getroot()
	WireTable = wire(XMLroot)
	WireTable = WireGroup(XMLroot,WireTable)
	connectList = connectDevice(XMLroot)	
	ExtremeBasicTable = extremeBasic(XMLroot)
	ExtremeTable = connectNumberToPartNumber(connectList, ExtremeBasicTable)
	ExtremeFinalTable = mergeExtreme(ExtremeTable)
	final = mergeWireAndExtreme(WireTable,ExtremeFinalTable)
	excelOutput(i,final)


