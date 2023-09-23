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

在上面的示例中， `Manager` 可以将调用委托给 `JavaProgrammer` 实例，但是对 `Manager` 的引用不能分配给对 `JavaProgrammer` 的引用——也就是说，`Manager` 可以使用 `JavaProgrammer`，但 `Manager` 不能作为 `JavaProgrammer`。换句话说，`Manager` 有一个 `JavaProgrammer`，但它不是 `JavaProgrammer` 的一种。

`Kotlin` 实现委托的方式有一个小的问题。委托类实现了委托接口，因此对委托的引用可以分配给对委托接口的一个引用。同样，对委托类的一个引用也可以传递给一个需要委托接口的方法。换句话说，例如，以下是无效的：

```kotlin
val coder: JavaProgrammer = doe	// ERROR: type mismatch
```

但以下在 `Kotlin` 中是可以的：

```kotlin
val employee: Worker = doe
```

另外，在委托给属性时要谨慎。我们使用 `val` 向`Manager` 的构造函数传递了一个 `Worker` 类型的参数。如果我们决定将用作委托的属性从 `val` 改为 `var`，那么会产生一些后果。让我们举个例子来看看这些是什么：

```kotlin
interface Worker {
	fun work()
	fun takeVacation()
	fun fileTimeSheet() = println("Why? Really?")
}

class JavaProgrammer : Worker {
	override fun work() = println("...write Java...")
	override fun takeVacation() = println("...code at the beach...")
}

class CSharpProgrammer : Worker {
	override fun work() = println("...write C#...")
	override fun takeVacation() = println("...branch at the ranch...")
}

class Manager(var staff: Worker) : Worker by staff

fun main() {
	val doe = Manager(JavaProgrammer())
	
	println("Staff is ${doe.staff.javaClass.simpleName}")
	doe.work()
	
	println("changing staff")
	doe.staff = CSharpProgrammer()
	println("Staff is ${doe.staff.javaClass.simpleName}")
	doe.work()
}
```

`class Manager(var staff: Worker) : Worker by staff` 声明实际上是接受一个名为 `staff` 的参数并将其分配给一个名为 `staff` 的成员，就像这样：`this.staff = staff`。因此，对给定对象有两个引用：一个是在类内部作为幕后字段保存的，另一个是为委托保存的。但是，我们将属性变为 `CSharpProgrammer` 的一个实例时，只修改了字段，而没有修改对委托的引用。因此，输出如下：

```
Staff is JavaProgrammer
...write Java...
changing staff
Staff is CSharpProgrammer
...write Java...
```

另一个问题是我们刚刚使用的代码。当我们用 `CSharpProgrammer` 的一个实例替换 `staff` 时，最初附着的 `JavaProgrammer` 实例不再作为其属性附着到对象上。但它不能被垃圾回收，因为委托持有它。因此委托的生命周期与对象的生命周期相同，尽管属性可能会在此过程中时有时无。