[toc]

+ 一个项目只有一个 ServletContext 对象。
+ 我们可以在 N 多个 Servlet 中来获取这个唯一的对象，使用它可以给多个 Servlet 传递数据。
+ 这个对象在 Tomcat 启动时就创建，在 Tomcat 关闭时才会死去。

### 1. 获取 ServletContext

```java
HttpServlet.getServletContext();
HttpServlet.getServletConfig().getServletContext();
HttpSession.getServletContext();
ServletContextEvent.getServletContext();
```

### 2. 使用 ServletContext 保存数据

**AServlet.java** 存储数据

```java
package com.qty.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class AServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        /*
         * 1. 获取 ServletContext 对象
         * 2. 调用 setAttribute() 方法完成保存数据
         */
        ServletContext application = getServletContext();
        application.setAttribute("name", "张三");
        resp.getWriter().append("Server at: ").append(req.getContextPath());
    }
}
```

**BServlet.java** 读取数据

```java
package com.qty.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * 演示从 ServletContext 中获取数据
 */
public class BServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        /*
         * 1. 获取 ServletContext 对象
         * 2. 调用其 getAttribute() 方法完成获取数据
         */
        ServletContext application = getServletContext();
        String name = (String)application.getAttribute("name");
        System.out.println(name);
    }
}
```

**web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <servlet>
        <servlet-name>AServlet</servlet-name>
        <servlet-class>com.qty.servlet.AServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>AServlet</servlet-name>
        <url-pattern>/AServlet</url-pattern>
    </servlet-mapping>

    <servlet>
        <servlet-name>BServlet</servlet-name>
        <servlet-class>com.qty.servlet.BServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>BServlet</servlet-name>
        <url-pattern>/BServlet</url-pattern>
    </servlet-mapping>

</web-app>
```

