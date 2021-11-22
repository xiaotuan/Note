`TextView` 可以使用 `autoLink` 属性设置文本的自动链接，包括 `web`、`email`、`phone` 或 `map`，或使用 `none` （默认值）或 `all`。

### 1. 在 XML 中使用 autoLink 属性

```xml
<TextView
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:autoLink="email|web"
          android:text="My websit is https://www.baidu.com，you can send email to custome@qq.com." />
```

>   注意：如果需要设置多个 `autoLink` 属性，可以使用竖线  `|` 将多个属性分隔开来。 

### 2. 在代码中设置 autoLink 属性

在代码中可以使用 `setAutoLinkMask()` 方法设置 `autoLink` 属性，传递一个 `int` 值来表示各种值的组合，比如 `Linkify.EMAIL_ADDRESSES|Linkify.WEB_ADDRESSES` 。

#### 2.1 kotlin版本

```kotlin
import android.text.util.Linkify

val tv = findViewById<TextView>(R.id.tv)
tv.autoLinkMask = Linkify.ALL
tv.text = "Please visit http://www.androidbook.com or email me at davemac327@gmail.com."
```

#### 2.2 Java 版本

```java
import android.text.util.Linkify;

TextView tv = findViewById(R.id.tv);
tv.setAutoLinkMask(Linkify.ALL);
tv.setText("Please visit my website, http://www.androidbook.com or email me at davemac327@gmail.com");
```

>   注意：必须在 `TextView` 中设置文本之前就设置了自动链接选项，因为在设置文本后设置自动链接选项不会影响现有文本。如果希望在设置文本之后也可以设置自动链接选项，可以调用 `Linkify` 类的静态 `addLinks()` 方法：
>
>   ```kotlin
>   Linkify.addLinks(tv, Linkify.ALL)
>   ```

