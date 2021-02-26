如何让浏览器访问 Servlet？

1. 给 Servlet 指定一个 Servlet 路径！（让 Servlet 与一个路径绑定在一起）
2. 浏览器访问 Servlet 路径。



如何给 Servlet 配置 Servlet 路径？

这需要在 web.xml 中对 Servlet 进行配置。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">
	
	<servlet>
		<servlet-name>xxx</servlet-name>
		<servlet-class>com.qty.servlet.AServlet</servlet-class>
	</servlet>
	
	<servlet-mapping>
		<servlet-name>xxx</servlet-name>
		<url-pattern>/AServlet</url-pattern>
	</servlet-mapping>
	
</web-app>
```

在浏览器中输入请求路径：

```txt
http://localhost:8080/Day09_1/AServlet
```

Servlet 声明周期方法：

+ void init(ServletConfig config)：出生之后（1次）
+ void service(ServletRequest request, ServletResponse response)：每次处理请求时都会被调用；
+ void destroy()：临死之前（1次）；

特性：

+ 单例，一个类只有一个对象；当然可能存在多个 Servlet 类！
+ 线程不案例的，所以它的效率是高的！

> Servlet 类由我们来写，但对象由服务器来创建，并且由服务器来调用相应的方法。

**AServlet.java**

```java
package com.qty.servlet;

import java.io.IOException;

import javax.servlet.Servlet;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

/**
 * 查看 Servlet 接口的方法
 *
 */
public class AServlet implements Servlet {

	/*
	 * 它也是生命周期方法
	 * 它会在 Servlet 被销毁之前调用，并且它只会被调用一次
	 */
	@Override
	public void destroy() {
		System.out.println("destory()...");
	}

	/*
	 * 可以用来获取 Servlet 的配置信息
	 */
	@Override
	public ServletConfig getServletConfig() {
		System.out.println("getServletConfig()...");
		return null;
	}

	/*
	 * 获取 Servlet 的信息 
	 */
	@Override
	public String getServletInfo() {
		System.out.println("getServletInfo()...");
		return "我是一个快乐的Servlet";
	}

	/*
	 * 它是生命周期方法
	 * 它会在 Servlet 对象创建之后马上执行，并只执行一次！（出生之后）
	 */
	@Override
	public void init(ServletConfig config) throws ServletException {
		System.out.println("init()...");
	}

	/*
	 * 它是生命周期方法
	 * 它会被调用多次！！！
	 * 每次处理请求都是在调用这个方法！
	 */
	@Override
	public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
		System.out.println("service()...");
	}

}
```

> 注意：
>
> + 不要在 Servlet 中创建成员！创建局部变量即可。
> + 可以创建无状态成员。
> + 可以创建有状态成员，但状态必须为只读的！