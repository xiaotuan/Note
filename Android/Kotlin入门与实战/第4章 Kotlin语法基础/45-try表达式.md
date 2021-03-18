### 4.11.3　try表达式

try是一个表达式，它可以有返回值。代码如下。

```python
val a: Int? = try {  parseInt(input)  } catch (e: NumberFormatException) { null }
```

try表达式的返回值可能是try代码块中的最后一个或者catch代码块中的一个，finally代码块不会影响表达式的运行结果，可以省略。但需要注意的是，在try表达式中，catch或者finally代码块必须出现一个。

