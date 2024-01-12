在项目发布之前，一般需要频繁地在开发环境、测试环境以及生成环境之间进行切换，这个时候大量的配置需要频繁更改。频繁修改带来了巨大的工作量，`Spring` 对此提供了解决方案（`@Profile` 注解），`Spring Boot` 则更进一步提供了更加简洁的解决方案，`Spring Boot` 中约定的不同环境下配置文件名称规则为 `application-{profile}.properties`，`profile` 占位符表示当前环境的名称，具体配置步骤如下：

### 1. 创建配置文件

首先在 `resources` 目录下创建两个配置文件：`application-dev.properties` 和 `application-prod.properties`，分别表示开发环境中的配置和生产环境中的配置。其中，`application-dev.properties` 文件的内容如下：

```properties
server.port=8080
```

`application-prod.properties` 文件的内容如下：

```properties
server.port=80
```

### 2. 配置 application.properties

然在 `application.properties` 中进行配置：

```properties
spring.profiles.active=dev
```

### 3. 在代码中配置

在启动类的 `main` 方法上添加如下代码，可以替换第二步的配置：

```java
SpringApplicationBuilder builder = new SpringApplicationBuilder(App.class);
builder.application().setAdditionalProfiles("prod");
builder.run(args);
```

### 4. 项目启动时配置

也可以在将项目打包成 jar 后启动时，在命令行动态指定当前环境，示例命令如下：

```shell
$ java -jar chapter01-3-0.0.1-SNAPSHOT.jar --spring.profiles.active=prod
```

