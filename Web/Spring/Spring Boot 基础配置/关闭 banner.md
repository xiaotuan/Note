修改项目启动类的 `main` 方法，代码如下：

```java
import org.springframework.boot.Banner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;

@SpringBootApplication
public class App 
{
    public static void main( String[] args )
    {
    	SpringApplicationBuilder builder = new SpringApplicationBuilder(App.class);
    	builder.bannerMode(Banner.Mode.OFF);
    	builder.run(args);
    }
}
```

