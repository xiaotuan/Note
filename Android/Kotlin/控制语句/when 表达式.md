`when` 表达式定义具有多个分支的表达式。它类似于 `C` 语言中的 `switch` 语句。它的基本形式如下：

```kotlin
when (obj) {
    1		   -> "One"
    "Hello"    -> "Greeting"
    is Long	   -> "Long"
    !is String -> "Not a string"
    else	   -> "Unknown"
```

`when` 语句依次将其参数与所有分支匹配，直到满足某个分支条件。

`when` 既可以用作表达式，也可以用作语句。如果用作表达式，则第一个匹配分支的值将成为整个表达式的值。如果它用作语句，则忽略各个分支的值。如果其他分支条件都不满足，则 `else` 分支的值将成为整个表达式的值。

如果 `when` 用作表达式，则 `else` 分支是强制性的，除非编译器可以证明所有可能的情况都包含分支条件，例如 `enum` 类条目和 `sealed` 类子类型）。

```kotlin
enum class Bit {
    ZERO, ONE
}

val numericValue = when (getRandomBit()) {
    Bit.ZERO -> 0
    Bit.ONE -> 1
    // 'else' is not required because all cases are covered
}

enum class Color {
    RED, GREEN, BLUE
}

when (getColor()) {
    Color.RED -> println("red")
    Color.GREEN -> println("green")
    Color.BLUE -> println("blue")
    // 'else' is not required because all cases are covered
}

when (getColor()) {
    Color.RED -> println("red") // no branches for GREEN and BLUE
    else -> println("not red") // 'else' is required
}
```

要为多种情况定义共同行为，请将它们的条件用逗号组合在一行中：

```kotlin
when (x) {
    0, 1 -> print("x == 0 or x == 1")
    else -> print("otherwise")
}
```

您可以使用任意表达式（不仅是常量）作为分支条件

```kotlin
when (x) {
    s.toInt() -> print("s encodes x")
    else -> print("s does not encode x")
}
```

您还可以检查存在的值 `in` 或 `!in` 范围或集合：

```kotlin
when (x) {
    in 1..10 -> print("x is in the range")
    in validNumbers -> print("x is valid")
    !in 10..20 -> print("x is outside the range")
    else -> print("none of the above")
}
```

另一种选择是检查值 `is` 或 `!is` 特定类型。请注意，由于[智能转换](https://kotlinlang.org/docs/typecasts.html#smart-casts)，您无需任何额外检查即可访问该类型的方法和属性。

```kotlin
fun hasPrefix(x: Any) = when(x) {
    is String -> x.startsWith("prefix")
    else -> false
}
```

`when` 也可以用作链条的替代 `if-else if`。如果没有提供参数，分支条件只是布尔表达式，当条件为真时执行分支：

```kotlin
when {
    x.isOdd() -> print("x is odd")
    y.isEven() -> print("y is even")
    else -> print("x+y is odd")
}
```

你可以使用下面语法捕获 `when` 主体：

```kotlin
fun Request.getBody() =
	when (val response = executeRequest()) {
        is Success -> response.body
        is HttpError -> throw HttpException(response.status)
    }
```

`when` 主体中引用的变量的作用域被限制在 `when` 主体中。
