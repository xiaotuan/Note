与专用的 `reduce` 操作 `sum()` 非常相似，`Kotlin` 也有一个函数 `first()`，用于返回给定集合中的第一个元素。当与 `filter()` 和 `map()` 一起使用时，我们可以在从结果集合中提取第一个元素之前执行过滤和转换。

例如，使用 `first()` 函数，我们可以得到第一个成年人的名字，其中成人是根据年龄大于 17 而不是一个人的成熟度来定义的：

```kotlin
data class Person(val firstName: String, val age: Int)

val people = listOf(
	Person("Sara", 12),
	Person("Jill", 51),
	Person("Paula", 23),
	Person("Paul", 25),
	Person("Mani", 12),
	Person("Jack", 70),
	Person("Sue", 10)
)

fun main() {
	val result = people.filter { person -> person.age > 17 }
		.map { person -> person.firstName }
		.first()
	println(result) // Jill
}
```

如果你希望得到的不是第一个成人的名字，而是最后一个成人的名字，那么用 `last()` 替换 `first()` 调用。上面示例中的结果将是 "Jack"。