[toc]

`Integer` 数据类型保存 32 位（4 字节）带符号整数，值的范围为 -2,147,483,648 到 2,147,483,647。

### 注解

`Integer` 数据类型为 32 位处理器提供了优化性能。 其他整数类型在内存中的加载和存储的速度都要稍慢一些。

`Integer` 的默认值为 0。

### 文本赋值

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `Integer` 变量。 如果整数文本在 `Integer` 范围之外（即，如果它小于 [Int32.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.int32.minvalue) 或大于 [Int32.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.int32.maxvalue)），会发生编译错误。

在以下示例中，表示为十进制、十六进制和二进制文本且等于 90,946 的整数被分配给 `Integer` 值。

```vb
Dim intValue1 As Integer = 90946
Console.WriteLine(intValue1)
Dim intValue2 As Integer = &H16342
Console.WriteLine(intValue2)

Dim intValue3 As Integer = &B0001_0110_0011_0100_0010
Console.WriteLine(intValue3)
' The example displays the following output:
'          90946
'          90946
'          90946
```

> 备注
>
> 使用前缀 `&h` 或 `&H` 表示十六进制文本，使用前缀 `&b` 或 `&B` 表示二进制文本，使用前缀 `&o` 或 `&O` 表示八进制文本。 十进制文本没有前缀。

从 Visual Basic 2017 开始，还可以使用下划线字符 `_` 作为数字分隔符，以增强可读性，如下例所示。

```vb
Dim intValue1 As Integer = 90_946
Console.WriteLine(intValue1)

Dim intValue2 As Integer = &H0001_6342
Console.WriteLine(intValue2)

Dim intValue3 As Integer = &B0001_0110_0011_0100_0010
Console.WriteLine(intValue3)
' The example displays the following output:
'          90946
'          90946
'          90946
```

从 Visual Basic 15.5 开始，还可以使用下划线字符 (`_`) 作为前缀与十六进制、二进制或八进制数字之间的前导分隔符。 例如：

```vb
Dim number As Integer = &H_C305_F860
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```config
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

有关详细信息，请参阅[选择 Visual Basic 语言版本](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/language-reference/configure-language-version)。

数字文本还可以包括`I`[类型字符](https://learn.microsoft.com/zh-cn/dotnet/visual-basic/programming-guide/language-features/data-types/type-characters)来表示 `Integer` 数据类型，如以下示例所示。

```vb
Dim number = &H_035826I
```

### 编程提示

- **互操作注意事项。** 如果与不是为 .NET Framework 编写的组件（如自动化或 COM 对象）交互，请记住，`Integer` 在其他环境中具有不同的数据宽度（16 位）。 如果将一个 16 位自变量传递给此类组件，请在新的 Visual Basic 代码中将其声明为 `Short` 而不是 `Integer`。
- **Widening。** `Integer` 数据类型加宽到 `Long`、`Decimal`、`Single` 或 `Double`。 这意味着，你可以将 `Integer` 转换为这些类型中的任意类型，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。
- **类型字符。** 将文本类型字符 `I` 追加到文本会将其强制转换为 `Integer` 数据类型。 将标识符类型字符 `%` 追加到任何标识符会将其强制转换为 `Integer`。
- **Framework 类型。** .NET Framework 中的对应类型是 [System.Int32](https://learn.microsoft.com/zh-cn/dotnet/api/system.int32) 结构。

### 范围

如果尝试将整型变量设置为其类型范围以外的数字，则将出错。 如果尝试将其设置为小数，则数字将向上或向下舍入为最接近的整数值。 如果数字同样接近两个整数值，则值将舍入为最接近的偶数整数。 这种做法可将因单方向持续舍入中点值而导致的舍入误差降到最低。 下面的代码演示了舍入的示例。

```vb
' The valid range of an Integer variable is -2147483648 through +2147483647.  
Dim k As Integer  
' The following statement causes an error because the value is too large.  
k = 2147483648  
' The following statement sets k to 6.  
k = 5.9  
' The following statement sets k to 4  
k = 4.5  
' The following statement sets k to 6  
' Note, Visual Basic uses banker’s rounding (toward nearest even number)  
k = 5.5
```

