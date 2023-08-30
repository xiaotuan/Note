[toc]

像 `equals()` 和 `toString()` 这样的方法非常普遍。在 `Java` 中，你可以在对象基类中找到它们。在 `Kotlin` 中，这些方法包含在 `Any` 类中，还有许多对任何类的实例有用的其他方法。`Any` 是 `Kotlin` 中对应的 `Java` 对象类，但是 `Any` 有许多通过扩展函数引入的特殊方法。`Kotlin` 还有一个名为 `Nothing` 的类，当一个函数在字面上没有返回任何内容时，这个类可以作为类型来使用。`Java` 中的任何东西都不等同于 `Kotlin` 的 `Nothing`。

### 1. Any 是基类

`Kotlin` 中的所有类都继承自 `Any`，`Any` 映射到 `Java` 中的对象。如果一个函数将接受不同类型的对象作为参数，那么你可以将其类型指定位 `Any`。同样，如果不能指定要返回的特定类型，则可以返回 `Any`。

`Any` 的目的不是让我们将变量、参数或返回类型定位为 `Any`，而是提供了一些通用方法，这些方法可用于所有 `Kotlin` 类型。例如，像 `equals()`、`hashCode()` 和 `toString()` 这样的方法。

即使字节码中的 `Any` 映射到 `Java` 中的对象，它们也不完全相同。此外，`Any` 通过扩展函数提供了一些特殊的方法。例如，`to()` 扩展函数就是一个很好的例子。

同样，在对象的上下文中执行代码块可以删除大量冗长和重复的代码。为了方便实现这一点，`Any` 具有诸如 `let()`、`run()`、`apply()` 和 `also()` 等扩展函数。

### 2. Nothing 比 void 更深入

在 `Java` 等语言中，我们使用 `void` 表示方法不返回任何东西。但是在 `Kotlin` 中，使用 `Unit` 来高数我们什么时候函数没有返回任何有用的东西。但是也有一些情况，一个函数实际上什么也没有返回，这就是 `Nothing` 类出现的地方。`Nothing` 类没有实例，它表示一个永远不存在的值或 结果。当用作方法的返回类型时，这意味着函数永远不会返回——函数调用只会导致异常。

`Nothing` 的一个独特能力是它可以代表任何东西——也就是说，`Nothing` 可以替代任何类，包括 `Int`、`Double`、`String` 等。例如，看看下面的代码：

```kotlin
fun computeSqrt(n: Double): Double {
	if (n >= 0) {
		return Math.sqrt(n)
	} else {
		throw RuntimeException("No negative please")
	}
}
```

`if` 部分返回一个 `Double`，而 `else` 部分抛出一个异常。异常部分由类型 `Nothing` 表示。因此，`Nothing` 的唯一目的是能够帮助编译器验证程序中类型的完整性是健全的。