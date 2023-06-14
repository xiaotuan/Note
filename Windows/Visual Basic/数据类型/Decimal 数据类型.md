[toc]

`Decimal` 数据类型保存由表示 96 位（12 字节）整数按 10 的可变次幂缩放所得的 128 位（16 字节）值。 缩放系数指定小数点右侧的数字位数；范围为 0 到 28。 如果小数位数为 0（无小数位数），则可能的最大值为 +/-79,228,162,514,264,337,593,543,950,335 (+/-7.9228162514264337593543950335E+28)。 如果有28个小数位数，则最大值为 +/-7.9228162514264337593543950335，最小非零值为 +/-0.0000000000000000000000000001 (+/-1E-28)。

### 注解

`Decimal` 数据类型为数字提供的有效位数最多。 它最多支持 29 个有效位数，并可表示超过 7.9228 x 10 ^ 28 的值。 它特别适用于需要大量数字但不允许舍入误差的计算（例如财务）。

`Decimal` 的默认值为 0。

### 编程提示

- **精度。** `Decimal` 不是浮点数据类型。 `Decimal` 结构包含一个二进制整数值以及一个符号位和一个整数比例因子，该比例因子用于指定该值的小数部分。 因此，在内存中，`Decimal` 数字的表示形式比浮点类型（`Single` 和 `Double`）更精确。

- **性能。** `Decimal` 数据类型是所有数值类型中最慢的。 在选择数据类型之前，应权衡精度与性能的重要性。

- **Widening。** `Decimal` 数据类型加宽到 `Single` 或 `Double`。 这意味着，你可以将 `Decimal` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。

- **尾随零。** Visual Basic 不会在 `Decimal` 文本中存储尾随零。 但是，`Decimal` 变量保留了所有计算得出的尾随零。 下面的示例对此进行了演示。

  ```vb
  Dim d1, d2, d3, d4 As Decimal
  d1 = 2.375D
  d2 = 1.625D
  d3 = d1 + d2
  d4 = 4.000D
  Console.WriteLine("d1 = " & CStr(d1) & ", d2 = " & CStr(d2) &
        ", d3 = " & CStr(d3) & ", d4 = " & CStr(d4))
  ' d1 = 2.375, d2 = 1.625, d3 = 4.000, d4 = 4
  ```

- **类型字符。** 将文本类型字符 `D` 追加到文本会将其强制转换为 `Decimal` 数据类型。 将标识符类型字符 `@` 追加到任何标识符会将其强制转换为 `Decimal`。

- **Framework 类型。** .NET Framework 中的对应类型是 [System.Decimal](https://learn.microsoft.com/zh-cn/dotnet/api/system.decimal) 结构。

### 范围

你可能需要使用 `D` 类型字符将较大的值分配给 `Decimal` 变量或常数。 此要求是因为编译器会将文本解释为 `Long`，除非文本类型字符跟在文本后，如下面的示例所示。

```vb
Dim bigDec1 As Decimal = 9223372036854775807   ' No overflow.
Dim bigDec2 As Decimal = 9223372036854775808   ' Overflow.
Dim bigDec3 As Decimal = 9223372036854775808D  ' No overflow.
```

`bigDec1` 的声明不会产生溢出，因为赋给它的值落在范围 `Long` 内。 将 `Long` 值分配给 `Decimal` 变量。

`bigDec2` 的声明会生成溢出错误，因为赋给它的值对于 `Long` 太大。 由于不能首先将数字文本解释为 `Long` ，因此不能将其分配给 `Decimal` 变量。

对于 `bigDec3` ，文本类型字符 `D` 通过强制编译器将文本解释为 `Decimal` 而不是 `Long`，来解决此问题。