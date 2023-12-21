`@SpringBootApplication` 实际上是一个组合注解，定义如下：

```java
package com.qty.springweb;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.autoconfigure.AutoConfigurationExcludeFilter;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.context.TypeExcludeFilter;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScan.Filter;
import org.springframework.context.annotation.FilterType;

@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(excludeFilters = {
		@Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),
		@Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class)
})
public class App 
{
    public static void main( String[] args )
    {
        SpringApplication.run(App.class, args);
    }
}
```

① 第一个 `@SpringBootConfiguration` 的定义如下：

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Configuration
@Indexed
public @interface SpringBootConfiguration {
    
}
```

原来就是一个 `@Configuration`，所以 `@SpringBootConfiguration` 的功能就是表明这是一个配置类，开发者可以在在这个类中配置 Bean。从这个角度来讲，这个类所扮演的角色有点类似于 Spring 中 applicationContext.xml 文件的角色。

② 第二个注解 `@EnableAutoConfiguration` 表示开启自动化配置。Spring Boot 中的自动化配置是非侵入式的，在任意时刻，开发者都可以使用自定义配置代替自动化配置中的某一个配置。

③ 第三个注解 `@ComponentScan` 完成包扫描，也是 Spring 中的功能。由于 `@ComponentScan` 注解默认扫描的类都位于当前类所在包的下面，因此建议在实际项目开发中把项目启动类放在根包中。

虽然项目的启动类也包含 `@Configuration` 注解，但是开发者可以创建一个新的类专门用来配置 `Bean`，这样便于配置的管理。这个类只需要加上 `@Configuration` 注解即可，代码如下：

```java
@Configuration
public class MyConfig {
   
}
```

项目启动类中的 `@ComponentScan` 注解，除了扫描 `@Service`、`@Repository`、`@Component`、`@Controller` 和 `@RestController` 等之外，也会扫描 `@Comfiguration` 注解的类。