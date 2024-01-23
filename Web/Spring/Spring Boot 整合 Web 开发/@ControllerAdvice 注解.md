[toc]

顾名思义，`@ControllerAdvice` 就是 `@Controller` 的增强版。`@ControllerAdvice` 主要用来处理全局数据，一般搭配 `@EceptionHandler`、`@ModelAttribute` 以及 `@InitBinder` 的使用。

### 1. 全局异常处理

`@ControllerAdvice` 最常见的使用场景就是全局异常处理，可以通过 `@ControllerAdvice` 结合 `@ExceptionHandler` 定义全局异常捕获机制，代码如下：

```java
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.multipart.MaxUploadSizeExceededException;

import java.io.IOException;
import java.io.PrintWriter;

@ControllerAdvice
public class CustomExceptionHandler {

    @ExceptionHandler(MaxUploadSizeExceededException.class)
    public void uploadException(MaxUploadSizeExceededException e, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/html;charset=utf-8");
        PrintWriter out = resp.getWriter();
        out.write("上传文件大小超出限制！");
        out.flush();
        out.close();
    }
}
```

只需在系统中定义 `CustomExceptionHandler` 类，然后添加 `@ControllerAdvice` 注解即可。当系统启动时，该类就会被扫描到 `Spring` 容器中，然后定义 `uploadException` 方法，在该方法上添加了 `@ExceptionHandler` 注解，其中定义的 `MaxUploadSizeExceededException.class` 表明该方法用来处理 `MaxUploadSizeExceededException` 类型的异常。如果想让该方法处理所有类型的异常，只需将 `MaxUploadSizeExceededException` 改为 `Exception` 即可。方法的参数可以有异常实例、`HttpServletResponse` 以及 `HttpServletRequest`、`Model` 等，返回值可以是一段 `JSON`、一个 `ModelAndView`、一个逻辑视图名等。

如果返回参数是一个 `ModelAndView`，假设使用的页面模板为 `Thymeleaf` （注意添加 `Thymeleaf` 相关依赖），此时异常处理方法定义如下：

```java
@ControllerAdvice
public class CustomExceptionHandler {

    @ExceptionHandler(MaxUploadSizeExceededException.class)
    public ModelAndView uploadException(MaxUploadSizeExceededException e) throws IOException {
        ModelAndView mv = new ModelAndView();
        mv.addObject("msg", "上传文件大小超出限制!");
        mv.setViewName("error");
        return mv;
    }
}
```

然后在 `resources/templates` 目录下创建 `error.html` 文件，内容如下：

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
    <head>
        <meta charset="UTF-8" />
        <title>错误</title>
    </head>
    <body>
        <div th:text="${msg}"></div>
    </body>
</html>
```

### 2. 添加全局数据

`@ControllerAdvice` 是一个全局数据处理组件，因此也可以在 `@ControllerAdvice` 中配置全局数据，使用 `@ModelAttribute` 注解进行配置，代码如下：

```java
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ModelAttribute;

import java.util.HashMap;
import java.util.Map;

@ControllerAdvice
public class GlobalConfig {

    @ModelAttribute(value = "info")
    public Map<String, String> userInfo() {
        HashMap<String, String> map = new HashMap<>();
        map.put("username", "罗贯中");
        map.put("gender", "男");
        return map;
    }
}
```

代码解释：

+ 在全局配置中添加 `userInfo` 方法，返回一个 `map`。该方法有一个注解 `@ModelAttribute`，其中的 `value` 属性表示这条返回数据的 `key`，而方法的返回值是返回数据的 `value`。
+ 此时在任意请求的 `Controller` 中，通过方法参数中的 `Model` 都可以获取 `info` 的数据。

`Controller` 示例代码如下：

```java
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.Iterator;
import java.util.Map;
import java.util.Set;

@RestController
public class HelloController {

    @GetMapping("/hello")
    @ResponseBody
    public void hello(Model model) {
        Map<String, Object> map = model.asMap();
        Set<String> keySet = map.keySet();
        Iterator<String> iterator = keySet.iterator();
        while (iterator.hasNext()) {
            String key = iterator.next();
            Object value = map.get(key);
            System.out.println(key + ">>>>>>>>" + value);
        }
    }

}
```

也可以通过 `model.getAttribute("info")` 方法获取上面定义的 `Map` 数据，例如：

```java
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

@RestController
public class HelloController {

    @GetMapping("/hello")
    @ResponseBody
    public void hello(Model model) {
        Object info = model.getAttribute("info");
        if (info instanceof HashMap<?, ?>) {
            HashMap<String, String> userInfo = (HashMap<String, String>) info;
            Set<String> keySet = userInfo.keySet();
            Iterator<String> iterator = keySet.iterator();
            while (iterator.hasNext()) {
                String key = iterator.next();
                Object value = userInfo.get(key);
                System.out.println(key + ">>>>>>>>" + value);
            }
        }
    }

}
```

### 3. 请求参数预处理

`@ControllerAdvice` 结合 `@InitBinder` 还能实现请求参数预处理，即将表单中的数据绑定到实体类上时进行一些额外处理。

例如有两个实体类 `Book` 和 `Author`，代码如下：

```java
public class Book {
    private String name;
    private String author;
    // 省略 getter/setter
}

public class Author {
    private String name;
    private int age;
    // 省略 getter/setter
}
```

在 `Controoler` 上需要接收两个实体类的数据，`Controller` 中的方法定义如下：

```java
@RestController
public class BookController {

    @GetMapping("/book")
    @ResponseBody
    public String book(Book book, Author author) {
        return book.toString() + ">>>" + author.toString();
    }
}
```

此时在参数传递时，两个实体类中的 `name` 属性会混淆，`@ControllerAdvice` 结合 `@InitBinder` 可以顺利解决该问题。配置步骤如下：

首先给 `Controller` 中的方法的参数添加 `@ModelAttribute` 注解，代码如下：

```java
@GetMapping("/book")
@ResponseBody
public String book(@ModelAttribute("b") Book book, @ModelAttribute("a") Author author) {
    return book.toString() + ">>>" + author.toString();
}
```

然后配置 `@ControllerAdvice`，代码如下：

```java
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.InitBinder;

@ControllerAdvice
public class GlobalConfig {

    @InitBinder("b")
    public void init(WebDataBinder binder) {
        binder.setFieldDefaultPrefix("b.");
    }

    @InitBinder("a")
    public void init2(WebDataBinder binder) {
        binder.setFieldDefaultPrefix("a.");
    }
}
```

代码解释：

+ 在 `GlobalConfig` 类中创建两个方法，第一个 `@InitBinder("b")` 表示该方法处理 `@ModelAttribute("b")` 对应的参数的，第二个 `@InitBinder("a")` 表示该方法是处理 `@ModelAttribute("a")` 对应的参数的。
+ 每个方法中给相应的 `Field` 设置一个前缀，然后在浏览器中请求 <http://localhost:8080/book?b.name=三国演义&b.author=罗贯中&a.name=曹雪芹&a.age=48>，即可成功地区分出 `name` 属性。
+ 在 `WebDataBinder` 对象中，还可以设置允许的字段、禁止的字段、必填字段以及验证器等。

