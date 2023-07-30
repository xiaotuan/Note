最简单的 `if` 语句只有一个 `if` 条件，仅当条件为 `true` 时，它才执行一组语句：

```swift
var temperatureInFahrenheit = 30
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
}
// Prints "It's very cold. Consider wearing a scarf."
```

对于条件为 `false` 的情况，`if` 可以提供一组替代语句，称为 `else` 子句。例如：

```swift
temperatureInFahrenheit = 40
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
} else {
    print("It's not that cold. Wear a T-shirt.")
}
// Prints "It's not that cold. Wear a T-shirt."
```

你可以将多个 `if` 语句链接在一起：

```swift
temperatureInFahrenheit = 90
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
} else if temperatureInFahrenheit >= 86 {
    print("It's really warm. Don't forget to wear sunscreen.")
} else {
    print("It's not that cold. Wear a T-shirt.")
}
// Prints "It's really warm. Don't forget to wear sunscreen."
```

>   提示：最后一个 `else` 子句是可选的，如果不需要完整的条件集，则可以将其排除：
>
>   ```swift
>   temperatureInFahrenheit = 72
>   if temperatureInFahrenheit <= 32 {
>       print("It's very cold. Consider wearing a scarf.")
>   } else if temperatureInFahrenheit >= 86 {
>       print("It's really warm. Don't forget to wear sunscreen.")
>   }
>   ```

`Swift` 提供了可以在设置值时使用 `if` 的简单写法。例如，考虑以下代码：

```swift
let temperatureInCelsius = 25
let weatherAdvice: String


if temperatureInCelsius <= 0 {
    weatherAdvice = "It's very cold. Consider wearing a scarf."
} else if temperatureInCelsius >= 30 {
    weatherAdvice = "It's really warm. Don't forget to wear sunscreen."
} else {
    weatherAdvice = "It's not that cold. Wear a T-shirt."
}


print(weatherAdvice)
// Prints "It's not that cold. Wear a T-shirt."
```

使用替代语法（称为 `if` 表达式），你可以更简洁地写成：

```swift
let weatherAdvice = if temperatureInCelsius <= 0 {
    "It's very cold. Consider wearing a scarf."
} else if temperatureInCelsius >= 30 {
    "It's really warm. Don't forget to wear sunscreen."
} else {
    "It's not that cold. Wear a T-shirt."
}


print(weatherAdvice)
// Prints "It's not that cold. Wear a T-shirt."
```

`if` 表达式的所有分支都需要包含相同类型的值。如果 `if` 表达式分支返回 `nil` ，则你需要显示指定类型：

```swift
let freezeWarning: String? = if temperatureInCelsius <= 0 {
    "It's below freezing. Watch for ice!"
} else {
    nil
}
```

也可以使用下面代码，而不是显示指定类型：

```swift
let freezeWarning = if temperatureInCelsius <= 0 {
    "It's below freezing. Watch for ice!"
} else {
    nil as String?
}
```

`if` 表示式可以通过抛出错误或调用永不返回的 `fatalError(_:file:line:)` 函数来响应意外失败：

```swift
let weatherAdvice = if temperatureInCelsius > 100 {
    throw TemperatureError.boiling
} else {
    "It's a reasonable temperature."
}
```

