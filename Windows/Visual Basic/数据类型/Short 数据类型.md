[toc]

`Short` 数据类型保存 16 位（2 字节）带符号整数，值的范围为 -32,768 到 32,767。

### 注解

使用 `Short` 数据类型可包含不需要 `Integer` 的完整数据宽度的整数值。 在某些情况下，公共语言运行时可以将 `Short` 变量紧密地打包在一起，并节省内存消耗。

`Short` 的默认值为 0。

### 文本赋值

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `Short` 变量。 如果整数文本在 `Short` 范围之外（即，如果它小于 [Int16.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.int16.minvalue) 或大于 [Int16.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.int16.maxvalue)），会发生编译错误。

在以下示例中，表示为十进制、十六进制和二进制文本的等于 1,034 的整数从[整数](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/data-types/integer-data-type)隐式转换为 `Short` 值。

```vb
Dim shortValue1 As Short = 1034
Console.WriteLine(shortValue1)

Dim shortValue2 As Short = &H040A
Console.WriteLine(shortValue2)

Dim shortValue3 As Short = &B0100_00001010
Console.WriteLine(shortValue3)
' The example displays the following output:
'          1034
'          1034
'          1034
```

> 备注
>
> 使用前缀 `&h` 或 `&H` 表示十六进制文本，使用前缀 `&b` 或 `&B` 表示二进制文本，使用前缀 `&o` 或 `&O` 表示八进制文本。 十进制文本没有前缀。

从 Visual Basic 2017 开始，还可以使用下划线字符 `_` 作为数字分隔符，以增强可读性，如下例所示。

```vb
Dim shortValue1 As Short = 1_034
Console.WriteLine(shortValue1)

Dim shortValue3 As Short = &B00000100_00001010
Console.WriteLine(shortValue3)
' The example displays the following output:
'          1034
'          1034
```

从 Visual Basic 15.5 开始，还可以使用下划线字符 (`_`) 作为前缀与十六进制、二进制或八进制数字之间的前导分隔符。 例如：

```vb
Dim number As Short = &H_3264
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```vb
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

有关详细信息，请参阅[选择 Visual Basic 语言版本](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/configure-language-version)。

数字文本还可以包括`S`[类型字符](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/type-characters)来表示 `Short` 数据类型，如以下示例所示。

```vb
Dim number = &H_3264S
```

### 编程提示

- **Widening。** `Short` 数据类型加宽到 `Integer`、`Long`、`Decimal`、`Single` 或 `Double`。 这意味着，你可以将 `Short` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **类型字符。** 将文本类型字符 `S` 追加到文本会将其强制转换为 `Short` 数据类型。 `Short` 不具有标识符类型字符。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.Int16](https://learn.microsoft.com/zh-cn/dotnet/api/system.int16) 结构。