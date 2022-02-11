[toc]

可以使用 `createPackageContext(String packageName, int flags)` 方法构造其他应用的 Context 对象：

### 1. Kotlin

```Kotlin
import android.content.pm.PackageManager

try {
    val otherAppContext = createPackageContext("packagename", CONTEXT_IGNORE_SECURITY)
} catch (e : PackageManager.NameNotFoundException) {
    e.printStackTrace();
}
```

### 2. Java

```java
import android.content.Context;
import android.content.pm.PackageManager;

try {
    Context otherAppContext = createPackageContext("packagename", CONTEXT_IGNORE_SECURITY);
} catch (PackageManager.NameNotFoundException e) {
    e.printStackTrace();
}
```

其中 `flags` 参数可以是如下值：

+  `Context.CONTEXT_INCLUDE_CODE`：`Android` 允许将目标应用程序代码加载到当前进程中。该代码然后像你的应用程序一样运行。只有在两个拥有相同的签名和一个共享用户 ID 时，此过程才能成功。如果共享用户 ID 不匹配，使用此标志将导致安全异常。
+  `Context.CONTEXT_RESTRICTED`：我们仍然应该能够访问资源路径，而不会遇到请求加载代码的极端情形。
+  `Context.CONTEXT_IGNORE_SECURITY`：将忽略证书并加载代码，但代码将在你的用户 ID 下运行。因此，文档建议如果将使用此标记，请非常小心。

 
