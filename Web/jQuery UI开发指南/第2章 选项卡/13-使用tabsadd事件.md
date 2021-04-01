### 2.5.5　使用 `tabsadd` 事件

使用同样的例子，只是这次用 `bind()` 方法来管理事件。在添加选项卡时，jQuery UI会触发 `tabsadd` 事件（如粗体部分所示）：

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css
 　　　href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<div id=tabs>
　<ul>
　　<li><a href=#tab1>Tab 1</a></li>
　　<li><a href=#tab2>Tab 2</a></li>
　　<li><a href=#tab3>Tab 3</a></li>
　</ul>
　<div id=tab1>Contents of first tab</div>
　<div id=tab2>Contents of the second tab</div>
　<div id=tab3>Contents of the third tab</div>
</div>
<script>
$("#tabs").tabs ({
　　fx : { opacity : "toggle" }
　}).bind ("tabsadd", function (event, tab)
　{
　　$ (tab.panel).load ("action.php");
　}).tabs ("add", "#tab4", "Tab 4");
</script>
```

首先创建选项卡，然后监听 `tabsadd` 事件，最后向列表中插入一个选项卡。要小心，这个顺序是很重要的，否则没有任何效果。

<a class="my_markdown" href="['#ac21']">①</a>　如果自己添加的样式写在jQuery UI的前面，则根据CSS的优先级规则，自己添加的样式会被jQuery UI的样式覆盖，就像被“忽略”了一样。——译者注



