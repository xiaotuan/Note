### 1.6.1　为Canvas封装JavaScript代码

前面已经创建了一种测试HTML页面是否加载完毕的方法，下面开始创建JavaScript应用程序。因为JavaScript在HTML页面中运行，所以它可以与其他JavaScript应用程序和代码一起运行。通常，这不会导致什么问题。但是，可能会出现一种情况，即代码中的变量或者函数会与HTML页面中的其他JavaScript代码产生冲突。

Canvas应用程序与在浏览器中运行的其他应用有所不同。由于Canvas只在屏幕上特定的区域执行并显示结果，可以说它的功能是独占的，因此不太会受到页面上其他内容的影响，反之亦然。读者如果想在同一个页面上放置多个Canvas应用，那么在定义JavaScript代码时必须将对应的代码分开。

为避免出现这个问题，可以将变量和函数都封装在另一个函数中。JavaScript函数本身就是对象，Javascript对象既可以有属性也可以有方法。将一个函数放到另一个函数中，读者可以使第二个函数只在第一个函数的局部作用域中。

在示例中，从window load事件中调用的canvasApp()函数将包含整个Canvas应用程序。“Hello World!”示例中将会有一个名为drawScreen()的函数。一旦canvasApp()被调用，则立即调用drawScreen()来绘制“Hello World!”文本。

drawScreen()函数现在是canvasApp()的局部函数。在canvasApp()中创建的任何变量或函数对于drawScreen()来说都是局部的。但是，对于HTML页面的其余部分或其他可能运行的JavaScript应用程序来说却并非如此。

以下是如何封装函数的示例代码，也是Canvas应用程序的代码。

```javascript
function canvasApp(){
　 drawScreen();
　 ...
　 function drawScreen(){
　　　　...
　 }
}
```

