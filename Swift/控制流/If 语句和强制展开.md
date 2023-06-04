您可以使用 `if` 语句通过将可选值与 `nil` 进行比较来确定可选值是否包含值。您使用“等于”运算符 ( `==` ) 或“不等于”运算符 ( `!=` ) 执行此比较。

如果一个可选项有一个值，它被认为是“不等于” `nil`：

```swift
if convertedNumber != nil {
    print("convertedNumber contains some integer value.")
}
// Prints "convertedNumber contains some integer value."
```

一旦您确定可选项确实*包含*一个值，您就可以通过在可选项名称的末尾添加感叹号 (  `!` ) 来访问其基础值。感叹号实际上是在说，“我知道这个可选的肯定有一个值；请使用它。这被称为可选值的*强制展开：*

```swift
if convertedNumber != nil {
    print("convertedNumber has an integer value of \(convertedNumber!).")
}
// Prints "convertedNumber has an integer value of 123."
```

有关该`if`语句的更多信息，请参阅[控制流](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow)。

>   注意：
>
>   尝试使用 `!` 访问不存在的可选值会触发运行时错误。`nil` 在使用 `!` 强制展开其值之前，始终确保可选包含非值。

