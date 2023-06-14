`for` 循环用于遍历提供迭代器的容器对象，其语法如下：

```kotlin
for (item in collection) print(item)
```

`for` 的主体可以是一个块：

```kotlin
for (item : Int in ints) {
    // ...
}
```

要迭代一系列数字，请使用范围表达式：

```kotlin
for (i in 1..3) {
    println(i)
}
for (i in 6 downTo 0 step 2) {
    println(i)
}
```

如果你想遍历一个数组或一个带有索引的列表，你可以这样做：

```kotlin
for (i in array.indices) {
    println(array[i])
}
```

或者，你可以使用 `withIndex` 库函数：

```kotlin
for ((index, value) in array.withIndex()) {
    println("the element at $index is $value")
}
```

