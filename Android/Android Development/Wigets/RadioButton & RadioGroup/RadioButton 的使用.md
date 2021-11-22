[toc]

### 1. 在 xml 中定义 RadioButton

```xml
<RadioButton
             android:id="@+id/chRBtn"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:checked="true" />
```

### 2. 在代码中使用 RadioButton

#### 2.1 Kotlin

```kotlin
import android.widget.RadioButton


```

#### 2.2 Java

```java
import android.widget.RadioButton;

RadioButton rbtn = findViewById(R.id.chRBtn);
rbtn.setChecked(true);
rbtn.setOnCheckedChangeListener((checkBox, isChecked) -> {
  ......
});
```

>   注意：如果 `RadioButton` 没有放在 `RadioGroup` 中，那么它们是独立的。