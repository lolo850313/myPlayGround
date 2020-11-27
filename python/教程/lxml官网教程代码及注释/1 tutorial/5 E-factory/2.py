from lxml.builder import ElementMaker # lxml only !
from lxml import etree
#带命名空间
E = ElementMaker(nsmap=
    {'dc' : "http://www.purl.org/dc/elements/1.1/",
    'rdf' : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'xlink' : "http://www.w3.org/1999/xlink",
    'xsi' : "http://www.w3.org/2001/XMLSchema-instance"})

# 'noNamespaceSchemaLocation' : "http://www.s1000d.org/S1000D_4-1/xml_schema_flat/wrngdata.xsd"
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

print(etree.tostring(my_doc, pretty_print=True))