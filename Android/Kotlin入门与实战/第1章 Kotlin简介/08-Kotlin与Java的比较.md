### 1.5　Kotlin 与 Java 的比较

作为面向对象编程时代的明星编程语言，Java 在开放的生态环境下，赢得了 Oracle、Google、Apache、Eclipse 基金会等各大厂商的支持，这些厂商的支持加快了 Java 生态圈的建设。一时间 Java 的生态圈异常繁荣，各种优秀的开源框架层出不穷，较为著名的有 Spring Boot、Spring Cloud、Hadoop、Spark 和 Kafka 等。

虽然 Java 的生态圈异常强大，但是作为纯命令式语言时代的产物，Java 和当前流行的函数式编程语言相比，在类型、语法与编程范式方面显得越来越落后。所以，寻找一种既可以突破 Java 的这些局限，又可以与 Java 和谐共处的语言成为软件行业努力的方向。不过庆幸的是，Java 之父詹姆斯·高斯林在创造 Java 语言时就想到了这些问题，所以在设计之初，就有意将 Java 语言与运行时环境 JVM 进行分离。JVM 负责与操作系统的交互，屏蔽了具体操作系统的细节，这使得基于 JVM 开发的系统可以运行在任何操作系统之上。如今众多的新兴语言都运行在 JVM上，Groovy、Scala、Kotlin、Clojure 算得上是其中的佼佼者。

那么，Kotlin 相比 Java 有哪些优势呢？

+ 更容易学习：Kotlin 是一门具备函数式编程思想的面向对象编程语言，它具有静态编程语言的很多特点，更加容易学习。
+ 更快的编译速度：第一次编译 Kotlin 代码时，它需要比 Java 更长的时间，当使用增量编译的时候，Kotlin 则比 Java 更快。
+ 性能：由于有着非常相似的字节码结构，因此 Kotlin 应用程序的运行速度与 Java 类似。随着 Kotlin 对内联函数的支持，使用Lambda 表达式的代码通常比用 Java 写的代码运行得更快。
+ 空指针安全：Kotlin 对比于 Java 的一个优点就是可以有效解决空指针问题，毕竟“价值十亿美元的错误”不是人人都犯得起的。
+ 跨平台特性：Kotlin 除了可以用来开发移动 Android App 之外，还可以用来进行服务端框架开发和 Web 浏览器开发。
+ 与 IDE 无缝融合：在 Google 官方发布的 Android Studio 3.0 上，已经默认集成了 Kotlin，对于一些老版本，也可以通过插件的方式来集成 Kotlin。所以，使用 JetBrains 提供的 IDE，可以为 Kotlin 开发提供较好的环境支持。

当然，除了上面提到的一些优势之外，Kotlin 还具有很多现代静态编程语言的编程特点，如类型推断、多范式支持、可空性表达、扩展函数、DSL 支持等，而这些功能 Java 在最近的版本才陆续添加。

另外，对于 Android 开发来说，Kotlin 还提供了 Kotlin Android 扩展和 Anko 库。其中，Kotlin Android 扩展是编译器扩展，可以让开发者摆脱代码中繁杂的 findViewById() 调用并将其替换为合成的编译器生成的属性。Anko 是 JetBrains 开发的围绕 Android API 的包装器库，目的是替代传统 XML 方式构建 UI 布局。

