### 14.4　使用kotlinx.html创建DSL

kotlinx.html是一款可以使用DSL构建HTML页面的工具库，它可以作为传统页面模板系统（例如JSP、FreeMarker等页面引擎）的替代品。

kotlinx.html提供kotlinx-html-jvm和kotlinx-html-js库来构建DSL，通过这两个库可以在JVM和浏览器（或其他JavaScript引擎）中直接使用Kotlin代码来构建HTML，这改变了原有的HTML标签式的前端代码构建方式。

在使用kotlinx.html构建HTML的DSL之前，需要添加kotlinx.html相关的环境依赖，kotlinx.html提供了4种集成方式，分别是Maven、Gradle、NPM和Bintray。

