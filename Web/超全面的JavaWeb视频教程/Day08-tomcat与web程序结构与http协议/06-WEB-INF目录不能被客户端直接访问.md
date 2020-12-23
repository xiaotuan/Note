WEB-INF 目录下可以创建 classes 和 lib 目录。classes 目录用于存储 class 文件；lib 目录用于存放 jar 包。

WEB-INF 目录名称必须大写，这个目录下的东西是无法通过浏览器直接访问的，也就是说放到这里的东西是安全的。

web.xml 文件是应用程序的部署描述符文件，可以在该文件中对应用进行配置，例如配置应用的首页：

```xml
<welcome-file-list>
	<welcome-file>index.html</welcome-file>
</welcome-file-list>
```

### 