[toc]

`Servlet` 的生命周期可以分为 3 个阶段：初始化阶段、运行时阶段和销毁阶段。在 `javax.servlet.Servlet` 接口中定义了 3 个方法：`init()`、`service()` 和 `destroy()`，它们将分别在 `Servlet` 的不同阶段被 `Servlet` 容器调用。

### 1. 初始化阶段

`Servlet` 的初始化阶段包括四个步骤：

（1）`Servlet` 容器加载 `Servlet` 类，把它的 `.class` 文件中的数据读入到内存中。

（2）`Servlet` 容器创建 `ServletConfig` 对象。`ServletConfig` 对象包含了特定 `Servlet` 的初始化配置信息，如 `Servlet` 的初始参数。此外，`Servlet` 容器还会使得 `ServletConfig` 对象与当前 `Web` 应用的 `ServletContext` 对象关联。

（3）`Servlet` 容器创建 `Servlet` 对象。

（4）`Servlet` 容器调用 `Servlet` 对象的 `init(ServletConfig config)` 方法。在 `Servlet` 接口的 `GenericServlet` 实现类的 `init(ServletConfig config)` 类的 `init(ServletConfig config)` 方法中，会建立 `Servlet` 对象与 `ServletConfig` 对象的关联关系。

以上初始化步骤创建了 `Servlet` 对象和 `ServletConfig` 对象，并且 `Servlet` 对象与 `ServletConfig` 对象关联，而 `ServletConfig` 对象与当前 `Web` 应用的 `ServletContext` 对象关联。当 `Servlet` 容器初始化完 `Servlet` 后，`Servlet` 对象只要通过 `getServletContext()` 方法就能得到当前 `Web` 应用的 `ServletContext` 对象。

在下列情况之一，`Servlet` 会进入初始化阶段：

（1）当前 `Web` 应用处于运行时阶段，特定 `Servlet` 被客户端首次请求访问。多数 `Servlet` 都会在这种情况下被 `Servlet` 容器初始化。

（2）如果在 `web.xml` 文件中为一个 `Servlet` 设置了 `<load-on-startup>` 元素，那么当 `Servlet` 容器启动 `Servlet` 所属的 `Web` 应用时，就会初始化这个 `Servlet`。以下代码配置了是三个 `Servlet`：`servlet1`、`Servlet2` 和 `ServletX`。

```xml
<servlet>
	<servlet-name>servlet1</servlet-name>
    <servlet-class>Servlet1</servlet-classs>
    <load-on-startup>1</load-on-startup>
</servlet>
<servlet>
	<servlet-name>servlet2</servlet-name>
    <servlet-class>Servlet2</servlet-classs>
    <load-on-startup>2</load-on-startup>
</servlet>
<servlet>
	<servlet-name>servletX</servlet-name>
    <servlet-class>ServletX</servlet-classs>
</servlet>
```

其中 `Servlet1` 和 `Servlet2` 的 `<load-on-startup>` 的值分别为 1 和 2，因此当 `Servlet` 容器启动当前 `Web` 应用时，`Servlet1` 被第一个初始化，`Servlet2` 被第二个初始化。而 `ServletX` 没有配置 `<load-on-startup>` 元素，因此当 `Servlet` 容器启动当前 `Web` 应用时，`ServletX` 不会被初始化，只有当客户端首次请求访问 `ServletX` 时，它才会被初始化。

（3）当 `Web` 应用被重新启动时，`Web` 应用中的所有 `Servlet` 都会在特定的时刻被重新初始化。

### 2. 运行时阶段

在这个阶段，`Servlet` 可以随时响应客户端的请求。当 `Servlet` 容器接收到要求访问特定 `Servlet` 的客户请求，`Servlet` 容器创建针对于这个请求的 `ServletRequest` 对象和 `ServletResponse` 对象，然后调用相应 `Servlet` 对象的 `Service()` 方法。`service()` 方法从 `ServletRequest` 对象中获得客户请求信息并处理该请求，通过 `ServletResponse` 对象生成响应结果。

当 `Servlet` 容器把 `Servlet` 生成的响应结果发送给了客户，`Servlet` 容器就会销毁 `ServletRequest` 对象和 `ServletResponse` 对象。

### 3. 销毁阶段

当 `Web` 应用被终止时，`Servlet` 容器会先调用 `Web` 应用中所有 `Servlet` 对象的 `destroy()` 方法，然后再销毁这些 `Servlet` 对象。在 `destroy()` 方法的实现中，可以释放 `Servlet` 所占用的资源。

### 4. 演示 Servlet  的上面周期的范例

**LifeServlet.java**

```java
package com.qty.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.GenericServlet;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class LifeServlet extends GenericServlet {
	
	private int initVar = 0;
	private int serviceVar = 0;
	private int destroyVar = 0;
	private String name;
	
	@Override
	public void init(ServletConfig config) throws ServletException {
		super.init(config);
		name = config.getServletName();
		initVar++;
		System.out.println(name + ">init(): Servlet 被初始化了 " + initVar + " 次");
	}
	
	@Override
	public void destroy() {
		destroyVar++;
		System.out.println(name + ">destroy(): Servlet 被销毁了 " + destroyVar + " 次");
	}

	@Override
	public void service(ServletRequest req, ServletResponse rsp) throws ServletException, IOException {
		serviceVar++;
		System.out.println(name + ">service(): Servlet 共响应了 " + serviceVar + " 次请求");
		
		String content1 = "初始化次数：" + initVar;
		String content2 = "响应客户请求次数：" + serviceVar;
		String content3 = "销毁次数：" + destroyVar;
		
		rsp.setContentType("text/html;charset=GBK");
		
		PrintWriter out = rsp.getWriter();
		out.print("<html><head><title>LifeServlet</title>");
		out.print("</head><body>");
		out.print("<h1>" + content1 + "</h1>");
		out.print("<h1>" + content2 + "</h1>");
		out.print("<h1>" + content3 + "</h1>");
		out.print("</body></html>");
		out.close();
	}

}
```

**Web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>LiftServlet</display-name>
  <welcome-file-list>
    <welcome-file>LifeInit</welcome-file>
  </welcome-file-list>
  <servlet>
  	<servlet-name>lifeInit</servlet-name>
  	<servlet-class>com.qty.web.LifeServlet</servlet-class>
  	<load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
  	<servlet-name>lifeInit</servlet-name>
  	<url-pattern>/LifeInit</url-pattern>
  </servlet-mapping>
  <servlet>
  	<servlet-name>life</servlet-name>
  	<servlet-class>com.qty.web.LifeServlet</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>life</servlet-name>
  	<url-pattern>/life</url-pattern>
  </servlet-mapping>
</web-app>
```

