### 12.3.4　runBlocking函数

Kotlin提供runBlocking函数来实现类似主协程的功能，该runBlocking函数主要用来桥接普通阻塞代码和挂起的非阻塞代码。

```python
fun main(args: Array<String>) = runBlocking<Unit> {
    launch(CommonPool) {
        delay(1000L)
        println("World!")
    }
    println("Hello,")
    delay(2000L)
}
```

可以发现，运行结果跟传统的Thread.sleep方式的执行结果是一样的，但是这里并没有使用Thread.sleep，而是使用了非阻塞的delay函数。

实际上，runBlocking和launch一样，也是启动一个协程，只不过它传入的上下文对象（context）不会进行线程切换，也就是说，由它创建的协程会直接运行在主线程上。其次，delay函数所实现的功能和Thread.sleep类似，但使用delay函数的好处在于它不会阻塞线程，而只是挂起协程本身。

