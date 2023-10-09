假设我们有一个嵌套的列表，比如 `List<List<Persion>>`，其中顶级列表包含家族，家族的成员在 `Person` 的子列表中。如果我们想要将它转换为 `Person` 的平面列表呢？与 `Ruby` 等语言一样，`Kotlin` 也有一个 `fatten()` 函数。

给定一个 `Iterable<Iterable<T>>`，`flatten()` 函数将返回一个 `Iterable<T>`，其中嵌套的 `iterable` 中的所有元素都组合到顶层，从而使层次结构变平。

让我们子啊一个简短的例子中使用 `flatten()`：

```kotlin
data class Person(val firstName: String, val age: Int)

val families = listOf(
	listOf(Person("Jack", 40), Person("Jill", 40)),
	listOf(Person("Eve", 18), Person("Adam", 18))
)

fun main() {
	println(families.size)	// 2
	println(families.flatten().size) // 4
}
```

在前面的示例中，我们有意在列表中创建了嵌套列表。有时，这种嵌套可能是对另一个集合执行 `map()` 操作的结果。让我们研究一个这样的场景，看看 `flatten()` 是如何在该上下文中发挥作用的。

让我们重新访问 `people` 集合，获取每个人名字的小写和名字的反写。通过调用 `map()` 函数，可以从 `people` 集合中获得名字的列表。由此，我们可以再次使用另一个 `map()` 调用来获得小写的名字。最后，我们可以第三次使用 `map()` 来获得名字的小写和反写。让我们使用这些步骤并观察结果：

```kotlin
import kotlin.text.reversed

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
	val namesAndReversed = people.map { person -> person.firstName }
		.map(String::lowercase)
		.map { name -> listOf(name, name.reversed())}
	println(namesAndReversed.size) // 7
}
```

在最后一步中，我们对原始列表中的每个 `Person` 返回一个包含两个字符串的列表。`namesAndReversed` 的类型是 `List<List<String>>` ，结果的大小是 7,。但是我么真正想要的是 `List<String>`，而不是 `List<List<String>>`。这可以通过调用 `flatten()` 实现：

```kotlin
fun main() {
	val namesAndReversed = people.map { person -> person.firstName }
		.map(String::lowercase)
		.map { name -> listOf(name, name.reversed())}
		.flatten()
	println(namesAndReversed.size) // 14
}
```

尽管这可以正常工作，但是如果我们可以将 `map` 操作与 `flatten` 操作结合起来就更好了，因为我们的目的是创建一个平面列表。因此，`Kotlin` 提供了一个在 `map` 后面跟一个 `flatten` 操作的迭代器 `flatMap()`。上面的代码可以写成如下：

```kotlin
fun main() {
	val namesAndReversed = people.map { person -> person.firstName }
		.map(String::lowercase)
		.flatMap { name -> listOf(name, name.reversed())}
	println(namesAndReversed.size) // 14
}
```

如果你在考虑是应该使用 `map()` 还是 `flatMap()`，这里有一些小建议：

+ 如果 `lambda` 是一个一对一的函数——也就是说，它接受一个对象或值，并返回一个对象或值——那么可以使用 `map()` 转换原始集合。
+ 如果 `lambda` 是一个一对多的函数——也就是说，它接受一个对象或值，并返回一个集合——那么可以使用 `map()` 将原始集合转换为集合的集合。
+ 如果 `lambda` 是一个一对多的函数，但是你希望将原始集合转换为经过转换的对象或值的集合，那么可以使用 `flatMap()`。
