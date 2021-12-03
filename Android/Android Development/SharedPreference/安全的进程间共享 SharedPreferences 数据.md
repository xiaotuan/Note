虽然可以通过在使用 `Context.getSharedPreferences()` 方法创建 `SharedPreferences` 对象时传入非 `Context.MODE_PRIVATE` 模式来达到与其他应用共享 `SharedPreferences` 数据，但是这是不安全的。

要想安全的与其他可信任的应用共享 `SharedPreferences` 数据，可以在其他应用中使用与该应用相同的的 `sharedUserId`，例如在两个应用的 `AndroidManifest.xml` 文件中都定义相同的 `android:sharedUserId` 值：

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:sharedUserId="uid.jwei.apps.dataforandroid"
    ......>
</manifest>
```

然后在使用相同的签名文件对这两个应用进行签名。

最后可以在其他应用中使用如下方法访问另一个应用的 `SharedPreferences` 数据：

**Kotlin**

```kotlin
import android.content.Context
import android.content.SharedPreferences
import android.content.pm.PackageManager

try {
    val context = createPackageContext("jwei.apps.dataforandroid.ch1", CONTEXT_IGNORE_SECURITY);
    val sp = context.getSharedPreferences("my_db", Context.MODE_PRIVATE);
    val stringValue = sp.getString("testStringKey", "error");
    val booleanValue = sp.getBoolean("testBooleanKey", false);

    Log.i("SPE", "Retrieved string value: $stringValue);
    Log.i("SPE", "Retrieved boolean value: $booleanValue");
} catch (e: PackageManager.NameNotFoundException) {
    Log.i("SPE", "error: ", e);
}
```

**Java**

```java
import android.content.Context;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;

try {
    Context context = createPackageContext("jwei.apps.dataforandroid.ch1", CONTEXT_IGNORE_SECURITY);
    SharedPreferences sp = context.getSharedPreferences("my_db", Context.MODE_PRIVATE);
    String stringValue = sp.getString("testStringKey", "error");
    boolean booleanValue = sp.getBoolean("testBooleanKey", false);

    Log.i("SPE", "Retrieved string value: " + stringValue);
    Log.i("SPE", "Retrieved boolean value: " + booleanValue);
} catch (PackageManager.NameNotFoundException e) {
    Log.i("SPE", "error: ", e);
}
```

