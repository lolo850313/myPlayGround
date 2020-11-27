from lxml import etree

page = etree.Element('html')
doc = etree.ElementTree(page)

headElt = etree.SubElement(page, 'head')
bodyElt = etree.SubElement(page, 'body')
title = etree.SubElement(headElt, 'title')
title.text = 'YOur page title here'

#直接修改标签的tag值，在不需要生成新树的情况下，修改老树达到ata转s1000d的要求
#此步直接将head标签改变为newHead标签
headElt.tag = "newHead"

# #删除子元素
# headElt.remove(title)

# #清空子元素
# headElt.clear()

linkElt = etree.SubElement(headElt,'link',rel='stylesheet',href='mystyle.css',type='text/css')
outFile= open('/Users/hewenhao/homemade.xml','wb+')
doc.write(outFile)