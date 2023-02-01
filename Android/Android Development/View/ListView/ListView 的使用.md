[toc]

### 1. 在 xml 中定义 ListView

```xml
<?xml version="1.0" encoding="utf-8"?>
<ListView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@android:id/list"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
```

### 2. 在代码中使用 ListView

#### 2.1 Kotlin

```kotlin
import android.content.ContentUris
import android.content.Intent
import android.os.Bundle
import android.provider.ContactsContract
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.ListView
import android.widget.SimpleCursorAdapter
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ListViewActivity2: AppCompatActivity(), AdapterView.OnItemClickListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.listview)

        val listView = findViewById<ListView>(android.R.id.list)

        val c = contentResolver.query(ContactsContract.Contacts.CONTENT_URI,
            null, null, null, ContactsContract.Contacts.DISPLAY_NAME)

        val cols = arrayOf(ContactsContract.Contacts.DISPLAY_NAME)
        val views = intArrayOf(android.R.id.text1)

        val adapter = SimpleCursorAdapter(this,
            android.R.layout.simple_list_item_1,
            c, cols, views
        )

        listView.adapter = adapter
        listView.onItemClickListener = this
    }

    override fun onItemClick(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        Log.v("ListViewActivity", "in onItemClick with ${(view as TextView).text}. Position = $position. Id = $id")
        val selectedPersion = ContentUris.withAppendedId(
            ContactsContract.Contacts.CONTENT_URI, id
        )
        val intent = Intent(Intent.ACTION_VIEW, selectedPersion)
        startActivity(intent)
    }
}
```

#### 2.2 Java

```java

import android.content.ContentUris;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;
import android.widget.TextView;
import android.widget.AdapterView.OnItemClickListener;

import androidx.appcompat.app.AppCompatActivity;

public class ListViewActivity2 extends AppCompatActivity implements OnItemClickListener {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.listview);

        ListView lv = findViewById(android.R.id.list);

        Cursor c = getContentResolver().query(ContactsContract.Contacts.CONTENT_URI,
                null, null, null, ContactsContract.Contacts.DISPLAY_NAME);

        String[] cols = new String[]{ContactsContract.Contacts.DISPLAY_NAME};
        int[] views = new int[]{android.R.id.text1};

        SimpleCursorAdapter adapter = new SimpleCursorAdapter(this,
                android.R.layout.simple_list_item_1,
                c, cols, views);
        lv.setAdapter(adapter);
        lv.setOnItemClickListener(this);
    }

    public void onItemClick(AdapterView<?> adView, View target, int position, long id) {
        Log.v("ListViewActivity", "in onItemClick with " + ((TextView) target).getText() +
                ". Position = " + position + ". Id = " + id);
        Uri selectedPerson = ContentUris.withAppendedId(
                ContactsContract.Contacts.CONTENT_URI, id);
        Intent intent = new Intent(Intent.ACTION_VIEW, selectedPerson);
        startActivity(intent);
    }
}
```

