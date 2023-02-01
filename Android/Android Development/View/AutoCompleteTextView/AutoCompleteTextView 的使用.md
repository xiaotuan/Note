[toc]

`AutoCompleteTextView` 控件在用户前几个字母后，如果这些字母与适配器中的数据前几个字母一致，会在控件下方以列表方式显示出来，用户点击某项后，该项内容将会直接显示在 `AutoCompleteTextView` 控件上。但是当该控件输入完一个单词后就不会再提示了。

### 1. 在 xml 中定义 AutoCompleteTextView

```xml
<AutoCompleteTextView 
    									android:id="@+id/actv"
                      android:layout_width="match_parent"
                      android:layout_height="wrap_content"/
```

### 2. 在代码中初始化 AutoCompleteTextView

#### 2.1 Kotlin 版本

```kotlin
import android.widget.AutoCompleteTextView

val actv = findViewById<AutoCompleteTextView>(R.id.actv)

val aa = ArrayAdapter<String>(this,
                              android.R.layout.simple_dropdown_item_1line,
                              arrayOf("English", "Hebrew", "Hindi", "Spanish", "German", "Greek")
                             )

actv.setAdapter(aa)
```

#### 2.2 Java 版本

```java
import android.widget.AutoCompleteTextView;

AutoCompleteTextView actv = findViewById(R.id.actv);

ArrayAdapter<String> aa = new ArrayAdapter<>(this,
                                             android.R.layout.simple_dropdown_item_1line,
                                             new String[]{"English", "Hebrew", "Hindi", "Spanish", "German", "Greek"});

actv.setAdapter(aa);
```

