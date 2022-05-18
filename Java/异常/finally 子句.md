当代码抛出一个异常时，就会终止方法中剩余代码的处理，并退出这个方法的执行。如果方法获得了一些本地资源，并且只有这个方法自己知道，又如果这些资源在退出方法之前必须被回收，那么就会产生资源回收问题。Java 的解决方案就是 `finally` 子句。

不管是否有异常捕获，`finally` 子句中的代码都被执行。例如：

```java
InputStream in = new FileInputStream(...);
try {
    code that might throw exceptions
} catch (IOException e) {
    show error message
} finally {
    in.close();
}
```

`try` 语句可以只有 `finally` 子句，而没有 `catch` 子句。例如：

```java
InputStream in = new FileInputStream(...);
try {
    code that might throw exceptions
} finally {
    in.close();
}
```

无论在 `try` 语句块中是否遇到异常，`finally` 子句中的 `in.close()` 语句都会被执行。当然，如果真的遇到一个异常，这个异常将会被重新抛出，并且必须由另一个 `catch` 子句捕获。

> 提示：强烈建议解耦合 `try/catch` 和 `try/finally` 语句块，这样可以提高代码的清晰度。例如：
>
> ```java
> InputStream in = new FileInputStream(...);
> try {
>     try {
>     	code that might throw exceptions
>     } finally {
>         in.close();
>     }
> } catch (IOException e) {
>     show error message
> }
> ```

> 警告：当 `finally` 子句包含 `return` 语句时，将会出现一种意想不到的结果。假设利用 `return` 语句从 `try` 语句块中退出。在方法返回前，`finally` 子句的内容将被执行。如果 `finally` 子句中也有一个 `return` 语句，这个返回值将会覆盖原始的返回值。