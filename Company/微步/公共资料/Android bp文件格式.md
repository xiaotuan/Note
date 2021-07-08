[toc]

按照设计，`Android.bp` 文件非常简单。没有条件或控制流语句——任何复杂的逻辑都在 `Go` 编写的构建逻辑中处理。

### 1. 模块

`Android.bp` 文件中的模块以模块类型开头，然后是一组 `name: value,` 格式的属性：

```json
cc_binary {
    name: "gzip",
    srcs: ["src/test/minigzip.c"],
    shared_libs: ["libz"],
    stl: "none",
}
```

每个模块都必须有一个 `name` 属性，并且该值在所有 `Android.bp` 文件中必须是唯一的。

> 提示：
>
> 有关有效模块类型及其属性的列表，请参阅 [Soong Modules Reference](./Soong Modules Reference.md)。

### 2. 文件列表

文件列表的属性可以采用全局模式和输出路径扩展。

+  `Glob` 模式可以包含正常的 `Unix` 通配符 `*`，例如 `"*.java"`.

  `Glob` 模式还可以包含一个 `**` 通配符作为路径元素，它将匹配零个或多个路径元素。例如，`java/**/*.java` 将匹配 `java/Main.java` 和 `java/com/android/Main.java`。

+ 输出路径扩展采用 `:module` 或 `:module{.tag}`，其中 `module` 是生成输出文件的模块的名称，它扩展为这些输出文件的列表。使用可选的 `{.tag}` 后缀，模块可能会根据生成不同的输出列表 `tag`。

  例如，一个名为 `my-docs` 的 `droiddoc` 模块将以 `:my-docs` 输出路径扩展名输出 `.stubs.srcjar` 文件，而 `:my-docs{.doc.zip}` 则会输出 `.doc.zip` 的文件。

文件列表通常用于 `filegroup` 模块中的 `srcs` 属性。

  ### 3. 变量

`Android.bp` 文件可能包含顶级变量：

```json
gzip_srcs = ["src/test/minigzip.c"],

cc_binary {
    name: "gzip",
    srcs: gzip_srcs,
    shared_libs: ["libz"],
    stl: "none",
}
```

变量的作用域是声明它们的文件的其余部分，以及任何子 `Android.bp` 文件。变量是不可变的，只有一个例外——它们可以用 `+=` 赋值附加到后面，但只能在它们被引用之前。

### 4. 注释

`Android.bp` 文件可以包含 `C` 风格的多行`/* */`和 `C++` 风格的单行`//`注释。

### 5. 类型

变量和属性是强类型的，变量是基于第一次赋值的动态变量，而属性是基于模块类型的静态属性。支持的类型有：

- 布尔 (`true`或`false`)
- 整数 ( `int`)
- 字符串 ( `"string"`)
- 字符串列表 ( `["string1", "string2"]`)
- 字典( `{key1: "value1", key2: ["value2"]}`)

字典可以是任何类型的值，包括嵌套字典。列表和字典的最后一个值后可能有尾随逗号。

可以使用 `\` 转义双引号。

### 6. 操作符

可以使用 `+` 运算符附加字符串、字符串列表和字典。可以使用 `+` 运算符对整数求和。

### 7. 默认模块

如果多个模块中重复使用相同的属性，可以使用默认模块包含这些相同的属性。例如：

```json
cc_defaults {
    name: "gzip_defaults",
    shared_libs: ["libz"],
    stl: "none",
}

cc_binary {
    name: "gzip",
    defaults: ["gzip_defaults"],
    srcs: ["src/test/minigzip.c"],
}
```

### 8. 包

一个包的目录下包含一个名为 `Android.bp` 的文件，`Android.bp` 位于包的顶级目录下。一个包包含其目录下的所有文件，已经它下面的所有子目录，但那些本身包含 `Androd.bp` 文件的目录除外。

例如，在下面的目录树种（其中 `../android/` 是顶级目录）有两个 包： `my/app` 和 `my/app/test`。请注意，`my/app/data` 不是包，而是属性`my/app` 包的一部分。

```
.../android/my/app/Android.bp
.../android/my/app/app.cc
.../android/my/app/data/input.txt
.../android/my/app/tests/Android.bp
.../android/my/app/tests/test.cc
```

