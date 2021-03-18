### 4.2.2　getter和setter

在Kotlin中声明变量时，编译器会默认为变量添加getter和setter方法，其完整的声明格式如下。

```python
var <propertyName>: <PropertyType> [= <property_initializer>]
[<getter>]
[<setter>]
```

这当中initializer、getter和setter都是可选的。使用var定义的变量允许同时有getter和setter方法；如果变量是使用val声明的，那么这个变量只能有getter方法而没有setter方法，因为val定义的变量值是不可变的。

```python
fun variablesTest() {
    var data: Any = Any()
    //相当于getData()
    var a = data
    println("a"+a.toString())
    println("data"+data.toString())
    //相当于setData()
    data = Any()
    println("data"+data.toString())
}
```

运行上面的代码，输出结果如下。

```python
a:java.lang.Object@5e481248
data:java.lang.Object@5e481248
data:java.lang.Object@66d3c617
```

在Kotlin中，是不允许getter和setter本身有局部变量的，因为属性的调用也就是对get函数的调用，所以会产生递归，造成内存溢出。

为此，Kotlin提供了后端变量（Backing Field），在编译器检查函数体的过程中，如果使用了field，就会生成一个后端变量，在具体使用的时候，field会代替属性本身进行操作，Kotlin官方提供了访问属性值的例子。

```python
val isEmpty: Boolean
get() = this.size == 0
```

在访问属性值isEmpty时，并不会生成后端变量，因为它的值是由其实例的长度决定的，并不需要一个后端域变量进行过渡。

如果上面的方案还不能解决问题，那可以尝试使用后端属性（Backing Property）。它实际上是一个隐含的对属性值的初始化声明，能有效避免空指针问题的产生。

```python
var size: Int = 2
private var _table: Map<String, Int>? = null
val table: Map<String, Int>
    get() {
        if (_table == null)
            _table = HashMap()
        return _table ?: throw AssertionError("Set to null by another thread")
    }
```

在Java中，访问private成员变量需要通过getter和setter来实现，此处通过table来获取_table变量，优化了Java中函数调用带来的开销。

前面说过，在设置变量属性时，编译器会默认为变量添加getter和setter方法。当然，也可以根据实际情况自定义get和set。代码如下。

```python
// People实体，包含lastName、no和heiht属性
class People {
    var lastName: String = "hello"
        get() = field.toUpperCase()
        set
    var no: Int = 100
        get() = field
        set(value) {
            if (value < 10) {
                field = value
            } else {
                field = -1
            }
        }
    var heiht: Float = 145.4f
        private set
}
```

自定义get和set的重点在field，field指代当前参数，类似于Java的this关键字。

