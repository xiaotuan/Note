### 17.1.2　time.sleep()函数

如果需要让程序暂停一下，就调用 `time.sleep()` 函数，并传入希望程序暂停的秒数。在交互式环境中输入以下代码：

```javascript
   >>> import time
   >>> for i in range(3):
         ❶ print('Tick')
         ❷ time.sleep(1)
         ❸ print('Tock')
         ❹ time.sleep(1)
   Tick
   Tock
   Tick
   Tock
   Tick
   Tock
❺ >>> time.sleep(5)
```

`for` 循环将输出 `Tick` ❶，暂停1秒❷，输出 `Tock` ❸，暂停1秒❹，再输出 `Tick` ，暂停1秒，如此继续，直到 `Tick` 和 `Tock` 分别被输出3次。

`time.sleep()` 函数将“阻塞”（也就是说，它不会返回或让程序执行其他代码），直到传递给 `time.sleep()` 的秒数流逝。例如，如果输入 `time.sleep(5)`  ❺，那你会在5秒后才看到下一个提示符（ `>>>` ）。

