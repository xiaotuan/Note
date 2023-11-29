首先我们定义一个 `Mailer` 类：

```kotlin
class Mailer {
    val details = StringBuilder()
    fun from(addr: String) = details.append("from $addr...\n")
    fun to(addr: String) = details.append("to $addr...\n")
    fun subject(line: String) = details.append("subject $line...\n")
    fun body(message: String) = details.append("body $message...\n")
    fun send() = "...sending...\n$details"
}
```

下面是使用这个 `Mailer` 类的一个相当冗长的示例：

```kotlin
fun main(args: Array<String>) {
    val mailer = Mailer()
    mailer.from("builder@agiledeveloper.com")
    mailer.to("venkats@agiledeveloper.com")
    mailer.subject("Your code sucks")
    mailer.body("...details...")
    val result = mailer.send()
    println(result)
}
```

运行输出如下：

```
...sending...
from builder@agiledeveloper.com...
to venkats@agiledeveloper.com...
subject Your code sucks...
body ...details......
```

`apply()` 方法在被调用的对象的上下文中执行 `lambda`，并将 `context` 对象返回给调用方。`apply()` 方法可以形成一个方法调用链。让我们使用 `apply()` 方法重新上面的代码：

```kotlin
fun main(args: Array<String>) {
    val mailer = Mailer()
        .apply { from("builder@agiledeveloper.com") }
        .apply { to("venkats@agiledeveloper.com") }
        .apply { subject("Your code sucks") }
        .apply { body("...details...") }
    val result = mailer.send()
    println(result)
}
```

`apply()` 方法在其目标对象的上下文中执行 `lambda`。因此，我们可以在 `lambda` 中放置多个对 `Mailer` 的调用，如下所示：

```kotlin
fun main(args: Array<String>) {
    val mailer = Mailer().apply {
        from("builder@agiledeveloper.com")
        to("venkats@agiledeveloper.com")
        subject("Your code sucks")
        body("...details...")
    }

    val result = mailer.send()
    println(result)
}
```

