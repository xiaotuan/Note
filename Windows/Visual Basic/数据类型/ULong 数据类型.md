[toc]

`ULong` 数据类型保留值范围从 0 到 18446744073709551615 的 64 位 (8 字节) 整数，超过 1.84 倍 10^19。

### 注解

使用 `ULong` 数据类型去包含对于 `UInteger` 来说太大的二进制数据，或者包含可能的最大无符号整数值。

`ULong` 的默认值为 0。

### 文本赋值

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `ULong` 变量。 如果整数文本在 `ULong` 范围之外（即，如果它小于 [UInt64.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint64.minvalue) 或大于 [UInt64.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint64.maxvalue)），会发生编译错误。

在以下示例中，表示为十进制、十六进制和二进制文本且等于 7,934,076,125 的整数被分配给 `ULong` 值。

```vb
Dim ulongValue1 As ULong = 7934076125
Console.WriteLine(ulongValue1)

Dim ulongValue2 As ULong = &H0001D8e864DD
Console.WriteLine(ulongValue2)

Dim ulongValue3 As ULong = &B0001_1101_1000_1110_1000_0110_0100_1101_1101
Console.WriteLine(ulongValue3)
' The example displays the following output:
'          7934076125
'          7934076125
'          7934076125
```

> 备注
>
> 使用前缀 `&h` 或 `&H` 表示十六进制文本，使用前缀 `&b` 或 `&B` 表示二进制文本，使用前缀 `&o` 或 `&O` 表示八进制文本。 十进制文本没有前缀。

从 Visual Basic 2017 开始，还可以使用下划线字符 `_` 作为数字分隔符，以增强可读性，如下例所示。

```vb
Dim longValue1 As Long = 4_294_967_296
Console.WriteLine(longValue1)

Dim longValue2 As Long = &H1_0000_0000
Console.WriteLine(longValue2)

Dim longValue3 As Long = &B1_0000_0000_0000_0000_0000_0000_0000_0000
Console.WriteLine(longValue3)
' The example displays the following output:
'          4294967296
'          4294967296
'          4294967296
```

从 Visual Basic 15.5 开始，还可以使用下划线字符 (`_`) 作为前缀与十六进制、二进制或八进制数字之间的前导分隔符。 例如：

```vb
Dim number As ULong = &H_F9AC_0326_1489_D68C
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```xml
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

有关详细信息，请参阅[选择 Visual Basic 语言版本](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/configure-language-version)。

数字文本还可以包括 `UL` 或 `ul`[类型字符](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/type-characters)来表示 `ULong` 数据类型，如以下示例所示。

```vb
Dim number = &H_00_00_0A_96_2F_AC_14_D7ul
```

### 编程提醒

- **负数。** 由于 `ULong` 是无符号类型，因此它不能表示负数。 如果对计算结果为类型 `ULong` 的表达式使用一元减号 (`-`) 运算符，Visual Basic 会将表达式首先转换为 `Decimal`。
- **符合 CLS。** `ULong` 数据类型不是[公共语言规范](https://www.ecma-international.org/publications-and-standards/standards/ecma-335/) (CLS) 的一部分，因此符合 CLS 的代码不能使用使用它的组件。
- **互操作注意事项。** 如果与不是为 .NET Framework 编写的组件（如自动化或 COM 对象）交互，请记住，在其他环境中类型 `ulong` 具有不同的数据宽度（32 位）。 如果将一个 32 位自变量传递给此类组件，请在托管 Visual Basic 代码中将其声明为 `UInteger` 而不是 `ULong`。
- **Widening。** `ULong` 数据类型加宽到 `Decimal`、`Single` 和 `Double`。 这意味着，可以将 `ULong` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **类型字符。** 将文本类型字符 `UL` 追加到文本会将其强制转换为 `ULong` 数据类型。 `ULong` 不具有标识符类型字符。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.UInt64](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint64) 结构。

