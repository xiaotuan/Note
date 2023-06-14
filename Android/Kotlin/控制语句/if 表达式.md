在 `Kotlin` 中，`if` 是一个表达式：它返回一个值。因此，没有三元运算符（`condition ? then : else`），因为 `if` 表达式就可以做得很好：

```kotlin
var max = a
if (a < b) max = b

// With else
if (a > b) {
    max = a
} else {
    max = b
}

// As expression
max = if (a > b) a else b

// You can also 'else if' in expressions:
var maxLimit = 1
val maxOrLimit = if (maxLimit > a) maxLimit else if (a > b) a else b
```

`if` 表达式的分支可以是块。在这种情况下，最后一个表达式的值是块的值：

```vb
val max = if (a > b) {
    print("Choose a")
    a
} else {
    print("Choose b")
    b
}
```

> 注意：如果将 `if` 用作表达式，例如，用于返回其值或将其赋值给变量，则 `else` 分支是强制性的。
