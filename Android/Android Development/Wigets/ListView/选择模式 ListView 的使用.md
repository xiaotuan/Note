[toc]

### 1. 在 xml 中定义 ListView

```xml
<?xml version="1.0" encoding="utf-8"?>
<ListView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@android:id/list"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
```

### 2. 在代码中使用 ListView 的多选模式

#### 2.1 Kotlin

```kotlin
import android.content.ContentUris
import android.os.Bundle
import android.provider.ContactsContract
import android.util.Log
import android.view.View
import android.widget.ListView
import android.widget.SimpleCursorAdapter
import androidx.appcompat.app.AppCompatActivity

class ListViewActivity4: AppCompatActivity() {

    private lateinit var adapter: SimpleCursorAdapter
    private lateinit var lv: ListView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.list)

        lv = findViewById(android.R.id.list)

        val projection = arrayOf(
            ContactsContract.Contacts._ID,
            ContactsContract.Contacts.DISPLAY_NAME
        )

        val c = contentResolver.query(ContactsContract.Contacts.CONTENT_URI,
            null, null, null, ContactsContract.Contacts.DISPLAY_NAME)

        val cols = arrayOf(ContactsContract.Contacts.DISPLAY_NAME)
        val views = intArrayOf(android.R.id.text1)

        adapter = SimpleCursorAdapter(this,
            android.R.layout.simple_list_item_multiple_choice,
            c, cols, views
        )

        lv.adapter = adapter

        lv.choiceMode = ListView.CHOICE_MODE_MULTIPLE
    }

    public fun doClick(view: View?) {
        if(!adapter.hasStableIds()) {
            Log.v(TAG, "Data is not stable")
            return
        }
        val viewItems = lv.checkedItemIds
        for (i in viewItems.indices) {
            val selectedPerson = ContentUris.withAppendedId(
                ContactsContract.Contacts.CONTENT_URI, viewItems[i]
            )
            Log.v(TAG, "$selectedPerson is checked.")
        }
    }

    companion object {
        const val TAG = "ListViewActivity4"
    }
}
```

#### 2.2 Java

```java
import android.content.ContentUris;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.View;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;

import androidx.appcompat.app.AppCompatActivity;

public class ListViewActivity4 extends AppCompatActivity {
    private static final String TAG = "ListViewActivity4";
    private static final Uri CONTACTS_URI = ContactsContract.Contacts.CONTENT_URI;
    private SimpleCursorAdapter adapter = null;
    private ListView lv = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.list);

        lv = findViewById(android.R.id.list);

        String[] projection = new String[]{ContactsContract.Contacts._ID,
                ContactsContract.Contacts.DISPLAY_NAME};

        Cursor c = getContentResolver().query(CONTACTS_URI,
                null, null, null, ContactsContract.Contacts.DISPLAY_NAME);

        String[] cols = new String[]{ContactsContract.Contacts.DISPLAY_NAME};
        int[] views = new int[]{android.R.id.text1};

        adapter = new SimpleCursorAdapter(this,
                android.R.layout.simple_list_item_multiple_choice,
                c, cols, views);

        lv.setAdapter(adapter);

        lv.setChoiceMode(ListView.CHOICE_MODE_MULTIPLE);
    }

    public void doClick(View view) {
        if (!adapter.hasStableIds()) {
            Log.v(TAG, "Data is not stable");
            return;
        }
        long[] viewItems = lv.getCheckedItemIds();
        for (int i = 0; i < viewItems.length; i++) {
            Uri selectedPerson = ContentUris.withAppendedId(
                    CONTACTS_URI, viewItems[i]);

            Log.v(TAG, selectedPerson.toString() + " is checked.");
        }
    }
}
```

>   注意：
>
>   1.   在获取选中项前，最好调用 `hasStableIds()` 方法，判断当前选中状态是否稳定。
>   2.   可以将 `ListView` 的选择模式设置为 `ListView.CHOICE_MODE_SINGLE`，这样 `ListView` 为单选模式。可以通过 `getItemAtPosition()` 获取选中的项。