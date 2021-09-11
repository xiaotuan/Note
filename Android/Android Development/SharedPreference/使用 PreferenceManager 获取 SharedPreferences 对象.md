可以通过如下方法获取 `SharedPreferences` 实例：

**Kotlin 版本**

```kotlin
import androidx.preference.PreferenceManager

val prefs = PreferenceManager.getDefaultSharedPreferences(context)
```

**Java 版本**

```java
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(mContext);
```

