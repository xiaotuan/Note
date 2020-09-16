> 当 Intent 带有组件名称时，它成为显式 Intent。当 Intent 没有组件名称，但依赖于其他部分（比如操作和数据）时，它称为隐式 Intent。

**1. Intent 和数据 URI**

要调用拨号键盘，在该代码清单中所需要做的只是拨号键盘的操作，不需要其他任何内容：

```java
public static void dial(Activity activity) {
    Intent intent = new Intent(Intent.ACTION_DIAL);
    activity.startActivity(intent);
}
```

用于呼叫给定电话号码的 Intent.ACTION_CALL，还接受一个名为 Data 的参数。此参数执行一个 URI，该 URI 又指向所拨的电话号码：

```java
public static void call(Activity activity) {
    Intent intent = new Intent(Intent.ACTION_CALL);
    intent.setData(Uri.parse("tel:555-555-5555"));
    action.startActivity(intent);
}
```

**2. 一般操作**

Intent 操作和它所调用的程序之间并不存在一对一的关系。例如：

```java
public static void invokeWebBrowser(Activity activity) {
    Intent intent = new Intent(Intent.ACTION_VIEW);
    intent.setData(Uri.parse("https://www.baidu.com"));
    activity.startActivity(intent);
}
```

在这种情况下，Android 不仅依赖于一般操作名称，而且依赖于 URI 的性质。Android 查看 URI 的方案（恰好是 http），然后询问所有一注册的活动，看看哪个活动能理解此方案。在这些活动中，它询问哪个活动能处理 VIEW，然后调用该活动。为此，浏览器活动应该为数据方案 http 注册了 VIEW Intent。描述文件中的 Intent 声明可能类似于：

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="http" />
        <data android:scheme="https" />
    </intent-filter>
</activity>
```

要了解数据选项的更多信息，可以查看 Intent 过滤器的 data 元素的 XML 定义，网址为 <https://developer.android.google.cn/guide/topics/manifest/data-element.html>。Intent 过滤器节点 data XML 子节点的子元素或特性包括：

+ host
+ mimeType
+ path
+ pathPattern
+ pathPrefix
+ port
+ scheme

mimeType 是一个经常用到的特性。例如，下面是显示一个笔记列表的活动的 Intent 过滤器，它表明 MIME 类型为笔记目录：

```xml
<intent-filter>
	<action android:name="android.intent.action.VIEW" />
    <data android:mimeType="vnd.android.cursor.dir/vnd.google.note" />
</intent-filter>
```

**3. 使用 extra 信息**

extra 数据以键/值对的形式表示：键名称应该以包名称开头，值可以是任何基本的数据类型或任意对象。只要它实现了 android.os.Parcelable 接口即可。 extra 信息使用 Android 类 android.os.Bundle 表示。

Intent 类的以下两个方法可用于访问 extra Bundle：

```java
// Get the Bundle from an Intent 
Bundle extraBundle = intent.getExtras();

// Place a bundle in an intent
Bundle anotherBundle = new Bundle();

// populate the boundle with key/value pairs
...
// set the bundle on the Intent
intent.putExtras(anotherBundle);
```

可以使用许多方法来向包添加基本类型。下面给出了一些向 extra 数据添加简单数据类型的方法：

```java
putExtra(String name, boolean value);
putExtra(String name, int value);
putExtra(String name, double value);
putExtra(String name, String value);
```

以下是一些稍微复杂的 extra 数据：

```java
// simple array support
putExtra(String name, int[] values);
putExtra(String name, float[] values);

// Serializable objects
putExtra(String name, Serializable value);

// Parcelable support
putExtra(String name, Parcelable value);

// Add another bundle at a given key
// Bundles in bundles
putExtra(String name, Bundle value);

// Add bundles from another intent
// copy of bundles
putExtra(String name, Intent anotherIntent);

// Explicit Array List support
putIntegerArrayListExtra(String name, ArrayList arrayList);
putParcelableArrayListExtra(String name, ArrayList arrayList);
putStringArrayListExtra(String name, ArrayList arrayList);
```

Intent 类定义带有某些操作的 extra 键字符串。在 <https://developer.android.google.cn/reference/android/content/Intent.html#EXTRA_ALARM_COUNT> 上可以看到大量 extra 信息键常量。

**4. 使用组件直接调用活动**

Android 提供了一种更直接的方式来启动活动：指定活动的 ComponentName。Intent 类中有许多方法可用于指定组件：

```java
setComponent(ComponentName name);
setClassName(String packageName, String classNameInThatPackage);
setClassName(Context context, String classNameInThatContext);
setClass(Context context, Class classObjectInThatContext);
```

ComponentName 将一个包名和类名包装在一起。例如，以下代码调用模拟器附带的 contacts 活动：

```java
Intent intent = new Intent();
intent.setComponent(new ComponentName("com.android.contacts", "com.android.contacts.DialContactsEntryActivity"));
startActivity(intent);
```

请注意，包名和类名是完全限定的。再看看 BasicViewActivity 代码片段：

```java
public class BasicViewActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.some_view);
    }
}
```

有了这段代码，可以使用以下diam来启动此活动：

```java
Intent directIntent = new Intent(activity, BasicViewActivity.class);
activity.start(directIntent);
```

**5. Intent 类别**

可以将活动分类为各种类别，以便可以根据类别名来搜索它们。

类别的字符串格式遵循 category 定义约定：

```
android.intent.category.LAUNCHER
```

<center>表5-1 活动类别及其说明</center>

| 类别名称                      | 说明                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| CATEGORY_DEFAULT              | 此类活动可以将自身声明为 DEFAULT 活动，以供隐式 Intent 调用，如果未为活动定义此类别，那么每次都需要通过该活动的类名显示调用它。这就是会看到通过一般操作或其他操作名称来调用的活动使用默认类别规范的原因 |
| CATEGORY_BROWSABLE            | 此类活动可以将自身声明为 BROWSABLE，方法是向浏览器承诺它启动后不会影响浏览器安全 |
| CATEGORY_TAB                  | 此类活动可以嵌入在带选项卡的父活动中                         |
| CATEGORY_ALTERNATIVE          | 对于正在查看的某些数据类型，此类活动可以将自身声明为 ALTERNATIVE 活动。在查看文档时，这些项目通常显示为选项菜单的一部分。例如，打印视图被视为常规视图的替代视图 |
| CATEGORY_SELECTED_ALTERNATIVE | 对于某些数据类型，此类活动可以将自身声明为 ALTERNATIVE活动。这类似于为文本文档或 HTML 文档列出一系列可用的编辑器 |
| CATEGORY_LAUNCHER             | 如果将此类别分配给一个活动，可以在启动屏幕上列出该活动       |
| CATEGORY_HOME                 | 此类活动表示主屏幕。通常，应该只有一个这种类型的活动。如果有多个，系统将提示挑选一个 |
| CATEGORY_PREFERENCE           | 此活动将一个活动标识为首选活动，这样该活动就会显示在首选项屏幕上 |
| CATEGORY_GADGET               | 此类活动可以嵌入到父活动中                                   |
| CATEGORY_TEST                 | 测试活动                                                     |
| CATEGORY_EMBED                | 此类别已由 GADGET 类别取代，但为了实现向后兼容性，它仍然被保留了下来。 |

要了解这些活动类别的详细信息，可以访问 Intent 类的 Android SDK URL：

<https://developer.android.com/android/reference/android/content/Intent.html#CATEGORY_ALTERNATIVE>。

下面这个例子检索与 CATEGERY_LAUNCHER 类别匹配的主要活动的集合：

```java
Intent mainIntent = new Intent(Intent.ACTION_MAIN, null);
mainIntent.addCategory(Intent.CATEGORY_LAUNCHER);
PackageManager pm = getPackageManager();
List<ResolveInfo> list = pm.queryIntentActivities(mainIntent, 0);
```

这是前面代码的扩展，它遍历活动列表，如果一个活动与一个名称相匹配，则调用该活动。在代码中，我们随意使用了一个名称来测试它。

```java
for (ResolveInfo ri : list) {
    // ri.activityInfo.
    Log.d("test", ri.toString());
    String packagename = ri.activityInfo.packageName;
    String classname = ri.activityInfo.name;
    Log.d("test", packagename + ":" + classname);
    if (classname.equals("com.ai.androidbook.resources.TestActivity")) {
        Intent ni = new Intent();
        ni.setClassName(packageName, classname);
        activity.startActivity(in);
    }
}
```

实际上还可以进一步完善，可以根据前面的 Intent 类别 CATEGORY_LAUNCHER 来启动活动：

```java
public static void invokeAMainApp(Activity activity) {
    Intent mainIntent = new Intent(Intent.ACTION_MAIN, null);
    mainIntent.addCategory(Intent.CATEGORY_LAUNCHER);
    activity.startActivity(mainIntent);
}
```

下面给出了另一个使用 Intent 转到主页的例子：

```java
// Go to home screen
Intent mainIntent = new Intent(Intent.ACTION_MAIN, null);
mainIntent.addCategory(Intent.CATEGORY_HOME);
startActivity(mainIntent);
```

如果不希望使用 Android 的默认主页，可以编写自己的活动并将其声明为 HOME 类别。对于这种情况，前面的代码将提供一个打开主活动的选项，因为在注册了多个主活动：

```xml
// Replace the home screen with yours
<intent-file>
	<action android:name="android.intent.action.MAIN" />
    <category android:name="android.intent.category.HOME" />
    <category android:name="android.intent.category.DEFAULT" />
</intent-file>
```

**6. 将 Intent 解析为组件的规则**

让我们看看隐式 Intent 的每个部分的匹配条件。

+ 操作

如果一个 Intent 有一个操作，Intent 过滤器必须将该操作包含到其操作列表中，或者不包含任何操作。所以，如果 Intent 过滤器没有定义操作，则该 Intent 过滤器可匹配所有传入的 Intent 操作。

如果在 Intent 过滤器中指定了一个或多个操作，至少一个操作必须与传入的 Intent 操作匹配。

+ 数据

如果 Intent 过滤器中没有指定数据特征，它将不会匹配包含任何数据或数据特性的传入的 Intent。这意味着它仅查找没有指定任何数据的 Intent。

（过滤器中）缺少数据和缺少操作的情况是相反的。如果过滤器中没有操作，将匹配所有内容。如果过滤器中没有数据，Intent 中的每部分数据都不会匹配。

+ 数据类型

  要匹配一种数据类型，传入 Intent 的数据类型必须是 Intent 过滤器中指定的数据类型之一。Intent 中数类型必须存在于 Intent 过滤器中。

  传入 Intent 的数据类型可通过两种方式确定。第一种是，如果数据 URI 是一个内容或文件 URI，ContentProvider 或 Android 将确定类型。第二种方式是查看 Intent 的显示数据类型。此方式要生效，传入的 Intent 不应设置数据 URI，因为当对 Intent 调用 setType 时会自动设置它。

  作为其 MIME 类型规范的一部分，Android 还支持使用星号（*）作为子类型来涵盖所有可能的子类型。

  另外，数据类型区分大小写。

+ 数据模式

  要匹配数据模式，传入 Intent 的数据模式必须是 Intent 过滤器中指定的模式之一。换句话说，传入的数据模式必须存在于 Intent 过滤器中。

  传入 Intent 的模式是数据 URI 的第一部分。Intent 没有设置模式的方法。它完全从类似 <http://www.somesit.com/somepath> 这样的 Intent 数据 URI 派生而来。

  如果传入 Intent URI 的数据模式为 content: 或 file:，它会被视为一个匹配值，无论 Intent 过滤器模式、域和路径是什么。依据 SDK，情况就是如此，因为每个组件都应该知道如何从内容或文件 URL 处读取数据，这些 URL 基本上位于本地。换句话说，所有组件都应该支持这两种 URL 类型。

  模式也区分大小写。

+ 数据授权

  如果过滤器中没有授权，则可以匹配任何传入的数据 URI 的授权（或域名）。如果在过滤器中指定了授权，比如 www.somesite.com，那么一种模式和一种授权应该与该传入 Intent 的数据 URI 相匹配。

  授权也区分大小写。

+ 数据路径

  如果 Intent 过滤器中没有数据路径，则可以匹配任何传入数据 URI 的路径。如果在过滤器中指定了路径，比如 somepath，那么一种模式，一种授权和一个数据路径应该与传入 Intent 的数据 URI 相匹配。

  路径也区分大小写。

+ Intent 类别

  传入的 Intent 中的每个类别都必须存在于过滤器类别列表中。过滤器中也可以包含更多类别。如果过滤器没有任何类别，它只会与没有提及任何类别的 Intent 匹配。

  但是，有一点需要注意。Android 将所有传递给 startActivity() 的隐式 Intent 视为好像它们至少包含一个类别：android.intent.category.DEFAULT。如果传入的 Intent 为隐式 Intent，startActivity() 中的代码只会搜索定义了 DEFAULT 类别的活动。所以每个希望通过隐式 Intent 调用的活动都必须在其过滤器中包含默认类别。

  即使活动的 Intent 过滤器中没有默认类别，如果知道它的显示组件名称，也能够像启动程序一样启动它。如果自行显示搜索匹配的 Intent，而不使用默认类别作为搜索条件，将能够通过这种方式启动这些活动。

  在这种意义上，这个 DEFAULT 类别是 startActivity 实现的一部分，而不是过滤器的内在行为。

  还需要注意另一点，Android 表明如果活动仅希望从启动程序屏幕调用，则没有必要包含默认类别。所以这些活动的过滤器中可能仅包含 MAIN 和 LAUNCHER 类别。不过，也可以为这些活动指定 DEFAULT 类别。

