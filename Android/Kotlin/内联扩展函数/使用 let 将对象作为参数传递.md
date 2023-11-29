假设你从一个函数接收了一个实例，但希望将该实例作为参数传递给另一个方法。这样的操作顺序通常会破坏代码的流畅性。`let()` 方法有助于恢复这种情况下的流畅性。

让我们看一个例子来说明这一点：

```kotlin
import java.lang.StringBuilder

fun main(args: Array<String>) {
    val mailer = createMailer()
    val result = prepareAndSend(mailer)
    println(result)
}

fun createMailer() = Mailer()

fun prepareAndSend(mailer: Mailer) = mailer.run {
    from("builder@agiledeveloper.com")
    to("venkats@agiledeveloper.com")
    subject("Your code sucks")
    body("...details...")
    send()
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

忽略 `println()`，我们可以像这样修改对这两个函数的调用：

```kotlin
val result = prepareAndSend(createMailer())
```

这时，我们可以使用 `let()` 方法来简化代码：

```kotlin
val result = createMailer().let { mailer ->
    prepareAndSend(mailer)
}
```

我们可以做一个小小的修改，去掉这个参数名：

```kotlin
val result = createMailer().let {
    prepareAndSend(it)
}
```

这里 `lambda` 并没做什么，它接受了一个参数并将其传递给 `prepareAndSend()` 方法。这里我们不使用 `lambda`，而是使用一个方法引用：

```kotlin
val result = createMailer().let(::prepareAndSend)
```

如果你想使用传递给 `let()` 的 `lambda` 的结果作为参数，那么 `let()` 方法是一个不错的选择。但是要继续对调用 `let()` 的目标执行一些操作，还需要使用 `also()` 方法。