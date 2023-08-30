我们可以在一个 `when` 表达式或语句中使用 `is` 和 `!is` 以及智能转换。

```kotlin
fun whatToDo(dayOfWeek: Any) = when (dayOfWeek) {
    "Saturday", "Sunday" -> "Relax"
    in listOf("Monday", "Tuesday", "Wednesday", "Thursday") -> "Work hard"
    in 2..4 -> "Word hard"
    "Firday" -> "Party"
    is String -> "What?"
    else -> "No clue"
}
```

`when` 中的一个路径使用 `is` 运算符执行类型检查，来验证给定参数在运行时是否为类型 `String`。我们可以更进一步，在该路径中使用 `String` 的属性和方法，而不需要进行任何显示转换。

```kotlin
is String -> "What, you provided a string of length ${dayOfWeek.length}"
```



