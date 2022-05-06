`with` 函数的语法结构如下所示：

```kotlin
with(object) {
    // todo
}
```

`with` 函数和前面的几个函数使用方式略有不同，因为它不是以扩展的形式存在的。它是将某对象作为函数的参数，在函数块内可以通过 `this` 指代该对象。返回值为函数块的最后一行或指定 `return` 表达式。

可以看出 `with` 函数是接收了两个参数，分别为 T 类型的对象 receiver 和一个 lambda 函数块，所以 `with` 函数最原始样子如下：

```kotlin
val result = with(user, {
    println("my name is $name, I am $age years old, my phone number is $phoneNum")
    1000
})
```

但是由于 `with` 函数最后一个参数是一个函数，可以把函数提到圆括号的外部，所以最终 `with` 函数的调用形式如下：

```kotlin
val result = with(user) {
    println("my name is $name, I am $age years old, my phone number is $phoneNum")
    1000
}
```

`with` 函数适用的场景：

适用于调用同一个类的多个方法时，可以省去类名重复，直接调用类的方法即可，经常用于 Android 中 `RecyclerView` 中 `onBinderViewHolder` 中，数据 model 的属性映射到UI上。