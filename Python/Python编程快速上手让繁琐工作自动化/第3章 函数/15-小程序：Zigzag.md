### 3.9　小程序：Zigzag

让我们利用到目前为止所学的编程知识，创建一个小型动画程序。该程序将创建往复的锯齿形图案，直到用户单击Mu编辑器的Stop按钮或按Ctrl-C快捷键停止它为止。运行该程序时，输出结果如下所示：

```javascript
     ********
    ********
   ********
  ********
********
  ********
   ********
    ********
     ********
```

在文件编辑器中输入以下代码，并保存为zigzag.py：

```javascript
import time, sys
indent = 0  #  How  many  spaces to indent. 
indentIncreasing = True # Whether the indentation is increasing or not. 
try: 
     while True: # The main program loop. 
          print('  ' *  indent,  end='') 
          print('********') 
          time.sleep(0.1) # Pause for 1/10 of a second. 
          if indentIncreasing: 
               #  Increase  the  number  of  spaces: 
               indent  =  indent  +  1
               if indent  ==  20: 
                    #  Change  direction: 
                    indentIncreasing = False
          else: 
               # Decrease the number of spaces: 
               indent  =  indent - 1
               if indent == 0: 
                    # Change  direction:
                    indentIncreasing = True
except KeyboardInterrupt: 
    sys.exit()
```

让我们逐行来看看代码，从头开始。

```javascript
import time, sys
indent = 0  #  How  many  spaces to indent. 
indentIncreasing = True # Whether the indentation is increasing or not. 
```

首先，我们将导入 `time` 和 `sys` 模块。我们的程序使用两个变量： `indent` 变量跟踪星号带之前的缩进间隔； `indentIncreasing` 变量包含一个布尔值，用于确定缩进量是增加还是减少。

```javascript
try: 
   while True: # The main program loop. 
      print('  ' *  indent,  end='') 
      print('********') 
      time.sleep(0.1) # Pause for 1/10 of a second. 
```

接下来，我们将程序的其余部分放在 `try` 语句中。当用户在运行Python程序的同时按 `Ctrl-C` 快捷键，Python会引发 `KeyboardInterrupt` 异常。如果没有 `try...except` 语句来捕获这个异常，程序将崩溃，并显示错误信息。但是，对于我们的程序，我们希望它通过调用 `sys.exit()函数` 来干净地处理 `KeyboardInterrupt` 异常。（此代码位于程序末尾的 `except` 语句中。）

`while True:`  无限循环将永远重复我们程序中的指令。这包括使用 `' ' * indent` 来输出正确数量的缩进空格。我们不希望在这些空格之后自动输出换行，因此我们也将 `end =''` 传递给第一个 `print()` 调用。第二个 `print()` 调用将输出星号带。 `time.sleep()` 函数还没有介绍过，但是此时只要知道，它在我们的程序中引入了1/10秒的暂停即可。

```javascript
       if indentIncreasing: 
           #  Increase  the  number  of  spaces:
           indent  =  indent  +  1
           if indent  ==  20: 
               indentIncreasing  =  False  #  Change  direction. 
```

接下来，我们要在下次输出星号时调整缩进量。如果 `indentIncreasing` 为 `True` ，则要向 `indent` 添加1。但是一旦缩进达到20，我们就希望缩进减少。

```javascript
       else: 
          # Decrease the number of spaces: 
          indent  =  indent  -  1
          if indent == 0: 
              indentIncreasing  =  True  #  Change  direction. 
```

同时，如果 `indentIncreasing` 为 `False` ，那么我们想从缩进量中减去1。缩进量达到0后，我们希望缩进量再次增加。无论哪种情况，程序执行都将跳回到主程序循环的开头，再次输出星号。

```javascript
except KeyboardInterrupt: 
    sys.exit()
```

如果用户在程序执行位于 `try` 块中的任何时候按 `Ctrl-C` 快捷键，则会引起 `Keyboard- Interrupt` 异常，该异常由 `except` 语句处理。程序执行转向 `except` 块内，该块调用 `sys.exit()` 函数并退出程序。这样，即使主程序循环是一个无限循环，用户也可以关闭程序。

