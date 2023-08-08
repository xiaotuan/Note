`GenericServlet` 抽象类为 `Servlet` 接口提供了通用实现，它与任何网络应用层协议无关。`GenericServlet` 类除了实现 `Servlet` 接口，还实现了 `ServletConfig` 接口和 `Serializable` 接口。

`GenericServlet` 类还自定义了一个不带参数的 `init()` 方法，`init(ServletConfig config)` 方法会调用此方法。对于 `GenericServlet` 类的子类，如果希望覆盖父类的初始化行为，有两种方法：

（1）覆盖父类的不带参数的 `init()` 方法：

```java
public void init() {
    // 子类具体的初始化行为
    ......
}
```

（2）覆盖父类的带参数的 `init(ServletConfig config)` 方法。如果希望当前 `Servlet` 对象与 `ServletConfig` 对象关联，应该在该方法中先调用 `super.init(config)` 方法：

```java
public void init(ServletConfig config) {
    super.init(config);	// 调用父类的 init(config) 方法
    // 子类具体的初始化行为
    ......
}
```

`GenericServlet` 类没有实现 `Servlet` 接口中的 `service()` 方法，`service()` 方法是 `GenericServlet` 类中唯一的抽象方法，`GenericServlet` 类的具体子类必须实现该方法，从而为特定的客户请求提供具体的服务。

`GenericServlet` 类尽管实现了 `Servlet` 接口中的 `destroy()` 方法，实际上什么也没做。`GenericServlet` 类的具体子类可以覆盖该方法，从而为待销毁的当前 `Servlet` 对象释放锁占用的各种资源（例如关闭文件输入流和输出流，关闭与数据库的连接等）。

