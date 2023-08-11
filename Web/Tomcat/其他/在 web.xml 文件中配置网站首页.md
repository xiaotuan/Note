在 `web.xml` 文件中添加 `<welcome-file-list>` 节点配置网站首页，例如：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>sdfsd</display-name>
  <welcome-file-list>
  	<welcome-file>info</welcome-file>
    <welcome-file>index.html</welcome-file>
    <welcome-file>index.jsp</welcome-file>
    <welcome-file>index.htm</welcome-file>
    <welcome-file>default.html</welcome-file>
    <welcome-file>default.jsp</welcome-file>
    <welcome-file>default.htm</welcome-file>
  </welcome-file-list>
  <servlet>
        <servlet-name>info</servlet-name>
        <servlet-class>sdfsd.RequestInfoServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>info</servlet-name>
        <url-pattern>/info</url-pattern>
    </servlet-mapping>
</web-app>
```

上面代码中将 `info` 容器配置成首页。