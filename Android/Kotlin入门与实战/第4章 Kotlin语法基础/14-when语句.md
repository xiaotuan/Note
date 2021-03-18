### 4.5.2　when语句

在Kotlin中，when取代了C风格语言的switch语句，相比switch语句而言，when语句更加强大、灵活性更好。一个简单的when语句形式如下。

```python
val x : Int = 10
when (x) {
    9 -> println("x:${x + 10}")
    10 -> println("x:$x")
    else -> print("x:$x")
}
```

在具体使用的时候，when会对所有的分支进行检查，直到有一个条件满足为止，when既可以被当作表达式使用，也可以被当作语句使用。如果当作表达式使用，则符合条件的分支的值就是整个表达式的值；如果当作语句使用，则不满足条件的分支的值会被忽略，只保留满足条件的分支，而且返回的也是最后一个表达式的值。

如果有很多分支需要用相同的方式处理，则可以将多个分支条件放在一起，分支之间用逗号分隔。代码如下。

```python
val x : Int = 10
    when (x) {
        0,1 -> print("x == 0 or x == 1")
        else -> print("otherwise")
    }
```

如果要执行相同代码的条件比较多或无法枚举，则可以使用in或者!in来确定一个范围。

```python
var n = 25
    when(n) {
        in 1..10 ->println("在1~10范围内")
        in 11.. 20 ->println("在11~20范围内条件")
        !in 30..60 ->println("不再上面的范围内")   // !in表示不在范围内
        else->println("在其他范围内")
    }
```

除了检测范围之外，另一种可能性检测是使用is或者!is来检测一个特定类型的值。

```python
fun main(args: Array<String>) {
    var x="that is prefix"
    hasPrefix(x)
}
fun hasPrefix(x: Any) = when(x) {
    is String -> println(x.startsWith("prefix"))  //输出flase
    else -> false
}
```

其实，when中的分支条件不仅可以是常量，还可以是任意表达式。

```python
fun main(args: Array<String>) {
    val x=10
    val s=5
    when (x) {
        parseInt(s) -> print("s encodes x")
        else -> print("s does not encode x")
    }
}
fun parseInt(x:Int):Int {
    return x * x
}
```

除此之外，when还可以用来取代if-else if语句链，如果不提供参数，那么所有的分支条件都是布尔表达式，当其中某个分支的条件为真时执行该分支。

```python
when {
    x.isOdd() -> print("x is odd")
    x.isEven() -> print("x is even")
    else -> print("x is funny")
}
```

