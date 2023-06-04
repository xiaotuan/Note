`nil` 合并运算符（ `a ?? b` ）解包一个可选的 `a`，如果它包含一个值，则返回 `a`，否则返回 `b`。

`nil` 合并运算符是以下代码的简写：

```swift
a != nil ? a! : b
```

>   提示：
>
>   如果 `a` 的值为 `non-nil`，则不计算 `b` 的值。这被称为短路。

```swift
let defaultColorName = "red"
var userDefinedColorName: String?   // defaults to nil

var colorNameToUse = userDefinedColorName ?? defaultColorName
// userDefinedColorName is nil, so colorNameToUse is set to the default of "red"
```

