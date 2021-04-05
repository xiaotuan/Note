### 8.1.1　关键字参数min、max、greaterThan和lessThan

接收 `int` 和 `float` 数的 `inputNum()` 、 `inputInt()` 和 `inputFloat()` 函数还具有 `min` 、 `max` 、 `greaterThan` 和 `lessThan` 关键字参数，用于指定有效值范围。例如，在交互式环境中输入以下内容：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ', min=4)
Enter num:3
Input must be at minimum 4. 
Enter num:4
>>>  response
4
>>> response = pyip.inputNum('Enter num: ', greaterThan=4)
Enter num: 4
Input must be greater than 4. 
Enter num: 5
>>> response
5
>>> response = pyip.inputNum('>', min=4, lessThan=6)
Enter num: 6
Input must be less than 6. 
Enter num: 3
Input must be at minimum 4. 
Enter num: 4
>>>  response
4
```

这些关键字参数是可选的，但只要提供，输入就不能小于 `min` 参数或大于 `max` 参数（但输入可以等于它们）。而且，输入必须大于 `greaterThan` 且小于 `lessThan` 参数（也就是说，输入不能等于它们）。

