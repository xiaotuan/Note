### 8.1.3　关键字参数limit、timeout和default

在默认情况下， `PyInputPlus` 模块的函数会一直（或在程序运行时）要求用户提供有效输入。如果你希望某个函数在经过一定次数的尝试或一定的时间后停止要求用户输入，就可以使用 `limit` 和 `timeout` 关键字参数。用 `limit` 关键字参数传递一个整数，以确定 `PyInputPlus` 的函数在放弃之前尝试接收有效输入多少次。用 `timeout` 关键字参数传递一个整数，以确定用户在多少秒之内必须提供有效输入，然后 `PyInputPlus` 模块的函数会放弃。

如果用户未能提供有效输入，那么这些关键字参数将分别导致函数引发 `RetryLimitException` 或 `TimeoutException` 异常。例如，在交互式环境中输入以下内容：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(limit=2) 
blah
'blah' is not a number.
Enter num: number 
'number' is not a number.
Traceback (most recent call last):
    --snip--
pyinputplus.RetryLimitException
>>> response = pyip.inputNum(timeout=10) 
42 (entered after 10 seconds of waiting)
Traceback (most recent call last):
    --snip--
pyinputplus.TimeoutException
```

当你使用这些关键字参数并传入 `default` 关键字参数时，该函数将返回默认值，而不是引发异常。在交互式环境中输入以下内容：

```javascript
>>>  response = pyip.inputNum(limit=2, default='N/A') 
hello
'hello' is not a number.
world
'world' is not a number.
>>> response
'N/A'
```

`inputNum()` 函数不会引发 `RetryLimitException` ，只会返回字符串'N/A'。

