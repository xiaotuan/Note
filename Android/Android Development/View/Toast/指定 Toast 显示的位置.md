> 警告：下面的方法在 Android R（Android 11）版本后无效。

可以通过调用 `Toast` 的 `setGravity()` 方法设置 `Toast` 显示的位置。

### 1. Kotlin

```kotlin
import android.view.Gravity
import android.widget.Toast

val toast = Toast.makeText(
    this,
    R.string.correct_toast,
    Toast.LENGTH_SHORT);
toast.setGravity(Gravity.TOP, 0, 0)
toast.show()
```

### 2. Java

```java
import android.view.Gravity;
import android.widget.Toast;

Toast toast = Toast.makeText(this, R.string.correct_toast, Toast.LENGTH_SHORT);
toast.setGravity(Gravity.TOP, 0, 0);
toast.show();
```

