[toc]

### 1. ListPreference 的一些特性

| 特性                 | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| android:key          | 选项的名称或键                                               |
| android:title        | 选项的标题                                                   |
| android:summary      | 选项的简短摘要                                               |
| android:entries      | 可将选项设置成的列表项的文本                                 |
| android:entryValues  | 定义每个列表的键或值。请注意，每个列表项具有一些文本和一个值。文本由 entries 定义，值由 entryValues 定义。 |
| android:dialogTitle  | 对话框的标题，在视图显示为模态对话框时使用                   |
| android:defaultValue | 项列表中选项的默认值                                         |

### 2. 定义首选项 XML 文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android"
    android:key="flight_option_preference"
    android:title="@string/prefTitle"
    android:summary="@string/prefSummary">

    <ListPreference
        android:key="@string/selected_flight_sort_option"
        android:title="@string/listTitle"
        android:summary="@string/listSummary"
        android:entries="@array/flight_sort_options"
        android:entryValues="@array/flight_sort_options_values"
        android:dialogTitle="@string/dialogTitle"
        android:defaultValue="@string/flight_sort_option_default_value" />

</PreferenceScreen>
```

相关资源文件：

**arrays.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="flight_sort_options">
        <item>Total Cost</item>
        <item># of Stops</item>
        <item>Airline</item>
    </string-array>
    <string-array name="flight_sort_options_values">
        <item>0</item>
        <item>1</item>
        <item>2</item>
    </string-array>
</resources>
```

**strings.xml**

```xml
<resources>
    <string name="prefTitle">My Preferences</string>
    <string name="prefSummary">Set Flight Option Preferences</string>
    <string name="flight_sort_option_default_value">1</string>
    <string name="dialogTitle">Choose Flight Options</string>
    <string name="listSummary">Set Search Options</string>
    <string name="listTitle">Flight Options</string>
    <string name="selected_flight_sort_option">selected_flight_sort_option</string>
</resources>
```

### 2. 显示首选项

#### 2.1 Kotlin 版本

```kotlin
import android.os.Bundle
import android.preference.PreferenceActivity

class MainActivity : PreferenceActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        addPreferencesFromResource(R.xml.flightoptions)
    }

}
```

#### 2.2 Java 版本

```java
import android.os.Bundle;
import android.preference.PreferenceActivity;

public class MainActivity extends PreferenceActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        addPreferencesFromResource(R.xml.flightoptions);
    }

}
```

