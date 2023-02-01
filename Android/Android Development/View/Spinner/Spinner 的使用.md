[toc]

### 1. 在 xml 中定义 Spinner

```xml
<Spinner
    android:id="@+id/spinner"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:prompt="@string/spinnerprompt" />
```

### 2. 在代码中使用 Spinner

#### 2.1 Kotlin

```kotlin
import android.widget.ArrayAdapter;
import android.widget.Spinner;

Spinner spinner = findViewById(R.id.spinner);

ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                                                                     R.array.planets, android.R.layout.simple_spinner_item);

adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

spinner.setAdapter(adapter);
```

#### 2.2 Java

```java
import android.widget.ArrayAdapter
import android.widget.Spinner

val spinner = findViewById<Spinner>(R.id.spinner)

val adapter = ArrayAdapter.createFromResource(this,
    R.array.planets, android.R.layout.simple_spinner_item)

adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

spinner.adapter = adapter
```

