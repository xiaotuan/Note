### 11.4.1　Lambda表达式语法

在完整的Lambda表达式语法格式中，Lambda表达式总是被包含在大括号之内，参数声明在大括号内并有可选的类型标注，函数体放在“->”符号之后。如果Lambda表达式的返回类型不是Unit，那么将Lambda表达式函数体内的最后一个（也可能是单个）表达式作为其返回值。

Lambda表达式的完整语法格式如下。

```python
val sum = { x: Int, y: Int -> x + y }
```

如果保留所有可选标注的形式，那么可以改写为如下的格式。

```python
val sum: (Int, Int) -> Int = { x, y -> x + y }
```

当Lambda表达式只有一个参数时，如果Kotlin能够自行推断出Lambda表达式的参数含义，那么可以不声明唯一的参数，因为Kotlin会隐含地声明一个名为it的参数。

```python
val ints= setOf("Kotlin","Java","Scale")
ints.filter { it.equals("Kotlin") }
```

除此之外，如果使用带有标签限定的return语法，那么可以从Lambda表达式中显式返回一个结果值，否则隐式返回最后一个表达式的值。

```python
val ints= setOf("Kotlin","Java","Scale")
    ints.filter {
        val shouldFilter = it.equals("Kotlin")
        shouldFilter
    }
    //等价于
    ints.filter {
        val shouldFilter = it.equals("Kotlin")
        return@filter shouldFilter
    }
```

如果一个函数接收另一个函数作为最后一个参数，则Lambda表达式参数可以被放在括号参数列表之外进行传递。

