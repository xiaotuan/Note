### 2.9　用sys.exit()函数提前结束程序

要介绍的最后一个控制流概念是如何终止程序。当程序执行到指令的底部时，总是会终止。但是，调用 `sys.exit()` 函数，可以让程序提前终止或退出。因为这个函数在 `sys` 模块中，所以必须先导入 `sys` 才能使用它。

打开一个新的文件编辑器窗口，输入以下代码，保存为exitExample.py：

```javascript
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```

在IDLE中运行这个程序。该程序有一个无限循环，里面没有 `break` 语句。结束该程序的唯一方式就是用户输入 `exit` ，让 `sys.exit()` 函数被调用。如果 `response` 等于 `exit` ，程序就会终止。因为 `response` 变量由 `input()` 函数赋值，所以用户必须输入 `exit` 才能停止该程序。

