### 15.2.5　JavaScript DCE

自Kotlin 1.1.4版本起，Kotlin/JavaScript提供了一个无用代码消除（Dead Code Elimination，DCE）工具，允许在生成的JavaScript中删除未使用的属性、函数和类。出现未使用声明的可能情况有以下几种。

+ 函数内联并且从未直接调用（除少数情况外）。
+ 使用的共享库提供了比实际需要更多的功能函数。例如，Kotlin/Script标准库提供了用于操作列表、数组、字符序列、DOM适配器等的功能函数，但是这些函数并不都能被使用到。

目前，使用Gradle方式可以很容易地集成DCE工具，只需要在build.gradle文件中添加以下配置即可。

```python
apply plugin: 'kotlin-dce-js'
```

如果项目中涉及多个build.gradle配置文件，那么请将配置插件应用在主项目中。默认情况下，可以在项目文件的“$BUILD_DIR/min/”目录中找到生成的JavaScript文件，其中，$BUILD_DIR是生成JavaScript的路径，通常是build/classes/main。

要在主源上配置DCE，可以使用runDceKotlinJs任务以及其他源集对应的runDce< sourceSetName>KotlinJs。有时候，直接在JavaScript中使用Kotlin声明会被DCE当成无用的声明给清除掉，如果想要在JavaScript中保留这些声明，可以在build.gradle中使用以下语法。

```python
runDceKotlinJs.keep "declarationToKeep"[, "declarationToKeep", …]
```

declarationToKeep具有以下语法。

```python
moduleName.dot.separated.package.name.declarationName
```

考虑将一个模块命名为kotlin-js-example，它在org.jetbrains.kotlin.examples包中有一个名为toKeep的函数，则保留该声明的语法如下。

```python
runDceKotlinJs.keep "kotlin-js-example_main.org.jetbrains.kotlin.examples.  toKeep"
```

如果函数具有参数，则它的名称可能会被修饰，因此在keep指令中应该使用修饰后的名称。

构建带有DCE的项目，每次运行会额外花费一些时间，可以通过修改DCE任务的dceOptions.devMode模式来跳过实际的无效代码消除，从而缩短项目的开发构建时间。

例如，禁用自定义条件main源集的DCE和test代码的DCE，将下述几行代码添加到构建脚本中。

```python
runDceKotlinJs.dceOptions.devMode = isDevMode
runDceTestKotlinJs.dceOptions.devMode = true
```

在JavaScript中使用DCE工具时，需要注意以下几点。

+ 在Kotlin 1.1.x版本中，DCE工具只是一个实验性的功能，但可以通过更改默认配置和参数来在项目中使用它。
+ DCE工具通常只适用于开发应用程序，如果开发的是共享库，那么不应使用DCE工具，因为DCE不知道库的哪些部分会被用户的应用程序所使用。
+ 通常，DCE并不会通过删除不必要的空格和缩短标识符来执行代码压缩，如果有这方面的需求，则可以使用如UglifyJ或者Google Closure Compiler等工具。

