import docx

from docx import Document

path = "D:\\程序源数据\\amm31.pdf"

document = Document(path)

words = {"按需", "建议","尽量","推荐","视情","如果有必要","必要","最好","如果需要","按需","按需","尽量","按需","建议","推荐"}


for paragraph in document.paragraphs:

    print(paragraph.text)
