### 12.2.2　Maven构建方式

如果采用Maven的方式来构建项目，则可以打开IntelliJ IDEA，依次选择【File】→【New Project】→【Maven】，勾选【Create from archetype】选项，如图12-2所示。项目构建完成之后，在pom.xml依赖文件中添加kotlinx.coroutines依赖。

```python
<dependencies>
       …
    <!—协程依赖-->
    <dependency>
        <groupId>org.jetbrains.kotlinx</groupId>
        <artifactId>kotlinx-coroutines-core</artifactId>
        <version>0.21</version>
    </dependency>
</dependencies>
```

![48.png](../images/48.png)
<center class="my_markdown"><b class="my_markdown">图12-2　采用Maven方式构建项目工程</b></center>

值得注意的是，因为协程是在Kotlin 1.1版本中才添加的新功能，所以请确保Kotlin的本地运行版本。

