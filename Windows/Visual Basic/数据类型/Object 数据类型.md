[toc]

`Object` 数据类型保存引用对象的地址。 可以将任何引用类型（字符串、数组、类或接口）分配到 `Object` 变量。 `Object` 变量还可以引用任意值类型的数据，（数值、`Boolean` 、`Char` 、`Date` 、结构或枚举）。

### 注解

`Object` 数据类型可以指向任何数据类型的数据，包括应用程序识别的任何对象实例。 在编译时不知道变量可能指向的数据类型时，请使用 `Object`。

`Object` 的默认值为 `Nothing`（空引用）。

### 数据类型

可以将任何数据类型的变量、常量或表达式分配给 `Object` 变量。 若要确定 `Object` 变量当前引用的数据类型，可以使用 [System.Type](https://learn.microsoft.com/zh-cn/dotnet/api/system.type) 类的 [GetTypeCode](https://learn.microsoft.com/zh-cn/dotnet/api/system.type.gettypecode) 方法。 下面的示例对此进行了演示。

```vb
Dim myObject As Object = "skdfj"
' Suppose myObject has now had something assigned to it.
Dim datTyp As TypeCode
datTyp = Type.GetTypeCode(myObject.GetType())
Console.WriteLine($"Type is {datTyp}")
' Type is String
```

`Object` 数据类型也是引用类型。 但是，当变量引用值类型的数据时，Visual Basic 将 `Object` 变量视为值类型。

### 存储

无论它引用哪种数据类型， `Object` 变量都不包含数据值本身，而是指向值的指针。 它在计算机内存中始终使用四个字节，但这不包括表示变量值的数据的存储。 由于使用指针查找数据的代码，保存值类型的 `Object` 变量比显式类型化变量略慢。

### 编程提示

- **互操作注意事项。** 如果你与不是为 .NET Framework 编写的组件（如自动化或 COM 对象）交互，请记住，其他环境中的指针类型与 Visual Basic `Object` 类型不兼容。

- **性能。** 用 `Object` 类型声明的变量的灵活性足以包含对任何对象的引用。 但是，在此类变量上调用方法或属性时，始终会（在运行时）引发 *后期绑定*。 若要（在编译时）强制进行 *早期绑定* 并获得更好的性能，请使用特定类名声明变量，或将其转换为特定的数据类型。

  声明对象变量时，请尝试使用特定类类型，例如 [OperatingSystem](https://learn.microsoft.com/zh-cn/dotnet/api/system.operatingsystem)，而不是通用 `Object` 类型。 还应使用最具体的类，如 [TextBox](https://learn.microsoft.com/zh-cn/dotnet/api/system.windows.forms.textbox) 而不是 [Control](https://learn.microsoft.com/zh-cn/dotnet/api/system.windows.forms.control)，以便您可以访问其属性和方法。 通常可以使用 **对象浏览器** 中的 **类** 列表来查找可用的类名。

- **Widening。** 所有数据类型和所有引用类型都扩大到 `Object` 数据类型。 这意味着，可以将任意类型转换为 `Object`，而不会遇到 [System.OverflowException](https://learn.microsoft.com/zh-cn/dotnet/api/system.overflowexception) 错误。

  但是，如果在值类型和 `Object` 之间进行转换，Visual Basic 将执行称为 *装箱* 和 *取消装箱* 的操作，这会使执行速度变慢。

- **类型字符。** `Object` 没有文本类型字符或标识符类型字符。

- **Framework 类型。** .NET Framework 中的对应类型是 [System.Object](https://learn.microsoft.com/zh-cn/dotnet/api/system.object) 类。

### 示例

下面的示例演示指向对象实例的 `Object` 变量。

```vb
Dim objDb As Object
Dim myCollection As New Collection()
myCollection.Add(#05/06/2023#)
' Suppose myCollection has now been populated.
objDb = myCollection.Item(1)
Console.WriteLine($"Type is {objDb.GetType()}")
' Type is System.DateTime
```

