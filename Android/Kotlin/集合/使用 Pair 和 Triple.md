元组是小的、有限大小的对象序列。`Kotlin` 提供了两种特定类型：`Pair` 用于大小为 2 的元组，`Triple` 用于大小为 3 的元组。

下面是一个创建字符串 `Pair` 的例子：

```kotlin
println(Pair("Tom", "Jerry"))	// (Tom, Jerry)
println(mapOf("Tom" to "Cat", "Jerry" to "Mouse"))	// {Tom=Cat, Jerry=Mouse}
```

使用 `to()` 扩展函数（对 `Kotlin` 中的任何对象都可以使用）为映射创建一对条目。`to()` 方法创建 `Pair` 的实例，目标值作为 `Pair` 中的第一个值，参数作为 `Pair` 中的第二个值。

为了了解 `Pair` 的好处，让我们创建一个示例来收集不同机场代码的温度值：

```kotlin
package com.qty.test

import kotlin.random.Random
import java.text.DecimalFormat

fun main() {
	val airportCodes = listOf("LAX", "SFO", "POX", "SEA")
	
	val temperatures = airportCodes.map { code -> code to getTemperatureAtAirport(code) }
	
	for (temp in temperatures) {
		println("Airport: ${temp.first}, Temperature: ${temp.second}")
	}
}

fun getTemperatureAtAirport(code: String) = "${Math.round(Math.random() * 30) + code.count()} ℃"
```

我们使用函数式风格的 `map()` 迭代器遍历集合 `airportCodes`，将列表中的每个机场代码转换为 `(code, temperature)` 对。

`Pair` 和 `Triple` 都是不可变的，并且分别用于创建由两个和三个值组成的分组。如果需要对三个以上不可变值进行分组，那么考虑创建一个数据类。
