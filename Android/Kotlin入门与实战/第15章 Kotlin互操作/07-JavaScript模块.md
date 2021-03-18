### 15.2.3　JavaScript模块

Kotlin允许将Kotlin项目编译为JavaScript模块系统，以下是可用选项列表。

+ 无模块（Plain），不为任何模块系统执行编译，在该选项下，访问模块的方式和普通的访问方式并无二致，默认使用该选项。
+ 异步模块定义（Asynchronous Module Definition，AMD），该选项常在require.js库中使用。
+ CommonJS约定广泛应用于node.js/npm，即module.exports对象和require函数中。
+ 通用模块定义（Unified Module Definition，UMD）与CommonJS、AMD相互兼容，而且在AMD和CommonJS都不可用时，它可以作为“plain”使用。

#### 1．选择目标模块系统

目标模块系统的选择方式取决于构建：IntelliJ IDEA方式、Maven方式和Gradle方式。

##### （1）在IntelliJ IDEA中

如果需要在IntelliJ IDEA **中** 选择模块系统，那么依次选择【File】→【Project Structure…】→【Modules】，然后找到对应的模块并选择其下的Kotlin facet，然后在Module kind字段中选择合适的模块系统。

如果是为整个项目选择模块系统，那么依次选择【File】→【Settings】→【Build, Execution, Deployment】→【Compiler】→【Kotlin compiler】，然后在 Module kind字段中选择合适的模块系统。

##### （2）在Maven中

如果需要在Maven构建的项目中选择模块系统，则可以设置moduleKind配置属性。代码如下。

```python
<plugin>
    <artifactId>kotlin-maven-plugin</artifactId>
    <groupId>org.jetbrains.kotlin</groupId>
    <version>${kotlin.version}</version>
    <executions>
        <execution>
            <id>compile</id>
            <goals>
                <goal>js</goal>
            </goals>
        </execution>
    </executions>
    <!-- 此处插入开始-->
    <configuration>
        <moduleKind>commonjs</moduleKind>
    </configuration>
    <!-- 插入文本结束 -->
</plugin>
```

moduleKind配置属性的可用值包括plain、amd、commonjs和umd。

##### （3）在Gradle中

如果需要在Gradle构建的项目中选择编译时的模块系统，可以设置moduleKind配置属性，该属性的可用值和Maven一样。代码如下。

```python
compileKotlin2Js.kotlinOptions.moduleKind = "commonjs"
```

#### 2．@JsModule注解

要让Kotlin知道一个external类、包、函数或者属性是JavaScript模块，可以使用@JsModule注解。例如，有一个CommonJS模块如下。

```python
module.exports.sayHello = function(name) { alert("Hello, " + name); }
```

要告诉Kotlin，上面的函数是一个JavaScript模块，可以使用@JsModule注解进行声明。

```python
@JsModule("hello")
external fun sayHello(name: String)
```

#### 3．@JsModule注解应用到包

有时候需要从一些JavaScript库中导出包，而不是函数和类。从JavaScript的角度来讲，导出的包可以理解为是一个具有成员的对象。这些成员可以是类、函数和属性。将这些包作为Kotlin对象进行导入通常是不便于理解的，可以使用特殊的助记符将导入的JavaScript包映射到Kotlin包。

```python
@file:JsModule("extModule")
package ext.jspackage.name
external fun foo()
external class C
```

对应的JavaScript模块的声明如下。

```python
module.exports = {
    foo:  {  /*函数体*/ },
    C:  { /*函数体*/ }
}
```

但是，标有@file:JsModule注解的文件无法声明非外部成员。

```python
@file:JsModule("extModule")
package ext.jspackage.name
external fun foo()
fun bar() = "!" + foo() + "!"   //此处编译报错
```

#### 4．更深的包层次结构

JavaScript模块既可以导出单个包，也可以导出多个包。Kotlin虽然也支持这种场景，但必须为每个导入的包声明一个新的.kt文件。代码如下。

```python
module.exports = {
    mylib: {
        pkg1: {
            foo: function() {  /*代码*/  },
            bar: function() {  /*代码*/  }
        },
        pkg2: {
            baz: function() {  /*代码*/  }
        }
    }
}
```

要在Kotlin中导入该模块，就必须编写两个Kotlin源文件，第一段代码如下。

```python
@file:JsModule("extModule")
@file:JsQualifier("mylib.pkg1")
package extlib.pkg1
external fun foo()
external fun bar()
```

另一段代码如下。

```python
@file:JsModule("extModule")
@file:JsQualifier("mylib.pkg2")
package extlib.pkg2
external fun baz()
```

#### 5．@JsNonModule注解

使用@JsModule注解声明JavaScript模块，如果没有把它编译到JavaScript模块中，则此时不能在Kotlin代码中使用该模块。通常，开发人员既可以将库作为JavaScript模块来使用，也可以作为可下载的 .js文件进行分发，将这些文件复制到项目的静态资源文件中并通过<script>元素进行包含。要告诉Kotlin，可以在非模块环境中使用@JsModule声明和@JsNonModule声明。

```python
function topLevelSayHello(name) { alert("Hello, " + name); }
if (module && module.exports) {
     module.exports = topLevelSayHello;
}
```

在Kotlin中，可以在非模块环境中使用一个@JsModule声明，在模块环境中使用@JsNonModule声明。

```python
@JsModule("hello")
@JsNonModule
@JsName("topLevelSayHello")
external fun sayHello(name: String)
```

