如果我们追求的是对对象一系列调用的结果，而不关心示例，我们可以使用 `run()`。与 `apply()` 不同，`run()` 方法返回 `lambda` 的结果，但与 `apply()` 一样，它在目标对象的上下文中运行 `lambda`。

```kotlin
import java.lang.StringBuilder

fun main(args: Array<String>) {
    val result = Mailer().run {
        from("builder@agiledeveloper.com")
        to("venkats@agiledeveloper.com")
        subject("Your code sucks")
        body("...details...")
        send()
    }

    println(result)
}

class Mailer {
    val details = StringBuilder()
    fun from(addr: String) = details.append("from $addr...\n")
    fun to(addr: String) = details.append("to $addr...\n")
    fun subject(line: String) = details.append("subject $line...\n")
    fun body(message: String) = details.append("body $message...\n")
    fun send() = "...sending...\n$details"
}
```

`lambda` 中的每个方法调用都在用作 `run()` 目标的 `Mailer` 实例上执行。`send()` 方法的结果，即字符串，由 `run()` 方法返回给调用方。调用 `run()` 的 `Mailer` 实例不再可用。

要将目标对象保留在调用序列的末尾，请使用 `apply()`，而要将最后一个表达式的结果保留在 `lambda` 中，可以使用 `run()`。在任何情况下，只有当你想在目标的上下文中运行 `lambda` 时，才使用这些方法。