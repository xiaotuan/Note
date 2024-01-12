[toc]

> 提示：
>
> 关于 `FreeMarker` 的更多资料，可以查看 <https://freemarker.apache.org/>

`FreeMarker` 是一个非常古老的模板引擎，可以用在 `Web` 环境或者非 `Web` 环境中。与 `Thymeleaf` 不同，`FreeMarker` 需要警告解析才能够在浏览器中展示出来。`FreeMarker` 不仅可以用来配置 `HTML` 页面模板，也可以作为电子邮件模板、配置文件模板以及源码模板等。Spring Boot 中对 `FreeMarker` 整合也提供了很好的支持，主要整合步骤如下：

### 1. 创建项目，添加依赖

首先创建 `Spring Boot` 项目，然后添加 `spring-boot-starter-web` 和 `spring-boot-starter-freemarker` 依赖，代码如下：

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-freemarker</artifactId>
</dependency>
```

### 2. 配置 FreeMarker

`Spring Boot` 对 `FreeMarker` 也提供了自动化配置类 `FreeMarkerAutoConfiguration`，相关的配置属性在 `FreeMarkerProperties` 中，`FreeMarkerProperties` 部分源代码如下：

```java
@ConfigurationProperties(
    prefix = "spring.freemarker"
)
public class FreeMarkerProperties extends AbstractTemplateViewResolverProperties {
    public static final String DEFAULT_TEMPLATE_LOADER_PATH = "classpath:/templates/";
    public static final String DEFAULT_PREFIX = "";
    public static final String DEFAULT_SUFFIX = ".ftlh";
    ...
}
```

从该默认配置中可以看到，`FreeMarker` 默认模板位置和 `Thymeleaf` 一样，都在 `classpath:/templates/` 中，默认文件后缀是 `.ftlh`。开发者可以在 `application.properties` 中对这些默认配置进行修改，部分常见配置如下：

```properties
# HttpServletRequest 的属性是否可以覆盖 controller 中 model 的同名项
spring.freemarker.allow-request-override=false
# HttpSession 的属性是否可以覆盖 controller 中 model 的同名项
spring.freemarker.allow-session-override=false
# 是否开启缓存
spring.freemarker.cache=false
# 模板文件编码
spring.freemarker.charset=UTF-8
# 是否检查模板位置
spring.freemarker.check-template-location=true
# Content-Type 的值
spring.freemarker.content-type=text/html
# 是否将 httpServletRequest 中的属性添加到 Model 中
spring.freemarker.expose-request-attributes=false
# 是否将 HttpSession 中的属性添加到 Model 中
spring.freemarker.exprose-session-attributes=false
# 模板文件后缀
spring.freemarker.suffix=.ftlh
# 模板文件位置
spring.freemarker.template-loader-path=classpath:/templates/
```

### 3. 配置控制器

创建 `Book` 实体类，然后在 `Controller` 中返回 `ModelAndView`，代码如下：

**Book.java**

```java
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

public class Book {
    private Integer id;
    private String name;
    private String author;
    // 省略 getter/setter
}
```

**BookController.java**

```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.util.ArrayList;
import java.util.List;

@RestController
public class BookController {

    @GetMapping("/books")
    public ModelAndView books() {
        List<Book> books = new ArrayList<>();
        Book b1 = new Book();
        b1.setId(1);
        b1.setAuthor("罗贯中");
        b1.setName("三国演义");
        Book b2 = new Book();
        b2.setId(2);
        b2.setAuthor("曹雪芹");
        b2.setName("红楼梦");
        books.add(b1);
        books.add(b2);
        ModelAndView mv = new ModelAndView();
        mv.addObject("books", books);
        mv.setViewName("books");
        return mv;
    }
}
```

### 4. 创建视图

按照配置文件，在 `resources/templates` 目录下创建 `books.ftl` 文件，内容如下：

```ftl
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>图书列表</title>
    </head>
    <body>
        <table border="1">
            <tr>
                <td>图书编号</td>
                <td>图书名称</td>
                <td>图书作者</td>
            </tr>
            <#if books?? && (books?size>0)>
            <#list books as book>
            <tr>
                <td>${book.id}</td>
                <td>${book.name}</td>
                <td>${book.author}</td>
            </tr>
            </#list>
            </#if>
        </table>
    </body>
</html>
```

