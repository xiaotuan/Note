可以通过 `Context` 中调用 `getSharedPreferences()` 方法创建指定存储文件名字的 SharedPreferences 对象，例如：

**Kotlin**

```kotlin
import android.content.SharedPreferences
import android.content.Context

val sp = context.getSharedPreferences("my_db", Context.MODE_PRIVATE);
```

**Java**

```java
import android.content.SharedPreferences;
import android.content.Context;

SharedPreferences sp = context.getSharedPreferences("my_db", Context.MODE_PRIVATE);
```

上面创建了一个存储文件名为 "my_db"，

