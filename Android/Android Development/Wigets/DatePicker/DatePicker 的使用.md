[toc]

### 1. 在 xml 中定义 DatePicker

```xml
<DatePicker
    android:id="@+id/datePicker"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### 2. 在代码中使用 DatePicker

#### 2.1 Kotlin 版本

```kotlin
import android.widget.DatePicker

val dp = findViewById<DatePicker>(R.id.datePicker)
// And here, subtract 1 from December (12) to set it to December
dp.init(2008, 11, 10, null)
```

#### 2.2 Java 版本

```java
import android.widget.DatePicker;

DatePicker dp = findViewById(R.id.datePicker);
// And here, subtract 1 from December (12) to set it to December
dp.init(2008, 11, 10, null);
```

