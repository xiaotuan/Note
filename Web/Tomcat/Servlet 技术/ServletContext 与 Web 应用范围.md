`Serlet` 容器在启动一个 `Web` 应用时，会为它创建唯一的 `ServletContext` 对象。当 `Servlet` 容器终止一个 `Web` 应用时，就会销毁它的 `ServletContext` 对象。由此可见，`ServletContext` 对象与 `Web` 应用具有同样的生命周期。

"范围" 在这里有两层含义：

+ 表示一个特定时间段。
+ 表示在特定时间段内可以共享数据的所有 `Web` 组件的集合。

`Web` 应用范围具有以下两层含义：

+ 表示由 `Web` 应用的生命周期构成的时间段。
+ 表示在 `Web` 应用的生命周期内所有 `Web` 组件的集合。

存放在 `Web` 应用范围内的共享数据具有以下特定：

+ 共享数据的生命周期位于 `Web` 应用的生命周期中的一个时间片段内。
+ 共享数据可以被 `Web` 应用中的所有 `Web` 组件共享。

利用 `ServletContext` 对象来存取 `Web` 应用范围内的共享数据，基本思想如下：

+ 面向对象编程的一个基本思想就是万物皆对象，因此，共享数据也理所当然地用 `java.lang.Object` 类型的任意 `Java` 对象来表示。
+ 只要把代表共享数据的 `Java` 对象与 `ServletContext` 对象关联，该 `Java` 对象的生命周期就依附于 `ServletContext` 对象的生命周期，并且 `Web` 组件就可以通过 `ServletContext` 对象来访问它。从语义上理解，该 `Java` 对象就被存放到 `Web` 应用范围内。
+ 在 `Web` 应用范围内可以存放各种类型的共享数据。为了方便地存取特定共享数据，可以把代表共享数据的 `Java` 对象作为 `ServletContext` 的属性来存放。每个属性包括一对属性名和属性值。属性值代表共享数据，属性名则用于表示数据共享。

`ServletContext` 接口中常用的用于存取共享数据的方法包括：

+ `setAttribute(String name, Object object)`：向 `Web` 应用范围内存入共享数据。参数 `name` 指定属性名，参数 `object` 表示共享数据。
+ `removeAttribute(String name)`：根据参数给定的属性名，从 `Web` 应用范围内删除匹配的共享数据。
+ `getAttribute(String name)`：根据参数给定的属性名，返回 `Web` 应用范围内匹配的共享数据。

**示例代码：在 Web 应用范围内存放共享数据的范例**
**Counter.java**

```java
package com.qty.web;

public class Counter {

	private int count;	// 计数值
	
	public Counter() {
		this(0);
	}
	
	public Counter(int count) {
		this.count = count;
	}
	
	public void setCount(int count) {
		this.count = count;
	}
	
	public int getCount() {
		return count;
	}
	
	public void add(int step) {
		count += step;
	}
}
```

**CounterServlet.java**

```java
package com.qty.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CounterServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 获得 ServletContext 的引用
		ServletContext context = getServletContext();
		
		// 从 ServletContext 中读取 counter 属性
		Counter counter = (Counter) context.getAttribute("counter");
		
		// 如果 ServletContext 中没有 counter 属性，就创建 counter 属性
		if (counter == null) {
			counter = new Counter();
			context.setAttribute("counter", counter);
		}
		
		resp.setContentType("text/html;charset=GBK");
		PrintWriter out = resp.getWriter();
		out.println("<html><head><title>CounterServlet</title></head>");
		out.println("<body>");
		// 输出当前的 counter 属性
		out.println("<h1>欢迎光临本站，你是第 " + counter.getCount() + " 位访问者。</h1>");
		out.println("</body></html>");
		counter.add(1);	// 将计数器递增 1
		out.close();
	}
}
```

**CounterClearServlet.java**

```java
package com.qty.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CounterClearServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 获得 ServletContext 的引用
		ServletContext context = getServletContext();
		
		context.removeAttribute("counter");	// 删除 counter 属性
		
		PrintWriter out = resp.getWriter();
		out.println("The counter is removed.");
		out.close();
	}
}
```

**web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>CounterServlet</display-name>
  <welcome-file-list>
    <welcome-file>counter</welcome-file>
  </welcome-file-list>
  <servlet>
  	<servlet-name>counter</servlet-name>
  	<servlet-class>com.qty.web.CounterServlet</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>counter</servlet-name>
  	<url-pattern>/counter</url-pattern>
  </servlet-mapping>
  <servlet>
  	<servlet-name>clear</servlet-name>
  	<servlet-class>com.qty.web.CounterClearServlet</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>clear</servlet-name>
  	<url-pattern>/clear</url-pattern>
  </servlet-mapping>
</web-app>
```

