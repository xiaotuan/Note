### 1. 创建静态应用

+ 在 webapps 下创建一个 hello 目录；
+ 在 webapps\hello\ 目录下创建 index.html；
+ 启动 tomcat;
+ 打开浏览器访问：<http://localhost:8080/hello/index.html>

**index.html**

```html
<!DOCTYPE html>
<html lang="utf-8">
    <head>
        <title>hello - html</title>
    </head>
    <body>
        <h1>Hello1</h1>
    </body>
</html>
```

### 2. 创建动态应用

+ 在 webapps 目录下创建一个项目目录；

+ 在项目目录下创建如下内容：

  + WEB-INF 目录；

    + 在 WEB-INF 目录下创建 web.xml 文件。(可以拷贝其他网站下的 web.xml 内容)
  + 创建静态或动态页面

目录结构：

```txt
hello2
	|__ index.html
	|__ index.jsp
	|__ WEB_INF
			|__ web.xml
```

**web.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

</web-app>
```

**index.html**

```html
<!DOCTYPE html>
<html lang="utf-8">
    <head>
        <title>hello2 - html</title>
    </head>
    <body>
        <h1>Hello2</h1>
    </body>
</html>
```

**index.jsp**

```jsp
<%@page pageEncoding="utf-8"%>
<!DOCTYPE html>
<html lang="utf-8">
    <head>
        <title>hello2 - html</title>
    </head>
    <body>
        <h1>Hello2</h1>
        <h3>
            ${header['User-Agent']}
        </h3>
    </body>
</html>
```

