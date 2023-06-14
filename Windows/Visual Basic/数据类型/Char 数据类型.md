`Char` 数据类型保存 16 位（2 字节）无符号码位，值的范围为 0 到 65535。 每个码位或字符代码表示单个 Unicode 字符。

如果需要仅保存单个字符且不需要 `String` 的开销，请使用 `Char` 数据类型。 在某些情况下，可以使用 `Char()`（即 `Char` 元素的数组）来保存多个字符。

默认值 `Char` 是码位为 0 的字符。

Unicode 的前 128 个码位 (0–127) 对应于标准美国键盘上的字母和符号。 前 128 个码位与 ASCII 字符集定义的码位相同。 第二个 128 码位 (128–255) 表示特殊字符，例如拉丁字母、重音、货币符号和小数。 Unicode 使用剩余的码位 (256-65535) 来表示各种符号，其中包括全球文本字符、音调符号以及数学和技术符号。

可以在 `Char` 变量上使用 [IsDigit](https://learn.microsoft.com/zh-cn/dotnet/api/system.char.isdigit) 和 [IsPunctuation](https://learn.microsoft.com/zh-cn/dotnet/api/system.char.ispunctuation) 等方法来确定其 Unicode 分类。

Visual Basic 不会在 `Char` 和数值类型之间直接转换。 可以使用 [Asc](https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.visualbasic.strings.asc) 或 [AscW](https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.visualbasic.strings.ascw) 函数将 `Char` 值转换为表示其码位的 `Integer`。 可以使用 [Chr](https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.visualbasic.strings.chr) 或 [ChrW](https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.visualbasic.strings.chrw) 函数将 `Integer` 值转换为具有该码位的 `Char`。

如果类型检查开关（[Option Strict 语句](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/statements/option-strict-statement)）处于打开状态，则必须将文本类型字符追加到单字符字符串文本中，以将其标识为 `Char` 数据类型。 下面的示例对此进行了演示。 `charVar` 变量的第一个赋值生成编译器错误 [BC30512](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/misc/bc30512)，因为 `Option Strict` 处于打开状态。 第二个赋值成功编译，因为 `c` 文本类型字符将文本标识为 `Char` 值。

```vb
Option Strict On

Module CharType
    Public Sub Main()
        Dim charVar As Char

        ' This statement generates compiler error BC30512 because Option Strict is On.  
        charVar = "Z"  

        ' The following statement succeeds because it specifies a Char literal.  
        charVar = "Z"c
    End Sub
End Module
```

