<center><b>表3-1 资源类型</b></center>

| 资源类型     | 位置                                                  | 说明                                                         |
| ------------ | ----------------------------------------------------- | ------------------------------------------------------------ |
| 颜色         | /res/values/any-file                                  | 表示指向颜色编码的颜色标识符。这些资源 id<br/> 在 R.java 中公开为 R.color.*。文件中的 XML <br/>节点为 `/resources/color` |
| 字符串       | /res/values/any-file                                  | 表示字符串资源。除了简单字符串，字符串<br/>资源还支持 java 格式的字符串和原始 HTML。<br/>这些资源 id 在 R.java 中公开为 R.string.*。<br/>文件中的 XML 节点为 `/resources/string` |
| 字符串数组   | /res/values/any-file                                  | 表示一个作为字符串数组的资源。这些资源ID在<br/> R.java 中公开为 R.array.*。文件中的 XML 节点为 <br/>`/resources/string-array` |
| 复数         | /res/values/any-file                                  | 根据数量值表示一个合适的字符串集合。数量是<br/>一个数字。在各种语言中，编写语句的方式取决<br/>于你引用了0个、1个或多个对象。这些资源ID在<br/>R.java 中公开为 R.plural.*。值文件中的XML节点<br/>为 `/resources/plurals` |
| 尺寸         | /res/values/any-file                                  | 表示Android中各种元素或试图的尺寸或大小。<br/>支持像素、英寸、毫米、与密度无关的像素以及<br/>与比例无关的像素。这些资源id在R.java中公开为<br/>R.dimen.*。文件中的XML节点为 `/resources/dimen`。 |
| 图像         | /res/drawable/multiple-files                          | 表示图像资源。支持的图像格式包括.jpg、.gif、<br/>.png等。每个图像位于独立的文件中，并根据<br/>文件名获得自己的id。这些资源id在R.java<br/>中公开为R.drawable.*。图像支持还包括一种<br/>名为可拉伸图像的图像类型，这种类型支持拉<br/>伸图像的一部分，而其他部分保持不变。这种<br/>可拉伸图像也称为9-patch文件（.9.png） |
| 色图         | /res/values/any-file以及<br/>/drawable/multiple-files | 表示用作视图背景的矩形色块或普通图形<br/>对象，比如位图。可以使用色块作为背景，<br/>而无需指定单个彩色位图。在Java中，这相<br/>当于创建一个彩色矩形并将其设置为视图背景 |
| 任意XML文件  | /res/xml/*.xml                                        | Android允许将任意XML文件用作资源。<br/>这些文件使用AAPT编译器编译。这些<br/>资源id在R.java中公开为R.xml.* |
| 任意原始资源 | /res/raw/\*.\*                                        | Android支持此目录下的任意未编译的二进<br/>制文件或文本文件。每个文件都会获得一个<br/>唯一资源id。这些资源id在R.java中公开为R.raw.* |
| 任意原始资产 | /assets/\*.\*/\*.\*                                   | Android支持/assets子目录下任意子目录中<br/>的任意文件。这些文件不是真实的资源，只<br/>是原始文件。与/res/资源子目录不同，这个<br/>目录支持任意深度的子目录。这些文件不会<br/>生成任何资源id。必须使用以/assets开始<br/>（不包含它）的相对路径名 |

**代码清单3-10** 指定字符串数组

```xml
<resources ...>
    ...Other resources
    <string-array name="test_array">
        <item>one</item>
        <item>two</item>
        <item>three</item>
    </string-array>
    ..Other resources
</resources>
```

**代码清单3-11** 使用字符串数组资源

```java
// Get access to Resources object from an Activity
Resources res = your-activity.getResources();
String strings[] = res.getStringArray(R.array.test.array);

// Print strings
for (String s : strings) {
    Log.d("example", s);
}
```

**代码清单3-12** 指定复数

```xml
<resources>
    <plurals name="eggs_in_a_nest_text">
        <item quantity="one">There is 1 egg</item>
        <item quantity="other">There are %d eggs</item>
    </plurals>
</resources>
```

**代码清单3-13** 使用复数资源

```java
Resources res = your-activity.getResources();
String s1 = res.getQuantityString(R.plurals.eggs_in_a_nest_text, 0, 0);
String s2 = res.getQuantityString(R.plurals.eggs_in_a_nest_text, 1, 1);
String s3 = res.getQuantityString(R.plurals.eggs_in_a_nest_text, 2, 2);
String s4 = res.getQuantityString(R.plurals.eggs_in_a_nest_text, 10, 10);
```

> 强烈建议阅读 `Android` 源代码发布版本中的 `Resources.java` 和 `PluralRules.java` 的源代码，以真正理解这一点。
>
> 基本原则是，对于 en （英语）语言环境，仅有的两个可能值是 "one" 和 "other"。所有其他语言也是如此，除了 cs（捷克语）、对于 cs，可能的值为 "one"（表示1）、"few"（表示2~4）和 "other"（表示其他值）。

**代码清单3-14** 定义字符串资源的 XML 语法

```xml
<resources>
    <string name="simple_string">simple string</string>
    <string name="quoted_string">"quoted 'xyz' string"</string>
    <string name="double_quoted_string">\"double quotes\"</string>
    <string name="java_format_string">hello %2$s Java format string. %1$s again</string>
    <string name="tagged_string">Hello <b><i>Slanted Android</i></b>, You are bold.</string>
</resources>
```

**代码清单3-15** 在 Java 代码中使用字符串资源

```java
// Read a simple string and set it in a text view
String simpleString = activity.getString(R.string.simple_string);
textView.setText(simpleString);

// Read a quoted string and set it in a text view
String quotedString = activity.getString(R.string.quoted_string);
textView.setText(quotedString);

// Read a double quoted string and set it in a text view
String doubleQuotedString = activity.getString(R.string.double_quoted_string);
textView.setText(doubleQuotedString);

// Read a Java format string
String javaFormatString = activity.getString(R.string.java_format_string);
// Convert the formatted string by passing in arguments
String substitutedString = String.format(javaFormatString, "Hello", "Android");
// set the output in a text view
textView.setText(substitutedString);

// Read an html string from the resource and set it in a text view
String htmlTaggedString = activity.getString(R.string.tagged_string);
// Convert it to a text span so that it can be set in a text view
// android.text.Html class allows painting of "html" strings
// This is strictly an Android class and does not support all html tags
Spanned textSpan = android.text.Html.fromHtml(htmlTaggedString);
// Set it in a text view
textView.setText(textSpan);
```

**代码清单3-16** 在 XML 中使用字符串资源

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:gravity="center_horizontal"
    android:text="@string/tagged_string" />
```

**代码清单3-17** 定义颜色资源的 XML 语法

```xml
<resources>
    <color name="red">#f00</color>
    <color name="blue">#0000ff</color>
    <color name="green">#f0f0</color>
    <color name="main_back_ground_color">#ffffff00</color>
</resources>
```

**代码清单3-18** Java 代码中的颜色资源

```java
int mainBackGroundColor = activity.getResources().getColor(R.color.main_back_ground_color);
```

**代码清单3-19** 在视图定义中使用颜色

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textColor="@color/red"
    android:text="Sample Text to Show Red Color" />
```

**代码清单3-20** 定义尺寸资源的 XML 语法

```xml
<resources>
    <dimen name="mysize_in_pixels">1px</dimen>
    <dimen name="mysize_in_dp">5dp</dimen>
    <dimen name="medium_size">100sp</dimen>
</resources>
```

可以采用以下任何单位来指定尺寸：

+ px：像素；
+ in：英寸；
+ mm：毫米；
+ pt：磅；
+ dp：与密度无关的像素，基于 160dpi （每英寸的像素数）屏幕（尺寸适应屏幕密度）；
+ sp：与比例无关的像素（这种尺寸支持用户调整大小，适合在字体中使用）。

**代码清单3-21** 在 Java 代码中使用尺寸资源

```java
float dimen = activity.getResources().getDimension(R.dimen.mysize_in_pixels);
```

**代码清单3-22** 在 XML 中使用尺寸资源

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textSize="@dimen/medium_size" />
```

**代码清单3-23** 在 XML 中使用图像资源

```xml
<Button 
    android:id="@+id/button1"
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:text="Dial"
    android:background="@drawable/sample_image" />
```

> 警告，如果两个文件名中包含相同的基本文件名，将得到一个错误。另外，`/res/drawable` 下的子目录将被忽略。这些子目录下的任何文件都不会被读取。

**代码清单3-24** 在 Java 中使用图像资源

```java
// Call getDrawable to get the image
BitmapDrawable d = activity.getResources().getDrawable(R.drawable.sample_image);

// You can use the drawable then so set the background
button.setBackgroundDrawable(d);

// or you can set the background directly from the resource Id
button.setBackgroundResource(R.drawable.sample_image);
```

**代码清单3-25** 定义色图资源的 XML 语法

```xml
<resources>
    <drawable name="red_rectangle">#f00</drawable>
    <drawable name="blue_rectangle">#0000ff</drawable>
    <drawable name="green_rectangle">#f0f0</drawable>
</resources>
```

**代码清单3-26** 在 Java 代码中使用色图资源

```java
// Get a drawable
ColorDrawable redDrawable = (ColorDrawable)activity.getResources().getDrawable(R.drawable.red_rectangle);

// Set it as a background to a text view
textView.setBackgroundDrawable(redDrawable);
```

**代码清单3-27** 在 XML 代码中使用色图资源

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textAlign="center"
    android:background="@drawable/red_rectangle" />
```

**代码清单3-28** 定义圆角矩形

```xml
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#f0600000" />
    <stroke android:width="3dp" color="#ffff8080" />
    <corners android:radius="13dp" />
    <padding android:left="10dp" android:top="10dp" android:right="10dp" android:bottom="10dp" />
</shape>
```

**代码清单3-29** 在 Java 代码中使用图形对象

```java
// Get a drawable
GradientDrawable roundedRectangle = (GradientDrawable)activity.getResources().getDrawable(R.drawable.my_rounded_rectangle);

// Set it as a background to a text view
textView.setBackgroundDrawable(roundedRectangle);
```

> 没有必要将返回的基础 `Drawable` 转换为 `GradientDrawable`，这里这样做是为了演示此 `<shape>` 标记变成了一个 `GradientDrawable`。
>
> 最后，图形对象子目录中的一个位图将解析为 `BitmapDrawable` 类。“drawable” 资源值解析为 `ColorDrawable`。包含形状标记的 XML 文件解析为 `GradientDrawable`。