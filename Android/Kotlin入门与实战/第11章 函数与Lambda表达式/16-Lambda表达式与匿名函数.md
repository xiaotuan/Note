### 11.4　Lambda表达式与匿名函数

Lambda表达式本质上是一个匿名函数，它是一种“函数字面值”，即一个没有声明的函数，可以把该函数当作普通表达式进行参数传递。Lambda表达式基于数学中的λ演算而得名，它可以访问自己的闭包函数。

```python
max(strings, { a, b -> a.length < b.length })
```

max是一个高阶函数，它接受一个函数作为函数的第二个参数。在这当中，第二个参数是一个Lambda表达式，而它本身又是一个函数，如果用传统函数实现，等价于下面的代码。

```python
fun compare(a: String, b: String): Boolean = a.length < b.length
```

