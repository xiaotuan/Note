### 15.2.4　JavaScript反射

目前，JavaScript环境不支持完整的Kotlin反射API，唯一支持该API的是::class语法。它允许开发人员引用一个实例类或者与给定类型相对应的类。一个::class表达式的值，就是一个支持simpleName和isInstance成员的精简版KClass实现。

除此之外，使用KClass.js可以访问与JsClass类对应的实例。该实例本身就是对构造函数的引用，该特性可以用于与构造函数引用的JavaScript函数进行互操作。

```python
class A
class B
class C
inline fun <reified T> foo() {
      println(T::class.simpleName)
}
val a = A()
println(a::class.simpleName)     //获取一个实例的类；输出"A"
println(B::class.simpleName)     //获取一个类型的类；输出"B"
println(B::class.js.name)        //输出"B"
foo<C>()                         //输出"C"
```

