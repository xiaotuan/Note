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

```java

```

