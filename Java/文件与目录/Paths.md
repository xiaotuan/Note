静态的 `Paths.get` 方法接受一个或多个字符串，并将它们用默认文件系统的路径分隔符连接起来。然后它解析连接起来的结果，如果其表示的不是给定文件系统中的合法路径，那么就抛出 `InvalidPathException` 异常。这个连接起来的结果就是一个 `Path` 对象。

`get` 方法可以获取包含多个部件构成的单个字符串，例如：

```java
String baseDir = props.getProperty("base.dir");
// May be a string such as /opt/myprog or C:\Program Files\myprog
Path basePath = Paths.get(baseDir);	// OK the baseDir has separators
```

组合或解析路径是司空见惯的操作，调用 `p.resolve(q)` 将按照下列规则返回一个路径：

+ 如果 q 是绝对路径，则结果就是 q。
+ 否则，根据文件系统的规则，将 "p 后面跟着 q" 作为结果。

```java
Path workRelative = Paths.get("work");
Path workPath = basePath.resolve(workRelative);
```

`resolve` 方法有一种快捷方式，它接受一个字符串而不是路径：

```java
Path workPath = basePath.resolve("work");
```

还有一个很方便的方法 `resolveSibling`，它通过解析指定路径的父路径产生其兄弟路径。

```java
Path tempPath = workPath.resolveSibling("temp");
```

上面代码将创建 `/opt/myapp/temp`。

`resolve` 的对立面是 `relativize`，即调用 `p.relativize(r)` 将产生路径 q，而对 q 进行解析的结果正是 r。例如，以 "/home/cay" 为目标对 "/home/fred/myprog" 进行相对化操作，会产生 "../fred/myprog"。

`normalize` 方法将移除所有冗余的 `.` 和 `..` 部件。例如，规范化 `/home/cay/../fred/./myprog` 将产生 `/home/fred/myprog`。

`toAbsolutePath` 方法将产生给定路径的绝对路径，该绝对路径从根部件开始。

`Path` 类有许多有用的方法用来将路径断开：

```java
Path p = Paths.get("/home", "fred", "myprog.properties");
Path parent = p.getParent();	// the path /home/fred
Path file = p.getFileName();	// the path myprog.properties
Path root = p.getRoot();	// the path /
```

> 提示：偶尔，你可能需要与遗留系统的 API 交互，它们使用的是 `File` 类而不是 `Path` 接口。`Path` 接口有一个 `toFile` 方法，而 `File` 类有一个 `toPath` 方法。

