`HttpServlet` 类是 `GenericServlet` 类的子类。`HttpServlet` 类为 `Servlet` 接口提供了与 HTTP 协议相关的通用实现。也就是说，`HttpServlet` 对象适合运行在与客户端采用 HTTP 协议通信的 `Servlet` 容器或者 Web 服务器中。在开发 Java Web 应用时，自定义的 `Servlet` 类一般都扩展 `HttpServlet` 类。

`HttpServlet` 类针对每一种请求方式都提供了相应的服务方法，如 `doGet()`、`doPost()`、`doPut()` 和 `doDelete()` 等方法。

`HttpServlet` 类实现了 `Servlet` 接口中的 `service(ServletRequest req, ServletResponse res)` 方法，该方法实际上调用的是它的重载方法：

```java
service(HttpServletRequest req, HttpServletResponse resp)
```

在以上重载 `service()` 方法中，首先调用 `HttpServletRequest` 类型的 `req` 参数的 `getMethod()` 方法，从而获得客户端的请求方式，然后依据请求方式来调用匹配的服务方法。如果为 GET 方式，则调用 `doGet()` 方法；如果为 POST 方式，则调用 `doPost()` 方法，以此类推。

`HttpServlet` 类为所有针对特定请求方式的 `doXXX()` 方法提供了默认的实现。在 `HttpServlet` 类的默认实现中，`doGet()` 、`doPost()`、`doPut()` 和 `doDelete()` 方法都向客户端返回一个错误。

+ 如果客户与服务器之间采用 HTTP 1.1 协议通信，那么返回的错误为 `HttpServletResponse.SC_METHOD_NOT_ALLOWED`（对应 HTTP 协议中响应状态代码为 405 的错误）
+ 如果客户与服务器之间不是采用 HTTP 1.1 协议通信，那么返回的错误为 `HttpServletResponse.SC_BAD_REQUEST`（对应 HTTP 协议中响应状态代码为 400 的错误）。

对于 `HttpServlet` 类的具体子类，一般会针对客户端的特定请求方式，来覆盖 `HttpServlet` 父类中的相应 `doXXX()` 方法。为了使 `doXXX()` 方法能被 `Servlet` 容器访问，应该把访问权限设为 `public`。

```java
public class HelloServlet extends HttpServlet {
    @Override
    public void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 提供具体的实现代码
        ......
    }
}
```

