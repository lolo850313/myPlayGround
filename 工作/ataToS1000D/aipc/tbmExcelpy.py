#将item中tbm转换前和转换后的数据写入字典中
def tbmExcel(item):
    from lxml import etree

    #techData
    if item.find("tbm")!=None:
        tbm = item.find("tbm").text
        
        if tbm.count("，")==3:
            tbmList= tbm.split("，")
            aa = tbmList[0][:tbmList[0].find(" IN")]
            bb = tbmList[1][:tbmList[1].find(" IN")]
            cc = tbmList[2][:tbmList[2].find(" MM.")]
            dd = tbmList[3][:tbmList[3].find(" ")]
            ee = tbmList[3][tbmList[3].find(" "):].strip()
            
        elif tbm.count(",")==3:
            tbmList= tbm.split(",")
            aa = tbmList[0][:tbmList[0].find(" IN")]
            bb = tbmList[1][:tbmList[1].find(" IN")]
            cc = tbmList[2][:tbmList[2].find(" MM.")]
            dd = tbmList[3][:tbmList[3].find(" ")]
            ee = tbmList[3][tbmList[3].find(" "):].strip()

        elif tbm.count(",")==4:
            tbmList= tbm.split(",")
            aa = tbmList[0][:tbmList[0].find(" IN")]
            bb = tbmList[1][:tbmList[1].find(" IN")]
            cc = tbmList[2][:tbmList[2].find("MM.")]
            ddee = tbmList[3]+ tbmList[4]
            ddeeList = ddee.split(" ")
            dd = ddeeList[0]           
            ee = ddeeList[1].strip()

        else:
            aa = ""
            bb = ""
            cc = ""
            dd = ""
            ee = ""
        # tbmDic = {"导管材料信息":tbm,"管径":aa,"壁厚":bb,"管长":cc,"材料规范":dd,"材料牌号":ee}
        return  {"导管材料信息":tbm,"管径":aa,"壁厚":bb,"管长":cc,"材料规范":dd,"材料牌号":ee}




