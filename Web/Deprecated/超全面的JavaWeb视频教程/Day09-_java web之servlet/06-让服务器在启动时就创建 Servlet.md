默认情况下，服务器会在某个 Servlet 第一次收到请求时创建它。也可以在 web.xml 中对 Servlet 进行配置，使服务器启动时就创建 Servlet。

在服务器启动时就创建 Servlet 的方法是：

在 `<servlet>` 中配置 `<load-on-startup>`，其中给出一个非负整数，这个整数表示创建 Servlet 的顺序。

```xml
<servlet>
    <servlet-name>hello1</servlet-name>
    <servlet-class>cn.itcast.servlet.Hello1Servlet</servlet-class>
    <load-on-startup>0</load-on-startup>
</servlet>
```

