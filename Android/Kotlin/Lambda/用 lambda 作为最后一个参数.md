一个函数接受一个以上的 `lambda` 参数并不少见。在调用中，我们用逗号把类型为 `lambda` 的第一个参数与第二个参数分开。这两个参数都在 `()` 中。使用了 `{}`、逗号和 `()`，该调用有点乱。

`kotlin` 改变了 `lambda` 在末尾位置的规则。因此，在设计至少有一个 `lambda` 参数的函数时，将 `lambda` 参数能放在末尾的位置。

```kotlin
fun walk1To(n: Int, action: (Int) -> Unit) = (1..n).forEach{ action(it) }
```

上面的代码仍然可以把 `lambda` 放在括号内，但是是作为第二个参数，如下所示：

```kotlin
walk1To(5, {i -> print(i) })
```

也可以把 `lambda` 放在括号外面：

```kotlin
walk1To(5) { i -> print(i) }
```

我们也可以编写多行的 `lambda`：

```kotlin
walk1To(5) { i -> 
	print(i)
}
```

也可在这里选择使用隐式 `it` 而不是 `i` 来进一步减少混乱：

```kotlin
walk1To(5) { print(it) }
```

