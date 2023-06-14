[toc]

`UInteger` 数据类型保存 32 位（4 字节）无符号整数，值的范围为 0 到 4,294,967,295。

### 注解

`UInteger` 数据类型以最有效的数据宽度提供最大的无符号值。

`UInteger` 的默认值为 0。

### 文本赋值

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `UInteger` 变量。 如果整数文本在 `UInteger` 范围之外（即，如果它小于 [UInt32.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint32.minvalue) 或大于 [UInt32.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint32.maxvalue)），会发生编译错误。

在以下示例中，表示为十进制、十六进制和二进制文本且等于 3,000,000,000 的整数被分配给 `UInteger` 值。

```vb
Dim uintValue1 As UInteger = 3000000000ui
Console.WriteLine(uintValue1)

Dim uintValue2 As UInteger = &HB2D05E00ui
Console.WriteLine(uintValue2)

Dim uintValue3 As UInteger = &B1011_0010_1101_0000_0101_1110_0000_0000ui
Console.WriteLine(uintValue3)
' The example displays the following output:
'          3000000000
'          3000000000
'          3000000000
```

### 备注

使用前缀 `&h` 或 `&H` 表示十六进制文本，使用前缀 `&b` 或 `&B` 表示二进制文本，使用前缀 `&o` 或 `&O` 表示八进制文本。 十进制文本没有前缀。

从 Visual Basic 2017 开始，还可以使用下划线字符 `_` 作为数字分隔符，以增强可读性，如下例所示。

```vb
Dim uintValue1 As UInteger = 3_000_000_000ui
Console.WriteLine(uintValue1)

Dim uintValue2 As UInteger = &HB2D0_5E00ui
Console.WriteLine(uintValue2)

Dim uintValue3 As UInteger = &B1011_0010_1101_0000_0101_1110_0000_0000ui
Console.WriteLine(uintValue3)
' The example displays the following output:
'          3000000000
'          3000000000
'          3000000000
```

从 Visual Basic 15.5 开始，还可以使用下划线字符 (`_`) 作为前缀与十六进制、二进制或八进制数字之间的前导分隔符。 例如：

```vb
Dim number As UInteger = &H_0F8C_0326
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```xml
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

有关详细信息，请参阅[选择 Visual Basic 语言版本](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/configure-language-version)。

数字文本还可以包括 `UI` 或 `ui`[类型字符](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/type-characters)来表示 `UInteger` 数据类型，如以下示例所示。

```vb
Dim number = &H_0FAC_14D7ui
```

### 编程提示

`UInteger` 和 `Integer` 数据类型在 32 位处理器上提供最佳性能，因为较小的整数类型（`UShort`、`Short`、`Byte` 和 `SByte`）即使使用较少的位，也需要更多时间来加载、存储和获取。

- **负数。** 由于 `UInteger` 是无符号类型，因此它不能表示负数。 如果对计算结果为类型 `UInteger` 的表达式使用一元减号 (`-`) 运算符，Visual Basic 会将表达式首先转换为 `Long`。
- **符合 CLS。** `UInteger` 数据类型不是[公共语言规范](https://www.ecma-international.org/publications-and-standards/standards/ecma-335/) (CLS) 的一部分，因此符合 CLS 的代码不能使用使用它的组件。
- **互操作注意事项。** 如果与不是为 .NET Framework 编写的组件（如自动化或 COM 对象）交互，请记住，在其他环境中类型 `uint` 具有不同的数据宽度（16 位）。 如果将一个 16 位自变量传递给此类组件，请在托管 Visual Basic 代码中将其声明为 `UShort` 而不是 `UInteger`。
- **Widening。** `UInteger` 数据类型加宽到 `Long`、`ULong`、`Decimal`、`Single` 和 `Double`。 这意味着，可以将 `UInteger` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **类型字符。** 将文本类型字符 `UI` 追加到文本会将其强制转换为 `UInteger` 数据类型。 `UInteger` 不具有标识符类型字符。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.UInt32](https://learn.microsoft.com/zh-cn/dotnet/api/system.uint32) 结构。