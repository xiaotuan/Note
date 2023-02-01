[toc]

### 1. 在 xml 中定义 GridView

```xml
<?xml version="1.0" encoding="utf-8"?><!-- This file is at /res/layout/gridview.xml -->
<GridView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/gridview"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:columnWidth="100px"
    android:gravity="center"
    android:horizontalSpacing="10px"
    android:numColumns="auto_fit"
    android:padding="10px"
    android:stretchMode="columnWidth"
    android:verticalSpacing="10px" />
```

### 2. 在代码中使用 GridView

#### 2.1 Kotlin

```kotlin
import android.provider.ContactsContract
import android.widget.GridView
import android.widget.SimpleCursorAdapter

val gv = findViewById<GridView>(R.id.gridview)

val c = contentResolver.query(ContactsContract.Contacts.CONTENT_URI,
                              null, null, null, ContactsContract.Contacts.DISPLAY_NAME)

val cols = arrayOf(ContactsContract.Contacts.DISPLAY_NAME)
val views = intArrayOf(android.R.id.text1)

val adapter = SimpleCursorAdapter(this,
                                  android.R.layout.simple_list_item_1,
                                  c, cols, views
                                 )
gv.adapter = adapter
```

#### 2.2 Java

```java
import android.database.Cursor;
import android.provider.ContactsContract;
import android.widget.GridView;
import android.widget.SimpleCursorAdapter;

GridView gv = findViewById(R.id.gridview);

Cursor c = getContentResolver().query(ContactsContract.Contacts.CONTENT_URI,
null, null, null, ContactsContract.Contacts.DISPLAY_NAME);

String[] cols = new String[]{ContactsContract.Contacts.DISPLAY_NAME};
int[] views = new int[]{android.R.id.text1};

SimpleCursorAdapter adapter = new SimpleCursorAdapter(this,
android.R.layout.simple_list_item_1,
c, cols, views);
gv.setAdapter(adapter);
```

