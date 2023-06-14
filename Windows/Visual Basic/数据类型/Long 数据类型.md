[toc]

`Long` 数据类型保存 64 位（8 字节）无符号整数，值的范围为 -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 (9.2...E+18)。

### 注解

使用 `Long` 数据类型可包含太大而不符合 `Integer` 数据类型的整数。

`Long` 的默认值为 0。

### 文本赋值

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `Long` 变量。 如果整数文本在 `Long` 范围之外（即，如果它小于 [Int64.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.int64.minvalue) 或大于 [Int64.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.int64.maxvalue)），会发生编译错误。

在以下示例中，表示为十进制、十六进制和二进制文本的等于 4,294,967,296 的整数被分配给 `Long` 值。

```vb
Dim longValue1 As Long = 4294967296
Console.WriteLine(longValue1)

Dim longValue2 As Long = &H100000000
Console.WriteLine(longValue2)

Dim longValue3 As Long = &B1_0000_0000_0000_0000_0000_0000_0000_0000
Console.WriteLine(longValue3)
' The example displays the following output:
'          4294967296
'          4294967296
'          4294967296
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
Dim number As Long = &H_0FAC_0326_1489_D68C
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```xml
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

有关详细信息，请参阅[选择 Visual Basic 语言版本](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/configure-language-version)。

数字文本还可以包括`L`[类型字符](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/type-characters)来表示 `Long` 数据类型，如以下示例所示。

```vb
Dim number = &H_0FAC_0326_1489_D68CL
```

### 编程提示

- **互操作注意事项。** 如果你与并非为 .NET Framework 编写的组件（如自动化或 COM 对象）交互，请记住，`Long` 在其他环境中具有不同的数据宽度（32 位）。 如果将一个 32 位参数传递给此类组件，请在新的 Visual Basic 代码中将其声明为 `Integer` 而不是 `Long`。
- **Widening。** `Long` 数据类型加宽到 `Decimal`、`Single` 或 `Double`。 这意味着，你可以将 `Long` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **类型字符。** 将文本类型字符 `L` 追加到文本会将其强制转换为 `Long` 数据类型。 将标识符类型字符 `&` 追加到任何标识符会将其强制转换为 `Long`。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.Int64](https://learn.microsoft.com/zh-cn/dotnet/api/system.int64) 结构。