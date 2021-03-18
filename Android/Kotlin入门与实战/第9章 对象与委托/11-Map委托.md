### 9.3.3　Map委托

Map委托常常用来将Map中的key-value映射到对象的属性中，这经常出现在解析JSON或者其他“动态”事情的应用中。在这种情况下，可以使用映射实例自身作为委托来实现委托属性。

```python
fun main(args: Array<String>) {
    //构造函数接收一个映射参数
    val user = User(mapOf(
            "name" to "jack",
            "age"  to 30
    ))
    println(user.name)
    println(user.age)
}
class User(var map: Map<String, Any>) {
    val name: String by map
    val age: Int  by map
}
```

执行上面的代码，输出结果如下。

```python
jack
30
```

可以看到，User类中使用val声明了name和age属性，这就意味着这两个属性值是不可以被修改的。当然，Map委托也是支持使用var属性的，只不过需要把Map换成MutableMap。

```python
fun main(args: Array<String>) {
    var map: MutableMap<String, Any?> = mutableMapOf(
            "name" to "Kotlin",
            "age" to 30
    )
    val user = User(map)
    println(user.name)
    println(user.age)
    println("--------------")
    map.put("name", "Google")
    map.put("age", 20)
    println(user.name)
    println(user.age)
}
class User(var map: MutableMap<String, Any?>) {
    val name: String by map
    val age: Int  by map
}
```

运行上面的代码，输出结果如下。

```python
Kotlin
30
--------------
Google
20
```

可以看到，如果将属性委托给MutableMap，那么无论是修改MutableMap中的值，还是修改User类的属性值，变化都是同步的。

