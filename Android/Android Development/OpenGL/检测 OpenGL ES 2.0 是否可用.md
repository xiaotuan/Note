可用通过如下代码检测 OpenGL ES 2.0 在设备上是否可用：

**Kotlin**

```kotlin
import android.app.ActivityManager

fun detectOpenGLES20(): Boolean {
    val am = getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
    return (am.deviceConfigurationInfo.reqGlEsVersion >= 0x20000)
}
```

**Java**

```java
import android.app.ActivityManager;
import android.content.Context;
import android.content.pm.ConfigurationInfo;

private boolean detectOpenGLES20() {
    ActivityManager am = (ActivityManager) getSystemService(Context.ACTIVITY_SERVICE);
    ConfigurationInfo info = am.getDeviceConfigurationInfo();
    return (info.reqGlEsVersion >= 0x20000);
}
```

