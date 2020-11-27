import os
root = "D:\\win yun\\OneDrive\\工作\\各种手册dmrl生成\\"
confirmPath = root + "各科室反馈DMRL\\"
dmrlPath = root + "dmrl\\"
comparePath = root + "compare\\"

def dmrlCompare(confirmFile,dmrlFile):
    import xlrd
    import xlwt

    confirmFileDic = {}
    confirmtable = xlrd.open_workbook(confirmFile).sheets()[0]
    rowlength1 = confirmtable.nrows
    for row in range(1,rowlength1):
        confirmFileDic[confirmtable.cell(row,1).value] = [confirmtable.cell(row,2).value,confirmtable.cell(row,3).value,confirmtable.cell(row,4).value,confirmtable.cell(row,5).value,confirmtable.cell(row,6).value,confirmtable.cell(row,7).value,confirmtable.cell(row,8).value,confirmtable.cell(row,9).value,confirmtable.cell(row,10).value,confirmtable.cell(row,11).value,confirmtable.cell(row,12).value,confirmtable.cell(row,13).value,confirmtable.cell(row,14).value,confirmtable.cell(row,15).value]
    dmrlFileDic = {}
    dmrltable = xlrd.open_workbook(dmrlFile).sheets()[0]
    rowlength2 = dmrltable.nrows
    for row in range(1,rowlength2):
        dmrlFileDic[dmrltable.cell(row,1).value] = [dmrltable.cell(row,0).value,dmrltable.cell(row,2).value,dmrltable.cell(row,3).value,dmrltable.cell(row,4).value,dmrltable.cell(row,5).value,dmrltable.cell(row,6).value,dmrltable.cell(row,7).value,dmrltable.cell(row,8).value,dmrltable.cell(row,9).value,dmrltable.cell(row,10).value,dmrltable.cell(row,11).value,dmrltable.cell(row,12).value,dmrltable.cell(row,13).value,dmrltable.cell(row,14).value,dmrltable.cell(row,15).value]
    
    for i in dmrlFileDic:
        if i in confirmFileDic:
            tmp = 0
            for j in range(13):                
                if confirmFileDic[i][j] != dmrlFileDic[i][j+1]:
                    tmp = 1
            if tmp == 1:
                dmrlFileDic[i].append("not same with confirmExcel")
        else:
            dmrlFileDic[i].append("new data")

    resultbook = xlwt.Workbook()
    resultSheet = resultbook.add_sheet("new")
    k = 0
    for i in dmrlFileDic:
        resultSheet.write(k,0,dmrlFileDic[i][0])
        resultSheet.write(k,1,i)
        for j in range(1,len(dmrlFileDic[i])):
            resultSheet.write(k,j+1,dmrlFileDic[i][j])
        k = k + 1

    resultbook.save("d:\\result.xls")

    
        
    
    #如果完全一致，则不输出结果文件
    
    


comfirmList= os.listdir(confirmPath)
dmrlPathList= os.listdir(dmrlPath)
for i in comfirmList:
    if i in dmrlPathList:
        dmrlCompare(confirmPath + i,dmrlPath + i)
    