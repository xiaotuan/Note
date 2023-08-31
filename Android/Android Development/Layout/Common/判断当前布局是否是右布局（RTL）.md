可以通过如下方法判断当前布局是否是右布局（RTL）：

**Kotlin 版本**

```kotlin
import android.content.res.Resources
import android.text.TextUtils
import android.view.View
import java.util.Locale;

private fun isRtl(res: Resources): Boolean {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
        return res.configuration.layoutDirection == View.LAYOUT_DIRECTION_RTL
    } else {
        return TextUtils.getLayoutDirectionFromLocale(Locale.getDefault()) == View.LAYOUT_DIRECTION_RTL
    }
}
```

**Java 版本**

```java
import android.content.res.Resources;
import android.text.TextUtils;
import android.view.View;
import java.util.Locale;
    
public static boolean isRtl(Resources res) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
        return res.getConfiguration().getLayoutDirection() == View.LAYOUT_DIRECTION_RTL;
    } else {
        return TextUtils.getLayoutDirectionFromLocale(Locale.getDefault()) == View.LAYOUT_DIRECTION_RTL;
    }
}
```

