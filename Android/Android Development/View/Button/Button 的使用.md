[toc]

### 1. 在 XML 定义 Button 控件

```xml
<Button
        android:id="@+id/ccbtn1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/basicBtnLabel" />
```

### 2 在代码中使用 Button 控件

#### 2.1 Kotlin

```kotlin
import android.content.Intent
import android.widget.Button

val btn = findViewById<Button>(R.id.ccbtn1)

tn.setOnClickListener { 
  val intent = Intent(Intent.ACTION_VIEW, Uri.parse("http://www.androidbook.com"));
  startActivity(intent);
}
```

#### 2.2 Java

```java
import android.content.Intent;
import android.widget.Button;

Button btn = findViewById(R.id.ccbtn1);

btn.setOnClickListener(view -> {
	Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.androidbook.com"));
  startActivity(intent);
});
```

