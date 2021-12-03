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

上面创建了一个存储文件名为 "my_db"，并且设置创建文件的模式为只有应用可以访问（`Context.MODE_PRIVATE`）。可用的模式有：

+ `MODE_PRIVATE`：只有您的应用可以访问 SharedPreferences 的内容。
+ `MODE_WORLD_READABLE`：其他用户可以访问你应用的 `SharedPreferences` 但是不能修改。
+ `MODE_WORD_WRITEABLE`：其他用户即可以访问，也可以修改你的 `SharedPreferences`。
+ `MODE_MULTI_PROCESS`：API 11 可用，允许您通过多个进程来修改您的 `SharedPreference`。



