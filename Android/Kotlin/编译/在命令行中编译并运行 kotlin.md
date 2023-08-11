`Kotlin` 在 `JVM` 上的 `SDK` 包括 `Kotlin` 编译器命令 `kotlinc-jvm`，以及 `Kotlin` 运行命令 `kotlin`。它们类似于 `Java` 文件中的 `javac` 与 `java` 一样。

**示例代码：hello.kt**

```kotlin
fun main() {
    println("Hello, Kotlin!")
}
```

编译 `hello.kt`：

```shell
> kotlinc-jvm hello.kt
```

执行完上面命令后将会生成 `hellokt` 文件，可以使用下面命令运行 `hellokt`：

```shell
> kotlin hellokt.class
```

如果你希望生成一个自包含的可以被 `Java` 命令执行的 `JAR` 文件，可以添加 `-include-runtime` 参数。这将允许你生成一个可以使用 `java` 命令执行的 `JAR`。

```shell
> kotlinc-jvm Test.kt -include-runtime -d Test.jar 
> java -jar .\Test.jar
Hello, Kotlin!
```

移除 `-include-runtime` 参数将生成一个 `JAR` 文件，该文件需要 `Kotlin` 运行时在类路径上执行。