`Servlet` 容器在启动一个 Web 应用时，会为它创建一个 `ServletContext` 对象。可以把 `ServletContext` 对象形象地理解为 Web 应用的总管家，同一个 Web 应用中的所有 `Servlet` 对象都共享一个总管家，`Servlet` 对象们可通过这个总管家来访问容器中的各种资源。

`ServletContext` 接口提供的方法可分为以下几种类型：

（1）用于在 Web 应用范围内存储共享数据的方法：

+ `setAttribute(String name, java.lang.Object object)`：把一个 Java 对象与一个属性名绑定，并把它存入到 `ServletContext` 中。参数 name 指定属性名，参数 object 表示共享数据。
+ `getAttribute(String name)`：根据参数给定的属性名，返回一个 `Object` 类型的对象，它表示 `ServletContext` 中与属性名匹配的属性值。
+ `getAttributeNames()`：返回一个 `Enumeration` 对象，该对象包含了所有存放在 `ServletContext` 中的属性名。
+ `removeAttribute(String name)`：嗯句参数指定的属性名，从 `ServletContext` 中删除匹配的属性。

（2）访问当前 Web 应用的资源：

+ `getContextPath()`：返回当前 Web 应用的 URL 入口。
+ `getInitParameter(String name)`：根据给定的参数名，返回 `Web` 应用范围内的匹配的初始化参数值。在 `web.xml` 文件中，直接在 `<web-app>` 根元素下定义的 `<context-param>` 元素表示应用范围内的初始化参数。
+ `getInitParameterNames()`：返回一个 `Enumeration` 对象，它包含了 `Web` 应用范围内所有的初始化参数名。
+ `getServletContextName()`：返回 Web 应用的名字，即 `web.xml` 文件中 `<display-name>` 元素的值。
+ `getRequestDispatcher(String path)`：返回一个用于向其他 `Web` 组件转发请求的 `RequestDispatcher` 对象。

（3）访问 `Servlet` 容器中的其他 Web 应用：

+ `getContext(String uripath)`：根据参数指定的 URI，返回当前 `Servlet` 容器中其他 Web 应用的 `ServletContext` 对象。

（4）访问 `Servlet` 容器的相关信息：

+ `getMajorVersion()`：返回 `Servlet` 容器支持的 `Java Servlet API` 的主版本号。
+ `getMinorVersion()`：返回 `Servlet` 容器支持的 `Java Servlet API` 的次版本号。
+ `getServerInfo()`：返回 `Servlet` 容器的名字和版本。

（5）访问服务器端的文件系统资源：

+ `getRealPath(String path)`：根据参数指定的虚拟路径，返回文件系统中一个真实的路径。
+ `getResource(String path)`：返回一个映射到参数指定的路径的 URL。
+ `getResourceAsStream(String path)`：返回一个用于读取参数指定的文件的输入流。
+ `getMimeType(String file)`：返回参数指定的文件的 MIME 类型。

（6） 输出日志

+ `log(String msg)`：向 `Servlet` 的日志文件中写日志。
+ `log(String message, java.lang.Throwable throwable)`：向 `Servlet`  的日志文件中写错误日志，以及异常的堆栈信息。

**示例代码：ContextTesterServlet.java**

```java
package mypack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ContextTesterServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 获得 ServletContext 对象
		ServletContext context = getServletContext();
		
		// 设置 HTTP 响应的正文的 MIME 类型及字符编码
		resp.setContentType("text/html;charset=GBK");
		
		// 输出 HTML 文档
		PrintWriter out = resp.getWriter();
		out.println("<html><head><title>FontServlet</title></head>");
		out.println("<body>");
		out.println("<br>Email: " + context.getInitParameter("emailOfwebmaster"));
		out.println("<br>MimeType: " +  context.getMimeType("/WEB-INF/web.xml"));
		out.println("<br>MajorVersion: " + context.getMajorVersion());
		out.println("<br>ServerInfo: " + context.getServerInfo());
		out.println("</body></html>");
		
		// 输出日志
		context.log("这是 ContextTesterServlet 输出的日志。");
		out.close();	// 关闭 PrintWriter
	}
}
```

在 `web.xml` 文件中对 `ContextTesterServlet` 类做了如下配置：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>ContextTesterServlet</display-name>
  <context-param>
  	<param-name>emailOfwebmaster</param-name>
  	<param-value>webmaster@hotmail.com</param-value>
  </context-param>
  <welcome-file-list>
    <welcome-file>ServletContext</welcome-file>
  </welcome-file-list>
  <servlet>
  	<servlet-name>ServletContext</servlet-name>
  	<servlet-class>mypack.ContextTesterServlet</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>ServletContext</servlet-name>
  	<url-pattern>/ServletContext</url-pattern>
  </servlet-mapping>
</web-app>
```

