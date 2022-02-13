[toc]

> 提示
>
> `IntentService` 以被标记为过时类，推荐使用 androidx.core.app.JobIntentService 类。

要使用 `IntentService` ，可以扩展 `IntentService` 并实现 `onHandleIntent(Intent intent)`。`IntentService` 接收 Intent，启动一个工作线程，然后适当地停止服务。所有请求都在单个工程线程上处理，它们可以根据需要占用任意长的诗句，但一次只能处理一个请求。

**Kotlin**

```kotlin
import android.app.IntentService
import android.content.Intent

class MyService(name: String? = "MyService") : IntentService(name) {

    override fun onHandleIntent(intent: Intent?) {
        TODO("Not yet implemented")
    }

}
```

**Java**

```java
import android.app.IntentService;
import android.content.Intent;

import androidx.annotation.Nullable;

public class MyService extends IntentService {
    
   	private static final String NAME = "MyService";

    public MyService() {
        super(NAME);
    }

    @Override
    protected void onHandleIntent(@Nullable Intent intent) {

    }

}
```

