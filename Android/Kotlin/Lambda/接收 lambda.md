现在让我们看看如何创建一个接收 `lambda` 的函数。这个函数把一个 `Int` 和一个 `lambda` 作为参数。它遍历从 1 到给定数字的值，并使用范围内的每个值来调用给定的 `lambda` 表达式。

```kotlin
fun walk1To(action: (Int) -> Unit, n: Int) = (1..n).forEach{ action(it) }
```

让我们通过传递两个参数来调用这个函数：一个 `lambda` 表达式和一个 `Int`：

```kotlin
fun walk1To(action: (Int) -> Unit, n: Int) = (1..n).forEach{ action(it) }

fun main() {
	walk1To({i -> print(i) }, 5)	// 12345
}
```

