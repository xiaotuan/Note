### 18.6　多个DOM元素

现在大家已经知道如何遍历、获取和查询元素，那么可以对这些元素做些什么呢？就从修改元素内容开始吧。由前面的学习可以知道，每个元素都有text Content和innerHTML属性，可以用来访问（和修改）元素的内容。textContent可以去除所有的HTML标签，只留下纯文本数据，而innerHTML则可以用来创建HTML元素（产生一个新的DOM节点）。下面来看看如何访问并修改下面例子中的第一个段落：

```javascript
const para1 = document.getElementsByTagName('p')[0];
para1.textContent;    // "This is a simple HTML file."
para1.innerHTML;      // "This is a <i>simple</i> HTML file."
para1.textContent = "Modified HTML file";       // 在浏览器中看看有什么变化
para1.innerHTML = "<i>Modified</i> HTML file";  // 在浏览器中看看有什么变化
```

> <img class="my_markdown" src="../images/3.png" style="width:151px;  height: 145px; " width="10%"/>
> textContent和innerHTML是一种灾难性的操作：它会替换掉元素中的所有内容，不管里面有什么。例如，可以通过在<body>元素上设置innerHTML来替换掉整个页面的内容！

