让我们用函数式风格实现一个函数，来判断给定的数字是否是质数：

```kotlin
fun isPrime(n: Int) = n > 1 && (2 until n).none({ i: Int -> n % i == 0})
```

代码段 `2 until n` 返回 `IntRange` 类的一个实例。这个类有两个 `none()` 的重载版本，其中一个是接受 `lambda` 作为参数的高阶2函数。如果 `lambda` 对范围内的任何一个值都返回 `true`，那么 `none()` 返回 `false`，否则，返回 `true`。`none()` 函数会短路求值——也就是说，只要对 `lambda` 的调用返回 `true`，就不会再计算其他元素，`none()` 将立即返回 `false`。

传递给 `none()` 的 `lambda` 参数列表指定了参数的类型：`i: Int`。`Kotlin` 并不坚持使用 `lambda` 参数的类型。它可以根据 `lambda` 传递给函数的参数来推断它们的类型。因此，我们可以从 `lambda` 的参数列表中去掉类型：

```kotlin
fun isPrime(n: Int) = n > 1 && (2 until n).none({ i -> n % i == 0})
```

由于我们使用的 `none()` 版本只2接受一个参数，所以可以在调用中去掉圆括号 `()`：

```kotlin
fun isPrime(n: Int) = n > 1 && (2 until n).none { i -> n % i == 0}
```

如果可能的话，可以省略类型和 `()`。