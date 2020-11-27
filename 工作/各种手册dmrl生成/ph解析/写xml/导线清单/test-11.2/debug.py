path = "/Users/Hewenhao/wb103+/WB_8810C05700G20_A_fd5deb8e-b964-431b-ae30-0e313a0fbddf.xls"
import xlrd
book = xlrd.open_workbook(path)
sh = book.sheet_by_index(0)
rowTotal = sh.nrows
for i in range(sh.nrows):
    for j in range(sh.ncols):
        print(i,j)
        print(sh.row(i)[j].value)