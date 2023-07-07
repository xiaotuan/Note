在 `Web` 或企业环境中部署 `JDBC` 应用时，数据库连接管理与 `Java` 名字和目录接口（`JNDI`）是集成在一起的。遍布企业的数据源的属性可以存储在一个目录中，采用这种方式使得我们可以集中管理用户名、密码、数据库和 `JDBC URL`。

在这样的环境中，可以使用下列代码创建数据库连接：

```java
Context jndiContext = new InitialContext();
DataSource source = (DataSource) jndiContext.lookup("java:comp/env/jdbc/corejava");
Connection conn = source.getConnection();
```

> 注意：在 `Java EE` 的容器中，甚至不必编程进行 `JNDI` 查找，只需在 `DataSource` 域上使用 `Resource` 注解，当加载应用时，这个数据源引用将被设置：
>
> ```java
> @Resource(name="jdbc/corejava")
> private DataSource source;
> ```

建立数据库连接池意味着数据库连接在物理上并未被关闭，而是保留在一个队列中并被反复重用。连接池是一种非常重要的服务，`JDBC` 规范为实现者提供了用以实现连接池服务的手段。不过，`JDK` 本身并未实现这项服务，数据库供应商提供的 `JDBC` 驱动程序中通常也不包含这项服务。相反，`Web` 容器和应用服务器的开发商通常会提供连接池服务的实现。

连接池的使用对程序员来说是完全透明的，可以通过获取数据源并调用 `getConnection` 方法来得到连接池中的连接。使用完连接后，需要调用 `close` 方法。该方法并不在物理上关闭连接，而只是告诉连接池已经使用完该连接。连接池通常还会将池机制作用于预备语句上。





