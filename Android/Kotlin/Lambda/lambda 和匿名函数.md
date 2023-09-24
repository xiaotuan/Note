`lambda` 通常作为参数传递给函数，但是如果在多个调用中需要相同的 `lambda`，这可能会导致代码重复。我们可以通过几种方式来避免这种情况。一种方法是将 `lambada` 存储到变量中以便重用。或者可以创建匿名函数而不是 `lambda`。

当 `lambda` 作为参数传递给函数时，`Kotlin` 可以推断出参数的类型。但是如果定义一个变量来存储 `lambda`，`Kotlin` 没有任何关于类型的上下文。因此，在这种情况下，我们需要提供足够的类型信息。

让我们创建一个变量来存储 `lambda`：

```kotlin
val checkLength5 = { input: String -> input.length == 5 }

fun main() {
	val names = listOf("Pam", "Pat", "Paul", "Paula")
	println(names.find(checkLength5))	// Paula
}
```

在本例中，我们指定了 `lambda` 参数的类型，`Kotlin` 将变量的类型推断为 `(String) -> Boolean`。或者，。可以让 `Kotlin` 从相反的方向进行推断，可以指定变量的类型，并要求它推断出 `lambda` 参数的类型：

```kotlin
val checkLength5: (String) -> Boolean = { name -> name.length == 5 }
```

另一个不受欢迎的选择是，人们可能会试图同时指定变量的类型和 `lambda` 参数的类型，例如：

```kotlin
val checkLength5: (String) -> Boolean = { name: String -> name.length == 5 }
```

如果你想要传递和强制 `lambda` 的返回类型，请指定变量的类型。如果希望推断返回类型，那么请指定 `lambda` 参数的类型。

如果将变量的类型定义为 `lambda` 所赋值的类型，则应该指定返回类型。如果只指定 `lambda` 参数的类型，则会推断返回类型。在推断变量类型时指定返回类型的另一个选项是匿名函数。

匿名函数的编写方式与常规函数类似，因此指定返回类型的规则——对于块体没有类型推断，需要 `return` 等——都使用，但有一个区别：函数没有名称：

```kotlin
val checkLength5 = fun(name: String): Boolean { return name.length == 5 }
```

与将匿名函数存储在变量中不同，你可以在函数调用中直接使用它作为参数，来代替 `lambda`：

```kotlin
names.find(fun(name: String): Boolean { return name.length == 5 })
```

当使用匿名函数而不是 `lambda` 时，会应用一些限制。对于返回值的块体匿名函数，`return` 关键字是必需的。返回总是从匿名函数返回，而不是从包含函数返回。另外，如果 `lambda` 参数位于末尾位置，那么你可以将 `lambda` 传递到 `()` 之外。但是，匿名函数需要在 `()` 内。简而言之，以下情况是不允许的：
```kotlin
names.find { fun(name: String) : Boolean { return name.length == 5 }}	// ERROR
```

在可能的情况下，最好选择 `lambda` 而不是匿名函数，而且只在适合使用匿名函数而不是 `lambda` 的罕见情况下才有选择地使用匿名函数。