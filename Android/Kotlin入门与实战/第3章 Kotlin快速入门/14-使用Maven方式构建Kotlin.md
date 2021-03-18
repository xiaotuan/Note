### 3.4.2　使用Maven方式构建Kotlin

作为Web时代知名的项目构建工具，Maven的功能可以说非常强大。如果读者喜欢使用Maven来构建项目，Kotlin也是支持的。对于现有的Maven项目，可以通过Kotlin IntelliJ IDEA插件来完成。依次选择【Tools】→【Kotlin】→【Conﬁgure Kotlin】即可完成Kotlin的支持。

当然，除了借助工具之外，Kotlin还支持通过pom文件配置来添加环境支持，pom文件配置依赖关系如下。

```python
<dependencies>
    <dependency>
        <groupId>org.jetbrains.kotlin</groupId>
        <artifactId>kotlin-stdlib</artifactId>
        <version>${kotlin.version}</version>
    </dependency>
</dependencies>
```

如果JDK环境是JDK 7或JDK 8，则使用kotlin-stdlib-jre7或kotlin-stdlib-jre8 取代上面的kotlin-stdlib即可。Maven还支持指定Kotlin代码编译，只需要在pom文件的<build>标签中指定需要编译的源代码即可。

```python
<build>
<sourceDirectory>${project.basedir}/src/main/kotlin</sourceDirectory>   <testSourceDirectory>${project.basedir}/src/test/kotlin</testSourceDirectory>
</build>
```

当然，对于一些Java和Kotlin混合的项目，如果要进行混合代码的编译，那么必须在Java编译器调用之前调用Kotlin编译器。为了加快项目的编译速度，Kotlin从1.1.2版本开始启用了增量编译，相关属性设置如下。

```python
<properties>
    <kotlin.compiler.incremental>true</kotlin.compiler.incremental>
</properties>
```

