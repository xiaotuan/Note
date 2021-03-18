### 3.4.5　Kotlin与Kapt

在Kotlin项目开发中，借助Kapt（Kotlin annotation processing tool，Kotlin注解处理工具）编译器插件可以很轻松地实现注解处理功能。做过Android开发的读者都知道，Android提供了大量的注解工具，如Dagger、Butterknife和Data Binding等。注解作为一种自动生成的模板代码，有助于减少代码的冗余度，方便程序的阅读与维护。

#### 1．在Gradle构建的项目中使用Kapt添加依赖库

在Gradle构建的项目中使用Kapt需要引入kotlin-kapt插件。

```python
apply plugin: 'kotlin-kapt'
```

然后在配置文件的dependencies块中使用Kapt配置需要添加的依赖项。例如，使用Kapt引入Glide v4库。

```python
apply plugin: 'kotlin-kapt' 
dependencies {
   kapt 'com.github.bumptech.glide:compiler:4.0.0-RC1'
}
```

在Gradle构建的项目中使用kotlin-kapt插件时应注意以下几点。

+ 在一个项目中，不要同时使用Kapt和annotationProcessor注解插件，如果项目中包含Java代码，使用Kapt插件即可。
+ 不使用kapt { generateStubs true }，Kapt3不支持它。
+ 如果项目依赖的第三方库中使用了android-apt插件，为避免重复，需要在项目的build. gradle文件中移除多余的插件。

#### 2．在Maven构建的项目中使用Kapt添加依赖库

在Maven构建的项目中使用Kapt插件添加其他依赖库的示例如下。

```python
<execution>
    <id>kapt</id>
    <goals>
        <goal>kapt</goal>
    </goals>
    <configuration>
        <sourceDirs>
             <sourceDir>src/main/kotlin</sourceDir>
             <sourceDir>src/main/java</sourceDir>
        </sourceDirs>
        <annotationProcessorPaths>
             <!-- 此处指定你的注解处理器 -->
             <annotationProcessorPath>
                 <groupId>com.google.dagger</groupId>
                 <artifactId>dagger-compiler</artifactId>
                 <version>2.9</version>
             </annotationProcessorPath>
        </annotationProcessorPaths>
    </configuration>
</execution>
```

需要注意的是，IntelliJ IDEA自身的构建系统目前还不支持Kapt，想要在IntelliJ IDEA中使用Kapt，请参考上面的构建方式。

Kotlin提供了多种构建方式，我们可以使用像Maven、Gradle或者Ant这样的构建系统来构建项目，Kotlin跟这些构建系统都是兼容的。同时，这些构建系统也支持Kotlin和Java组成的混合项目。

