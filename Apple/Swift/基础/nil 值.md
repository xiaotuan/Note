您可以通过为其分配特殊值 `nil` 来将可选变量设置为无值状态：

```swift
var serverResponseCode: Int? = 404
// serverResponseCode contains an actual Int value of 404
serverResponseCode = nil
// serverResponseCode now contains no value
```

>   提示：
>
>   你不能将 `nil` 值赋给非可选常量或变量。如果你的代码中的常量或变量需要再特定条件下处理没有值的情况，请始终将其声明为适当类型的可选值。

如果您定义一个可选变量而不提供默认值，该变量会自动为您设置为 `nil`：

```swift
var surveyAnswer: String?
// surveyAnswer is automatically set to nil
```

>   提示：
>
>   Swift 与Objective-C 中 `nil` 的不同。`nil` 在 Objective-C 中，`nil` 是指向不存在对象的指针。在 Swift 中，`nil` 不是指针——它是某种类型的值的缺失。*任何*类型的可选值都可以设置为 `nil`，而不仅仅是对象类型。