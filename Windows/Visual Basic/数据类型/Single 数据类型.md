[toc]

`single` 数据类型保留已签名的 IEEE 32 位 (4 字节) 的单精度浮点数，范围为 -3.4028235E+38 到 -1.401298E-45（负值），从 1.401298E-45 到 3.4028235E+38（正值）。 单精度数字存储实数的近似值。

### 注解

使用 `Single` 数据类型可包含不需要 `Double` 的完整数据宽度的浮点值。 在某些情况下，公共语言运行时可以将 `Single` 变量紧密地打包在一起，并节省内存消耗。

`Single` 的默认值为 0。

### 编程提示

- **精度。** 使用浮点数时，请记住，它们在内存中不一定有精确的表示形式。 这可能会导致某些操作产生意外结果，如值比较和 `Mod` 运算符。 有关详细信息，请参阅[数据类型疑难解答](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/troubleshooting-data-types)。
- **Widening。** `Single` 数据类型加宽到 `Double`。 这意味着，可以将 `Single` 转换为 `Double`，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **尾随零。** 浮点数据类型不包含尾随 0 字符的任何内部表示形式。 例如，它们不区分 4.2000 和 4.2。 因此，在显示或打印浮点值时，不会出现尾随 0 字符。
- **类型字符。** 将文本类型字符 `F` 追加到文本会将其强制转换为 `Single` 数据类型。 将标识符类型字符 `!` 追加到任何标识符会将其强制转换为 `Single`。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.Single](https://learn.microsoft.com/zh-cn/dotnet/api/system.single) 结构。