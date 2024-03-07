创建一个继承自 `SimpleCursorAdapter` 的类后，需要重写并实现 `newView()` 和 `bindView()` 方法。

每次在显示新行时，都会调用 `newView()` 方法，通过在 `newView()` 方法中调用 `LayoutInflater` 类来加载适配器的布局。

一旦调用了 `newView()` 方法并初始化了行的实际布局，下一个被调用的方法就是 `bindView()`。此方法将先前实例化的新 `View` 对象以及属于此适配器类的 `Cursor` 作为参数。需要注意的是，传入的游标已经移动到正确的索引中。

**CustomContacts.java**

```java
package com.qty.customcontacts;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.loader.app.LoaderManager;
import androidx.loader.content.CursorLoader;
import androidx.loader.content.Loader;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.os.Build;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;

public class CustomContacts extends AppCompatActivity implements LoaderManager.LoaderCallbacks<Cursor>, AdapterView.OnItemClickListener {
    private static String TAG = "SimpleContactsActivity";
    private static int PERMISSION_REQUEST_CODE = 999;

    private ListView listView;
    private LoaderManager loaderManager;
    private SimpleCursorAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.list);

        listView = findViewById(android.R.id.list);
        listView.setOnItemClickListener(this);

        loaderManager = LoaderManager.getInstance(this);

        if (checkCallingOrSelfPermission(android.Manifest.permission.READ_CONTACTS) != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[]{android.Manifest.permission.READ_CONTACTS}, PERMISSION_REQUEST_CODE);
        } else {
            refreshUI();
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PERMISSION_REQUEST_CODE && resultCode == RESULT_OK
                && checkCallingOrSelfPermission(Manifest.permission.READ_CONTACTS) == PackageManager.PERMISSION_GRANTED) {
            refreshUI();
        } else {
            finish();
        }
    }

    private void refreshUI() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.ICE_CREAM_SANDWICH_MR1) {
            loaderManager.initLoader(0, null, this);
        } else {
            // Make query to contact contentprovider
            String[] projections = new String[]{
                    ContactsContract.CommonDataKinds.Phone._ID,
                    ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME,
                    ContactsContract.CommonDataKinds.Phone.NUMBER,
                    ContactsContract.CommonDataKinds.Phone.TYPE
            };
            Cursor c = getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI,
                    projections, null, null, null);
            startManagingCursor(c);

            // The desired columns to be bound
            String[] columns = new String[]{
                    ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME,
                    ContactsContract.CommonDataKinds.Phone.NUMBER,
                    ContactsContract.CommonDataKinds.Phone.TYPE
            };

            // The xml defined views for each field to be bound to
            int[] to = new int[]{
                    R.id.name_entry,
                    R.id.number_entry,
                    R.id.number_type_entry
            };

            // Create adapter with cursor pointing to desired data
            adapter = new CustomContactsAdapter(this, R.layout.list_entry, c, columns, to, SimpleCursorAdapter.FLAG_REGISTER_CONTENT_OBSERVER);

            // Set this adapter as your list activity's adapter
            listView.setAdapter(adapter);
        }
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Cursor c = (Cursor) adapter.getItem(position);

        int nameCol = c.getColumnIndex(ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME);
        int numCol = c.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER);
        int typeCol = c.getColumnIndex(ContactsContract.CommonDataKinds.Phone.TYPE);

        String name = c.getString(nameCol);
        String number = c.getString(numCol);
        int type = c.getInt(typeCol);

        Log.d(TAG, "onItemClick=>Click on " + name + " " + number + " " + type);
    }

    @NonNull
    @Override
    public Loader<Cursor> onCreateLoader(int id, @Nullable Bundle args) {
        String[] projections = new String[]{
                ContactsContract.CommonDataKinds.Phone._ID,
                ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME,
                ContactsContract.CommonDataKinds.Phone.NUMBER,
                ContactsContract.CommonDataKinds.Phone.TYPE
        };
        return new CursorLoader(this,
                ContactsContract.CommonDataKinds.Phone.CONTENT_URI,
                projections,
                null,
                null,
                null
        );
    }

    @Override
    public void onLoadFinished(@NonNull Loader<Cursor> loader, Cursor data) {
        if (data != null) {
            // The desired columns to be bound
            String[] columns = new String[]{
                    ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME,
                    ContactsContract.CommonDataKinds.Phone.NUMBER,
                    ContactsContract.CommonDataKinds.Phone.TYPE
            };

            // The xml defined views for each field to be bound to
            int[] to = new int[]{
                    R.id.name_entry,
                    R.id.number_entry,
                    R.id.number_type_entry
            };

            // Create adapter with cursor pointing to desired data
            adapter = new CustomContactsAdapter(this, R.layout.list_entry, data, columns, to, SimpleCursorAdapter.FLAG_REGISTER_CONTENT_OBSERVER);

            // Set this adapter as your list activity's adapter
            listView.setAdapter(adapter);
        }
    }

    @Override
    public void onLoaderReset(@NonNull Loader<Cursor> loader) {
        adapter.swapCursor(null);
    }

}
```

**CustomContactsAdapter.java**

```java
package com.qty.customcontacts;

import android.content.Context;
import android.database.Cursor;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.SimpleCursorAdapter;
import android.widget.TextView;

public class CustomContactsAdapter extends SimpleCursorAdapter {

    private LayoutInflater inflater;
    private int layout;

    public CustomContactsAdapter(Context context, int layout, Cursor c, String[] from, int[] to, int flags) {
        super(context, layout, c, from, to, flags);
        this.layout = layout;
        this.inflater = LayoutInflater.from(context);
    }

    @Override
    public View newView(Context context, Cursor cursor, ViewGroup parent) {
        View v = inflater.inflate(layout, parent, false);
        return v;
    }

    @Override
    public void bindView(View view, Context context, Cursor cursor) {
        int nameCol = cursor.getColumnIndex(ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME);
        int numCol = cursor.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER);
        int typeCol = cursor.getColumnIndex(ContactsContract.CommonDataKinds.Phone.TYPE);

        String name = cursor.getString(nameCol);
        String number = cursor.getString(numCol);
        int type = cursor.getInt(typeCol);

        String numType = "";
        switch (type) {
            case ContactsContract.CommonDataKinds.Phone.TYPE_HOME:
                numType = "HOME";
                break;

            case ContactsContract.CommonDataKinds.Phone.TYPE_MOBILE:
                numType = "MOBILE";
                break;

            case ContactsContract.CommonDataKinds.Phone.TYPE_WORK:
                numType = "WORK";
                break;

            default:
                numType = "MOBILE";
                break;
        }

        // Find the view and set the name
        TextView name_text = (TextView) view.findViewById(R.id.name_entry);
        name_text.setText(name);
        TextView number_text = (TextView) view.findViewById(R.id.number_entry);
        number_text.setText(number);
        TextView type_text = view.findViewById(R.id.number_type_entry);
        type_text.setText(numType);
    }

}
```

**list.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_marginTop="8dp"
    android:layout_marginBottom="8dp"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <ListView
        android:id="@android:id/list"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>

</LinearLayout>
```

**list_entry.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="10dp">

    <TextView
        android:id="@+id/name_entry"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="28sp" />

    <TextView
        android:id="@+id/number_entry"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="16sp" />

    <TextView
        android:id="@+id/number_type_entry"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textColor="#DDD"
        android:textSize="14sp" />

</LinearLayout>
```

