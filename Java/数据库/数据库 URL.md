`JDBC` 使用了一种与普通 `URL` 相类似的语法来描述数据源。下面是这种语法的两个实例：

```
jdbc:derby://localhost:1527/COREJAVA;create=true
jdbc:postgresql:COREJAVA
```

上述 `JDBC URL` 指定了名为 `COREJAVA` 的一个 `Derby` 数据库和一个` PostgreSQL` 数据库。`JDBC URL` 的一般语法为：

```
jdbc:subprotocol:other stuff
```

其中，`subprotocol` 用于选择连接到数据库的具体驱动程序。`other stuff` 参数的格式随所使用的 `subprotocol` 不同而不同。如果要了解具体格式，你需要查阅数据库供应商提供的文档。

