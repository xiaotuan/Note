### 3.1.3　HTML表单和画布之间的通信

回到JavaScript代码中，需要为textBox的keyup事件创建一个事件处理程序。本节通过用DOM文档对象的document.getElementById()函数查找表单元素，并把它存储到formElement变量中。然后，调用formElement的addEventListener()方法设置keyup事件，并将事件处理程序设置为已经定义的函数textBoxChanged。

```javascript
var formElement= document.getElementById("textBox");
formElement.addEventListener('keyup',textBoxChanged, false);
```

最后，要解决的问题是定义textBoxChanged()事件处理程序。这个函数的工作原理类似于本书在第1章创建的事件处理程序。当调用函数时，它传递一个参数。为了容易记忆，通常将事件对象命名为e。

事件对象包含一个名为target的属性，它包含了创建change事件的HTML表单元素的引用。Target又包含一个名为value的属性，该属性包含导致事件发生的表单元素的最新的变化值（如textBox）。程序获取这个值，并将其存储到JavaScript中创建的message变量中。也就是在绘制画布的drawScreen()方法中所用到的同一个message变量。现在，这里所要做的就是调用drawScreen()方法，新的message值将“自动”出现在画布上。

```javascript
Function textBoxChanged(e) {
　　　var target = e.target;
　　　message = target.value;
　　　drawScreen();
　 }
```

这里花了很多时间来讲述如何用JavaScript中的事件处理程序来处理HTML表单控制中的变化，然后把结果显示在HTML5 Canvas上。本章会在创建Text Arranger的过程中多次重复这类代码。然而，以后将会避免再次深入地解释它，取而代之的是聚焦于不同的方法渲染和捕捉表单数据，并把它用于画布中。

