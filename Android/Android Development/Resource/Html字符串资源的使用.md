[toc]

### 1. 定义 HTML 字符串资源

```xml
<resources>
    <string name="tagged_string">Hello <b><i>Slanted Android</i></b>, You are bold.</string>
</resources>
```

### 2. 在代码中使用 HTML 字符串资源

**Java 版本**

```java
TextView tv = findViewById(R.id.text1);
Resources res = getResources();
CharSequence htmlTaggedString = res.getText(R.string.tagged_string);
tv.setText(htmlTaggedString);
```

或者

```java
TextView tv = findViewById(R.id.text1);
Resources res = getResources();
Spanned textSpan = (Spanned) res.getText(R.string.tagged_string);
tv.setText(textSpan);
```

**Kotlin 版本**

```kotlin
val tv = findViewById<TextView>(R.id.text1)
val text = resources.getText(R.string.tagged_string)
tv.text = text
```

或者

```kotlin
val tv = findViewById<TextView>(R.id.text1)
val textSpan = resources.getText(R.string.tagged_string) as Spanned
tv.text = textSpan
```

> 注意：以前可以通过如下方式使用 HTML 资源：
>
> ```java
> TextView tv = findViewById(R.id.text1);
> Resources res = getResources();
> String htmlTaggedString = res.getString(R.string.tagged_string);
> Spanned textSpan = android.text.Html.fromHtml(htmlTaggedString);
> tv.setText(textSpan);
> ```
>
> 但是现在通过 `res.getString()` 方法获取到的字符串已经去掉了 `HTML` 标签，因此再使用 `Html.fromHtml()` 方法转换也就没有意义了。现在，可以通过 `res.getText()` 方法，其返回的值就是一个 `Spanned` 对象，因此可以直接将其值设置到 `TextView` 中即可。