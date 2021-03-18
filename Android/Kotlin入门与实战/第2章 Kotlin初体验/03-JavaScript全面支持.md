### 2.2.1　JavaScript全面支持

从Kotlin 1.1版本开始，JavaScript不再被当作是实验性的目标平台， Kotlin开始全面支持前端开发环境，从以下几点可以体现。

#### 1．统一的标准库

目前，Kotlin标准库的大部分代码都可以编译成JavaScript来使用，一些关键类和方法都可以在Kotlin依赖包中找到，如集合（ArrayList、HashMap）、异常（IllegalArgumentException）和其他关键类（StringBuilder、Comparator）。

#### 2．external修饰符

如果想要以类型安全的方式在Kotlin中访问JavaScript的实现类，可以使用 external 修饰符来声明Kotlin。与JVM目标平台不同，JavaScript平台允许对类和属性使用external修饰符，这是Kotlin对JavaScript平台提供的特有功能。使用external修饰符声明一个Kotlin的代码如下。

```python
external class Node { 
val firstChild: Node
fun appendChild(child: Node): Node 
fun removeChild(child: Node): Node 
 … //其他
}
```

#### 3．改进的导入操作

Kotlin优化了JavaScript模块的导入方式，可以通过在外部声明上添加@JsModule（模块名）注解来导入声明，该注解会在编译期间将模块导入到模块系统中。例如，要想在CommonJS中将声明作为模块或者全局的JavaScript对象导入，可以使用@JsNonModule 注解。下面是将JQuery声明导入Kotlin模块的相关代码。

```python
external interface JQuery {
   fun toggle(duration: Int = definedExternally): JQuery
   fun click(handler: (Event) -> Unit): JQuery
}
@JsModule("jquery")
@JsNonModule
@JsName("$")
external fun jquery(selector: String): JQuery
```

在这种情况下，Kotlin的JQuery模块被注解声明为jquery ，如果要在其他程序中使用Kotlin的JQuery模块，可以使用jquery 的模块导入。示例代码如下。

```python
fun main(args: Array<String>) {
    jquery(".toggle-button").click {
        jquery(".toggle-panel").toggle(300)
    }
}
```

