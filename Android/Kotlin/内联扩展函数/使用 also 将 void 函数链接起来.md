`also()` 方法对于将一系列 `void` 函数链接起来很有用，否则这些函数不会落入调用链中。

假如在 `kotlin` 中我们有一堆 `void` 函数：

```kotlin
import java.lang.StringBuilder

fun main(args: Array<String>) {
    val mailer = createMailer()
    prepareMailer(mailer)
    sendMail(mailer)
}

fun createMailer() = Mailer()

fun prepareMailer(mailer: Mailer) {
    mailer.run {
        from("builder@agiledeveloper.com")
        to("venkats@agiledeveloper.com")
        subject("Your code sucks")
        body("...details...")
    }
}

fun sendMail(mailer: Mailer) {
    mailer.send()
    println("Mail sent")
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

我们可以使用 `also()` 恢复函数调用链，因为 `also()` 将目标作为参数传递给 `lambda`，忽略 `lambda` 的返回，并返回调用的目标，下面是使用这些 `void` 函数的流畅代码：

```kotlin
createMailer()
        .also(::prepareMailer)
        .also(::sendMail)
```

