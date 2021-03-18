### 4.5.3　for循环

虽然所有循环结构都可以使用while或者do...while来实现，但使用for循环会使循环结构变得更加简单。在Kotlin中，for循环可以直接枚举集合中的元素，还可以按集合索引来枚举元素。for循环可以对任何迭代器（iterator）的对象进行遍历，语法格式如下。

```python
for (item in collection)   print(item)
```

当然，循环体还可以是一个代码块。

```python
val arr: Array<String> = arrayOf("java", "c", "Kotlin","Swift")
    for (item: String in arr) {
        println(item)
    }
```

如果想要通过索引遍历数组或者列表中的元素值，可以使用下面的方式。

```python
val arr: Array<String> = arrayOf("java", "c", "Kotlin","Swift")
    for (i in arr.indices) {
        println("arr[$i] = " + arr[i])
    }
```

执行上面的代码，会得到如下的结果。

```python
arr[0] = java
arr[1] = c
arr[2] = Kotlin
arr[3] = Swift
```

对于上面的循环，Kotlin提供了一个更加简单的库函数withIndex，它可以同时对索引和元素值进行循环操作。

```python
val arr: Array<String> = arrayOf("java", "c", "Kotlin","Swift")
    for ((index, value) in arr.withIndex()) {
        println("arr [$index] = " + arr[index])
    }
```

