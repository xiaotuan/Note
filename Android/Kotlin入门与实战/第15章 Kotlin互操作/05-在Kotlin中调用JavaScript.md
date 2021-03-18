### 15.2.1　在Kotlin中调用JavaScript

对于Java平台来说，Kotlin可以很轻松地实现与Java平台的互操作。JavaScript作为一种动态类型的编程语言，是不会在编译时检查系统类型的，但是它可以通过动态类型来实现与JavaScript的互操作。想要使用与Kotlin类型系统相关的内容，可以为JavaScript库创建Kotlin头文件。

#### 1．内联JavaScript

在JavaScript平台中，系统允许使用js("……")函数将一些JavaScript代码嵌入到Kotlin代码中。代码如下。

```python
fun jsTypeOf(o: Any): String {
     return js("typeof o")
}
```

而且js函数的参数必须是字符串常量，否则会报错。代码如下。

```python
fun jsTypeOf(o: Any): String {
     return js(getTypeof() + " o")   //此处编译报错
}
fun getTypeof() = "typeof"
```

#### 2．external修饰符

如果某个声明是用JavaScript编写的，则可以使用external修饰符来标记它。当Kotlin的编译器看到这样的声明时，它会假定相应类、函数或属性的实现由开发人员提供，因此不会从声明中生成任何与JavaScript相关的代码。

```python
external fun alert(message: Any?): Unit
external class Node {
    val firstChild: Node
    fun append(child: Node): Node
    fun removeChild(child: Node): Node
    //…
}
external val window: Window
```

需要注意的是，嵌套的声明会继承external修饰符，而且external修饰符只允许在包级声明中使用。即在上面代码的Node类中，不需要在成员函数和属性之前添加external修饰符。

#### 3．声明类静态成员

在JavaScript平台中，系统允许在原型或者类中定义成员。代码如下。

```python
function MyClass() {
  //函数体
}
MyClass.sharedMember = function() {  /*实现*/ };
MyClass.prototype.ownMember = function() { /*实现*/ };
```

然而，Kotlin提供了一种特殊的方式来处理external类的伴生对象：Kotlin假定伴生对象的成员就是该类自身的成员。以上例中的MyClass为例，可以这样写。

```python
external class MyClass {
     companion object {
        fun sharedMember()
    }
    fun ownMember()
}
```

#### 4．声明可选参数

外部函数可以含有可选参数，Kotlin实际上不知道JavaScript是如何设置参数的默认值的，因此在Kotlin中不可能使用通常的语法来声明这些默认参数。

```python
external fun myFunWithOptionalArgs(x: Int,
    y: String = definedExternally,
    z: Long = definedExternally)
```

myFunWithOptionalArgs函数是由一个必需参数和两个可选参数组成的函数，它的默认值由JavaScript代码计算后给出。

#### 5．扩展JavaScript类

在JavaScript平台中，开发者可以轻松地扩展JavaScript类，只需定义一个external类并在非external类中扩展它即可。

```python
external open class HTMLElement : Element() {
    /*成员函数或变量*/
}
//扩展类
class CustomElement : HTMLElement() {
    fun foo() {
        alert("bar")
    }
}
```

在扩展JavaScript类时，不允许外部类扩展非外部类。除此之外，还应注意以下两个使用限制。

+ 当一个外部基类的函数被签名重载时，不能在派生类中覆盖它。
+ 不能覆盖一个使用默认参数的函数。

#### 6．external接口

在面向对象语言中，可以使用关键字interface来定义接口，使用implement来实现接口。JavaScript虽然也是面向对象语言的，但它并没有接口的概念。对于静态类型的Kotlin来说，可以使用external来实现接口的作用。如果期望定义的函数参数支持方法，则传递含有这些方法的对象即可。代码如下。

```python
external interface HasFooAndBar {
    fun foo()
    fun bar()
}
external fun myFunction(p: HasFooAndBar)
```

external接口的另一个使用场景是描述设置对象。

```python
external interface JQueryAjaxSettings {
    var async: Boolean
    var cache: Boolean
    var complete: (JQueryXHR, String) -> Unit
    // …
}
fun JQueryAjaxSettings(): JQueryAjaxSettings = js("{}")
external class JQuery {
    companion object {
        fun get(settings: JQueryAjaxSettings): JQueryXHR
    }
}
fun sendQuery() {
     JQuery.get(JQueryAjaxSettings().apply {
        complete = { (xhr, data) ->
           window.alert("Request complete")
        }
    })
}
```

在Kotlin中调用JavaScript平台的外部接口时，需要注意以下几点限制。

+ 不能在is检查的右侧使用。
+ as可以转换为外部接口，但会在编译时产生警告。
+ JavaScript平台的external接口不能作为具体化类型参数传递。
+ 不能用在类的字面值表达式（I::class）中。

