### 4.9　Kotlin动态类型

作为一种静态类型的编程语言，Kotlin仍然需要与无类型或松散类型的环境进行互操作（如JavaScript生态系统）。为了配合这些使用场景，Kotlin提供了动态类型。

```python
val dyn: dynamic =…
```

dynamic类型基本上关闭了Kotlin的类型检查系统，具体表现在如下几点。

+ dynamic类型的值可以赋值给任何变量或作为参数进行传递。
+ 任何值都可以赋值给dynamic类型的变量，或者传递给一个接收dynamic 作为参数的函数。
+ 动态类型禁止了null检查。

对于动态类型来说，可以直接调用dynamic变量的任何属性或调用任何函数的任意参数。代码如下。

```python
dyn.whatever(1, "foo", dyn)     // whatever在任何地方都没有定义
dyn.whatever(*arrayOf(1, 2, 3))
```

在JavaScript平台上，代码总是按照原样进行编译。

动态调用总是返回一个dynamic类型作为结果，因此可以自由地按照下面这种方式进行链接调用。

```python
dyn.foo().bar.baz()
```

把一个Lambda表达式传给一个动态调用函数时，该函数的所有参数默认都是dynamic类型的。

```python
dyn.foo {
    x -> x.bar()     // x 为dynamic
}
```

在JavaScript平台中，使用dynamic类型值的表达式会按照原样进行转换，而且dynamic类型不使用Kotlin运算符进行约定。

