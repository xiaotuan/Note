[toc]

在 Spring Boot 项目中，可以内置 Tomcat、Jetty、Undertow、Netty 等容器。

### 1. Tomcat 配置

#### 1.1 常规配置

当开发者添加了 `spring-boot-starter-web` 依赖之后，默认会使用 `Tomcat` 作为 `web` 容器。如果需要对 `Tomcat` 做进一步的配置，可以在 `application.properties` 中进行配置，代码如下：

```properties
server.port=8081
server.error.path=/error
server.servlet.session.timeout=30m
server.servlet.context-path=/
server.tomcat.uri-encoding=utf-8
server.tomcat.max-threads=500
server.tomcat.basedir=C:\WorkSpaces\TempSpace
```

文件路径如下：

![02](./images/02.png)