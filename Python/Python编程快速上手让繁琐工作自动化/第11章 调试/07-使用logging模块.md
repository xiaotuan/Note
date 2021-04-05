### 11.4.1　使用logging模块

要启用 `logging` 模块以在程序运行时将日志消息显示在屏幕上，请将下面的代码复制到程序顶部（但在Python的#!行之下）：

```javascript
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)
s - %(message)s')
```

你不需要过于担心它的工作原理，当 Python 记录一个事件的日志时，它都会创建一个 `LogRecord` 对象以保存关于该事件的信息。 `logging` 模块的函数让你指定想看到的这个 `LogRecord` 对象的细节，以及希望的细节展示方式。

假如你编写了一个函数以计算一个数的阶乘。在数学上，4 的阶乘是1 × 2 × 3 × 4，即24。7的阶乘是1 × 2 × 3 × 4 × 5 × 6 × 7，即5040。打开一个新的文件编辑器窗口，输入以下代码。其中有一个bug，但你也会输入一些日志消息，帮助你弄清楚哪里出了问题。将该程序保存为factorialLog.py：

```javascript
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s
-  %(message)s') 
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total  =   1
    for i in range(n + 1): 
        total *= i
        logging.debug('i is ' +  str(i) +  ', total is ' +  str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')
```

我们在想如何输出日志消息时，使用了 `logging.debug()` 函数。这个 `debug()` 函数将调用 `basicConfig()以` 输出一行信息。这行信息的格式是我们在 `basicConfig()` 函数中指定的，这行信息包括我们传递给 `debug()` 的消息。 `print(factorial(5))` 调用是原来程序的一部分，因此就算禁用日志消息，结果仍会显示。

这个程序的输出结果就像这样：

```javascript
2019-05-23 16:20:12,664 - DEBUG - Start of program
2019-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2019-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2019-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2019-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2019-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2019-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2019-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2019-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2019-05-23 16:20:12,684 - DEBUG - End of program
```

`factorial()` 函数返回0作为5的阶乘结果，这是不对的。 `for` 循环应该用从1到5的数乘以 `total` 的值。但 `logging.debug()` 显示的日志消息表明， `i` 变量从0开始，而不是1。因为0乘任何数都是0，所以在接下来的迭代中， `total` 的值都是错的。日志消息提供了可以追踪的痕迹，帮助你弄清楚何时事情开始不对。

将代码行 `for i in range(n + 1)` ：改为 `for i in range(1,n + 1)` ：，再次运行程序。输出结果看起来像这样：

```javascript
2019-05-23 17:13:40,650 - DEBUG - Start of program
2019-05-23 17:13:40,651 - DEBUG - Start of factorial(5)
2019-05-23 17:13:40,651 - DEBUG - i is 1, total is 1
2019-05-23 17:13:40,654 - DEBUG - i is 2, total is 2
2019-05-23 17:13:40,656 - DEBUG - i is 3, total is 6
2019-05-23 17:13:40,659 - DEBUG - i is 4, total is 24
2019-05-23 17:13:40,661 - DEBUG - i is 5, total is 120
2019-05-23 17:13:40,661 - DEBUG - End of factorial(5)
120
2019-05-23 17:13:40,666 - DEBUG - End of program
```

`factorial(5)` 调用正确地返回120。日志消息表明循环内发生了什么，这直接指向了bug。

你可以看到， `logging.debug()` 调用不仅输出了传递给它的字符串，而且包含一个时间戳和单词DEBUG。

