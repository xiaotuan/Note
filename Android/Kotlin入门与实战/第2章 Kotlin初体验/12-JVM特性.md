### 2.3.5　JVM特性

#### 1．构造函数调用标准化

自1.0版本开始，Kotlin就支持复杂控制流表达式，例如try-catch表达式和内联函数调用，这也符合Java的虚拟机规范。不幸的是，当构造函数调用的参数中存在try-catch表达式时，字节码处理工具并不能很好地处理这些代码，从而造成一些编译上的错误。

为了减少字节码处理工具带来的问题，Kotlin为开发者提供了一个命令行选项（-Xnormalize-constructor-calls=MODE），此选项会告诉编译器为这样的结构生成更多的Java辅助字节码，其中，MODE的值有以下几种。

+ disable：默认值，采用与Kotlin 1.0和1.1版本相同的方式生成字节码。
+ enable：为构造函数调用生成类Java字节码，从而改变类加载和初始化的顺序。
+ preserve-class-initialization：为构造函数调用生成Java字节码，以保持类的初始化顺序。这可能会影响应用程序的整体性能，仅在多个类之间共享一些复杂的状态，并在类初始化更新时才使用此属性。

#### 2．Java默认方法调用

在Kotlin 1.2版本之前，接口成员在使用JVM 1.6版本重写Java默认方法时会在父调用中产生警告：“Super calls to Java default methods are deprecated in JVM target 1.6. Recompile with '-jvm-target 1.8'”。在Kotlin 1.2中，调用默认方法时将会报错，因此需要使用JVM 1.8来编译这些代码。

#### 3．x.equals(null)一致行为

Kotlin 1.2版本之前，在映射到Java原语的平台类型上调用“x.equals(null)”时，如果x为null，则不会正确地返回true或false。从Kotlin 1.2版本开始，如果在平台类型的空值上直接调用“x.equals(...)”，则会抛出NPE异常；但调用“x == ...”并不会产生异常。

如果要使用Kotlin 1.2版本之前的行为，可以在配置脚本中将“-Xno-exception-on- explicit-equals-for-boxed-null”标志传递给编译器。

#### 4．内联扩展接收器修复null转义

在平台类型空值上调用内联扩展函数时并没有检查接收器是否为null，这也就意味着允许null转义到其他代码中，而这往往会造成空指针异常。Kotlin 1.2版本修复了这一问题，在调用点强制执行空检查时，如果接收方为空，则抛出异常。

如果要切换到旧版本，请将fallback标志“-Xno-receiver-assertions”传递给编译器。

