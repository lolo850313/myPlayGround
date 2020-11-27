
#读取excel中列信息，输出导线信息字典
def wireDic(path):
    import xlrd
    book = xlrd.open_workbook(path)
    sh = book.sheet_by_index(0)

    #导线信息从第五行开始
    startRow = 5
    rowTotal = sh.nrows
    result = []

    for i in range(startRow, rowTotal):
        row = {}
        row["线束号"] = sh.row(i)[0].value
        row["从端设备号"] = sh.row(i)[1].value
        row["从端孔号"] = sh.row(i)[2].value        
        row["从端端接代号"] = sh.row(i)[3].value
        row["导线号"] = sh.row(i)[4].value
        row["导线材料"] = sh.row(i)[5].value
        row["AWG"] = sh.row(i)[6].value
        row["导线长度"] = sh.row(i)[7].value
        row["到端设备号"] = sh.row(i)[8].value
        row["到端孔号"] = sh.row(i)[9].value
        row["到端端接代号"] = sh.row(i)[10].value
        row["敷设字母"] = sh.row(i)[11].value
        row["线路图图内号"] = sh.row(i)[12].value
        row["备注"] = sh.row(i)[13].value
        result.append(row)
    
    return (result)

#读取excel中第五行第一列信息，构建dmcode字典
def dmCodeDic(path):    
    import xlrd
    import re

    
    book = xlrd.open_workbook(path)
    sh = book.sheet_by_index(0)

    harness = sh.row(5)[0].value

    #通过正则检查dmcode所用信息是否正确
    reCheck = r'[A-Za-z]{1}[0-9]{4}'
    if re.match(reCheck,harness) == None:
        print(path)

    dmCode = {"assyCode":"00","disassyCode":harness[2:],"disassyCodeVariant":"A","infoCode":"057","infoCodeVariant":"A","itemLocationCode":"A","modelIdentCode":"C919","subSubSystemCode":harness[2],"subSystemCode":harness[1],"systemCode":"88","systemDiffCode":"A"}
    
    return dmCode
