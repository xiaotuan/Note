### 15.1.2　在Java中调用Kotlin

因为Kotlin能够和Java完全兼容，所以在Java中可以很轻松地调用Kotlin。

#### 1．属性

当在Java中调用Kotlin的属性时，该属性会被编译成Java元素。

+ getter方法：通过在其名称前加get得到。
+ setter方法：通过在其名称前加set得到（只适用于var属性）。
+ 私有字段：与属性名称相同（仅适用于具有幕后字段的属性）。

例如，将Kotlin变量编译成Java中的变量声明。代码如下。

```python
//Kotlin变量
var name:String
//编译成对应的Java变量声明
private String name;
public String getName() {
    return name;
}
public void setName(String name) {
    this. name = name;
}
```

如果属性名称以is开头，则使用如下的名称映射规则：getter的名称与属性名称相同，而且setter的名称是通过将is替换成set获得的。例如，对于属性名isOpen，其getter会映射为isOpen()，而其setter则映射为setOpen()。这一规则适用于任何类型属性，并不仅限于Boolean类型。

#### 2．包级函数

假设在demo包内定义一个example.kt文件，并在文件中声明一个函数和属性。

```python
//example.kt文件
package demo
class Foo
fun bar() {
    //函数体
}
```

那么在Java中调用该Kotlin的属性或方法时，Kotlin代码都编译成了一个名为demo.ExampleKt的Java类的静态方法或属性。

```python
//Java调用
public static void main(String[]args){
        new demo.Foo();
        ExampleKt.bar();
}
```

当然，可以使用@JvmName注解来修改生成的Java类的类名。代码如下。

```python
@file:JvmName("JvmDemo")
package org.demo
fun bar(){
     println("这是一个方法")
}
```

然后在Java代码中调用前面的bar()。代码如下。

```python
org.demo.JvmDemo.bar();    //@JvmName注解类名.方法名
```

如果在同一个包中，则多个文件生成相同的Java类名（包名相同并且类名相同或者有相同的@JvmName注解）是不被允许的。然而，编译器能够生成一个唯一的Java外观类，它具有指定的名称且包含所有文件中的相关声明。要生成这样的外观，需要在相关文件中使用@JvmMultifileClass注解。

```python
@file:JvmName("JvmDemo")
@file:JvmMultifileClass
package org.demo
```

#### 3．实例字段

如果需要在Java中将Kotlin属性作为字段暴露出来，则可以使用@JvmField注解对其进行标注，使用注解标注的字段将具有与底层属性相同的可见性。如果一个属性含有幕后字段（Backing Field）、非私有或者const修饰符等，而且它不是被委托的，那么可以使用@JvmField注解该属性。

```python
class C(id: String) {
    @JvmField val ID = id
   }
```

在Java中调用该属性时，可以直接使用@JvmField注解暴露出来的字段。

```python
class JavaClient {
      public String getID(C c) {
          return c.ID;
    }
}
```

延迟初始化的属性也可以暴露为字段，暴露后字段的可见性与lateinit属性的setter相同。

在命名对象或伴生对象中声明Kotlin属性时，会在该命名对象或包含伴生对象的类中生成静态幕后字段。通常这些字段是私有的，但可以通过以下几种方式暴露出来。

+ 使用@JvmField注解。
+ 使用lateinit修饰符。
+ 使用const修饰符。

#### 4．静态方法

Kotlin允许将包级函数表示成静态方法。如果对这些函数使用@JvmStatic进行标注，那么可以为命名对象或伴生对象中定义的函数生成静态方法。使用该注解时，编译器既会在相应对象的类中生成静态方法，也会在对象自身中生成实例方法。代码如下。

```python
class StaticC {
      companion object {
        @JvmStatic fun foo() {}
        fun bar() {}
    }
}
```

现在，对于Java来说，foo()是静态的，而bar()不是静态的。

```python
//在Java中调用Kotlin静态方法
StaticC.foo();   //编译正确
StaticC.bar();   //编译错误，不是一个静态方法
StaticC.Companion.foo();  //保留实例方法
StaticC.Companion.bar();  //唯一的工作方式
```

当然，对于命名对象来说，@JvmStatic的使用也是一样的。

```python
object Obj {
    @JvmStatic fun foo() {}
    fun bar() {}
}
```

然后在Java中调用该静态对象。

```python
Obj.foo();       //编译正确
Obj.bar();       //编译错误
Obj.INSTANCE.bar();    //编译正确，通过单例实例调用
Obj.INSTANCE.foo();    //编译正确
```

除此之外，@JvmStatic注解也可以被应用于对象或伴生对象的属性中，使该对象或包含该伴生对象的类中的成员是静态的。

#### 5．可见性

Kotlin的可见性可以通过下列方式映射到Java中。

+ private成员被编译成Java的private成员，private顶层声明被编译成Java包级局部声明。
+ protected保持不变（注意，Java允许访问同一个包中其他类的受保护成员而Kotlin不能，因此Java类可以访问更广泛的代码）。
+ public保持不变。
+ internal声明被编译为Java中public、internal类的成员时会由于修饰名字而更难以在Java中使用，而且根据Kotlin的语法规则，允许重载签名相同的成员并令它们互不可见。

#### 6．空安全

在Java中调用Kotlin函数时，没有任何方法可以阻止Kotlin中的空值传入，这有可能造成NullPointerException。Kotlin在JVM虚拟机中运行时会检查所有的公共函数，可以检查非空值，这时通过NullPointerException能得到Java中的非空值代码。

#### 7．生成重载

通常，在一个带有默认参数值的Kotlin函数中，只会包含一个在Java中可见的所有参数都存在的完整参数签名方法。如果希望向Java调用者暴露多个重载函数，则可以使用@JvmOverloads注解进行声明。同时，该注解可以用于构造函数和静态方法，但它不能用于抽象方法，包括在接口中定义的方法。

```python
class Foo @JvmOverloads constructor(x: Int, y: Double = 0.0) {
      @JvmOverloads fun f(a: String, b: Int = 0, c: String = "abc") {
        //函数体
    }
}
```

对于每一个包含默认值的参数来说，系统都会生成一个额外的重载函数，这个重载函数会移除参数和它右边的所有参数。对于上面的例子，会生成以下代码。

```python
// 构造函数
Foo(int x, double y)
Foo(int x)
// 方法
void f(String a, int b, String c) { }
void f(String a, int b) { }
void f(String a) { }
```

值得注意的是，如此构造函数中所述，如果一个类的所有构造函数参数都有默认值，那么会生成一个公有的无参构造函数。

#### 8．受检异常

Kotlin没有受检异常，也就是说，Kotlin函数没有Java语法中的声明抛出异常。代码如下。

```python
fun foo() {
     throw IOException()
}
```

想在Java中调用上面的Kotlin函数，需要捕捉IOException异常。

```python
try {
  demo.Example.foo();
}
catch (IOException e) {   //编译错误：foo()未在Throws列表中声明IOException
  // …
}
```

但是如果直接在Java代码中捕捉IOException异常，Java编译器是会报错的，因为foo()并没有声明IOException异常。为了解决这个问题，需要在 Kotlin的异常方法上使用@Throws注解。

```python
@Throws(IOException::class)
fun foo() {
     throw IOException()
}
```

#### 9．型变的泛型

当在Kotlin类中使用声明处型变时，可以通过两种方式从Java代码中看到它们的用法。假设有以下的类和函数。

```python
class Box<out T>(val value: T)
interface Base
class Derived : Base
fun boxDerived(value: Derived): Box<Derived> = Box(value)
fun unboxBase(box: Box<Base>): Base = box.value
```

将上面代码中的两个函数转换成Java代码。代码如下。

```python
Box<Derived> boxDerived(Derived value) { … } 
Base unboxBase(Box<Base> box) { … }
```

上面的Java代码，如果直接使用“unboxBase(boxDerived(“s”))”来调用，对于Kotlin来说是可以的，但对于Java是行不通的。因为在Java中Box类在其泛型参数T上是不型变的。要使其在Java中正常工作，需要按以下方式定义unboxBase。

```python
Base unboxBase(Box<? extends Base> box) { … }
```

此处使用Java的通配符类型（? extends Base）来模拟声明处型变，因为在Java中，只有声明了具体类型的通配符才能使用。因此，上面示例中的函数实际上可以翻译为以下格式。

```python
//作为返回类型（没有通配符）
Box<Derived> boxDerived(Derived value) { … }
//作为参数（有通配符）
Base unboxBase(Box<? extends Base> box) { … }
```

但是，当参数类型是final时，生成通配符通常没有意义。如果希望在默认不生成通配符的地方生成通配符，那么可以使用@JvmWildcard注解。

```python
fun boxDerived(value: Derived): Box<@JvmWildcard Derived> = Box(value)
//将被转换成Box<? extends Derived> boxDerived(Derived value) { … }
```

另外，如果不需要默认的通配符转换，则可以使用@JvmSuppressWildcards注解。代码如下。

```python
fun unboxBase(box: Box<@JvmSuppressWildcards Base>): Base = box.value
//将转换成Base unboxBase(Box<Base> box) { … }
```

@JvmSuppressWildcards注解不仅可以用于单个类型的参数，还可用于整个声明（如函数或类），从而抑制范围内的所有通配符。

#### 10．Nothing类型

Nothing是特殊的，因为它在Java中找不到对应的类型。在Java中，每个Java引用类型，包括java.lang.void，都可以接受null值，但是Nothing不行。因此，这种类型不能在Java中准确表示。这也是在Kotlin中使用Nothing类型参数时，Kotlin会将它转换成一个原始类型的原因。

```python
fun emptyList(): List<Nothing> = listOf()
//会转换成 List emptyList() { … }
```

#### 11．KClass类型

当调用含有KClass类型参数的Kotlin方法时，因为没有从Class到KClass的自动转换，所以必须通过调用Class<T>.kotlin扩展属性的等价形式来进行手动转换。代码如下。

```python
kotlin.jvm.JvmClassMappingKt.getKotlinClass(MainView.class)
```

