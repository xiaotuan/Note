[toc]

### 1. 常规配置

在创建一个 `Spring Boot` 项目时，引入的 `spring-boot-starter-web` 依赖间接地引入了 `snakeyaml` 依赖，`snakeyaml` 会实现对 `YAML` 配置的解析。`YAML` 的使用非常简单，利用缩进来表示层级关系，并且大小写敏感。在 `Spring Boot` 项目中使用 `YAML` 只需要在 `resources` 目录下创建一个 `application.yml` 文件即可，然后向 `application.yml` 中添加如下配置：

```yaml
server:
	port: 80
	servlet:
		context-path: /chapter02
	tomcat:
		uri-encoding: utf-8
```

这段配置等效于 `application.properties` 中的如下配置：

```properties
server.port=80-
server.servlet.context-path=/chapter02
server.tomcat.uri-encoding=utf-8
```

### 2. 复杂配置

`YAML` 不仅可以配置常规属性，也可以配置复杂属性，例如下面一组配置：

```yaml
my:
	name: 江南一点雨
	address: China
```

像 `Properties` 配置文件一样，这段配置也可以注入一个 `Bean` 中，代码如下：

```java
package com.qty.springweb;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "my")
public class User {
    private String name;
    private String address;
    // 省略 getter/setter
}
```

`YAML` 还支持列表的配置，例如下面一组配置：

```yaml
my:
	name: 江南一点雨
	address: China
	favorites:
		- 足球
		- 徒步
		- Coding
```

这一组配置可以注入如下 `Bean` 中：

```java
package com.qty.springweb;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
@ConfigurationProperties(prefix = "my")
public class User {
    private String name;
    private String address;
    private List<String> favorites;
    // 省略 getter/setter
}
```

`YAML` 还支持更复杂的配置，即集合中也可以是一个对象，例如下面一组配置：

```yaml
my:
	users:
        - name: 江南一点雨
          address: China
          favorites:
              - 足球
              - 徒步
              - Coding
        - name: sang
          address: GZ
          favorites:
              - 阅读
              - 吉他
```

这一组配置可以注入如下 `Bean` 中：

```java
package com.qty.springweb;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
@ConfigurationProperties(prefix = "my")
public class Users {
	private List<User> users;
    // 省略 getter/setter
}
```

在 `Spring Boot` 中使用 `YAML` 虽然方便，但是 `YAML` 也有一些缺陷，例如无法使用 `@PropertySource` 注解加载 `YAML` 文件，如果项目中有这种需求，还是需要使用 `Properties` 格式的配置文件。