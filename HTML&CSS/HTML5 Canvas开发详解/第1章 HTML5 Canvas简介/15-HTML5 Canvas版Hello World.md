### 1.6　HTML5 Canvas版“Hello World！”

如前所述，将Canvas放入HTML5页面时第一件要做的事就是，看看整个页面是否已经加载，并且开始操作前是否所有HTML元素都已展现。在用Canvas处理图像和声音的时候，这点会非常重要。

为此，这里要使用JavaScript的事件。当定义的事件发生时，事件从对象发出。其他对象监听事件，这样就可以基于事件进行处理。用JavaScript可以监听对象的一些常见事件，包括键盘输入、鼠标移动以及加载结束。

第一个需要监听的事件是window对象的load事件。该事件在HTML页面加载结束时发生。

要为事件添加一个监听器，可以使用DOM的对象的 addEventListener()方法。因为window代表HTML页面，所以它是最高级别的DOM对象。

addEventListener()函数接受以下3个参数。

（1）load事件。

这是监听器的事件名称。对于诸如window的已有对象的事件已经预先定义过。

（2）eventWindowLoaded()事件处理器函数。

当事件发生时调用这个函数。在代码中会调用canvasApp()函数来开始执行主应用程序。

（3）useCapture：true或false。

这个参数设置函数是否在事件传递到DOM对象树的底层对象之前捕捉此种类型的事件。此处始终设为false。

下面是用来测试window是否加载完毕的最终代码。

```javascript
window.addEventListener("load", eventWindowLoaded, false);
function eventWindowLoaded (){
　 canvasApp();
}
```

另外，也可以用许多其他方式为load事件设置事件监听器。

```javascript
window.onload = function()
　 {
　　　 canvasApp();
　 }
```

或者使用如下代码。

```javascript
window.onload = canvasApp;
```

本书使用第一种方法。

