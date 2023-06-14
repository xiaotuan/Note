`Byte` 数据类型使用 8 位（1 个字节）保存，值的范围为 0 到 255.

`Byte` 的默认值为 0。

可以通过为其分配十进制文本、十六进制文本、八进制文本或（从 Visual Basic 2017 开始）二进制文本来声明和初始化 `Byte` 变量。 如果整数文本在 `Byte` 范围之外（即，如果它小于 [Byte.MinValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.byte.minvalue) 或大于 [Byte.MaxValue](https://learn.microsoft.com/zh-cn/dotnet/api/system.byte.maxvalue)），会发生编译错误。

> 提示：
>
> 使用前缀 `&h` 或 `&H` 表示十六进制文本，使用前缀 `&b` 或 `&B` 表示二进制文本，使用前缀 `&o` 或 `&O` 表示八进制文本。 十进制文本没有前缀。

```vb
Dim byteValue1 As Byte = 201
Console.WriteLine(byteValue1)

Dim byteValue2 As Byte = &H00C9
Console.WriteLine(byteValue2)

Dim byteValue3 As Byte = &B1100_1001
Console.WriteLine(byteValue3)
' The example displays the following output:
'          201
'          201
'          201
```

从 Visual Basic 2017 开始，还可以使用下划线字符 `_` 作为数字分隔符，以增强可读性，如下例所示。

```vb
Dim byteValue3 As Byte = &B1100_1001
Console.WriteLine(byteValue3)
' The example displays the following output:
'          201
```

从 Visual Basic 15.5 开始，还可以使用下划线字符 (`_`) 作为前缀与十六进制、二进制或八进制数字之间的前导分隔符。 例如：

```vb
Dim number As Byte = &H_6A
```

若要使用下划线字符作为前导分隔符，必须将以下元素添加到 Visual Basic 项目 (*.vbproj) 文件中：

```swift
<PropertyGroup>
  <LangVersion>15.5</LangVersion>
</PropertyGroup>
```

**示例代码：**

以下面的示例中，`b` 是 `Byte` 变量。 语句说明变量的范围以及对其应用移位运算符的应用程序。

```vb
' The valid range of a Byte variable is 0 through 255.
Dim b As Byte
b = 30
' The following statement causes an error because the value is too large.
'b = 256
' The following statement causes an error because the value is negative.
'b = -5
' The following statement sets b to 6.
b = CByte(5.7)

' The following statements apply bit-shift operators to b.
' The initial value of b is 6.
Console.WriteLine(b)
' Bit shift to the right divides the number in half. In this 
' example, binary 110 becomes 11.
b >>= 1
' The following statement displays 3.
Console.WriteLine(b)
' Now shift back to the original position, and then one more bit
' to the left. Each shift to the left doubles the value. In this
' example, binary 11 becomes 1100.
b <<= 2
' The following statement displays 12.
Console.WriteLine(b)
```

