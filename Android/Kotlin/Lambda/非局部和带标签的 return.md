[toc]

默认情况下，`lambda` 不允许有 `return` 关键字，即使它们返回一个值。这是 `lambda` 和匿名函数之间的一个显著区别——如果返回值，后者必须有 `return`，并且它表示只从当前 `lambda` 返回，而不是从外部调用函数返回。

### 1. 默认情况下不允许使用 return

默认情况下，`return` 在 `lambda` 中是无效的，但你可以在某些特殊情况下使用它。我们将使用一个函数来说明，这个函数接受两个参数，一个 `Int` 和一个 `lambda` ，返回 `Unit`。

```kotlin
fun invokeWith(n: Int, action: (Int) -> Unit) {
    println("enter invokeWith $n")
    action(n)
    println("exit invokeWith $n")
}
```

让我们从 `caller()` 函数中调用 `invokeWith()`，然后调用 `caller()` 函数：

```kotlin
fun invokeWith(n: Int, action: (Int) -> Unit) {
    println("enter invokeWith $n")
    action(n)
    println("exit invokeWith $n")
}

fun caller() {
	(1..3).forEach { i ->
		invokeWith(i) {
			println("enter for $it")
			
			if (it == 2) { return }	// ERROR, return is not allowed here
			
			println("exit for $it")
		}
	}
	
	println("end of caller")
}

fun main() {
	caller()
	println("after return from caller")
}
```

带有 `return` 的行将编译失败。如果我们在整个代码的整体上下文中查看这一行，那么原因就变得很清楚了。当我们在第 6 行调用 `return` 时，`kotlin` 不知道我们打算立即退出当前的 `lambda`，并在调用 `action(n)` 之后继续执行 `invokeWith()` 中的代码，或退出再第 2 行进入的 `for` 循环，或退出再第一行进入的函数 `caller()`。

### 2. 带标签的 return

如果你想立即退出当前的 `lambda`，那么你可以使用一个带标签的 `return`，即 `return@label`，其中 `label` 是一些你可以使用语法 `label@` 创建的标签。

```kotlin
fun invokeWith(n: Int, action: (Int) -> Unit) {
    println("enter invokeWith $n")
    action(n)
    println("exit invokeWith $n")
}

fun caller() {
	(1..3).forEach { i ->
		invokeWith(i) here@ {
			println("enter for $it")
			
			if (it == 2) { return@here }
			
			println("exit for $it")
		}
	}
	
	println("end of caller")
}

fun main() {
	caller()
	println("after return from caller")
}
```

运行结果如下：

```
enter invokeWith 1
enter for 1
exit for 1
exit invokeWith 1
enter invokeWith 2
enter for 2
exit invokeWith 2
enter invokeWith 3
enter for 3
exit for 3
exit invokeWith 3
end of caller
after return from caller
```

带标签的 `return` 导致控制流跳转到带标签的块的末尾——即退出 `lambda` 表达式。

我们可以使用隐式标签，即接收 `lambda` 的函数名称，而不使用像 `@here` 这样的显示标签。因此，我们可以将 `return@here` 替换为 `return@invokeWith`，并去掉标签 `here@`，如下所示：

```kotlin
fun caller() {
	(1..3).forEach { i ->
		invokeWith(i) {
			println("enter for $it")
			
			if (it == 2) { return@invokeWith }
			
			println("exit for $it")
		}
	}
	
	println("end of caller")
}
```

尽管 `kotlin` 允许使用方法名作为标签，但是更喜欢使用显示标签。这样使得意图更清晰，代码更容易理解。

编译器不允许带标签的 `return` 返回到任意的外部范围——你只能从当前所包含的 `lambda` 返回。如果你想退出当前定义的函数，那么默认情况下不能这样做，但是如果接收 `lambda` 的函数是内联的，那么就可以这样做。

### 3. 非局部 return

非局部 `return` 有助于从 `lambda` 内部中断正在实现的当前函数。让我们再次修改 `caller()` 函数来查看这个特性。

```kotlin
package com.agiledeveloper.util

fun invokeWith(n: Int, action: (Int) -> Unit) {
    println("enter invokeWith $n")
    action(n)
    println("exit invokeWith $n")
}

fun caller() {
	(1..3).forEach { i ->
		
		println("in forEach for $i")
		if (i == 2) { return }
		
		invokeWith(i) {
			println("enter for $it")
			
			if (it == 2) { return@invokeWith }
			
			println("exit for $it")
		}
	}
	
	println("end of caller")
}

fun main() {
	caller()
	println("after return from caller")
}
```

运行结果如下：

```
enter invokeWith 1
enter for 1
exit for 1
exit invokeWith 1
in forEach for 2
after return from caller
```

与带标签的 `return` （其退出所包含的 `lambad`）不同，`if (i == 2) { return }` 行上的这个 `return` 将退出本例中定义的包含函数 `caller()`。因此，称之为非局部 `return`。

现在的问题是：为什么 `Kotlin` 不允许使用没有标签的 `return`，当然，是在传递给 `invokeWith()` 的 `lambda` 中，但是对传递给 `forEach()` 的 `lambda` 中的 `return` 没有回避？答案隐藏在这两个函数的定义中。

我们将 `invokeWith()` 定义为：

```kotlin
fun invokeWith(n: Int, action: (Int) -> Unit)
```

另一方面，在 `kotlin` 标准库中定义了 `forEacth()`，如下所示：

```kotlin
inline fun <T> Iterable<T>.forEach(action: (T) -> Unit): Unit
```

答案在于关键字 `inline`。让我们回顾一下 `return` 的行为：

+ 默认情况下，在 `lambda` 中不允许使用 `return` 。
+ 你可以使用带标签的 `return` 来跳出所包含的 `lambda`。
+ 只有当接收 `lambda` 的函数使用 `inline` 定义时，才可能使用非局部 `return` 来从所定义的包含函数中退出。

这里有一些方法来处理与 `return` 行为相关的复杂情况：

+ 你可以在任何时候使用带标签的 `return` 来从 `lambda` 返回。
+ 如果你能够使用 `return`，请记住它将退出正在定义的包含函数，而不仅仅是从所包含的 `lambda` 或 `lambda` 的调用方退出。
+ 如果不允许你使用 `return`，请不要担心，`Kotlin` 会明确地告诉你。