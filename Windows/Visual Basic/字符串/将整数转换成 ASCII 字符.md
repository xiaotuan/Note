你可以使用 `Chr()` 方法将指定的字符代码转换成字符。`Chr()` 方法定义如下：

```vb
Public Function Chr(CharCode As Integer) As Char
```

例如：

```vb
Dim associatedChar As Char
' Returns "A".
associatedChar = Chr(65)
' Returns "a".
associatedChar = Chr(97)
' Returns ">".
associatedChar = Chr(62)
' Returns "%".
associatedChar = Chr(37)
```

