可以使用 `Spannable` 为 `TextView` 应用样式：

```java
tv.setText("This text is stored in a Spannable", TextView.BufferType.SPANNABLE);
```

或：

**Kotlin**

```kotlin
import android.graphics.Color
import android.graphics.Typeface
import android.text.style.BackgroundColorSpan
import android.text.style.StyleSpan
import android.widget.TextView

val tv3 = findViewById<TextView>(R.id.tv3)
tv3.setText("Styling the content of a TextView dynamically", TextView.BufferType.SPANNABLE)
val spn = tv3.text as Spannable
spn.setSpan(BackgroundColorSpan(Color.RED), 0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE)
spn.setSpan(StyleSpan(Typeface.BOLD_ITALIC), 0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE)
```

**Java**

```java
import android.graphics.Color;
import android.graphics.Typeface;
import android.text.style.BackgroundColorSpan;
import android.text.style.StyleSpan;
import android.widget.TextView;

TextView tv3 = findViewById(R.id.tv3);
tv3.setText("Styling the content of a TextView dynamically",
        TextView.BufferType.SPANNABLE);
Spannable spn = (Spannable) tv3.getText();
spn.setSpan(new BackgroundColorSpan(Color.RED), 0, 7,
        Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
spn.setSpan(new StyleSpan(android.graphics.Typeface.BOLD_ITALIC),
        0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
```

