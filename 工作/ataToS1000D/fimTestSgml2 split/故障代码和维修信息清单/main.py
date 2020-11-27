#输入输出路径
dirPath = "D:\\测试\\s1000d\\s1000d_fim\\table\\"
#表格名称
excelPath = dirPath + "ARJFRMFIM-故障代码和维修信息清单-2019.9-转S1000D-20191202.xls"
#xml发布版本号
issueNumber = "000"
#xml发布日期
date = {"day":"25","month":"11","year":"2019"}

from eicas import eicasfile
from cms import cmsfile
from cabin import cabinfile
from ob import obfile
eicasfile(dirPath,excelPath,issueNumber,date)
cmsfile(dirPath,excelPath,issueNumber,date)
cabinfile(dirPath,excelPath,issueNumber,date)
obfile(dirPath,excelPath,issueNumber,date)
