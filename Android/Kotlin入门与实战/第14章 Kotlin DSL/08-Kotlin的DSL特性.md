```python
val person = person {
     name = "John"
     age = 30
     address {
        street = "Main Street"
        number = 42
        city = "London"
    }
}
```

### 14.3　Kotlin的DSL特性

许多现代语言为创建内部DSL提供了一些先进的方法，Kotlin也不例外，在Kotlin中创建DSL，一般主要使用下面两种方式。

+ 扩展函数和扩展属性。
+ 带接收者的Lambda表达式，如高阶函数。

为了方便理解，本节以一个简单的模型来介绍如何使用Kotlin创建DSL，下面是本示例最终调用的相关代码。

```python
val person = person {
     name = "John"
     age = 30
     address {
        street = "Main Street"
        number = 42
        city = "London"
    }
}
```

对于上面的代码，即使没有开发者经验的人也很容易理解其含义，甚至对其进行修改，为了达到这一目的，首先需要准备一个模型。上面代码对应的模型如下。

```python
data class Person(var name: String? = null,
                      var age: Int? = null,
                      var address: Address? = null)
data class Address(var street: String? = null,
                       var number: Int? = null,
                       var city: String? = null)
```

接下来，要做的第一件事就是创建一个新文件，保持DSL与模型的实际类分离，首先为Person类创建一些构造函数。代码如下。

```python
fun person(block: (Person) -> Unit): Person {
     val p = Person()
     block(p)
     return p
}
```

在person函数的定义中，可以给Lambda表达式添加一个接收者，这样，在Lambda表达式中就可以访问那个接收器函数。由于Lambda中的函数在接收者的范围内，因此可以简单地在接收者上调用Lambda表达式，而不是将其作为参数使用。

```python
fun person(block: Person.() -> Unit): Person {
     val p = Person()
     p.block()
     return p
}
```

实际上，还可以通过使用Kotlin提供的apply函数对上述函数进行一个简单的重写。

```python
fun person(block: Person.() -> Unit): Person = Person().apply(block)
```

到目前为止，还差一个Address类，在我们期望的结果中，它看起来很像刚刚创建的person函数。唯一的区别是必须将它分配给Person对象的Address属性，为此，可以使用Kotlin提供的扩展函数。

扩展函数可以向类中添加函数而无须访问类本身的代码。在上面的实例中，创建Address对象并直接将其分配给Person的地址属性即可。

```python
fun person(block: Person.() -> Unit): Person = Person().apply(block)
fun Person.address(block: Address.() -> Unit) {
     address = Address().apply(block)
}
```

现在，为Person添加一个地址函数，它接收一个将Address对象作为接收者的Lambda表达式，然后，它将创建的Address对象设置为Person的属性。到此，就可以像本节开始时那样调用目标代码了。

