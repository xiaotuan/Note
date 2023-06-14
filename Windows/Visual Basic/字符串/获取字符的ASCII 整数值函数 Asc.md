`Asc` 函数返回表示与某个字符相对应的字符的 ASCII 整数值。其定义如下：

```vb
Public Function Asc([String] As Char) As Integer
Public Function Asc([String] As String) As Integer
```

> 注意：如果 `String` 是 `Nothing` 或不包含任何字符，将会抛出 `ArgumentException`错误。

> 提示：如果传递给 `Asc` 函数的参数是一个字符串，该函数将返回字符串的第一个字符的字符代码的整数值。
>
> ```vb
> Console.WriteLine("Sea char value is " & Asc("Sea"))
> ' Sea char value is 83
> ```

```vb
Dim codeInt As Integer
' The following line of code sets codeInt to 65.
codeInt = Asc("A")
' The following line of code sets codeInt to 97.
codeInt = Asc("a")
' The following line of code sets codeInt to 65.
codeInt = Asc("Apple")
```

