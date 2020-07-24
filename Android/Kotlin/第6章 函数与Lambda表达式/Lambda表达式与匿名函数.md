**Lambda 表达式语法**

```kotlin
val sum: (Int, Int) -> Int = { x: Int, y: Int -> x + y }
```

lambda 表达式总是括在花括号中，完整语法形式的参数声明放在花括号内，并有可选的类型标注，函数体跟在⼀个 `->` 符号之后。如果推断出的该 lambda 的返回类型不是 `Unit` ，那么该 lambda 主体中的最后⼀个（或可能是单个）表达式会视为返回值。

**传递末尾的 lambda 表达式**

在 Kotlin 中有⼀个约定：如果函数的最后⼀个参数是函数，那么作为相应参数传⼊的 lambda 表达式可以放在圆括号之外：

```kotlin
val product = items.fold(1) { acc, e -> acc * e }
```

**it: 单个参数的隐式名称**

如果编译器⾃⼰可以识别出签名，也可以不⽤声明唯⼀的参数并忽略 `->` 。该参数会隐式声明为 `it` ：

```kotlin
ints.filter { it > 0 } // 这个字⾯值是“(it: Int) -> Boolean”类型的
```

**从 lambda 表达式中返回一个值**

我们可以使⽤限定的返回语法从 lambda 显式返回⼀个值。否则，将隐式返回最后⼀个表达式的值。因此，以下两个⽚段是等价的：

```kotlin
ints.filter {
   val shouldFilter = it > 0
    shouldFilter
} 

ints.filter {
    val shouldFilter = it > 0
    return@filter shouldFilter
}
```

**下划线⽤于未使⽤的变量（⾃ 1.1 起）**

如果 lambda 表达式的参数未使⽤，那么可以⽤下划线取代其名称：

```kotlin
map.forEach { _, value -> println("$value!") }
```

**匿名函数**

如果确实需要显式指定，可以使⽤另⼀种语法：匿名函数 。

```kotlin
fun(x: Int, y: Int): Int = x + y
```

> 请注意，匿名函数参数总是在括号内传递。允许将函数留在圆括号外的简写语法仅适⽤于 lambda 表达式。

Lambda表达式与匿名函数之间的另⼀个区别是⾮局部返回的⾏为。⼀个不带标签的 `return` 语句总是在⽤ `fun` 关键字声明的函数中返回。这意味着 lambda 表达式中的 `return` 将从包含它的函数返回，⽽匿名函数中的 `return` 将从匿名函数⾃⾝返回。

**闭包**

Lambda 表达式或者匿名函数（以及局部函数和对象表达式）可以访问其 闭包 ，即在外部作⽤域中声明的变量。在 lambda 表达式中可以修改闭包中捕获的变量：

```kotlin
var sum = 0
ints.filter { it > 0 }.forEach {
    sum += it
}
print(sum)
```

**带有接收者的函数字面值**

带有接收者的函数类型，例如 `A.(B) -> C` ，可以⽤特殊形式的函数字⾯值实例化⸺ 带有接收者的函数字⾯值。

匿名函数语法允许你直接指定函数字⾯值的接收者类型。如果你需要使⽤带接收者的函数类型声明⼀个变量，并在之后使⽤它，这将⾮常有⽤。

```kotlin
val sum = fun Int.(other: Int): Int = this + other
```