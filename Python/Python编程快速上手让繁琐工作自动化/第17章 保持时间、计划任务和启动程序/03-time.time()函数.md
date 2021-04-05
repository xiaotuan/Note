### 17.1.1　time.time()函数

“UNIX纪元”是编程中经常参考的时间：1970年1月1日0点，即协调世界时（UTC）。 `time.time()` 函数返回自那一刻以来的秒数，它是一个浮点值（回想一下，浮点值只是一个带小数点的数）。这个数字称为UNIX“纪元时间戳”。例如，在交互式环境中输入以下代码：

```javascript
>>> import time
>>> time.time()
1543813875.3518236
```

这里，我在2018年12月2日，太平洋标准时间9:11 pm，调用 `time.time()` 。返回值是UNIX纪元的那一刻与 `time.time()` 被调用的那一刻之间的秒数。

纪元时间戳可以用于“剖析”代码，也就是测量一段代码的运行时间。如果在代码块开始时调用 `time.time()` ，并在结束时再次调用，就可以用第二个时间戳减去第一个，得到这两次调用之间的时间。例如，打开一个新的文件编辑器窗口，然后输入以下程序：

```javascript
   import time
❶ def calcProd():
       # Calculate the product of the first 100,000 numbers.
       product = 1
       for i in range(1, 100000):
             product = product * i
        return product
❷ startTime = time.time()
  prod = calcProd()
❸ endTime = time.time()
❹ print('The result is %s digits long.' % (len(str(prod))))
❺ print('Took %s seconds to calculate.' % (endTime - startTime))
```

在❶行，我们定义了函数 `calcProd()` ，循环遍历1至99 999的整数，并返回它们的乘积。在❷行，我们调用 `time.time()` ，将结果保存在 `startTime` 中。调用 `calcProd()` 后，我们再次调用 `time.time()` ，将结果保存在 `endTime` 中❸。最后我们输出 `calcProd()` 返回的乘积的长度❹，以及运行 `calcProd()` 的时间❺。

将该程序保存为calcProd.py，并运行它。输出结果看起来像这样：

```javascript
The result is 456569 digits long.
Took 2.844162940979004 seconds to calculate.
```



**注意：**
另一种剖析代码的方法是利用 `cProfile.run()` 函数。与简单的 `time.time()` 技术相比，它提供了更详细的信息。



`time.time()` 函数的返回值是有用的，但不是人类可读的。 `time.ctime()` 函数返回一个关于当前时间的字符串描述。你也可以选择传入由 `time.time()` 函数返回的自UNIX纪元以来的秒数，以得到一个时间的字符串值。在交互式环境中输入以下代码：

```javascript
>>> import time
>>> time.ctime()
'Mon Jun 15 14:00:38 2020'
>>> thisMoment  =  time.time()
>>> time.ctime(thisMoment)
'Mon  Jun  15  14:00:45  2020'
```

