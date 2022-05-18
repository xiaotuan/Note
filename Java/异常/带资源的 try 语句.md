带资源的 `try` 语句的最简单形式为：

```java
try (Resource res = ...) {
    work with res
}
```

`try` 块退出时，会自动调用 `res.close()`。

还可以指定多个资源。例如：

```java
try (Scanner in = new Scanner(new FileInputStream("/usr/share/dict/words"), "UTF-8");
    PrintWriter out = new PrintWrite("out.txt")) {
    while (in.hasNext()) {
        out.println(in.next().toUpperCase());
    }
}
```

带资源的 `try` 产生的资源异常将自动捕获，并由 `addSuppressed` 方法来增加到原来的异常。如果对这些异常感兴趣，可以调用 `getSuppressed` 方法，它会得到从 `close` 方法抛出并被抑制的异常列表。

> 提示：带资源的 `try` 语句自身也可以有 `catch` 子句和一个 `finally` 子句。