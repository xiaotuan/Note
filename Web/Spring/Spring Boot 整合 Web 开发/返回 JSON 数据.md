[toc]

### 1. 默认实现

默认情况下，当开发者新创建一个 `Spring Boot` 项目后，添加 `Web` 依赖，代码如下：

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

这个依赖中默认加入了 `jackson-databing` 作为 `JSON` 处理器，此时不需要添加额外的 `JSON` 处理器就能返回一段 `JSON` 了。创建一个 `Book` 实体类：

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;

import java.util.Date;

public class Book {
    
    private String name;
    private String author;
    @JsonIgnore
    private Float price;
    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date publicationDate;
    // 省略 getter/setter
}
```

然后创建 `BookController`，返回 `Book` 对象即可：

```java
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Date;

@Controller
public class BookController {

    @GetMapping("/book")
    @ResponseBody
    public Book book() {
        Book book = new Book();
        book.setAuthor("罗贯中");
        book.setName("三国演义");
        book.setPrice(30f);
        book.setPublicationDate(new Date());
        return book;
    }
}
```

如果需要频繁地用到 `@ResponseBody` 注解，那么可以采用 `@RestController` 组合注解代替 `@Controller` 和 `@ResponseBody`，代码如下：

```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Date;

@RestController
public class BookController {

    @GetMapping("/book")
    public Book book() {
        Book book = new Book();
        book.setAuthor("罗贯中");
        book.setName("三国演义");
        book.setPrice(30f);
        book.setPublicationDate(new Date());
        return book;
    }
}
```

这是 `Spring Boot` 自带的处理方式。如果采用这种方式，那么对于字段忽略、日期格式化等常见需求都可以通过注解来解决。这是通过 `Spring` 中默认提供的 `MappingJackson2HttpMessageConverter` 来实现的。

### 2. 自定义转换器

#### 2.1 使用 Gson

`Gson` 是 `Google` 的一个开源 `JSON` 解析框架。使用 `Gson`，需要先除去默认的 `jackson-databind`，然后加入 `Gson` 依赖，代码如下：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
</dependency>
```

由于 `Spring Boot` 中默认提供了 `Gson` 的自动转换类 `GsonHttpMessageConvertersConfiguration`，因此 `Gson` 的依赖添加成功后，可以像使用 `jackson-databind` 那样直接使用 `Gson`。但是在 `Gson` 进行转换时，如果想对日期数据进行格式化，那么还需要开发者自定义 `HttpMessageConverter`。自定义 `HttpMessageConverter` 可以通过如下方式。

首先看 `GsonHttpMessageConvertersConfiguration` 中的一段源码：

```java
@Bean
@ConditionalOnMissingBean
public GsonHttpMessageConverter gsonHttpMessageConverter(Gson gson) {
    GsonHttpMessageConverter converter = new GsonHttpMessageConverter();
    converter.setGson(gson);
    return converter;
}
```

> 注意：
>
> 在最新版本中没有找到 `GsonHttpMessageConvertersConfiguration` 类。

`@ConditionalOnMissingBean` 注解表示当项目中没有提供 `GsonHttpMessageConverter` 时才会使用默认的 `GsonHttpMessageConverter`，所以开发者只需要提供一个 `GsonHttpMessageConverter` 即可，代码如下：

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.converter.json.GsonHttpMessageConverter;

import java.lang.reflect.Modifier;

@Configuration
public class GsonConfig {

    @Bean
    GsonHttpMessageConverter gsonHttpMessageConverter() {
        GsonHttpMessageConverter converter = new GsonHttpMessageConverter();
        GsonBuilder builder = new GsonBuilder();
        builder.setDateFormat("yyyy-MM-dd");
        builder.excludeFieldsWithModifiers(Modifier.PROTECTED);
        Gson gson = builder.create();
        converter.setGson(gson);
        return converter;
    }
}
```

此时，将 `Book` 类中的 `price` 字段的修饰符改为 `protected`，代码如下：

```java
import com.alibaba.fastjson.annotation.JSONField;

import java.util.Date;

public class Book {

    private String name;
    private String author;
    @JSONField(serialize = false)
    private Float price;
    private Date publicationDate;
    // 省略 getter/setter
}
```

#### 2.2 使用 fastjson

不同于 `Gson`，`fastjson` 继承完成之后并不能立马使用，需要开发者提供相应的 `HttpMessageConverter` 后才能使用，集成 `fastjson` 的步骤如下：

首先除去 `jackson-databind` 依赖，引入 `fastjson` 依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.1</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.15.3</version>
</dependency>
```

然后配置 `fastjson` 的 `HttpMessageConverter`：

```java
package org.example;

import com.alibaba.fastjson.serializer.SerializerFeature;
import com.alibaba.fastjson.support.config.FastJsonConfig;
import com.alibaba.fastjson.support.spring.FastJsonHttpMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.MediaType;

import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

@Configuration
public class MyFastJsonConfig {

    @Bean
    FastJsonHttpMessageConverter fastJsonHttpMessageConverter() {
        FastJsonHttpMessageConverter converter = new FastJsonHttpMessageConverter();
        FastJsonConfig config = new FastJsonConfig();
        config.setDateFormat("yyyy-MM-dd");
        config.setSerializerFeatures(
                // 去掉 JSON 数据中的 "@type":"org.example.Book" 项
                // SerializerFeature.WriteClassName,
                SerializerFeature.WriteMapNullValue,
                SerializerFeature.PrettyFormat,
                SerializerFeature.WriteNullListAsEmpty,
                SerializerFeature.WriteNullStringAsEmpty
        );
		// 解决中文乱码问题
        List<MediaType> supportedMediaTypes = new ArrayList<MediaType>();
        supportedMediaTypes.add(MediaType.APPLICATION_JSON);
        converter.setSupportedMediaTypes(supportedMediaTypes);
        converter.setFastJsonConfig(config);
        return converter;
    }
}
```

测试控制器类代码如下：

```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Date;

@RestController
public class BookController {

    @GetMapping("/book")
    public Book book() {
        Book book = new Book();
        book.setAuthor("罗贯中");
        book.setName("三国演义");
        book.setPrice(30f);
        book.setPublicationDate(new Date());
        return book;
    }
}
```

对于 `FastJsonHttpMessageConverter` 的配置，除了上面这种方式之外，还有另一种方式。

在 `Spring Boot` 项目中，当开发者引入 `spring-boot-starter-web` 依赖之后，该依赖又依赖了 `spring-boot-autoconfigure`，在这个自动化配置中，有一个 `WebMvcAutoConfiguration` 类提供了对 `Spring MVC` 最基本的配置，如果某一项自动化配置不满足开发需求，开发者可以针对该项自定义配置，只需要实现 `WebMvcConfigurer` 接口即可（在 `Spring 5.0` 之前是通过继承 `WebMvcConfigurerAdapter` 类来实现的），代码如下：

```java
import com.alibaba.fastjson.serializer.SerializerFeature;
import com.alibaba.fastjson.support.config.FastJsonConfig;
import com.alibaba.fastjson.support.spring.FastJsonHttpMessageConverter;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.MediaType;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

@Configuration
public class MyWebMvcConfig implements WebMvcConfigurer {

    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        FastJsonHttpMessageConverter converter = new FastJsonHttpMessageConverter();
        FastJsonConfig config = new FastJsonConfig();
        config.setSerializerFeatures(
                // 去掉 JSON 数据中的 "@type":"org.example.Book" 项
                // SerializerFeature.WriteClassName,
                SerializerFeature.WriteMapNullValue,
                SerializerFeature.PrettyFormat,
                SerializerFeature.WriteNullListAsEmpty,
                SerializerFeature.WriteNullStringAsEmpty
        );
        // 解决中文乱码问题
        List<MediaType> supportedMediaTypes = new ArrayList<>();
        MediaType mediaType = new MediaType("application", "json", StandardCharsets.UTF_8);
        supportedMediaTypes.add(mediaType);
        converter.setSupportedMediaTypes(supportedMediaTypes);
        converter.setFastJsonConfig(config);
        converters.add(converter);
    }
}
```

这样修改后，`Book` 类也需要修改成如下代码：

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;

import java.util.Date;

public class Book {

    private String name;
    private String author;
    @JsonIgnore
    private Float price;
    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date publicationDate;
    // 省略 getter/setter
}
```

