### 4.11.4　throw表达式

在Kotlin中，throw是一个表达式，可以作为Elvis表达式的一部分，代码如下。

```python
val s = person.name ?: throw IllegalArgumentException("Name required")
```

throw表达式是一种特殊的Nothing类型。该类型没有返回值并且经常用来标识一些永远不会被访问的代码块。代码如下。

```python
fun fail(message: String): Nothing {
    throw IllegalArgumentException(message)
}
```

当调用该函数时，因为没有特定的返回类型，所以程序会终止执行，并会给出相应的错误提示。

```python
val s = person.name ?: fail("Name required")
println(s)     // s此时才初始化
```

