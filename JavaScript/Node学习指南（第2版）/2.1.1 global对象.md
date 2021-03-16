[toc]

### 2.1.1　global对象

在浏览器中，如果你在最顶层声明一个变量，它就会被声明成全局（global）的。但在Node中却不是这样。当你在模块或者应用中定义变量的时候，变量不是全局的；它被限制只能在定义它的模块或者应用中使用。也就是说，你可以在模块和使用这个模块的应用中都定义一个叫作 `str` 的全局变量，而这两个变量不会有任何冲突。

为了更好地演示，我们创建一个简单的函数：将基数与另一个数字相加，然后返回结果。我们会用两种方式来实现这个方法：写一个可以在浏览器中运行的JavaScript库和一个可以被Node使用的模块。

写在JavaScript库中的代码，被保存在一个叫作add2.js的文件中。它声明一个 `base` 变量，给它赋值2，然后将它与传入的数字相加：

```python
var base = 2; 
function addtwo(input) {
   return parseInt(input) + base;
}
```

接下来，我们来创建一个很简单的模块，它做了同样的事情，只不过使用了Node的语法。我会在第3章中详细介绍模块，现在，先把下面的代码保存到一个叫作addtwo.js的文件中：

```python
var base = 2; 
exports.addtwo = function(input) {
  return parseInt(input) + base;
};
```

现在就可以演示两种环境下 `global` 的区别了。在Web页面中使用add2.js文件，add2.js文件中也定义了一个 `base` 变量：

```python
<!DOCTYPE html>
<html>
   <head>
      <script src="add2.js"></script>
      <script>
         var base = 10; 
         console.log(addtwo(10));
      </script>
   </head> 
<body> 
</body>
</html>
```

在浏览器上打开页面，控制台上显示的是20，而不是期望的12。原因就是在浏览器的JavaScript里，所有定义在函数外面的变量，都被定义在全局对象中。所以当我们在页面中定义了一个新的 `base` 变量时，就覆盖了文件中的同名变量的值。

现在，我们在Node应用中使用 `addtwo` 模块：

```python
var addtwo = require('./addtwo').addtwo; 
var base = 10;
console.log(addtwo(base));
```

Node应用中的结果是12。在Node应用中定义新的 `base` 变量并不会影响模块中 `的base` 变量，因为它们不在同一个全局命名空间里。

避免使用共享的命名空间，是一个很显著的改进，然而也不是万能的。事实上， `global` 对象为所有环境都提供了一个可以访问Node对象和函数的机制，包括马上就要讲到的 `process` 对象。你可以自己试一下：把下面的代码放进文件中，然后运行你的应用。它会给出所有全局可用的对象和函数：

```python
console.log(global);
```

