[toc]

`Double` 数据类型保存有符号的 IEEE 64 位（8 字节）双精度浮点数，其的值范围是从 -1.79769313486231570E+308 到 -4.94065645841246544E-324（对于负值）和从 4.94065645841246544E-324 到 1.79769313486231570E+308（对于正值）。 双精度数字存储实数的近似值。

### 注解

`Double` 数据类型为数字提供最大和最小可能的量值。

`Double` 的默认值为 0。

### 编程提示

- **精度。** 当你使用浮点数时，请记住，它们在内存中并不一定具有精确的表示形式。 这可能会导致某些操作产生意外结果，如值比较和 `Mod` 运算符。 有关详细信息，请参阅[数据类型疑难解答](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/troubleshooting-data-types)。

- **尾随零。** 浮点数据类型不包含尾随 0 字符的任何内部表示形式。 例如，它们不区分 4.2000 和 4.2。 因此，在显示或打印浮点值时，不会出现尾随 0 字符。

- **类型字符。** 将文本类型字符 `R` 追加到文本会将其强制转换为 `Double` 数据类型。 例如，如果一个整数值后跟 `R`，则该值将更改为 `Double`。

  ```vb
  ' Visual Basic expands the 4 in the statement Dim dub As Double = 4R to 4.0:
  Dim dub As Double = 4.0R
  ```

  将标识符类型字符 `#` 追加到任何标识符会将其强制转换为 `Double`。 在以下示例中，会将变量 `num` 类型化为 `Double`：

  ```vb
  Dim num# = 3
  ```

- **Framework 类型。** .NET Framework 中的对应类型是 [System.Double](https://learn.microsoft.com/zh-cn/dotnet/api/system.double) 结构。