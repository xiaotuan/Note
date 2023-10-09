`filter()`、`map()` 和 `reduce()` 是用作内部迭代器的基本函数。`filter()` 函数从给定的集合中选取某些值，同时删除其他的值。`map()` 函数使用给定的函数或 `lambda` 转换集合中的值。最后，`reduce()` 函数对元素执行累计操作，通常得到单个值。所有这些函数都在补改变或更改给定集合的情况下执行它们的操作——它们返回一个具有适当值的副本。

`filter()` 返回的集合的大小从 0 到 n 不等，其中 n 是原始集合中的元素数。结果是一个子集合，也就是说，输出集合中的值是原始集合中的值。传递给 `filter()` 的 `lambda` 应用于原始集合中的每个元素。当且仅当 `lambda` 返回 `true` 时，对元素求值时，来自原始集合的元素将包含在输出集合中。

`map()` 返回集合的大小与原始集合的大小相同。传递给 `map()` 的 `lambda` 应用于原始集合中的每个元素，结果是这些转换后的值的集合。

传递给 `filter()` 和 `map()` 的 `lambda` 只接受一个参数，但是传递给 `reduce()` 的 `lambda` 接受两个参数。第一个参数是一个累计值，第二个参数是来自原始集合的一个元素。`lambda` 的结果是新的累计值。`reduce()` 的结果是最后一次调用 `lambda` 的结果。

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
	val result = people.filter { person -> person.age > 20 }
		.map { person -> person.firstName }
		.map { name -> name.uppercase() }
		.reduce { names, name -> "$names, $name" }
	println(result) // JILL, PAULA, PAUL, JACK
}
```

`filter()` 函数从给定的集合中只提取年龄超过 20 岁的 `Person`。然后将该列表传递给 `map()`，`map()` 将年龄超过 20 岁的 `Person` 列表转换为名字列表。然后第二个 `map()` 将名字列表转换为大写的名字列表。最后，我们使用 `reduce()` 函数将大写的名字组合成一个以逗号分隔的字符串。

`Kotlin` 为不同的操作，比如 `sum`、`max`，甚至 `join` 字符串等提供了许多专用的 `reduce` 函数。我们可以用下面的代码代替前面的 `reduce()` 调用，使代码更简洁：

```kotlin
val result = people.filter { person -> person.age > 20 }
		.map { person -> person.firstName }
		.map { name -> name.uppercase() }
		.joinToString(", ")
```

如果我们想计算列表中每个 `Person` 的年龄之和，可以使用 `map()` 和 `reduce()`，如下所示：

```kotlin
fun main() {
	val result = people.map { person -> person.age }
		.reduce { total, age -> total + age }
	println(result) // 203
}
```

同样，我们可以使用专用的 `reduce` 操作 `sum()`，而不是 `reduce()`，如下所示：

```kotlin
fun main() {
	val result = people.map { person -> person.age }
		.sum()
	println(result) // 203
}
```

