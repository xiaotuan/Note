### 3.1　def语句和参数

如果调用 `print()` 或 `len()` 函数，你会传入一些值放在括号之间，称为“参数”。也可以自己定义接收参数的函数。在文件编辑器中输入下面这个例子，将它保存为helloFunc2.py：

```javascript
❶  def hello(name):
     ❷ print('Hello, ' + name)
❸  hello('Alice')
   hello('Bob')
```

如果运行这个程序，输出结果看起来像下面这样：

```javascript
Hello, Alice
Hello, Bob
```

可以在https://autbor.com/hellofunc2/上查看该程序的执行情况。在这个程序的 `hello()` 函数定义中，有一个名为 `name` 的变元❶。“变元”是一个变量，当函数被调用时，参数就存放在其中。 `hello()` 函数第一次被调用时，使用的参数是 `'Alice'` ❸。程序执行进入该函数，变量 `name` 自动设为 `'Alice'` ，就是被 `print()` 语句输出的内容❷。

关于变元有一件特殊的事情值得注意：保存在变元中的值，在函数返回后就丢失了。例如前面的程序，如果你在 `hello('Bob')` 之后添加 `print(name)` ，程序会报 `NameError` ，因为没有名为 `name` 的变量。在函数调用 `hello('Bob')` 返回后，这个变量被销毁了，所以 `print(name)` 会引用一个不存在的变量 `name` 。

这类似于程序结束时，程序中的变量会被丢弃。在本章后续内容中，当我们探讨函数的局部作用域时，我会进一步分析为什么会这样。

