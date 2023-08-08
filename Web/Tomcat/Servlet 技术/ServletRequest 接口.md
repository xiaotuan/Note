`Servlet` 接口的 `service(ServletRequest req, ServletResponse res)` 方法中有一个 `ServletRequest` 类型的参数。`ServletRequest` 类表示来自客户端的请求。当 `Servlet` 容器接收到客户端要求访问特定 `Servlet` 的请求时，容器先解析客户端的原始请求数据，把它包装成一个 `ServletRequest` 对象。当容器调用 `Servlet` 对象的 `service()` 方法时，就会把 `ServletRequest` 对象作为参数传递给 `service()` 方法。

`ServletRequest` 接口提供了一系列用于读取客户端请求数据的方法：

+ `getContentLength()`：返回请求正文的长度。如果请求正文的长度未知，则返回 -1。
+ `getContentType()`：获得请求正文的 MIME 类型，如果请求正文的类型未知，则返回 `null`。
+ `getInputStream()`：返回用于读取请求正文的输入流。
+ `getLocalAddar()`：返回服务器端的 IP 地址。
+ `getLocalName()`：返回服务器端的主机名。
+ `getLocalPort()`：返回服务器端的 FTP 端口好。
+ `getParameter(String name)`：根据给定的请求参数名，返回来自客户请求中的匹配的请求参数值。
+ `getProtocol()`：返回客户端与服务器端通信所用的协议的名称以及版本号。
+ `getReader()`：返回用于读取字符串形式的请求正文的 `BufferedReader` 对象。
+ `getRemoteAddr()`：返回客户端的 IP 地址。
+ `getRemoteHost()`：返回客户端的主机名。
+ `getRemotePort()`：返回客户端的 FTP 端口好。

此外，`ServletRequest` 接口中还定义了一组用于在请求范围内存取共享数据的方法：

+ `setAttribute(String name, java.lang.Object object)`：在请求范围内保存一个属性，参数 `name` 表示属性名，参数 `object` 表示属性值。
+ `getAttribute(String name)`： 根据 `name` 参数给定的属性名，返回请求范围内的匹配的属性值。
+ ` removeAttribute(String name)`：从请求范围内删除一个属性。