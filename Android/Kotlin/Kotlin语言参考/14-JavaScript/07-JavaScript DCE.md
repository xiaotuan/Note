[toc]

[搭建项目](https://www.kotlincn.net/docs/reference/js-project-setup.html)

[动态类型](https://www.kotlincn.net/docs/reference/dynamic-type.html)

[Kotlin 中调用 JavaScript](https://www.kotlincn.net/docs/reference/js-interop.html)

[JavaScript 中调用 Kotlin](https://www.kotlincn.net/docs/reference/js-to-kotlin-interop.html)

[JavaScript 模块](https://www.kotlincn.net/docs/reference/js-modules.html)

[JavaScript 反射](https://www.kotlincn.net/docs/reference/js-reflection.html)

JavaScript DCE

原生

[并发](https://www.kotlincn.net/docs/reference/native/concurrency.html)

[不可变性](https://www.kotlincn.net/docs/reference/native/immutability.html)

[Kotlin 库](https://www.kotlincn.net/docs/reference/native/libraries.html)

[平台库](https://www.kotlincn.net/docs/reference/native/platform_libs.html)

[与 C 语言互操作](https://www.kotlincn.net/docs/reference/native/c_interop.html)

[与 Objective-C 及 Swift 互操作](https://www.kotlincn.net/docs/reference/native/objc_interop.html)

[CocoaPods 集成](https://www.kotlincn.net/docs/reference/native/cocoapods.html)

[Gradle 插件](https://www.kotlincn.net/docs/reference/native/gradle_plugin.html)

[调试](https://www.kotlincn.net/docs/reference/native/debugging.html)

[FAQ](https://www.kotlincn.net/docs/reference/native/faq.html)

工具

[Gradle](https://www.kotlincn.net/docs/reference/using-gradle.html)

[Maven](https://www.kotlincn.net/docs/reference/using-maven.html)

[Ant](https://www.kotlincn.net/docs/reference/using-ant.html)

[编译器选项](https://www.kotlincn.net/docs/reference/compiler-reference.html)

[编译器插件](https://www.kotlincn.net/docs/reference/compiler-plugins.html)

[Kapt](https://www.kotlincn.net/docs/reference/kapt.html)

[Dokka](https://www.kotlincn.net/docs/reference/kotlin-doc.html)

[OSGi](https://www.kotlincn.net/docs/reference/kotlin-osgi.html)

演进

[Kotlin 语言演进](https://www.kotlincn.net/docs/reference/evolution/kotlin-evolution.html)

[不同组件的稳定性](https://www.kotlincn.net/docs/reference/evolution/components-stability.html)

[Kotlin 1.3 的兼容性指南](https://www.kotlincn.net/docs/reference/compatibility-guide-13.html)

常见问题

[FAQ](https://www.kotlincn.net/docs/reference/faq.html)

[与 Java 比较](https://www.kotlincn.net/docs/reference/comparison-to-java.html)

[与 Scala 比较【官方已删除】](https://www.kotlincn.net/docs/reference/comparison-to-scala.html)

- [完整 Kotlin 参考（PDF）](https://www.kotlincn.net/docs/kotlin-docs.pdf)
- [完整 Kotlin 参考（字大PDF）](https://www.gitbook.com/download/pdf/book/hltj/kotlin-reference-chinese)
- [完整 Kotlin 参考（ePUB）](https://www.gitbook.com/download/epub/book/hltj/kotlin-reference-chinese)
- [完整 Kotlin 参考（Mobi）](https://www.gitbook.com/download/mobi/book/hltj/kotlin-reference-chinese)

 

[改进翻译](https://github.com/hltj/kotlin-web-site-cn/edit/master/pages/docs/reference/javascript-dce.md)

# JavaScript 无用代码消除（DCE）

Kotlin/JS Gradle 插件包含一个[*无用代码消除*](https://zh.wikipedia.org/wiki/死碼刪除)（*DCE*）工具。 无用代码消除通常也称为 *摇树*。 通过删除未使用的属性、函数和类，它减小了大小或生成的 JavaScript 代码。

在以下情况下会出现未使用的声明：

- 函数是内联的，永远不会直接调用（除了少数情况总是发生）。
- 模块使用共享库。没有 DCE 的情况下，未使用的组件仍会进入结果包。 例如，Kotlin 标准库中包含用于操作列表、数组、字符序列、DOM 适配器的函数。 它们总共构成了大约 1.3MB 的文件。 一个简单的 "Hello, world" 应用程序仅需要控制台例程，整个程序只有几 KB。

Kotlin/JS Gradle 插件在构建生产包时会自动处理 DCE，例如：使用 `browserProductionWebpack` 任务。 开发捆绑任务不包括 DCE。

## 从 DCE 排除的声明

有时，即使未在模块中使用函数或类，也可能需要在结果 JavaScript 代码中保留一个函数或一个类， 例如：如果要在客户端 JavaScript 代码中使用它，则可能会保留该函数或类。

为了避免某些声明被删除，请将 `dceTask` 代码块添加到 Gradle 构建脚本中，并将这些声明列为 `keep` 函数的参数。 参数必须是声明的完整限定名，并且模块名称为前缀： `moduleName.dot.separated.package.name.declarationName`

```
Groovy``Kotlin
kotlin.target.browser {
    dceTask {
        keep 'myKotlinJSModule.org.example.getName', 'myKotlinJSModule.org.example.User'
    }
}
kotlin.target.browser {
    dceTask {
        keep("myKotlinJSModule.org.example.getName", "myKotlinJSModule.org.example.User" )
    }
}
```

请注意，带有参数的函数名称在生成的 JavaScript 代码中会被[修饰](https://www.kotlincn.net/docs/reference/js-to-kotlin-interop.html#jsname-注解)。 为了避免消除这些函数，请在 `keep` 参数中使用修饰的名称。

## 已知问题：DCE 与 ktor

在 Kotlin 1.3.72 中，存在一个在 Kotlin/JS 项目中使用 [ktor](https://ktor.io/) 的已知[问题](https://github.com/ktorio/ktor/issues/1339)。 在某些情况下，可能会遇到类型错误，例如：`<something> is not a function` 这是来自 `io.ktor:ktor-client-js:1.3.0` 或 `io.ktor:ktor-client-core:1.3.0` 构件。 为避免此问题，请添加以下 DCE 配置：

```
Groovy``Kotlin
kotlin.target.browser {
    dceTask {
        keep 'ktor-ktor-io.\$\$importsForInline\$\$.ktor-ktor-io.io.ktor.utils.io'
    }
}
kotlin.target.browser {
    dceTask {
        keep("ktor-ktor-io.\$\$importsForInline\$\$.ktor-ktor-io.io.ktor.utils.io")
    }
}
```