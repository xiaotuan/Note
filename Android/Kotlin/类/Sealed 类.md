在 `Kotlin` 中，存在一种极端情况，我们有 `final` 类 —— 即未标记为 `open` 的类，它们不能有任何派生类。在另一种极端情况，我们有 `open` 类和 `abstract` 类，不知道哪个类可以继承它们。最好能有一个中间地带，让一个类只作为几个类的基，这几个类是由类的创建者指定的。

`Kotlin` 的 `sealed` 类对于同一个文件中定义的其他类进行扩展是开放的，但是对于其他类——也就是 `final` 或者不是 `open` 的类，则是关闭的。

下面是一个 `sealed` 类 `Card`，以及从它继承的几个类，都在同一个文件 `Card.kt` 中。

```kotlin
sealed class Card(val suit: String)

class Ace(suit: String): Card(suit)

class King(suit: String): Card(suit) {
	override fun toString() = "Queen of $suit"
}

class Jack(suit: String): Card(suit) {
	override fun toString() = "Jack of $suit"
}

class Pip(suit: String, val number: Int): Card(suit) {
	init {
		if (number < 2 || number > 10) {
			throw RuntimeException("Pip has to be between 2 and 10")
		}
	}
}
```

`sealed` 类的构造函数没有标记为 `private`，但是它们被认为是 `private` 的，所以我们不能实例化这些类的对象。但是，我们可以创建从 `sealed` 类继承的类的对象，假设它们的构造函数没有显示地标记为 `private`。

```kotlin
sealed class Card(val suit: String)

class Ace(suit: String): Card(suit)

class King(suit: String): Card(suit) {
	override fun toString() = "King of $suit"
}

class Queen(suit: String): Card(suit) {
	override fun toString() = "Queen of $suit"
}

class Jack(suit: String): Card(suit) {
	override fun toString() = "Jack of $suit"
}

class Pip(suit: String, val number: Int): Card(suit) {
	init {
		if (number < 2 || number > 10) {
			throw RuntimeException("Pip has to be between 2 and 10")
		}
	}
}

fun process(card: Card) = when (card) {
	is Ace -> "${card.javaClass.name} of ${card.suit}"
	is King, is Queen, is Jack -> "$card"
	is Pip -> "${card.number} of ${card.suit}"
}

fun main() {
	println(process(Ace("Diamond")))
	println(process(Queen("Clubs")))
	println(process(Pip("Spades", 2)))
	println(process(Pip("Hearts", 6)))
}
```

上面 `when` 表达式中不应该编写 `else` 路径。如果在 `when` 中有一个用于 `sealed` 类的所有派生类型的路径，那么放置一个 `else` 将导致对永远不会使用的路径发出警告。

`sealed` 类的派生类可以有任意数量的实例。一个特殊的情况是枚举，它将每个子类的实例数量限制为一个。