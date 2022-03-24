[toc]

### 16. ServletContext 获取公共的初始化参数

+ Servlet 也可以获取初始化参数，但它是局部的参数；也就是说，一个 Servlet 只能获取自己的初始化参数，不能获取别人的，即初始化参数只为一个 Servlet 准备！

  例如下面的 AServlet 只能获取自己定义的 name 参数，不能获取 BServlet 中的 age 参数，也不能获取 context-param 中定义的公共参数：

  **web.xml**

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
           version="4.0">
      
      <context-param>
          <param-name>address</param-name>
          <param-value>北京市</param-value>
      </context-param>
  
      <servlet>
          <servlet-name>AServlet</servlet-name>
          <servlet-class>com.qty.servlet.AServlet</servlet-class>
          <init-param>
              <param-name>name</param-name>
              <param-value>张三</param-value>
          </init-param>
      </servlet>
  
      <servlet-mapping>
          <servlet-name>AServlet</servlet-name>
          <url-pattern>/AServlet</url-pattern>
      </servlet-mapping>
  
      <servlet>
          <servlet-name>BServlet</servlet-name>
          <servlet-class>com.qty.servlet.BServlet</servlet-class>
          <init-param>
              <param-name>age</param-name>
              <param-value>23</param-value>
          </init-param>
      </servlet>
  
      <servlet-mapping>
          <servlet-name>BServlet</servlet-name>
          <url-pattern>/BServlet</url-pattern>
      </servlet-mapping>
  
  </web-app>
  ```

+ 可以配置公共的初始化参数，为所有 Servlet 而用！这需要使用 ServletContext 才能使用！

公共初始化参数使用 context-param 标签进行配置，方法如下：

**web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    
    <context-param>
        <param-name>address</param-name>
        <param-value>北京市</param-value>
    </context-param>
    
</web-app>
```

获取公共初始化参数的方法如下所示：

**CServlet.java**

```java
package com.qty.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * 演示 servletContext 获取公共的初始化参数
 */
public class CServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        /*
         * 1. 得到 ServletContext
         * 2. 调用它 getInitParameter(String) 得到初始化参数
         */
        ServletContext app = getServletContext();
        String value = app.getInitParameter("address");
        System.out.println(value);
    }
}
```

