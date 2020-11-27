def readExcel(path):
    import xlrd
    book = xlrd.open_workbook(path)
    sh = book.sheet_by_index(0)
    startRow = 7
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
