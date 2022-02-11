[toc]

> 警告
>
> `Context.MODE_WORLD_READABLE` 和 `Context.MODE_WORLD_WRITEABLE` 已被标志为过时，且该方法存在安全隐患。

### 1. 服务端

使用 `getSharedPreferences(String name, int mode)` 方法创建 SharedPreferences 对象，其中 mode 值设置为 `Context.MODE_WORLD_READABLE` 或 `Context.MODE_WORLD_WRITEABLE`。

#### 1.1 Kotlin

```kotlin
import android.content.SharedPreferences

val sp = context.getSharedPreferences("my-preference", Context.MODE_WORLD_READABLE);
```

#### 1.2 Java

```java
import android.content.SharedPreferences;

SharedPreferences sp = context.getSharedPreferences("my-preference", Context.MODE_WORLD_READABLE);
```

### 2. 客户端

在客户端通过

#### 2.1 Kotlin

```kotlin
import android.content.Context
import android.content.pm.PackageManager

try {
    val otherAppContext = createPackageContext("packagename", Context.CONTEXT_IGNORE_SECURITY)
    val sp = otherAppContext.getSharedPreferences("my-preference", Context.MODE_WORLD_READABLE)
} catch (e: PackageManager.NameNotFoundException) {
    e.printStackTrace()
}
```

#### 2.2 Java

```java
import android.content.Context;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;

try {
    Context otherAppContext = createPackageContext("packagename", CONTEXT_IGNORE_SECURITY);
    SharedPreferences sp = otherAppContext.getSharedPreferences("my-preference", Context.MODE_WORLD_READABLE);
} catch (PackageManager.NameNotFoundException e) {
    e.printStackTrace();
}
```

