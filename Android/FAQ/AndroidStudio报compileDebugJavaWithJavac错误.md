报错日志：

```console
> Task :app:compileDebugJavaWithJavac FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:compileDebugJavaWithJavac'.
> javax/xml/bind/JAXBException

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 2s
20 actionable tasks: 2 executed, 18 up-to-date
```

错误原因：

JAXB API 是 Java EE 的 API，因此在 Java SE 9.0 及以上版本不再包含这个Jar 包导致的。而我的机子上安装的是 Java SE 12 版本。

解决办法：

1. 将 Java 版本降至 [Java 1.8](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html)。

2. 下载相关包，并将其添加到下面中。

+ [javax.activation-1.2.0.jar](http://search.maven.org/remotecontent?filepath=com/sun/activation/javax.activation/1.2.0/javax.activation-1.2.0.jar)
+ [jaxb-api-2.3.0.jar](http://search.maven.org/remotecontent?filepath=javax/xml/bind/jaxb-api/2.3.0/jaxb-api-2.3.0.jar)
+ [jaxb-core-2.3.0.jar](http://search.maven.org/remotecontent?filepath=com/sun/xml/bind/jaxb-core/2.3.0/jaxb-core-2.3.0.jar)
+ [jaxb-impl-2.3.0.jar](http://search.maven.org/remotecontent?filepath=com/sun/xml/bind/jaxb-impl/2.3.0/jaxb-impl-2.3.0.jar)

3. Maven 项目添加依赖：

```json
<!-- Java 6 = JAX-B Version 2.0		-->
<!-- Java 7 = JAX-B Version 2.2.3   -->
<!-- Java 8 = JAX-B Version 2.2.8 	-->
<dependencies>
    <dependency>
        <groupId>javax.xml.bind</groupId>
        <artifactId>jaxb-api</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-impl</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-core</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>javax.activation</groupId>
        <artifactId>activation</artifactId>
        <version>1.1.1</version>
    </dependency>
</dependencies>
```

> 建议使用中心仓库，否则可能某些 jar 找不到：
> ```
> HTTP: http://repo1.maven.org/maven2
> HTTPS:https://repo1.maven.org/maven2
> ```