可以通过两种方式访问首选项的数据：

+ 调用 `PreferenceManager.getDefaultSharedPreferences(this)` 获取 `SharedPreferences` 对象，通过 `SharedPreferences` 对象对首选项的数据进行读取或修改。

  **Kotlin**

  ```kotlin
  import android.preference.PreferenceManager;
  
  val sp = PreferenceManager.getDefaultSharedPreferences(this)
  val value = sp.getString(getString(R.string.selected_flight_sort_option), null)
  ```

  **Java**

  ```java
  import android.content.SharedPreferences;
  import android.preference.PreferenceManager;
  
  SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(this);
  String value = sp.getString(getString(R.string.selected_flight_sort_option), null);
  ```

+ 调用 `getSharedPreferences()` 方法，传入首选项文件名称。例如：

  **Kotlin**
  
  ```kotlin
  val sp = getSharedPreferences("${packageName}_preferences", Context.MODE_PRIVATE);
          val value = sp.getString(getString(R.string.selected_flight_sort_option), null)
  ```
  
  **Java**
  
  ```java
  import android.content.SharedPreferences;
  
  SharedPreferences sp = getSharedPreferences(getPackageName()+"_preferences", Context.MODE_PRIVATE);
  String value = sp.getString(getString(R.string.selected_flight_sort_option), null);
  ```
  

> 注意
>
> + `SharedPreferences getSharedPreferences(String name, int mode)` 方法中，mode 的值必须是 Context.MODE_PRIVATE。
> + `String getString(String key, @Nullable String defValue)` 方法中的 key 对应着首选项的 key 。

