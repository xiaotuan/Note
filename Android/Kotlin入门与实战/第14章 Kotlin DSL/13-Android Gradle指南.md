### 14.5　Android Gradle指南

Groovy是一种基于JVM的敏捷开发语言，它结合了Smalltalk、Python和Ruby等多种编程语言的强大特性，能够与Java语言无缝结合。因为它运行在JVM上，所以可以和JVM语系的语言进行很好的融合。

Gradle自身属于DSL，但Gradle使用Groovy语言封装了一整套API，通常把这套API称为DSL。例如，Android项目的build.gradle配置文件使用Groovy编写，其语法如下。

```python
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.0.1'
    }
}
```

通过build.gradle配置文件可以发现，buildscript配置脚本包含repositories和dependencies配置，而在repositories和dependencies中又可以配置各自的一些属性。通过这种形式的配置，可以层次分明地看出整个项目构建的规律，而且Android项目的构建也遵循约定大于配置的设计思想，因此开发者只需要根据某些特定的需求修改自定义的部分即可轻松完成个性化构建流程。

Groovy本身作为一门脚本语言，可以像Python这类脚本语言一样直接执行。要理解Android项目build.gradle脚本配置中的DSL是如何被解析执行的，就需要理解Groovy的一些语法特点以及高级特性。

