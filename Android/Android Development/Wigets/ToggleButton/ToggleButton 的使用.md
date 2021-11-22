[toc]

`ToggleButton` 是一种具有两种状态的按钮。此按钮既可以处于 `On` （打开）状态，也可以处于 `Off`（关闭）状态。默认情况下，在按钮处于 `On` 状态时将其文本设置为 "On"，在处于 `Off` 状态时设置为 "Off"。可以通过 `android:textOn` 和 `android:textOff` 属性设置处于 `On` 和 `Off` 状态下的字符。

### 1. 在 xml 中定义 ToggleButton

```xml
<ToggleButton
              android:id="@+id/cctglBtn"
              android:layout_width="wrap_content"
              android:layout_height="wrap_content"
              android:text="Toggle Button"
              android:textOn="Stop"
              android:textOff="Run" />
```

### 2. 在代码中使用 ToggleButton

#### 2.1 Kotlin

```kotlin
import android.widget.ToggleButton

val toggleButton = findViewById<ToggleButton>(R.id.cctglbtn)
toggleButton.setOnCheckedChangeListener { buttonView, isChecked -> 
	......
}
```

#### 2.2 Java

```java
import android.widget.ToggleButton;

ToggleButton toggleButton = findViewById(R.id.cctglbtn);
toggleButton.setOnCheckedChangeListener((buttonView, isChecked) -> {
  ......
})
```

可以通过 `setChecked()` 或 `toggle()` 方法来切换状态。