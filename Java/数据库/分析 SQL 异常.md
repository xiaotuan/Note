每个 `SQLException` 都有一个由多个 `SQLException` 对象构成的链，这些对象可以通过 `getNextException` 方法获取。这个异常链是每个异常都具有的由 `Throwable` 对象构成的 “成因” 链之外的异常链，因此，我们需要用两个嵌套的循环来完整枚举所有的异常：

```java
for (Throwable t :sqlException) {
    do something with t
}
```

可以在 `SQLException` 上调用 `getSQLState` 和 `getErrorCode` 方法来进一步分析它，其中第一个方法将产生符合 `X/Open` 或 `SQL: 2003` 标准的字符串（调用 `DatabaseMetaData` 接口的 `getSQLStateType` 方法可以查出驱动程序所使用的标准）。而错误代码是与具体的提供商相关的。

`SQLWarning` 类是 `SQLException` 的子类，我们可以调用 `getSQLState` 和 `getErrorCode` 来获取有关警告的更多信息。要获得所有的警告，可以使用下面的循环：

```java
SQLWarning w = stat.getWarning();
while (w != null) {
    do something with w
    w = w.nextWarning();
}
```

当数据从数据库中读出并意外被截断时，`SQLWarning` 的 `DataTruncation` 子类将会被当做异常抛出。