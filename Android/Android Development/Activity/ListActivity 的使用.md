>   提示：`ListActivity` 已标记为过时类。

### 1. Kotlin 版本

```kotlin
import android.app.ListActivity
import android.os.Bundle
import android.provider.ContactsContract
import android.widget.CursorAdapter
import android.widget.SimpleCursorAdapter

class ListViewActivity: ListActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val c = contentResolver.query(ContactsContract.Contacts.CONTENT_URI,
            null, null, null, ContactsContract.Contacts.DISPLAY_NAME)
        
        val cols = arrayOf(ContactsContract.Contacts.DISPLAY_NAME)
        val views = intArrayOf(android.R.id.text1)
                CursorAdapter.FLAG_AUTO_REQUERY
        
        val adapter = SimpleCursorAdapter(this,
            android.R.layout.simple_list_item_1,
            c, cols, views)
        
        listView.adapter = adapter
    }
}
```

### 2. Java 版本

```java
import android.app.ListActivity;
import android.database.Cursor;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.widget.SimpleCursorAdapter;

public class ListViewActivity extends ListActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Cursor c = getContentResolver().query(ContactsContract.Contacts.CONTENT_URI,
                null, null, null, ContactsContract.Contacts.DISPLAY_NAME);

        String[] cols = new String[]{ContactsContract.Contacts.DISPLAY_NAME};
        int[] views = new int[]{android.R.id.text1};

        SimpleCursorAdapter adapter = new SimpleCursorAdapter(this,
                android.R.layout.simple_list_item_1,
                c, cols, views);
        this.setListAdapter(adapter);
    }
}
```

>   提示：如果需要创建布局文件，则在布局文件中必须包含 ID 为 `android:id/list` 的 `ListView` 控件。