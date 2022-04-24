[toc]

> 注意：下面调用的方法是系统 API ，如果需要在第三方应用中使用，可以通过反射来调用。

### 1. Kotlin

```kotlin
import android.os.UserHandle
import android.content.Context
import com.android.internal.widget.LockPatternUtils

fun setLockScreenDisabled(context: Context, disabled: Boolean) {
    val lockUtils = LockPatternUtils(context.applicationContext)
    if (!lockUtils.isSecure(UserHandle.myUserId())) {
        lockUtils.setLockScreenDisabled(true, UserHandle.myUserId())
    }
}
```

反射调用：

```kotlin
import android.os.UserHandle
import com.android.internal.widget.LockPatternUtils
import java.lang.Exception

fun setLockScreenDisabled(context: Context, disabled: Boolean) {
    try {
        val lockUtilsClass = Class.forName("com.android.internal.widget.LockPatternUtils")
        val constructor = lockUtilsClass.getDeclaredConstructor(Context::class.java)
        val lockUtils = constructor.newInstance(context.applicationContext)
        val isSecure = lockUtilsClass.getDeclaredMethod("isSecure", Int::class.java)
        val userId = UserHandle::class.java.getDeclaredMethod("myUserId")
        if (isSecure.invoke(lockUtils, userId.invoke(null) as Int) as Boolean) {
            val setLockScreenDisabled = lockUtilsClass.getDeclaredMethod(
                "setLockScreenDisabled",
                Boolean::class.java,
                Int::class.java
            )
            setLockScreenDisabled.invoke(disabled, userId.invoke(null) as Int)
        }
    } catch (e: Exception) {
        Log.d(TAG, "setLockScreenDisabled=>error: ", e)
    }
}
```

### 2. Java

```java
import android.os.UserHandle;
import android.content.Context;
import com.android.internal.widget.LockPatternUtils

public void setLockScreenDisabled(Context context, boolean disabled) {
    LockPatternUtils lockUtils = new LockPatternUtils(context.getApplicationContext());
    if (!lockUtils.isSecure(UserHandle.myUserId())) {
        lockUtils.setLockScreenDisabled(true, UserHandle.myUserId());
    }
}
```

反射调用方法：

```java
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import android.annotation.SuppressLint;
import android.content.Context;
import android.os.Build;
import android.os.UserHandle;

public void setLockScreenDisabled(Context context, boolean disabled) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        try {
            Class lockUtilsClass = Class.forName("com.android.internal.widget.LockPatternUtils");
            Constructor constructor = lockUtilsClass.getDeclaredConstructor(Context.class);
            Object lockUtils = constructor.newInstance(context.getApplicationContext());
            Method isSecure = lockUtilsClass.getDeclaredMethod("isSecure", int.class);
            Method myUserId = UserHandle.class.getDeclaredMethod("myUserId");
            if ((boolean) isSecure.invoke(lockUtils, (int) myUserId.invoke(null))) {
                @SuppressLint("BlockedPrivateApi") Method setLockScreenDisabled = lockUtilsClass.getDeclaredMethod("setLockScreenDisabled", boolean.class, int.class);
                setLockScreenDisabled.invoke(lockUtils, disabled, (int) myUserId.invoke(null));
            }
        } catch (Exception e) {
            Log.e(TAG, "setLockScreenDisabled=>error: ", e);
        }
    }
}
```

