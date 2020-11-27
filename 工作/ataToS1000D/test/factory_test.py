from lxml.builder import ElementMaker # lxml only !
from lxml import etree
#带命名空间
E = ElementMaker(namespace="http://my.de/fault/namespace",
                nsmap={'p' : "http://my.de/fault/namespace"})

# #不带命名空间
# E = ElementMaker()

DOC = E.doc
TITLE = E.title
SECTION = E.section
PAR = E.par

my_doc = DOC(
    TITLE("The dog and the hog"),
    SECTION(
    TITLE("The dog"),
    PAR("Once upon a time, ..."),
    PAR("And then ...")
    ),
    SECTION(
    TITLE("The hog"),
    PAR("Sooner or later ...")
    )
    )

applicRef = etree.Element('applicRef')
#直接使用insert对xml树添加子元素
my_doc.insert(2,applicRef)
#通过操作element来添加子元素
descr = etree.SubElement(my_doc[1][2], 'descr')

print(my_doc.xpath("section"))
etree.ElementTree(my_doc).write('/Users/hewenhao/homemade.xml',pretty_print=True)