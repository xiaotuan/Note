### 9.3.4　Not Null

对于那些无法在初始化阶段确定属性值的场合，可以使用notNull属性。代码如下。

```python
fun main(args: Array<String>) {
    val foo=Foo();
    foo.notNullBar = "bar"
    println(foo.notNullBar)
}
class Foo {
    var notNullBar: String by Delegates.notNull<String>()
}
```

需要注意的是，如果在赋值前访问属性，则会抛出异常。

