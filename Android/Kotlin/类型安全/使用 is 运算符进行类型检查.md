`is` 运算符用于检查引用所指向的对象是否属于特定类型。如果实例是预期的类型，那么该表达式的结果为 `true`，否则为 `false`。

```kotlin
class Animal {
    override operator fun equals(other: Any?) = other is Animal
}
```

`is` 运算符可以用于任何类型的引用。如果引用为 `null`，那么使用 `is` 运算符的结果为 `false`。

你也可以使用带否定的 `is` 运算符。例如，你可以使用 `other !is Animal` 来检查给定的引用是否指向 `Animal` 的实例。