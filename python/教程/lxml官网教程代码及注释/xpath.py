##############
位置路径可以是绝对路径，也可以是相对路径。绝对路径以 “/” 开头。每条路径包括一个或多个步，每步之间以 “/” 分隔。

    绝对路径：/step/step/…
    相对路径：step/step/…

##############
使用 “|” 运算符，你可以选取符合“或”条件的若干路径。
# 选取所有book的title元素或者price元素
>>> root.xpath('//book/title|//book/price')　　
[<Element title at 0x2d88738>, <Element price at 0x2d88940>, <Element title at 0x2ca20a8>, <Element price at 0x2d88a08>]

# 选择所有title或者price元素
>>> root.xpath('//title|//price')　　
[<Element title at 0x2d88738>, <Element price at 0x2d88940>, <Element title at 0x2ca20a8>, <Element price at 0x2d88a08>]

# 选择book子元素title或者全部的price元素
>>> root.xpath('/bookstore/book/title|//price')  
[<Element title at 0x2d88738>, <Element price at 0x2d88940>, <Element title at 0x2ca20a8>, <Element price at 0x2d88a08>]


#################
步（step）包括三部分：

    坐标轴（axis）：定义所选节点与当前节点之间的关系。
    节点测试（node-test）：识别某个坐标轴内部的节点。
    预判（predicate）：提出预判条件对节点集合进行筛选。

# child::nodename 选取所有属于当前节点的 book 子元素，等价于 './nodename'
>>> root.xpath('child::book')
[<Element book at 0x2d888c8>, <Element book at 0x2d88878>]
>>> root.xpath('./book')
[<Element book at 0x2d888c8>, <Element book at 0x2d88878>]

# attribute::lang 选取当前节点的 lang 属性，等价于 './@lang'
>>> root.xpath('//*[@lang]')[0].xpath('attribute::lang')
['eng']
>>> root.xpath('//*[@lang]')[0].xpath('@lang')
['eng']

# child::* 选取当前节点的所有子元素，等价于 './*'
>>> root.xpath('child::*')
[<Element book at 0x2d88878>, <Element book at 0x2d88738>]
>>> root.xpath('./*')
[<Element book at 0x2d88878>, <Element book at 0x2d88738>]

# attribute::* 选取当前节点的所有属性，等价于 './@*'
>>> root.xpath('//*[@*]')[0].xpath('attribute::*')
['eng']
>>> root.xpath('//*[@*]')[0].xpath('@*')
['eng']

# child::text() 选取当前节点的所有文本子节点，等价于 './text()'
>>> root.xpath('child::text()')
['\n    ', '\n    ', '\n']
>>> root.xpath('./text()')
['\n    ', '\n    ', '\n']

# child::node() 选取当前节点所有子节点，等价于 './node()'
>>> root.xpath('child::node()')
['\n    ', <Element book at 0x2d88878>, '\n    ', <Element book at 0x2d88738>, '\n']
>>> root.xpath('./node()')
['\n    ', <Element book at 0x2d88878>, '\n    ', <Element book at 0x2d88738>, '\n']

# descendant::book 选取当前节点所有 book 后代，等价于 './/book'
>>> root.xpath('descendant::book')
[<Element book at 0x2d88878>, <Element book at 0x2d88738>]
>>> root.xpath('.//book')
[<Element book at 0x2d88878>, <Element book at 0x2d88738>]

# ancestor::book 选取当前节点所有 book 先辈
>>> root.xpath('.//title')[0].xpath('ancestor::book')
[<Element book at 0x2d88878>]

# ancestor-or-self::book 选取当前节点的所有 book 先辈以及如果当前节点是 book 的话也要选取
>>> root.xpath('.//title')[0].xpath('ancestor-or-self::book')
[<Element book at 0x2d88878>]
>>> root.xpath('.//book')[0].xpath('ancestor-or-self::book')
[<Element book at 0x2d88878>]
>>> root.xpath('.//book')[0].xpath('ancestor::book')
[]

# child::*/child::price 选取当前节点的所有 price 孙节点，等价于 './*/price'
>>> root.xpath('child::*/child::price')
[<Element price at 0x2d88878>, <Element price at 0x2d88738>]
>>> root.xpath('./*/price')
[<Element price at 0x2d88878>, <Element price at 0x2d88738>]