#通过E-factory函数生成xml、html文件 
from lxml.builder import E
from lxml import etree
def CLASS(*args):
    return {"class":' '.join(args)}

html = page = (
    E.html(
        E.head(
            E.title("this is a sample document")
        ),
        E.body(
            E.h1("hello",CLASS("title")),
            E.p("this is a paragraph with" ,E.b("bold"), "text in it"),
            E.p("this is another paragraph with a" ,"\n    ",
                E.a("link",href="http://www.python.org"),"."),
            E.p("here are some reserved characters: <spam&egg>."),
            etree.XML("<p>And finally an embeded XHTML fragment.</p>")
        )
    )
)

print(etree.tostring(page, pretty_print=True))