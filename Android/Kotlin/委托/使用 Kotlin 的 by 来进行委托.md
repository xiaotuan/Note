`Kotlin` 通过 `by` 来进行委托的最简单用法如下：

```kotlin
interface Worker {
	fun work()
	fun takeVacation()
}

class JavaProgrammer : Worker {
	override fun work() = println("...write Java...")
	override fun takeVacation() = println("...code at the beach...")
}

class CSharpProgrammer : Worker {
	override fun work() = println("...write C#...")
	override fun takeVacation() = println("...branch at the ranch...")
}

class Manager() : Worker by JavaProgrammer()

fun main() {
	val doe = Manager()
	doe.work()	// ...write Java...
}
```

这个版本的 `Manager` 自己没有任何方法，至少在编写代码时没有。它通过 `JavaProgrammer` 实现 `Worker` 接口。看到 `by` 关键字后，`Kotlin` 编译器将在字节码层面上实现 `Manager` 类中属于 `Worker` 的方法，并将调用路由到 `by` 关键期之后所提供的 `JavaProgrammer` 实例。

`Kotlin` 要求 `by` 的左边是一个接口。右边是该接口的实现方。

这种委托方式与继承有一些区别：

首先，类 `Manager` 不是从 `JavaProgrammer` 继承的，因此下面的操作会导致失败：

```kotlin
val coder: JavaProgrammer = doe	// ERROR: type mismatch
```

其次，在继承解决方案中，对 `work()` 等方法的调用不是在 `Manager` 中实现的。相反，它们被发送到基类。在 `Kotlin` 委托的情况下，编译器在 `Manager` 类内部创建方法并执行路由。实际上，当调用 `doe.work()` 时，我们正在调用 `Manager` 类中不可见的方法 `work()`。