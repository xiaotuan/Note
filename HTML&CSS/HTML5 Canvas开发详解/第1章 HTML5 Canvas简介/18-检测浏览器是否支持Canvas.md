### 1.6.3　检测浏览器是否支持Canvas

现在已经得到了HTML页面上定义的canvas元素的引用，下面就需要检测它是否包含环境。Canvas环境是指支持Canvas的浏览器定义的绘图界面。简单地说，如果环境不存在，画布也不会存在。有多种方式可以对此进行验证。前面已经在HTML页面中定义了Canvas。第一种方式是在调用Canvas的getContext方法之前，检测Canvas对象以及getContext方法是否存在。

```javascript
if (!theCanvas || !theCanvas.getContext){
　 return;
}
```

实际上，这段代码测试了两件事：第一，它测试theCanvas是否包含false（如果命名的id不存在，document.getElementById()将返回此值）；第二，它测试getContext()函数是否存在。

如果测试失败，那么return语句将中断程序执行。

另一个方法是创建一个函数，在其中创建一个虚拟画布，以此来检测浏览器是否支持。这个方法是由Mark Pilgrim在他的HTML5网站创建并流行起来的。

```javascript
function canvasSupport (){
　　return !!document.createElement('canvas').getContext;
}
function canvasApp(){ 
　 if (!canvasSupport){
　　　return;
　}
}
```

作者最喜欢的方法是使用modernizr.js库Modernizr是一个易用并且轻量级的库，可以检测各种Web技术的支持情况。Modernizr创建了一组静态的布尔值，可以检测是否支持Canvas。

为了在HTML页面中包含modernizr.js，可以从<a class="my_markdown" href="['http://www.modernizr.com/']">http://www.modernizr.com/</a>的空口下载代码并将外部.js文件包含到HTML页面中。

```javascript
<script src="modernizr.js"></script>
```

为了检测是否支持Canvas，将canvasSupport()函数进行修改，如下所示。

```javascript
function canvasSupport (){
　 return Modernizr.canvas;
}
```

这里将要使用modernizr.js方法，因为它提供了测试Web浏览器是否支持Canvas的最佳途径。

