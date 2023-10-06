[toc]

> 提示：通过实验发现，未添加 `inline` 注释的函数，在可能的情况下，`Kotlin` 会对 `lambda` 函数进行优化。在下面的代码中，添加了 `noinline` 注释时还比未添加时调用层次还少，不清楚是怎么回事，暂时不用理会这个篇文章内容。

`Kotlin` 提供了 `inline` 关键字来消除调用开销，从而提高性能、提供非局部控制流，比如从 `forEach()` 中返回，并传递具体化的类型参数。

### 1. 默认情况下没有内联优化

要了解内联，让我们创建一个 `invokeTwo()` 函数，它接受一个 `Int` 和两个 `lambda`。它还返回一个 `lambda`：

```kotlin
fun invokeTwo(n: Int, action1: (Int) -> Unit, action2: (Int) -> Unit): (Int) -> Unit {
	println("enter invokeTwo $n")

	action1(n)
	action2(n)

	println("exit invokeTwo $n")
	return { _: Int -> println("lambda returned from invokeTwo") }
}
```

在定义了这个函数之后，让我们调用 `callInvokeTwo()`：

```kotlin
fun callInvokeTwo() {
	invokeTwo(1, { i -> report(i) }, { i -> report(i) })
}

fun main() {
	callInvokeTwo()
}
```

`report` 函数定义如下：

```kotlin
fun report(n: Int) {
	println("")
	print("called with $n, ")

	val stackTrace = RuntimeException().getStackTrace()

	println("Stack depth: ${stackTrace.size}")
	println("Partial listing of the stack:")
	stackTrace.take(3).forEach(::println)
}
```

函数报告当前执行 `report()` 时调用堆栈的层数。让我们运行代码来看看调用以及调用堆栈中的层数：

```shell
PS C:\Users\xiaotuan\Desktop> kotlinc-jvm .\KotlinTest.kt
PS C:\Users\xiaotuan\Desktop> kotlin .\KotlinTestKt.class
enter invokeTwo 1

called with 1, Stack depth: 14
Partial listing of the stack: 
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$1.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$1.invoke(KotlinTest.kt:12)

called with 1, Stack depth: 14
Partial listing of the stack:
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
exit invokeTwo 1
PS C:\Users\xiaotuan\Desktop>
```

### 2. 内联优化

你可以使用 `inline` 关键字来提高接收 `lambda` 的函数的性能。如果一个函数标记为 `inline`，那么该函数的字节吗将在调用位置置为内联，而不是调用该函数。这将消除函数调用的开销，但是字节码将会更大。内联长函数通常不是一个好注意。

尽管你可以用 `inline` 注释任何非递归函数，但是如果 `kotlin` 认为内联没有带来任何好处，它会给一个警告，例如，如果函数没有接收到任何 `lambda` 参数。

让我们使用 `inline` 来优化 `invokeTwo()` 函数：

```kotlin
inline fun invokeTwo(n: Int, action1: (Int) -> Unit, action2: (Int) -> Unit): (Int) -> Unit {
	println("enter invokeTwo $n")

	action1(n)
	action2(n)

	println("exit invokeTwo $n")
	return { _: Int -> println("lambda returned from invokeTwo") }
}
```

让我们在进行这个修改之后运行代码，并查看调用堆栈的深度：

```shell
PS C:\Users\xiaotuan\Desktop> kotlinc-jvm .\KotlinTest.kt
PS C:\Users\xiaotuan\Desktop> kotlin .\KotlinTestKt.class
enter invokeTwo 1

KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$1.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$1.invoke(KotlinTest.kt:12)

called with 1, Stack depth: 14
Partial listing of the stack:
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
exit invokeTwo 1
PS C:\Users\xiaotuan\Desktop> kotlinc-jvm .\KotlinTest.kt
PS C:\Users\xiaotuan\Desktop> kotlin .\KotlinTestKt.class
enter invokeTwo 1

called with 1, Stack depth: 14
Partial listing of the stack:
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$1.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$1.invoke(KotlinTest.kt:12)

called with 1, Stack depth: 14
Partial listing of the stack:
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
exit invokeTwo 1
PS C:\Users\xiaotuan\Desktop> 
```

可以看到它与未未添加 `inline` 注释的输出结果是一样的，因此可以说明最新版的 `Kotlin` 会自动对可能优化的 `lambda` 进行内联优化。

### 3. 对参数精心选择 noinline

如果由于某些原因，我们不想优化对 `lambda` 的调用，可以通过将 `lambda` 参数标记为 `noinline` 来消除该优化。当函数本身被标记为 `inline` 时，只能对参数使用该关键字。

让我们要求编译器内联 `invokeTwo()` 函数，因此也内联对 `action1()` 的调用，但通过对该参数使用 `noinline`，来专门排除对 `action2()` 调用的优化：

```kotlin
inline fun invokeTwo(n: Int, noinline action1: (Int) -> Unit, noinline action2: (Int) -> Unit): (Int) -> Unit {
```

`Kotlin` 不允许我们保留对 `action1` 的引用，因为它是内联的，但是如果愿意，我们可以在 `invokeTwo()` 函数中创建对 `action2` 的引用，因为 `action2` 被定义为 `noinline`。运行后输出如下：

```shell
PS C:\Users\xiaotuan\Desktop> kotlinc-jvm .\KotlinTest.kt
PS C:\Users\xiaotuan\Desktop> kotlin .\KotlinTestKt.class
enter invokeTwo 1

called with 1, Stack depth: 11
Partial listing of the stack:
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt.callInvokeTwo(KotlinTest.kt:12)
KotlinTestKt.main(KotlinTest.kt:27)

called with 1, Stack depth: 13
Partial listing of the stack:
KotlinTestKt.report(KotlinTest.kt:19)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
KotlinTestKt$callInvokeTwo$2.invoke(KotlinTest.kt:12)
exit invokeTwo 1
```

除了内联代码外，`inline` 关键字还可以使从内联函数调用的 `lambda` 具有非局部 `return`。

### 4. 内联 `lambda` 中允许非局部 return

`Kotlin` 允许作为参数传递的内联 `lambda` 具有非局部 `return` 和带标签的 `return`。这是因为，虽然内联 `lambda` 在函数中扩展，但非内联 `lambda` 将是一个单独的函数调用。虽然前者的 `return` 将退出函数，但后者的 `return` 将不会执行相同的操作，因为它处于一个嵌套更深的堆栈层。例如：

```kotlin
fun callInvokeTwo() {
	invokeTwo(1, { i ->
		if (i == 1) { return }
		report(i)
	}, { i -> 
		// if (i == 2) { return }	// ERROR, return not allowed here
		report(i)
	})
}
```

运行结果如下：

```shell
PS C:\Users\xiaotuan\Desktop> kotlinc-jvm .\KotlinTest.kt
PS C:\Users\xiaotuan\Desktop> kotlin .\KotlinTestKt.class
enter invokeTwo 1
```

除了用 `inline` 注释函数之外，如果愿意，你还可以用 `inline` 标记类的方法和属性。

### 5. crossinline 参数

如果一个函数被标记为 `inline`，那么为标记为 `noinline` 的 `lambda` 参数将自动认为是内联的。在函数中调用 `lambda` 的地方，`lambda` 的主体将是内联的。但有一个问题。如果函数不调用给定的 `lambda`，而是将 `lambda` 传递给另一个函数，或者传回调用方呢？

在传递而不是调用 `lambda` 的情况下，不对 `lambda` 参数放置任何注释是没有意义的。一种解决方案是将其标记为 `noinline`。但是如果你想让 `lambda` 在任何可能被调用的地方都内联呢？你可以要求函数将内联请求传递给调用方，这就是 `crossinline` 的作用。例如：

```kotlin
inline fun invokeTwo(n: Int, action1: (Int) -> Unit, crossinline action2: (Int) -> Unit): (Int) -> Unit {
	println("enter invokeTwo $n")

	action1(n)
	action2(n)

	println("exit invokeTwo $n")
	return { input: Int -> action2(input) }
}
```

