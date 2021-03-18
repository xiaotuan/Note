### 2.2.2　JVM新特性

在Java 1.7和1.8版本中，JVM引入了很多新的功能和概念，Kotlin也在第一时间对这些功能提供了支持。

#### 1．提供Java 8字节码支持

在不改变字节码语义的情况下，使用命令行选项“-jvm-target 1.8”，可以将Kotlin编译生成Java 8字节码。

#### 2．Java 8标准库支持

在此版本中，Kotlin新增了全面支持 Java 7和Java 8标准库的独立版本，如果想要访问这些新的API，可以使用kotlin-stdlib-jre7或kotlin-stdlib-jre8 的Maven构件，而不是使用标准的 kotlin-stdlib。

#### 3．字节码中的参数名

现在，Kotlin支持在字节码中存储参数名，如果要使用这个功能，可以通过命令行选项-java-parameters来开启。

#### 4．可变闭包变量

在Lambda表达式中，捕获可变闭包变量的装箱类不再需要volatile字段，虽然可变闭包变量可以提高性能，但在一些罕见的情况下可能会导致新的竞争条件，在这种情况下，可以使用同步机制来访问变量。

#### 5．javax.script支持

Kotlin集成了javax.script 的相关API，该API允许在运行时进行赋值操作。下面是示例代码。

```python
val engine = ScriptEngineManager().getEngineByExtension("kts")!!
engine.eval("val x = 3")
println(engine.eval("x + 2"))  // 输出结果为 5
```

#### 6．kotlin.reflect.full

为了在以后的版本中支持Java 9，kotlin-reflect.jar库中的扩展函数和属性已移动到 kotlin.reflect.full 包中，旧的kotlin.reflect中的内容将在1.2版本中被弃用。

