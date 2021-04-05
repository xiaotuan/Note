### 1.7　用console.log调试

在超越“Hello World!”去探索更强大更丰富的内容前，还有些内容需要讨论。本书通过使用现代Web浏览器的console.log功能实现了一个简单的调试方法。这个函数可以通过代码在JavaScript控制台中记录文本信息日志，从而可以帮助用户找出问题（或者机会）。每个浏览器都有一个可以使用console.log的JavaScript控制台（Chrome、Opera、Safari、安装Firebug的Firefox等）。同时，那些不支持console.log的浏览器将弹出讨厌的错误提示。

为了处理这个错误，可以用一个外壳将console.log包装一下，使其只在浏览器支持的情况下被调用。这个外壳创建了一个名叫Debugger的类，然后创建一个在任何位置都可以被调用的Debugger.log静态函数，如下所示。

```javascript
Debugger.log("Drawing Canvas");
```

以下是console.log()函数的代码。

```javascript
var Debugger = function (){ };
Debugger.log = function (message){
　 try {
　　　console.log(message);
　 } catch (exception){
　　　return;
　 }
}
```

