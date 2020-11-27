from lxml import etree

page = etree.Element('html')
doc = etree.ElementTree(page)

headElt = etree.SubElement(page, 'head')
bodyElt = etree.SubElement(page, 'body')
title = etree.SubElement(headElt, 'title')
title.text = 'YOur page title here'

# #删除子元素
# headElt.remove(title)

#清空子元素
headElt.clear()

linkElt = etree.SubElement(headElt,'link',rel='stylesheet',href='mystyle.css',type='text/css')
outFile= open('d://homemade.xml','wb+')
doc.write(outFile)
# etree.ElementTree(page).write('/Users/hewenhao/dmrl/homemade.xml',pretty_print=True,encoding="utf-8")