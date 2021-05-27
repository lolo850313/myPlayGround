简单控件独立存在，但界面上控件有时还要以某种关系存在。

第一种关系是 包含关系 。比如容器控件中包含其他控件，又比如
radioButtonGroup 包含若干个 radioButton 。这种关系中的控件分别称为父控件 ( parent control ) 和子控件 ( child control ) 。父控件对其它控件的参照称为聚合 ( aggregation )。
Aggregation 关系中，各个子控件的生命周期依赖于父控件，当父控件销毁的时候，子控件也被销毁。另外，子控件不使用 placeAt() 方法放在
DOM 对象中，而是利用父控件的方法添加到父控件的集合中，由父控件来渲染。下面使用 radioButtonGroup和 radioButton 说明聚合关系：

第二种关系叫做 association，指一个控件参照到另外一个控件。我们刚才的例子中，label 和 radioButtonGroup 是完全独立的，而按照 web设计的 ARIA 兼容原则 ( ARIA: Accessible Rich Internet Applications )，这两个控件应该关联起来。
和 Aggregation 不同的是，Association 中父子控件的生命周期是独立的。