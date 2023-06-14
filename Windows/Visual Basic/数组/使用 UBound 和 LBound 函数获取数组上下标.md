> 提示：
>
> 由于 Visual Basic 要求数组开始下标必须为 0，而可以通过数组的长度减 1 来获取最大的可用下标，因此这两个方法没有什么用处。

`UBound` 函数可以返回指定数组中的指维数可用的最大下标。其返回值为 `Long` 类型。而 `LBound` 函数与 `UBound` 函数相反，该函数可以返回指定数组中指定维数可用的最小下标，其值为 `Long` 类型。其语法格式如下：

```vb
UBound(<数组>[, <维数>])
LBound(<数组>[, <维数>])
```

例如：

```vb
Dim lowest, bigArray(10, 15, 20), littleArray(6) As Integer
highest = UBound(bigArray, 1)
highest = UBound(bigArray, 3)
highest = UBound(littleArray)
' The three calls to UBound return 10, 20, and 6 respectively.

lowest = LBound(bigArray, 1)
lowest = LBound(bigArray, 3)
lowest = LBound(littleArray)
' All three calls to LBound return 0.
```

