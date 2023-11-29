让我们练习这四种方法，并报告传递的 `lambda` 所接收到的参数、每个 `lambda` 表达式中的 `this` 接收方、它们返回的结果，以及这四种方法的调用端所接收到的结果：

```kotlin
fun main(args: Array<String>) {
    val format = "%-10s%-10s%-10s%-10s"
    val str = "context"
    val result = "RESULT"

    fun toString() = "lexical"

    println(String.format("%-10s%-10s%-10s%-10s%-10s", "Method", "Argument", "Receiver", "Return", "Result"))
    println("===============================================")

    val result1 = str.let { arg ->
        print(String.format(format, "let", arg, "N/A", result))
        result
    }
    println(String.format("%-10s", result1))

    val result2 = str.also { arg ->
        print(String.format(format, "also", arg, "N/A", result))
        result
    }
    println(String.format("%-10s", result2))

    val result3 = str.run {
        print(String.format(format, "run", "N/A", this, result))
        result
    }
    println(String.format("%-10s", result3))

    val result4 = str.apply {
        print(String.format(format, "apply", "N/A", this, result))
        result
    }
    println(String.format("%-10s", result4))
}
```

运行输出如下：

```
Method    Argument  Receiver  Return    Result    
===============================================
let       context   N/A       RESULT    RESULT    
also      context   N/A       RESULT    context   
run       N/A       context   RESULT    RESULT    
apply     N/A       context   RESULT    context 
```

`let()` 方法将 `context` 对象（其调用的对象）作为参数传递给 `lambda`。`lambda` 的 `this` 或接收方是有词法作用域的，其绑定到 `lambda` 所定义的作用域中的 `this`。`lambda` 的结果作为调用 `let()` 的结果传递。

`also()` 方法也将 `context` 对象作为参数传递给它的 `lambda`，并且接收方在词法作用域中与 `this` 绑定。但是，与 `let()` 不同，`also()` 方法忽略其 `lambda` 的结果，并将 `context` 对象作为结果返回。`also()` 接收到的 `lambda` 的返回类型是 `Unit`，因此忽略返回的 `result`。

`run()` 方法不向其 `lambda` 传递任何参数，而是将 `context` 对象绑定到 `lambda` 的 `this` 或接收方。`lambda` 的结果作为 `run()` 的结果返回。

`apply()` 方法也不向其 `lambda` 传递任何参数，而是将 `context` 对象绑定到 `lambda` 的 `this` 或接收方。但与 `run()` 方法不同，`apply()` 方法忽略 `lambda` 的结果——用于返回的 `Unit` 类型——并将 `context` 对象返回给调用方法。

让我们总结一下这四种方法的行为：

+ 所有四个方法都执行传给它们的 `lambda`。
+ `let()` 和 `run()` 执行 `lambda`，并将 `lambda` 的结果返回给调用方。
+ `also()` 和 `apply()` 忽略 `lambda` 的结果，而是将 `context` 对象返回给它们的调用方。
+ `run()` 和 `apply()` 在调用它们的 `context` 对象的上下文 `this` 的执行过程中运行 `lambda`。