你可以使用 `ChrW()` 方法将一个整数转换成 Unicode 字符。其定义如下：

```vb
Public Function ChrW(CharCode As Integer) As Char
```

例如：

```vb
Dim associatedChar As Char
' Returns "我".
associatedChar = ChrW(25105)
```

