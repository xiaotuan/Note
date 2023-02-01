[toc]

### 1. 在 xml 中定义 TimePicker

```xml
<TimePicker
    android:id="@+id/timePicker"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### 2. 在代码中使用 TimePicker

#### 2.1 Kotlin 版本

```kotlin
import android.widget.TimePicker
import java.util.*

val tp = findViewById<TimePicker>(R.id.timePicker)

val timeF = Formatter()
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    timeF.format("Time defaulted to %d:%02d", tp.hour, tp.minute)
} else {
    timeF.format("Time defaulted to %d:%02d", tp.currentHour, tp.currentMinute)
}
timeDefault.text = timeF.toString()

tp.setIs24HourView(true)
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    tp.hour = 10
    tp.minute = 10
} else {
    tp.currentHour = 10
    tp.currentMinute = 10
}
```

#### 2.2 Java 版本

```java
import android.widget.TimePicker;

TimePicker tp = findViewById(R.id.timePicker);

java.util.Formatter timeF = new java.util.Formatter();
timeF.format("Time defaulted to %d:%02d", tp.getCurrentHour(),
        tp.getCurrentMinute());
timeDefault.setText(timeF.toString());

tp.setIs24HourView(true);
tp.setCurrentHour(10);
tp.setCurrentMinute(10);
```

