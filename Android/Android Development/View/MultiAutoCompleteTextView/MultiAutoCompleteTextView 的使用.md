[toc]

`MultiAutoCompleteTextView` 控件会在用户输入几个字母后，如果这些字母与适配器中项前面几个字母匹配就会以菜单列表显示出来，点击其中一项将会输入到 `MultiAutoCompleteTextView` 控件中。当输入完一个单词后，再输入其他单词则会再次显示。

### 1. 在 XML 中定义 MultiAutoCompleteTextView 控件

```xml
<MultiAutoCompleteTextView
                           android:id="@+id/mactv"
                           android:layout_width="match_parent"
                           android:layout_height="wrap_content" />
```

### 2. 在代码中初始化 MultiAutoCompleteTextView 控件

#### 2.1 Kotlin

```kotlin
import android.widget.*

val mactv = findViewById<MultiAutoCompleteTextView>(R.id.mactv)
val aa2 = ArrayAdapter<String>(this,
                               android.R.layout.simple_dropdown_item_1line,
                               arrayOf("English", "Hebrew", "Hindi", "Spanish", "German", "Greek")
                              )

mactv.setAdapter(aa2)

mactv.setTokenizer(MultiAutoCompleteTextView.CommaTokenizer())
```

#### 2.2 Java

```java
import android.widget.ArrayAdapter;
import android.widget.MultiAutoCompleteTextView;

MultiAutoCompleteTextView mactv = findViewById(R.id.mactv);
ArrayAdapter<String> aa2 = new ArrayAdapter<>(this,
                                              android.R.layout.simple_dropdown_item_1line,
                                              new String[]{"English", "Hebrew", "Hindi", "Spanish", "German", "Greek"});

mactv.setAdapter(aa2);

mactv.setTokenizer(new MultiAutoCompleteTextView.CommaTokenizer());
```

`MultiAutoCompleteTextView` 控件需要调用 `setTokenizer()` 方法设置用于区分两个单词的标识符。本例中使用了 `CommaTokenizer` ，所以在将逗号（`,`）键入到 `MultiAutoCompleteTextView` 字段中只会，该字段将使用字符串数组再次给出建议。键入其他字符都不会触发字符串给出建议。

Android 为 E-mail 地址提供了另一个令牌化类，名为 `Rfc822Tokenizer`。