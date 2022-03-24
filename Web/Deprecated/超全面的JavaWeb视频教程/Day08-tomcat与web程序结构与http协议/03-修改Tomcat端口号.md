打开 %CATALANA_HOME%\conf\server.xml 文件：

```xml
<Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
```

只需将上面 `port="8080"` 中的 8080 修改成自己想要的端口号即可。

当把端口号修改为 80 后，在浏览器中只需要输入：<http://localhost> 就可以访问 Tomcat 主页了。