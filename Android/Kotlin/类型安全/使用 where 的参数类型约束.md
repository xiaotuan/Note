例如，在下面的代码中，类型 `T` 期望支持 `close()` 方法：

```kotlin
fun <T> useAndClose(input: T) {
	input.close()	// Error: unresolved reference: close
}
```

但是任意类型没有 `close()` 方法，因此编译器调用 `close()` 时失败。但是，我们可以告诉 `Kotlin` 通过一个带有 `close()` 方法的接口，例如 `AutoCloseable` 接口，来将参数类型约束位仅具有该方法的类型。让我们重写函数声明以使用约束：

```kotlin
fun <T: AutoCloseable> useAndClose(input: T) {
	input.close()
}
```

若要防止单个约束，请修改参数类型规范，将约束放置在冒号之后。但如果有多个约束，这种技术就行不通了。在这种情况下，我们需要使用 `where`。

```kotlin
fun <T> useAndClose(input: T)
	where T: AutoCloseable,
		  T: Appendable {
	input.append("there")
	input.close()	
}
```

在方法声明的最后，放置一个 `where` 子句并列出所有的约束，用逗号分隔。