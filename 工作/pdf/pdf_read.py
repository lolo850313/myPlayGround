import pdfplumber
path = "D:\\file\\amm31.pdf"

with pdfplumber.open(path) as pdf:
    page = pdf.pages[4]
    text = page.extract_text()
    print(text)