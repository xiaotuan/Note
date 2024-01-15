在 `FastJsonConfig` 类中调用 `setSerializerFeatures()` 方法时，不要设置 `SerializerFeature.WriteClassName` 项即可，最终代码如下：

```java
import com.alibaba.fastjson.serializer.SerializerFeature;
import com.alibaba.fastjson.support.config.FastJsonConfig;
import com.alibaba.fastjson.support.spring.FastJsonHttpMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.MediaType;

import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
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

        List<MediaType> supportedMediaTypes = new ArrayList<MediaType>();
        MediaType mediaType = new MediaType("application", "json", StandardCharsets.UTF_8);
        supportedMediaTypes.add(mediaType);
        converter.setSupportedMediaTypes(supportedMediaTypes);
        converter.setFastJsonConfig(config);
        return converter;
    }
}
```

