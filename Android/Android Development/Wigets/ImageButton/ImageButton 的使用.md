[toc]

### 1. 在 xml 中定义 ImageButton 控件

```xml
<ImageButton
             android:id="@+id/imageButton"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:onClick="myClickHandler"
             android:src="@drawable/icon" />
```

### 2. 在代码中使用 ImageButton 控件

#### 2.1 Kotlin

```Kotlin
import android.widget.Button

val btn = findViewById<ImageButton>(R.id.imageBtn)
btn.setImageResource(R.drawable.icon)
```

#### 2.2 Java

```Java
import android.widget.Button;

ImageButton btn = findViewById(R.id.imageBtn);
btn.setImageResource(R.drawable.icon);
```

