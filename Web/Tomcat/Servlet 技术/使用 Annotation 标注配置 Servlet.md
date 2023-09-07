> 提示：`Tomcat` 标注文档网址：<https://tomcat.apache.org/tomcat-9.0-doc/servletapi/javax/servlet/annotation/package-summary.html>

从 `Servlet 3` 版本开始，为了简化对 `Web` 组件的发布过程，可以不必在 `web.xml` 文件中配置 `Web` 组件，而是直接在相关的类中使用 `Annotation` 标注来配置发布信息。

**1. 在 Servlet 类中加入 @WebServlet 标注**

在 `web.xml` 文件中的配置如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>FontServlet</display-name>
  <welcome-file-list>
    <welcome-file>font</welcome-file>
  </welcome-file-list>
  <servlet>
	<servlet-name>Font</servlet-name>
    <servlet-class>mypack.FontServlet</servlet-class>
    <init-param>
    	<param-name>color</param-name>
        <param-value>blue</param-value>
    </init-param>
    <init-param>
    	<param-name>size</param-name>
        <param-value>15</param-value>
    </init-param>
  </servlet>

  <servlet-mapping>
    <servlet-name>Font</servlet-name>
    <url-pattern>/font</url-pattern>
  </servlet-mapping>
</web-app>
```

在 `FontServlet.java` 中可以使用 `@WebServlet` 标注来达到同样的目的：

```java
package mypack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.jws.WebService;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.annotation.*;

@WebServlet(name="FontServlet",
	urlPatterns={"/font"},
    initParams= {
    	@WebInitParam(name="color",value="blue"),
    	@WebInitParam(name="size", value="15")
    }
)
public class FontServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 获得 word 请求参数
		String word = req.getParameter("word");
		if (word == null) {
			word = "Hello";
		}
		
		// 读取初始化参数
		String color = getInitParameter("color");
		String size = getInitParameter("size");
		System.out.println("servletName: " + getServletName());	// 打印 servletName: Font
		
		// 设置 HTTP 响应的正文的 MIME 类型及字符编码
		resp.setContentType("text/html;charset=GBK");
		
		// 输出 HTML 文档
		PrintWriter out = resp.getWriter();
		out.println("<html><head><title>FontServlet</title></head>");
		out.println("<body>");
		out.println("<font size='" + size + "' color='" + color + "'>" + word + "</font>");
		out.println("</body></html>");
		
		out.close();	// 关闭 PrintWriter
	}
}
```

标注类位于 `javax.servlet.annotation` 包中，所以必须在 `FontServlet` 类中引入这个包：

```java
import javax.servlet.annotation.*;
```

> 提示：
>
> 对于一个 `Servlet`，到底按哪种方式来配置呢？如果这个 `Servlet` 的配置信息固定，不会发生变化，那么使用 `@WebServlet` 标注会更加方便。如果 `Servlet` 的配置信息可能会发生变化，那么在 `web.xml` 文件中进行配置会更加灵活。

`@WebServlet` 标注的各个属性和 `web.xml` 文件中配置 `Servlet` 的特定元素对应，下表介绍了 `@WebServlet` 标注的各个属性的用法。

| 属性             | 类型             | 描述                                                         |
| ---------------- | ---------------- | ------------------------------------------------------------ |
| `name`           | `String`         | 指定 `Servlet` 的名字，等价于 `<servlet-name>` 元素。如果没有显示指定，则其默认值为类的全限定名 |
| `urlPatterns`    | `String[]`       | 指定一组 `Servlet` 的 `URL` 匹配模式，等价于 `<url-pattern>` 元素。 |
| `loadOnStartup`  | `int`            | 指定 `Servlet` 的加载顺序，等价于 `<load-on-startup>` 元素   |
| `initParams`     | `WebInitParam[]` | 声明 `Servlet` 初始化参数，等价于 `<init-param>` 元素。      |
| `asyncSupported` | `boolean`        | 声明 `Servlet` 是否支持异步处理模式，等价于 `<async-supported>` 元素 |
| `description`    | `String`         | 指定 `Servlet` 的描述信息，等价于 `<description>` 元素       |
| `displayName`    | `String`         | 指定 `Servlet` 的显示名，通常配合工具使用，等价于 `<display-name>` 元素 |

`@WebServlet` 的 `urlPatterns` 属性有多种设置方式，以下是一些示范代码：

```java
// 访问 Servlet 的 URL 为：/hello
@WebServlet("/hello")

// 访问 Servlet 的 URL 为：/hello
@WebServlet(urlPatterns = {"/hello"})

// 访问 Servlet 的 URL 为： /hello1 或者 /hello2
@WebServlet(urlPatterns = { "/hello1", "/hello2" })

/* 访问 Servlet 的 URL 为所有以 ".do" 结尾的 URL,例如：
	/add.do 或者 /delete.do 或者 /update.do 等 */
@WebServlet(urlPatterns = {"*.do"})
```

**2. 在 ServletContextListener 类中加入 @WebListener 标注**

在 `web.xml` 文件中对 `ServletContextListener` 的配置如下：

```xml
<listener>
  	<listener-class>com.qty.web.MyServletContextListener</listener-class>
</listener>
```

如果在 `MyServletContextListener` 类中加入如下 `@WebListener` 标注，就不用在 `web.xml` 文件中进行上述配置了：

```java
package com.qty.web;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

@WebListener
public class MyServletContextListener implements ServletContextListener {

	@Override
	public void contextInitialized(ServletContextEvent sce) {
		System.out.println("helloapp apllication is Initialized.");
		
		// 获取 ServletContext 对象
		ServletContext context = sce.getServletContext();
		
		try {
			// 从文件中读取计数器的数值
			BufferedReader reader = new BufferedReader(
					new InputStreamReader(context.getResourceAsStream("/count/count.txt")));
			
			int count = Integer.parseInt(reader.readLine());
			reader.close();
			
			// 创建计数器对象
			Counter counter = new Counter(count);
			// 把计数器对象保存到 Web 应用范围
			context.setAttribute("counter", counter);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	@Override
	public void contextDestroyed(ServletContextEvent sce) {
		System.out.println("helloapp application is Destroyed.");
		
		// 获取 ServletContext 对象
		ServletContext context = sce.getServletContext();
		// 从 Web 应用范围获得计数器对象
		Counter counter = (Counter) context.getAttribute("counter");
		
		if (counter != null) {
			try {
				// 把计数器的数值写到 count.txt 文件中
				String filePath = context.getRealPath("/count");
				filePath = filePath + "/count.txt";
				PrintWriter pw = new PrintWriter(filePath);
				pw.println(counter.getCount());
				pw.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
```

