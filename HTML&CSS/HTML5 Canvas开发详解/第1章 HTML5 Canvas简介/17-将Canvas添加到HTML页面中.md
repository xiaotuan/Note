### 1.6.2　将Canvas添加到HTML页面中

在HTML的<body>部分添加一个<canvas>标签时，可以参考以下代码。

```javascript
<canvas id="canvasOne" width="500" height="300">
 Your browser does not support HTML5 Canvas.
</canvas>
```

现在，小结一下正在讨论的内容。<canvas>标签有3个主要属性。在HTML中，属性被设在尖括号括起来的HTML标签中。这3个属性分别如下。

+ id：id在JavaScript代码中用来指示特定<canvas>标签的名字，如canvasOne。
+ width：画布宽度，以像素为单位。width将设为500像素。
+ height：画布高度，以像素为单位。height将设为300像素。

提示

> HTML5元素（包括canvas）还有很多属性，如tabindex、title、class、accesskey、dir、draggable、hidden等。

在开始标签<canvas>和结束标签</canvas>中间可以添加文本，一旦浏览器执行HTML页面时不支持Canvas，就会显示这些文字。以本章的Canvas应用程序为例，这里将使用文本“Your browser does not support HTML5 Canvas（你的浏览器不支持HTML5 Canvas）”。实际上，此处可以放置任意文字。

#### 在JavaScript中使用document对象引用Canvas元素

接下来，用DOM引用HTML中定义的<canvas>标签。document对象加载后可以引用HTML页面的任何元素。

这里需要一个Canvas对象的引用，这样就能够知道当JavaScript调用Canvas API时其结果在哪里显示。

首先定义一个名为theCanvas的新变量，用来保存Canvas对象的引用。

接下来，通过调用document的getElementById()函数得到canvasOne的引用。canvasOne是在HTML页面中为创建的<canvas>标签定义的名字。

```javascript
var theCanvas = document.getElementById("canvasOne");
```

