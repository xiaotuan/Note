### 8.1.2　关键字参数blank

在默认情况下，除非将 `blank` 关键字参数设置为 `True` ，否则不允许输入空格字符：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ') 
Enter num:(blank input entered here)
Blank  values  are  not  allowed. 
Enter num: 42
>>>  response
42
>>>  response = pyip.inputNum(blank=True)
(blank input entered here)
>>>  response
''
```

如果你想使输入可选，请使用 `blank = True` ，这样用户不需要输入任何内容。

