[toc]

`UShort` 数据类型保存 16 位（2 字节）无符号整数，值的范围为 0 到 65,535。

### 注解

使用 `UShort` 数据类型来包含对于 `Byte` 来说太大的二进制数据。

`UShort` 的默认值为 0。

### 文本赋值

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `UShort` 变量。 如果整数文本在 `UShort` 范围之外（即，如果它小于 [UInt16.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint16.minvalue) 或大于 [UInt16.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint16.maxvalue)），会发生编译错误。

在以下示例中，表示为十进制、十六进制和二进制文本且等于 65,034 的整数被分配给 `UShort` 值。

```vb
Dim ushortValue1 As UShort = 65034
Console.WriteLine(ushortValue1)

Dim ushortValue2 As UShort = &HFE0A
Console.WriteLine(ushortValue2)

Dim ushortValue3 As UShort = &B1111_1110_0000_1010
Console.WriteLine(ushortValue3)
' The example displays the following output:
'          65034
'          65034
'          65034
```

> 备注
>
> 使用前缀 `&h` 或 `&H` 表示十六进制文本，使用前缀 `&b` 或 `&B` 表示二进制文本，使用前缀 `&o` 或 `&O` 表示八进制文本。 十进制文本没有前缀。

从 Visual Basic 2017 开始，还可以使用下划线字符 `_` 作为数字分隔符，以增强可读性，如下例所示。

```vb
Dim ushortValue1 As UShort = 65_034
Console.WriteLine(ushortValue1)

Dim ushortValue3 As UShort = &B11111110_00001010
Console.WriteLine(ushortValue3)
' The example displays the following output:
'          65034
'          65034
```

从 Visual Basic 15.5 开始，还可以使用下划线字符 (`_`) 作为前缀与十六进制、二进制或八进制数字之间的前导分隔符。 例如：

```vb
Dim number As UShort = &H_FF8C
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```xml
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

有关详细信息，请参阅[选择 Visual Basic 语言版本](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/configure-language-version)。

数字文本还可以包括 `US` 或 `us`[类型字符](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/type-characters)来表示 `UShort` 数据类型，如以下示例所示。

```vb
Dim number = &H_5826us
```

### 编程提示

- **负数。** 由于 `UShort` 是无符号类型，因此它不能表示负数。 如果对计算结果为类型 `UShort` 的表达式使用一元减号 (`-`) 运算符，Visual Basic 会将表达式首先转换为 `Integer`。
- **符合 CLS。** `UShort` 数据类型不是[公共语言规范](https://www.ecma-international.org/publications-and-standards/standards/ecma-335/) (CLS) 的一部分，因此符合 CLS 的代码不能使用使用它的组件。
- **Widening。** `UShort` 数据类型加宽到 `Integer`、`UInteger`、`Long`、`ULong`、`Decimal`、`Single` 和 `Double`。 这意味着，可以将 `UShort` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **类型字符。** 将文本类型字符 `US` 追加到文本会将其强制转换为 `UShort` 数据类型。 `UShort` 不具有标识符类型字符。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.UInt16](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint16) 结构。