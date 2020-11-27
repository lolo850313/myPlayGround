def effectToDic(effList):   
    effDic = {}
    #流水号
    idNum = 1
    #获得有效性与流水号的字典
    for i in effList:        
        if i not in effDic:
            id = "appRef-" + str(idNum).zfill(3)
            idNum = idNum + 1
            effDic[i] = id
            
    return effDic