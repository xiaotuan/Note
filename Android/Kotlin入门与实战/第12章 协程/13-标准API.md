### 12.3.7　标准API

协程有3个主要组成部分。

+ 语言支持（如前面所述的挂起功能）。
+ Kotlin标准库中的底层核心API。
+ 可以直接被用户使用的高级API。

Kotlin标准库的底层核心API相对简单，除了创建更高级的库之外，应尽量避免使用它。它由两个主要包组成：kotlin.coroutines.experimental.intrinsics和kotlin.coroutines.experimental。

在这当中，kotlin.coroutines.experimental带有主要类型与下述原语。

+ createCoroutine()。
+ startCoroutine()。
+ suspendCoroutine()。

例如，使用future函数完成某个即将发生的操作。

```python
fun <T> future(context: CoroutineContext = CommonPool, block: suspend () -> T): CompletableFuture<T> =
        CompletableFutureCoroutine<T>(context).also { block.startCoroutine (completion = it) }
```

而kotlin.coroutines.experimental.intrinsics则带有更底层的内在函数，例如suspendCoroutine OrReturn()、buildSequence()和buildIterator()。下面是使用yield函数构建惰性序列的实例。

```python
fun main(args: Array<String>) {
            val fibonacciSeq = buildSequence {
                var a = 0
                var b = 1
                yield(1)    //惰性生产1
                while (true) {
                    yield(a + b)  //惰性生产斐波那契数列
                    val tmp = a + b
                    a = b
                    b = tmp
                }
            }
            println(fibonacciSeq.take(8).toList())
        }
```

运行上面的代码，输出的结果如下。

```python
 [1, 1, 2, 3, 5, 8, 13, 21]
```

从Kotlin标准库中只能获取与协程相关的核心API，主要包括所有基于协程库可能使用的核心原语和接口。然而，大多数基于协程的应用程序API作为单独的库进行发布：kotlinx. coroutines，这个库主要包括以下几大模块。

+ 使用 kotlinx-coroutines-core 的平台无关异步编程。
+ 基于JDK 8中的CompletableFuture的API：kotlinx-coroutines-jdk8。
+ 基于JDK 7及更高版本API的非阻塞IO(NIO)：kotlinx-coroutines-nio。
+ 支持Swing(kotlinx-coroutines-swing)和JavaFx(kotlinx-coroutines-javafx)。
+ 支持RxJava：kotlinx-coroutines-rx。

这些库除了可以用于通用的API，还可以构建基于协程库的端到端程序。

