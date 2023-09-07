`Servlet` 接口的 `service()` 方法的完整定义如下：

```java
public void service(ServletRequest req, ServletResponse res) throws ServletException, java.io.IOException
```

以上 `service()` 方法声明抛出两个异常：

+ `ServletException`：表示当 `Servlet` 进行常规操作时出现的异常。
+ `IOException`：表示当 `Servlet` 进行 `I/O` 操作时出现的异常。

`ServletException` 有一个子类 `UnavailableException`，表示无法访问当前 `Servlet` 的异常。如果 `Servlet` 由于一些系统级别的原因而不能响应客户请求，就可以抛出这种异常。系统级别的原因包括：内存不足或无法访问第三方服务器（例如数据库服务器）等：

`UnavailableException` 有两个构造方法：

+ `UnavailableException(String msg)`：创建一个表示 `Servlet` 永远不能被访问的异常。
+ `UnavailableException(String msg, int seconds)`：创建一个表示 `Servlet` 不能被访问的异常。参数 `seconds` 表示 `Servlet` 暂且不能被访问的时间，以秒为单位。如果参数 `senconds` 取值为零或者负数，表示无法估计 `Servlet` 暂且不能被访问的时间。

**示例代码：**

**ExceptionTesterServlet.java**

```java
package com.qty.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.GenericServlet;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.UnavailableException;

public class ExceptionTesterServlet extends GenericServlet {

	@Override
	public void service(ServletRequest req, ServletResponse resp) throws ServletException, IOException {
		String condition = req.getParameter("condition");
		if (condition == null) condition = "ok";
		
		if (condition.equals("1")) {
			throw new ServletException("condition");
		} else if (condition.equals("2")) {
			// Servlet 在 2 秒内暂且不能被访问
			throw new UnavailableException("condition2", 2);
		} else if (condition.equals("3")) {
			// Servlet 永远不能被访问
			throw new UnavailableException("condition3");
		}
		PrintWriter out = resp.getWriter();
		out.println("It's ok.");
		out.close();
	}

}
```

**web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>ExceptionTesterServlet</display-name>
  <welcome-file-list>
    <welcome-file>exception</welcome-file>
  </welcome-file-list>
  <servlet>
  	<servlet-name>ExceptionTesterServlet</servlet-name>
  	<servlet-class>com.qty.web.ExceptionTesterServlet</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>ExceptionTesterServlet</servlet-name>
  	<url-pattern>/exception</url-pattern>
  </servlet-mapping>
</web-app>
```

