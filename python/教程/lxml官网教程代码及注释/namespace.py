# 导入库
import lxml.etree as etree

# 注册指定命名空间
etree.register_namespace("ttt", "http://www.hellojesson/ttt")

# 生成根节点
root = etree.Element("{http://www.hellojesson/ttt}jesson", xsi="http://www.hahaha.com", guid="33344555677777777777", version="1.0")
# 生成子节点：
order = etree.SubElement(root, "{http://www.hellojesson/ttt}order")
orderhead = etree.SubElement(order, "{http://www.hellojesson/ttt}orderhead")
guid = etree.SubElement(orderhead, "{http://www.hellojesson/ttt}guid")

# 节点赋值
order.text = "text"
orderhead.text = "111"
guid.text = "hello nihao"

# 输出 查看效果
print(etree.tostring(root, pretty_print=True))