[toc]

### 语法

```vb
#If expression Then
   statements
[ #ElseIf expression Then
   [ statements ]
...
#ElseIf expression Then
   [ statements ] ]
[ #Else
   [ statements ] ]
#End If
```

### 组成部分

+ `expression`：对于 `#If` 和 `#ElseIf` 语句是必需的，在其他位置为可选。 任何表达式（仅由一个或多个条件编译器常量、文本和运算符组成），其计算结果为 `True` 或 `False`。

+ `statements`：`#If` 语句块必需，在其他位置为可选。 如果关联的表达式的计算结果为 `True`，则 Visual Basic 编译的程序行或编译器指令。

+ `#End If`：终止 `#If` 语句块。

### 注解

在表面上，`#If...Then...#Else` 指令的行为将与 `If...Then...Else` 语句的行为相同。 但是，`#If...Then...#Else` 指令将计算编译器编译的内容，而 `If...Then...Else` 语句则计算运行时的条件。

条件编译通常用于针对不同平台编译相同的程序。 它还用于阻止调试代码出现在可执行文件中。 在条件编译期间排除的代码在最终可执行文件中被完全省略，因此它不会对大小或性能产生任何影响。

不管任何计算结果如何，都将使用 `Option Compare Binary` 计算所有表达式。 `Option Compare` 语句不影响 `#If` 和 `#ElseIf` 语句中的表达式。

> 备注
>
> 不存在 `#If`、`#Else`、`#ElseIf` 和 `#End If` 指令的单行形式。 任何其他代码都不能与任何指令出现在同一行上。

条件编译块内的语句必须是完整的逻辑语句。 例如，无法有条件地仅编译函数的属性，但可以有条件地声明函数及其属性：

```vb
#If DEBUG Then
<WebMethod()>
Public Function SomeFunction() As String
#Else
<WebMethod(CacheDuration:=86400)>
Public Function SomeFunction() As String
#End If
```

### 示例

此示例使用 `#If...Then...#Else` 构造来确定是否编译某些语句。

```vb
#Const CustomerNumber = 36
#If CustomerNumber = 35 Then
        ' Insert code to be compiled for customer # 35.
#ElseIf CustomerNumber = 36 Then
        ' Insert code to be compiled for customer # 36.
#Else
        ' Insert code to be compiled for all other customers.
#End If
```

