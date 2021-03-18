### 16.2.2　添加konan插件配置

创建完成之后，需要修改build.gradle文件配置，打开build.gradle文件并添加如下配置。

```python
buildscript {
    repositories {
        mavenCentral()
        maven {
            url "https://dl.bintray.com/jetbrains/kotlin-native-dependencies"
        }
    }
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-native-gradle-plugin:0.5"
    }
}
apply plugin: 'konan'
```

代码中，kotlin-native-gradle-plugin:0.5是Gradle构建Kotlin Native工程所使用的DSL插件。除此之外，还需要应用konan插件，它是用来将Kotlin代码编译为Native代码的插件。

此时，还需要创建一个kotliner.def文件，该文件主要用来配置C到Kotlin的映射关系。

```python
headers=cn_kotliner.h
```

