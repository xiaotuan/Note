SerlvetConfig 类介绍

一个 ServletConfig 对象，对应一段 web.xml 中 Servlet 的配置信息！

**web.xml**

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
		<init-param>
			<param-name>p1</param-name>
			<param-value>v1</param-value>
		</init-param>
		<init-param>
			<param-name>p2</param-name>
			<param-value>v2</param-value>
		</init-param>
	</servlet>
	
	<servlet-mapping>
		<servlet-name>xxx</servlet-name>
		<url-pattern>/AServlet</url-pattern>
	</servlet-mapping>
	
</web-app>
```

**API**

+ String getServletName()：获取的是 `<servlet-name>` 中的内容。
+ ServletContext getServletContext()：获取 Servlet 上下文对象。
+ String getInitParameter(String name)：获取 `<init-param>` 中的 `<param-value>` 的值。
+ Enumeration getInitParameterNames()：获取所有初始化参数的名称，即 `<param-name>` 的值。

**AServlet.java**

```java
package com.qty.servlet;

import java.io.IOException;
import java.util.Enumeration;

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
		
		/**
		 * 获取初始化参数
		 */
		System.out.println(config.getInitParameter("p1"));
		System.out.println(config.getInitParameter("p2"));
		
		Enumeration e = config.getInitParameterNames();
		while (e.hasMoreElements()) {
			System.out.println(e.nextElement());
		}
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

