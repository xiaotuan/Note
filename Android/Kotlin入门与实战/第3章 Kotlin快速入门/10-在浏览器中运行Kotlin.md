### 3.3.3　在浏览器中运行Kotlin

Kotlin 1.1版本添加了对JavaScript的支持，开发者可以使用Kotlin进行网页开发，Kotlin实现的是ECMAScript 5.1版本。Kotlin实现了一个kotlinc-js编译器，kotlinc-js编译器主要用来完成词法分析、语义分析和将Kotlin代码转换成JavaScript代码并交由JavaScript引擎执行。

使用Kotlin可以创建面向客户端JavaScript，实现与DOM元素的交互。另外，Kotlin还可以与现有的一些JavaScript框架配合使用（如ReactJS、JQuery等）。

接下来，创建一个名为kotlin_javascript.kt的文件并输入如下代码。

```python
fun main(args: Array<String>) {  
    println("hello, kotlin_Javascript" )    
}
```

然后，使用kotlinc-js命令将Kotlin代码转换为JavaScript代码，完成命令后，会在该目录下生成相应的JavaScript文件。

```python
kotlinc-js -output kotlin_javascript.js kotlin_javascript.kt
```

使用文本编辑器打开kotlin_javascript.js文件，代码如下。

```python
if (typeof kotlin === 'undefined') {
throw new Error("Error loading module 'kotlin_javascript'. Its dependency 'kotlin' was not found. Please, check whether 'kotlin' is loaded prior to 'kotlin_javascript'.");
}
var kotlin_javascript = function (_, Kotlin) {
  'use strict';
  var println = Kotlin.kotlin.io.println_s8jyv4$;
  function main(args) {
    println('hello\uFF0Cword!');
  }
  _.main_kand9s$ = main;
  main([]);
  Kotlin.defineModule('kotlin_javascript', _);
  return _;
}(typeof kotlin_javascript === 'undefined' ? {} : kotlin_javascript, kotlin);
/Users/xiangzhihong/Kotlin/workspace/kotlinDemo/kotlin_javascript.kt
```

对于转换后的JavaScript代码，不必深究里面的结构和语法，只需要明白一点，转换后的代码可供浏览器解析执行。不过，kotlin_javascript.kt中使用了println函数，因此需要引入Kotlin原生依赖库。对于JavaScript端来说，要执行原生的API，同样也需要一个JavaScript依赖库，这个文件就是kotlin.js。具体来说，在Kotlin编译器目录的lib文件夹下，有一个kotlin-jslib.jar文件，这个文件包含了JavaScript运行时需要的相关环境，使用解压工具将其解压，会发现目录中包含一个kotlin.js文件，将其复制到与kotlin_javascript.js同级的目录下。

接下来，新建一个名为javascript_test.html的文件并输入如下代码。

```python
<head>
 <meta charset="UTF-8">
 <title>Kotlin JavaScript</title>
</head>
<body>
<script type="text/javascript" src="./kotlin.js"></script>
<script type="text/javascript" src="./kotlin_javascript.js">
</script>
</body>
</html>
```

使用浏览器打开javascript_test.html文件，就会在浏览器的Console面板打印相关的信息。

