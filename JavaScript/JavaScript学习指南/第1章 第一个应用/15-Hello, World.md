### 1.10　Hello, World

最后用一个例子来结束本章，这个例子跟Brian Kernighan在1972年编写的例子具有相同的表现力。此时已经完成了所有的核心工作，剩下来要做的是添加文本。在onMouseDown事件处理器之前插入下面的代码：

```javascript
var c = Shape.Circle(200, 200, 80);
c.fillColor = 'black';
var text = new PointText(200, 200);
text.justification = 'center';
text.fillColor = 'white';
text.fontSize = 20;
text.content = 'hello world';
```

这段代码非常直观：创建另一个圆作为文本的背景，并且创建了一个真实的文本对象（ `PointText` ）。然后指定它的位置，以及一些额外的属性（对齐方式，颜色和字体尺寸）。最后，给它设置了真实的文字内容（“hello world”）。

注意：这里不是我们第一次使用JavaScript来展示文字了。第一次是在本章开始的 `console.log` 中打印文字。当然也可以将打印的文字改成“hello world.”，在许多方面，这更类似于在1972年可能会经历的事情（假如见证了Brian Kernighan在1972年编写了第一个hello world）。但是就这个例子，文字本身及如何渲染它不是重点，重点是创造的东西已经产生了显著的效果。

刷新浏览器，此刻犹如在参加一个庄严神圣而传统的“Hello, World”盛宴。如果读者是第一次编写“Hello, World”，欢迎加入“Hello, World”俱乐部。如果不是，希望通过这个例子，读者能对JavaScript有一个初步的认识。

<a class="my_markdown" href="['#ac11']">[1]</a>　微软的术语。

<a class="my_markdown" href="['#ac12']">[2]</a>　在第9章中会详细介绍function和method的不同之处。

<a class="my_markdown" href="['#ac13']">[3]</a>　如果你想学习更多关于CSS和HTML的内容，我推荐学习Codecademy上的免费HTML和CSS课程。

<a class="my_markdown" href="['#ac14']">[4]</a>　技术评论家Matt Inman提到，Page.js开发者可能是Photoshop用户，他们熟悉“手工具”“直接选择工具”等。



