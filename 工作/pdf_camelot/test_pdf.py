import pdfplumber
import os.path as ps
import re
from openpyxl import Workbook

# glob 英文：水滴，一滴，一团。 unix，php，pyhton都有对glob的实现。
# * 匹配任意 0 或多个任意字符
# ? 匹配任意一个字符
# [] 若字符在中括号中，例如[0-9]匹配数字
import glob

file_path = "/home/lolo/Documents/pdf_camelot/PDF/EO_253A2000-560-001_EO3_020表格没提取出来.pdf"

pdf = pdfplumber.open(file_path)

for p in range(0, len(pdf.pages)):
    table_lst = []
    text_lst = []
    page = pdf.pages[p]
    page_text = page.extract_text()


