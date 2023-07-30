`Swift` 内置了检查 `API` 可用性的支持，这可确保你不会意外使用在给定部署目标上不可用的 `API`。

你可以在 `if` 或 `guard` 语句中使用可用性条件来有条件地执行代码块，具体取决于你要使用的 `API` 在运行时是否可用。

```swift
if #available(iOS 10, macOS 10.12, *) {
    // Use iOS 10 APIs on iOS, and use macOS 10.12 APIs on macOS
} else {
    // Fall back to earlier iOS and macOS APIs
}
```

上面的可用性条件指定 `if` 语句主体仅在 `iOS 10` 及更高版本中执行；在 `macOS` 中，仅在 `macOS 10.12` 及更高版本中。最后一个参数 `*` 是必需的，它指定在任何其他平台上，`if` 主体在你的目标制定的最小部署目标上执行。

在其一般形式中，可用性条件采用平台名称和版本的列表。你可以使用平台名称，例如 `iOS`、`macOS`、`watchOs` 和 `tvOS`——有关完整列表，请参阅[声明属性](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#Declaration-Attributes)。除了指定主要版本号（如 `iOS 8` 或 `macOS 10.10` ）之外，你还可以指定次要版本号（如 `iOS 11.2.6` 和 `macOS 10.13.3`）。

```swift
if #available(<#platform name#> <#version#>, <#...#>, *) {
    <#statements to execute if the APIs are available#>
} else {
    <#fallback statements to execute if the APIs are unavailable#>
}
```

当你在 `guard` 语句中使用可用性条件时，它会细化用于该代码块中其余的可用性信息。

```swift
@available(macOS 10.12, *)
struct ColorPreference {
    var bestColor = "blue"
}


func chooseBestColor() -> String {
    guard #available(macOS 10.12, *) else {
       return "gray"
    }
    let colors = ColorPreference()
    return colors.bestColor
}
```

除了 `#available` 之外，`Swift` 还支持使用 `unavailable` 进行相反的检查。例如：

```swift
if #available(iOS 10, *) {
} else {
    // Fallback code
}


if #unavailable(iOS 10) {
    // Fallback code
}
```

