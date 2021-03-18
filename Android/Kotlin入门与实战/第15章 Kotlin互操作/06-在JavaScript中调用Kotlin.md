### 15.2.2　在JavaScript中调用Kotlin

在JavaScript平台中，Kotlin代码会被Kotlin编译器编译成JavaScript类、函数或属性，因此在JavaScript代码中可以自由地调用Kotlin的函数和属性。

#### 1．独立的JavaScript隔离声明

为了防止损坏全局对象，Kotlin创建了一个包含当前模块中所有Kotlin声明的模块（module）对象。如果Kotlin的模块名是myModule，那么在JavaScript中可以通过myModule对象来使用JavaScript声明。代码如下。

```python
fun foo() = "Hello"  // Kotlin模块名是myModule
```

然后，可以在JavaScript中调用Kotlin的模块名。代码如下。

```python
alert(myModule.foo());  //在JavaScript中调用Kotlin模块myModule
```

当把Kotlin模块编译为JavaScript模块时，直接使用上面的方式进行调用是不合适的。在此种情况下，Kotlin不会创建模块对象，而是将Kotlin声明对象作为相应类型的JavaScript模块对外暴露，此时，myModule作为Kotlin模块，会被编译为JavaScript模块。

```python
alert(require('myModule').foo());
```

#### 2．包结构

Kotlin将其包结构暴露给JavaScript，除非在根包中定义声明，否则必须在 JavaScript中使用完整的名称。代码如下。

```python
package my.qualified.packagename
fun foo() = "Hello"
```

在JavaScript中调用foo()时，需要使用完整的包结构名称。

```python
alert(myModule.my.qualified.packagename.foo());
```

#### 3．@JsName注解

在某些情况下（如重载操作），Kotlin编译器会使用代码修饰JavaScript生成的函数和属性的名称，要控制生成的名称，需要使用@JsName注解。代码如下。

```python
// Kotlin模块kjs
class Person(val name: String) {
      fun hello() {
          println("Hello $name!")
      }
    @JsName("helloWithGreeting")
    fun hello(greeting: String) {
         println("$greeting $name!")
    }
}
```

在JavaScript中可以按照下面的方式来调用Person类。

```python
var person = new kjs.Person("Dmitry");   //引用模块kjs
person.hello();                          //输出Hello Dmitry!
person.helloWithGreeting("Servus");      //输出Servus Dmitry!
```

如果没有指定@JsName注解，则相应函数的名称会包含由函数签名计算而来的后缀，例如hello_61zpoe$。@JsName注解参数往往需要一个常量字符串字面值，该字面值是一个标识符。

需要注意的是，在external声明类和方法中不能使用@JsName注解。除此之外，从外部类继承的非外部类也是不能使用@JsName注解的。

#### 4．在JavaScript中表示Kotlin类型

除了kotlin.Long的Kotlin数字类型映射到JavaScript的Number之外，还有一些常见的映射关系需要注意。

+ kotlin.Char映射到JavaScript 的Number类型来表示字符代码。
+ Kotlin在运行时无法区分数字类型（kotlin.Long除外），因此下面的代码是能够正常工作的。

```python
fun f() {
     val x: Int = 23
     val y: Any = x
     println(y as Float)
}
```

+ Kotlin保留了kotlin.Int、kotlin.Byte、kotlin.Short、kotlin.Char和kotlin.Long的溢出语义。
+ 由于JavaScript中设有64位整数，因此kotlin.Long不可以映射到任何JavaScript对象中，它是由一个Kotlin类模拟的。
+ kotlin.String映射到JavaScript的String中。
+ kotlin.Any映射到JavaScript的Object中（new Object()、{}等）。
+ kotlin.Array映射到JavaScript 的Array中。
+ Kotlin集合（List、Set、Map等）无对应的JavaScript类型映射。
+ kotlin.Throwable 映射到JavaScript 的Error中。
+ Kotlin在JavaScript中保留了惰性对象初始化。
+ Kotlin不会在JavaScript中实现顶层属性的惰性初始化。

自Kotlin 1.1.50版本开始，将Kotlin原生数组转换到JavaScript时采用TypedArray。

+ kotlin.ByteArray、kotlin.ShortArray、kotlin.IntArray、kotlin.DoubleArra和kotlin.FloatArray会映射成JavaScript的Int8Array、Int16Array、 Int32Array、Float32Array和Float64Array。
+ kotlin.BooleanArray会映射成JavaScript中具有$type$ == "BooleanArray"属性的Int8Array。
+ kotlin.CharArray会映射成JavaScript中具有$type$ == "CharArray"属性的 UInt16Array。
+ kotlin.LongArray会映射成JavaScript中具有$type$ == "LongArray"属性的 kotlin.Long类型数组。

