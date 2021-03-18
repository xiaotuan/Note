### 3.4.1　使用Gradle方式构建Kotlin

Gradle是构建Kotlin项目的推荐方式，Gradle具有灵活的项目模型，因为支持增量构建、长期构建过程和其他高级技术，所以得到了软件开发者的喜爱和追捧。

我们知道，Gradle是Android项目的标准构建系统，使用Groovy语法编写而成。不过，Gradle团队正在努力支持使用Kotlin来编写Gradle构建脚本。

构建Kotlin项目的标准Gradle脚本如下。

```python
buildscript {
    ext.kotlin_version = '1.2.20'   //Kotlin版本
    repositories {
        mavenCentral()
    }
    dependencies {
        //给Kotlin Gradle增加构建脚本依赖
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```

如果使用Gradle的DSL插件来构建Kotlin项目，则不需要进行上面的配置。

#### 1．在JVM中使用Gradle

在JVM环境下使用Kotlin进行开发前，需要为应用添加Kotlin插件。

```python
apply plugin: "kotlin"
```

或者，从Kotlin 1.1.1版本开始，使用Gradle提供的DSL插件来应用该插件。

```python
plugins {
    id "org.jetbrains.kotlin.jvm" version "1.2.20"
}
```

大多数情况下，Kotlin源码可以与同一文件夹或不同文件夹中的Java源码混用，系统默认使用不同的文件夹，如果要放到同一文件夹，需要对sourceSets设置如下属性。

```python
sourceSets {
    main.kotlin.srcDirs += 'src/main/myKotlin'
    main.java.srcDirs += 'src/main/myJava'
}
```

#### 2．在JavaScript中使用Gradle

在JavaScript中使用Kotlin进行开发前，需添加Kotlin的JS插件依赖。

```python
apply plugin: "kotlin2js"
```

因为该插件只适用于Kotlin文件，所以建议将Kotlin和Java文件分开存放。除了正常输出JavaScript文件外，该插件还会额外创建一个带二进制描述符的JS文件，是否生成JS文件由kotlinOptions.metaInfo选项控制。

```python
compileKotlin2Js {
    kotlinOptions.metaInfo = true
}
```

#### 3．在Android中使用Gradle

和普通的Java环境相比，Android环境使用了不同的构建过程，因此需要使用不同的Gradle插件来完成构建。具体来说，在构建脚本时使用kotlin-android插件取代Kotlin插件。

```python
apply plugin: 'kotlin-android'
```

其他设置和非Android应用的设置一样，完整的脚本配置如下。

```python
apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'
buildscript {
    ext.kotlin_version = '1.2.20'
    ……
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```

使用Android Studio来开发Android应用时，如果希望将Kotlin源代码放在特定目录下（如src/main/kotlin），则需要向系统注册它们，以便Android Studio将它们识别为Kotlin源代码目录。

```python
android {
  ……
  sourceSets {
    main.java.srcDirs += 'src/main/kotlin'
  }
}
```

#### 4．增量编译

从Kotlin 1.1.1版本开始，使用Gradle方式构建的Kotlin项目默认开启了增量编译，增量编译加快了编译速度，提高了用户体验。如果想要修改默认的增量编译设置，则可以使用下面的方式。

+ 在gradle.properties文件中设置kotlin.incremental=true/flase属性。
+ 将“-Pkotlin.incremental=true/false”添加到Gradle命令行参数中。

开启增量编译后，第一次项目构建不是增量的，编译速度依然会比较慢。

