from lxml import etree
from lxml import objectify

E = objectify.E
root = E.root(
    E.a(5),
    E.b(6.21),
    E.c(True),
    E.d("how", tell="me")
)

print(etree.tostring(root, pretty_print=True))

#除了上述方法，还可以使用以下方法生成xml树
ROOT = objectify.E.root
TITLE = objectify.E.title
HOWMANY = getattr(objectify.E, "how-many")

root1 =  ROOT(
    TITLE("title"),
    HOWMANY(5)
)
print(etree.tostring(root1, pretty_print=True))

#objectify.E是objectify.ElementMaker的实例。默认情况会有一个没有命名空间的pytype的注释。
#可以使用annotate关键字来控制pytype注释，也可以通过nsmap来定义一个命名空间
myE = objectify.ElementMaker(annotate=False, namespace = "http://my/ns", nsmap={None : "http://my/ns"})
root2 = myE.root(myE.someint(2))
print(etree.tostring(root2, pretty_print=True))
