在 `Servlet` API 中有一个 `ServletContextListener` 接口，它能够监听 `ServletContext` 对象的生命周期，实际上就是监听 `Web` 应用的生命周期。

在 `ServletContextListener` 接口中定义了处理 `ServletContextEvent` 事件的两个方法：

+ `contextInitialized(ServletContextEvent sce)`：当 `Servlet` 容器启动 `Web` 应用时调用该方法。在调用完该方法之后，容器再对 `Filter` 初始化，并且对那些在 `Web` 应用启动时就需要初始化的 `Servlet` 进行初始化。
+ `contextDestroyed(ServletContextEvent sce)`：当 `Servlet` 容器终止 `Web` 应用时调用该方法。在调用该方法之前，容器会先销毁所有的 `Servlet` 和 `Filter` 过滤器。

用户自定义的 `ServletContextListener` 监听器必须先向 `Servlet` 容器注册，`Servlet` 容器在启动或终止 `Web` 应用时，才会调用该监听器的相关方法。在 `web.xml` 文件中，`<listener>` 元素用于向容器注册监听器：

```xml
<listener>
	<listener-class>com.qty.web.MyServletContextListener</listener-class>
</listener>
```

如果不在 `web.xml` 文件中配置，那可以在 `MyServletContextListener` 类中用 `@WebListener` 标注来配置。

> 注意：当 `Servlet` 容器调用 `ServletContextListener` 监听器的 `contextDestroyed()` 方法时，该监听器所在的 `Web` 应用的 `Servlet` 以及 `Filter` 等对象都已经被销毁，因此在 `contextDestroyed()` 方法中不能访问这些对象，此外，也不能通过 `ServletContext.getAttribute()` 方法访问 `Web` 应用范围内的共享数据。

> 提示：下面示例中，需要在 `Web` 应用根目录下创建一个 `count` 目录，并且在 `count` 目录中创建一个名称为 `count.txt` 的文件，该文件中存放了一个数字 "5"。

**示例代码：**

**MyServletContextListener.java**

```java
package com.qty.web;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

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

**web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>MyServletContextListener</display-name>
  <welcome-file-list>
    <welcome-file>counter</welcome-file>
  </welcome-file-list>
  <listener>
  	<listener-class>com.qty.web.MyServletContextListener</listener-class>
  </listener>
  <servlet>
  	<servlet-name>counter</servlet-name>
  	<servlet-class>com.qty.web.CounterServlet</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>counter</servlet-name>
  	<url-pattern>/counter</url-pattern>
  </servlet-mapping>
</web-app>
```

