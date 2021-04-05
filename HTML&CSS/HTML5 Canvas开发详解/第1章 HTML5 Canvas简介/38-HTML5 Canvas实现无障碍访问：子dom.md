### 1.11.7　HTML5 Canvas实现无障碍访问：子dom

目前，用于实现画布无障碍访问的方法被称为“后备DOM概念”或者“子dom”（其中包括将文字直接加入的<canvas></canvas>标签中）。

众所周知，由于HTML5 Canvas是一个采用即时模式进行位图映射的屏幕区域，因此并不适合实现无障碍访问。在Canvas中，没有任何固定的DOM元素或显示列表可以帮助无障碍设备（比如屏幕阅读器）搜索画布上绘制的文字、图像以及它们的属性。为了使得Canvas可以无障碍访问，建议使用一种被称为“后备DOM”的概念，有时也被称为“子dom”。利用这种方法，开发者创建一个Dom元素使其匹配Canvas上的每一个元素，然后将其放入子dom中。

在创建的第一个“Hello World”的Canvas示例中（参见CH1EX3.html），文本“Hello World!”显示在一张背景图上（见图 1-3）。如果为这个示例创建一个子dom，可以这样做：

```javascript
<canvas id="canvasOne" width="500" height="300">
<div>A yellow background with an image and text on top:
　　<ol>
　　　 <li>The text says "Hello World"</li>
　　　 <li>The image is of the planet earth.</li>
　　　 </ol>
　　</div>
</canvas>
```

制作一个可以无障碍访问的标题替换下面的代码：

```javascript
<title>Ch1Ex6: Canvas Sub Dom Example </title>
```

将它改为：

```javascript
<title>Chapter 1 Example 6 Canvas Sub Dom Example </title>
```

为了测试这个页面，还需要一个屏幕阅读器（或者一个屏幕阅读器的模拟器）。Fangs是一个Firefox的屏幕模拟器插件，它可以在打开网页时将屏幕阅读器能够读出的文字列出来，这样就可以帮助用户进行无障碍的调试了。安装这个插件后，在页面上点击鼠标右键，选择“View Fangs”选项就可以看到屏幕阅读器是如何查看网页的了。

对于刚刚创建的Canvas页面，Fangs会显示，页面会按照下面的文字进行朗读：“Chapter one Example six Canvas Sub Dom Example dash Internet Explorer A yellow background with an image and text on top List of two items one The text says quote Hello World quote two The image is of the planet earth.List end.”

对于Google Chrome浏览器，可以选择Google Chrome的扩展程序Chrome Vox。这个工具会尝试朗读页面上所有的内容。

完整示例请参考本书代码中的CH1EX6.html。

#### 点击测试的提案

如果尝试在画布上制作更复杂的效果，而不仅仅是一个简单的动画，那么就会很快发现子dom是一个相当笨拙的办法。为什么呢？因为将后备元素与Canvas的交互效果相关联并不一个轻松的任务。对于屏幕阅读器来说，它需要知道画布上每个元素的确切位置才能进行解读，并且这个过程相当复杂。

为了解决这个问题，需要一些方法将子dom元素与画布上的位图区域相关联。新的W3C Canvas点击测试的提案中对于为什么将此类功能添加到Canvas规范做了以下阐述：

> 在目前的HTML5规范中，开发者被建议在canvas元素中创建一个后备DOM，使屏幕阅读器能够与画布的用户界面交互。由于这些元素的大小和位置都没有定义，因此会导致无障碍工具出现一些问题。例如，这些工具应该如何汇报这些元素的大小和位置？
> 因为画布元素需要经常响应用户的输入操作，所以使用同一种机制处理点击测试和无障碍访问的问题似乎是一个明智的决定。

（1）他们在暗示一种什么机制？

这个想法似乎是在创建两个新的方法，setElementPath（element）和clearElementPath（element）。这将允许程序员定义（和删除）的画布上的一个区域，该区域可以作为点击区域使用，并与画布的后备DOM元素关联。这样看来，必须为setElementPath()方法提供一个可访问的后备DOM元素，才能将之与点击测试相关联。当一个点击被检测到，就会触发一个事件，整个机制就是这样运作的。

（2）这对开发者意味着什么？

对于相对固定的用户界面，这会使事情变得更容易。有人曾经有多少次，想为游戏界面上的按钮点击创建一个简单的方法？但是最终，不得不使用与处理游戏精灵交互时用到的点击检测流程相同的方法（笔者每一次都不得不这么做）。然而，对于移动游戏中的精灵来说，这个方法没什么帮助。用户不得不在每次精灵移动时调用setElementPath()方法，并更新后备DOM元素的坐标。对于一个游戏来说，这意味着3倍的开销。显然，此时无障碍化的优先级不能可能排在第一位。

