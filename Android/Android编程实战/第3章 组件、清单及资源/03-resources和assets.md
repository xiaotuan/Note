[toc]

> 可在 <http://developer.android.com/guide/topics/resources/providing-resources.html#table2> 找到所有资源限定符的列表，以及它们的优先次序和含义。

### 1. 高级 string 资源

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="personal_welcome_message">Welcome %s!</string>
    <plurals name="inbox_message_count">
        <item quantity="zero">Your inbox is completely empty!</item>
        <item quantity="one">You one message in your inbox!</item>
        <item quantity="two">You two message waiting to be read!</item>
        <item quantity="few">You have %d messages waiting!</item>
        <item quantity="many">%1$d message in your inbox! %2$s, you should really login here more often!</item>
        <item quantity="other">%1$d message in your inbox! %2$s, you should really login here more often!</item>
    </plurals>
    <string-array name="default_categories">
        <item>Work</item>
        <item>Personal</item>
        <item>Private</item>
        <item>Spam</item>
        <item>Trash</item>
        <item>Draft</item>
    </string-array>
</resources>
```

下面的代码片段显示了如何使用 getString 方法来访问资源，并传递一个 String 变量作为输入。

```java
public void showWelcomeMessage(String name) {
    ((TextView) findViewById(R.id.welcome_message_field)).setText(getString(R.string.personal_welcome_message, name));
}
```

> 可在 <http://developer.android.com/reference/java/util/Formatter.html> 找到 java.util.Formatter 类格式化字符串资源的详细规则。

可以使用下面方法使用一个复数形式的字符串资源。

```java
public void showInboxCountMessage(int inboxCount, String name) {
    Resources res = getResources();
    String inboxCountMessage = res.getQuantityString(R.plurals.inbox_message_count, inboxCount, name);
    ((TextView) findViewById(R.id.inbox_count_field)).setText(inboxCountMessage);
}
```

可以通过下面代码使用字符串数组资源。

```java
public void displayCategories() {
    ListView listView = (ListView) findViewById(R.id.category_list);
    Resources res = getResources();
    String[] categories = res.getStringArray(R.array.default_categories);
    ArrayAdapter<String> categoriesadapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, android.R.id.text1, categories);
    listView.setAdapter(categoriesadapter);
}
```

### 2. 本地化

第一个选择是使用谷歌翻译工具包 Google Translator Toolkit。

>可在 <http://translate.google.com/toolkit> 访问谷歌翻译工具包。

### 3. 使用资源限定符

> <http://www.mcc-mnc.com> 上有各种移动国家码（MCC）和移动网络号码（MNC）。

如果运营商是英国沃达丰，资源目录应该命名为 values-mcc234-mnc15。接下来只需复制该资源文件，并把布尔值修改成 true。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
	<bool name="disable_ads_by_default">false</bool>
</resources>
```

> 使用带有 MCC 和 MNC 限定符的资源控制应用程序逻辑实际上并不安全。一个技术熟练的用户可以相对轻松地绕过这个检测。然而，在大多数情况下，可以认为这样做足够安全。但要注意的是，设备安装了电话支持才能过滤 MCC 和 MNC。

### 4. 使用 assets

raw 资源目录里存储任意文件。然而，由于 assets 目录支持子文件夹，在某些情况下，开发者可能仍然要使用 assets。

下面的代码显示了如何使用 SoundPool 和 AssetManager API 加载 assets/soundfx 目录内的音频文件。记得关闭用 AssetManager 打开的文件，否则，应用程序可能发生内存泄漏。

```java
public HashMap<String, Integer> loadSoundEffects(SoundPool soundPool) throws IOException {
    AssetManager assetManager = getAssets();
    String[] soundEffectFiles = assetManager.list("soundfx");
    HashMap<String, Integer> soundEffectMap = new HashMap<>();
    for (String soundEffectFile : soundEffectFiles) {
        AssetFileDescriptor fileDescriptor = assetManager.openFd("soundfx/" + soundEffectFile);
        int id = soundPool.load(fileDescriptor, 1);
        soundEffectMap.put(soundEffectFile, id);
        fileDescriptor.close();
    }
    return soundEffectMap;
}
```

