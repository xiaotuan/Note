`AscW` 函数用于返回某个字符的 Unicode 码位。其定义如下：

```vb
Public Function AscW([String] As Char) As Integer
Public Function AscW([String] As String) As Integer
```

> 注意：如果 `String` 是 `Nothing` 或不包含任何字符，将会抛出 `ArgumentException` 异常。

```vb
Console.WriteLine("我 AscW value is " & AscW("我"))
' 我 AscW value is 25105
```

