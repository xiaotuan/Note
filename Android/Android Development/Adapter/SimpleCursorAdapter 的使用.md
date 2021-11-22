`SimpleCursorAdapter` 的构造函数类似于：

```
SimpleCursorAdapter(Context context, int layout, Cursor c, String[] from, int[] to)
```

例如：

**Kotlin**

```kotlin
import android.provider.ContactsContract
import android.widget.ListView
import android.widget.SimpleCursorAdapter

val listView = findViewById<ListView>(android.R.id.list)

val c = contentResolver.query(ContactsContract.Contacts.CONTENT_URI,
    null, null, null, ContactsContract.Contacts.DISPLAY_NAME)

val cols = arrayOf(ContactsContract.Contacts.DISPLAY_NAME)
val views = intArrayOf(android.R.id.text1)

val adapter = SimpleCursorAdapter(this,
    android.R.layout.simple_list_item_1,
    c, cols, views)

listView.adapter = adapter
```

**Java**

```java
import android.database.Cursor;
import android.provider.ContactsContract;
import android.widget.SimpleCursorAdapter;

Cursor c = getContentResolver().query(ContactsContract.Contacts.CONTENT_URI,
        null, null, null, ContactsContract.Contacts.DISPLAY_NAME);

String[] cols = new String[]{ContactsContract.Contacts.DISPLAY_NAME};
int[] views = new int[]{android.R.id.text1};

SimpleCursorAdapter adapter = new SimpleCursorAdapter(this,
        android.R.layout.simple_list_item_1,
        c, cols, views);
this.setListAdapter(adapter);
```

>   注意：上面的构造函数已经标记为过时，推荐使用：
>
>   ```
>   SimpleCursorAdapter(Context context, int layout, Cursor c, String[] from,
>               int[] to, int flags)
>   ```
>
>   其中 flags 的值可以为：CursorAdapter.FLAG_REGISTER_CONTENT_OBSERVER