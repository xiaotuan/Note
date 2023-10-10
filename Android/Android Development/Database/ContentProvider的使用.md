[toc]

### 1. 计划数据库

#### 1.1 定义内容提供器的授权 URI

授权 `URI` 的格式如下：

**Kotlin 版本**

```kotlin
const val AUTHORITY = "com.qty.provider.BookProvider"
```

**Java 版本**

```java
public static final String AUTHORITY = "com.qty.provider.BookProvider";
```

#### 1.2 定义数据库和数据表、字段名称

完整的计划数据库代码如下：

**Kotlin 版本**

```kotlin
package com.qty.bookprovider

import android.net.Uri
import android.provider.BaseColumns

class BookProviderMetaData private constructor() {

    // inner class describing columns and their types
    class BookTableMetaData private constructor() {

        companion object {
            const val TABLE_NAME = "books"

            // uri and mime type definitions
            val CONTENT_URI = Uri.parse("content://$AUTHORITY/books")
            const val CONTENT_TYPE = "vnd.android.cursor.dir/vnd.androidbook.book"
            const val CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd/androidbook.book"

            const val DEFAULT_SORT_ORDER = "modified DESC"

            // Additional Columns start here.
            //Integer
            const val _ID = BaseColumns._ID
            // string type
            const val BOOK_NAME = "name"
            // string type
            const val BOOK_ISBN = "isbn"
            // string type
            const val BOOK_AUTHOR = "author"
            // Integer from System.currentTimeMillis()
            const val CREATED_DATE = "created"
            // Integer from System.currentTimeMillis()
            const val MODIFIED_DATE = "modified"
        }

    }

    companion object {
        const val AUTHORITY = "com.qty.provider.BookProvider"

        const val DATABASE_NAME = "book.db"
        const val DATABASE_VERSION = 1
        const val BOOKS_TABLE_NAME = "books"
    }
}
```

**Java 版本**

```java
package com.qty.bookprovider;

import android.net.Uri;
import android.provider.BaseColumns;

public class BookProviderMetaData {

    public static final String AUTHORITY = "com.qty.provider.BookProvider";

    public static final String DATABASE_NAME = "book.db";
    public static final int DATABASE_VERSION = 1;
    public static final String BOOKS_TABLE_NAME = "books";

    private BookProviderMetaData() {}

    //inner class describing columns and their types
    public static final class BookTableMetaData implements BaseColumns {

        private BookTableMetaData() {}

        public static final String TABLE_NAME = "books";

        //uri and mime type definitions
        public static final Uri CONTENT_URI = Uri.parse("content://" + AUTHORITY + "/books");
        public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.androidbook.book";
        public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.androidbook.book";

        public static final String DEFAULT_SORT_ORDER = "modified DESC";

        //Additional Columns start here.
        //string type
        public static final String BOOK_NAME = "name";
        //string type
        public static final String BOOK_ISBN = "isbn";
        //string type
        public static final String BOOK_AUTHOR = "author";
        //Integer from System.currentTimeMillis()
        public static final String CREATED_DATE = "created";
        //Integer from System.currentTimeMillis()
        public static final String MODIFIED_DATE = "modified";
    }

}
```

### 2. 扩展 ContentProvider

重写 `ContentProvider` 类的 `onCreate()` 方法来创建数据库，然后实现 `query`、`insert`、`update`、`delete` 和 `getType` 方法。下面是一个重写 `ContentProvider` 的示例:

**Kotlin 版本**

```kotlin
package com.qty.bookprovider

import android.content.*
import android.database.Cursor
import android.database.SQLException
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.database.sqlite.SQLiteQueryBuilder
import android.net.Uri
import android.text.TextUtils
import android.util.Log

class BookProvider : ContentProvider() {

    private lateinit var mOpenHelper: DatabaseHelper

    override fun onCreate(): Boolean {
        Log.d(TAG, "main onCreate called")
        mOpenHelper = DatabaseHelper(context)
        return true
    }

    @Synchronized override fun query(
        uri: Uri, projection: Array<String>?, selection: String?,
        selectionArgs: Array<String>?, sortOrder: String?
    ): Cursor? {
        val qb = SQLiteQueryBuilder()

        when (sUriMatcher.match(uri)) {
            INCOMING_BOOK_COLLECTION_RUI_INDICATOR -> {
                qb.tables = BookProviderMetaData.BookTableMetaData.TABLE_NAME
                qb.projectionMap = sBookProjectionMap
            }
            INCOMING_SINGLE_BOOK_URI_INDICATOR -> {
                qb.tables = BookProviderMetaData.BookTableMetaData.TABLE_NAME
                qb.projectionMap = sBookProjectionMap
                qb.appendWhere(BookProviderMetaData.BookTableMetaData._ID + "=" + uri.pathSegments[1])
            }
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }

        // if no sort order is specified use the default
        val orderBy = if (TextUtils.isEmpty(sortOrder)) {
            BookProviderMetaData.BookTableMetaData.DEFAULT_SORT_ORDER
        } else {
            sortOrder
        }

        // Get the database and run the query
        val c = qb.query(mOpenHelper.readableDatabase, projection, selection, selectionArgs, null, null, orderBy)

        // example of getting a count
        val i = c.count

        // Tell the cursor what uri to watch,
        // so it knows when its source data changes
        c.setNotificationUri(context?.contentResolver, uri)
        return c
    }

    @Synchronized override fun insert(uri: Uri, values: ContentValues?): Uri? {
        // Validate the requested uri
        if (sUriMatcher.match(uri) != INCOMING_BOOK_COLLECTION_RUI_INDICATOR) {
            throw IllegalArgumentException("Unknown URI $uri")
        }

        val values = if (values != null) {
            ContentValues(values)
        } else {
            ContentValues()
        }

        val now = System.currentTimeMillis() as Long

        // Make sure that the fields are all set
        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.CREATED_DATE)) {
            values.put(BookProviderMetaData.BookTableMetaData.CREATED_DATE, now)
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE)) {
            values.put(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE, now)
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_NAME)) {
            throw SQLException("Failed to insert row because Book Name is needed " + uri)
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_ISBN)) {
            values.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "Unknown ISBN")
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR)) {
            values.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "Unknown Author")
        }

        val rowId = mOpenHelper.writableDatabase.insert(BookProviderMetaData.BookTableMetaData.TABLE_NAME, BookProviderMetaData.BookTableMetaData.BOOK_NAME, values)
        if (rowId > 0) {
            val insertedBookUri = ContentUris.withAppendedId(BookProviderMetaData.BookTableMetaData.CONTENT_URI, rowId)
            context?.contentResolver?.notifyChange(insertedBookUri, null)
            return insertedBookUri
        }
        throw SQLException("Failed to insert row into $uri")
    }

    @Synchronized override fun delete(uri: Uri, selection: String?, selectionArgs: Array<String>?): Int {
        val count = when (sUriMatcher.match(uri)) {
            INCOMING_BOOK_COLLECTION_RUI_INDICATOR -> mOpenHelper.writableDatabase.delete(BookProviderMetaData.BookTableMetaData.TABLE_NAME, selection, selectionArgs)
            INCOMING_SINGLE_BOOK_URI_INDICATOR -> {
                val rowId = uri.pathSegments[1]
                mOpenHelper.writableDatabase.delete(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                    BookProviderMetaData.BookTableMetaData._ID + "=" + rowId
                            + (if(!TextUtils.isEmpty(selection))  " AND ( $selection )" else ""), selectionArgs)
            }
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }
        context?.contentResolver?.notifyChange(uri, null)
        return count
    }

    @Synchronized override fun update(
        uri: Uri, values: ContentValues?, selection: String?,
        selectionArgs: Array<String>?
    ): Int {
        val count = when (sUriMatcher.match(uri)) {
            INCOMING_BOOK_COLLECTION_RUI_INDICATOR -> mOpenHelper.writableDatabase.update(BookProviderMetaData.BookTableMetaData.TABLE_NAME, values, selection, selectionArgs)
            INCOMING_SINGLE_BOOK_URI_INDICATOR -> {
                val rowId = uri.pathSegments[1]
                mOpenHelper.writableDatabase.update(BookProviderMetaData.BookTableMetaData.TABLE_NAME, values,
                    BookProviderMetaData.BookTableMetaData._ID + "=" + rowId
                            + (if (!TextUtils.isEmpty(selection)) " AND ( $selection )" else ""), selectionArgs)
            }
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }
        context?.contentResolver?.notifyChange(uri, null)
        return count
    }

    override fun getType(uri: Uri): String? = when (sUriMatcher.match(uri)) {
        INCOMING_BOOK_COLLECTION_RUI_INDICATOR -> BookProviderMetaData.BookTableMetaData.CONTENT_TYPE
        INCOMING_SINGLE_BOOK_URI_INDICATOR -> BookProviderMetaData.BookTableMetaData.CONTENT_ITEM_TYPE
        else -> throw IllegalArgumentException("Unknown URI $uri")
    }

    private class DatabaseHelper(
        context: Context?
    ): SQLiteOpenHelper(context, BookProviderMetaData.DATABASE_NAME, null, BookProviderMetaData.DATABASE_VERSION) {

        override fun onCreate(db: SQLiteDatabase?) {
            Log.d(TAG, "inner oncreate called")
            db?.execSQL("CREATE TABLE " + BookProviderMetaData.BookTableMetaData.TABLE_NAME + " (" +
                    BookProviderMetaData.BookTableMetaData._ID + " INTEGER PRIMARY KEY," +
                    BookProviderMetaData.BookTableMetaData.BOOK_NAME + " TEXT," +
                    BookProviderMetaData.BookTableMetaData.BOOK_ISBN + " TEXT," +
                    BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR + " TEXT," +
                    BookProviderMetaData.BookTableMetaData.CREATED_DATE + " INTEGER," +
                    BookProviderMetaData.BookTableMetaData.MODIFIED_DATE + " INTEGER" +
                    ");"
            )
        }

        override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
            Log.d(TAG, "inner onupgrade called")
            Log.w(TAG, "Upgrading database from version "
                    + oldVersion + " to "
                    + newVersion + ", which will destroy all old data")
            db?.execSQL("DROP TABLE IF EXISTS " + BookProviderMetaData.BookTableMetaData.TABLE_NAME)
            onCreate(db)
        }
    }

    private companion object {
        // Logging helper tag. No significance to providers.
        const val TAG = "BookProvider"
        // Projection maps are similar to "as" construct
        // in an sql statement where by you can rename the
        // columns.
        val sBookProjectionMap: HashMap<String, String> = HashMap()
        // Provide a mechanism to identify
        // all the incoming uri patterns.
        val sUriMatcher = UriMatcher(UriMatcher.NO_MATCH)
        const val INCOMING_BOOK_COLLECTION_RUI_INDICATOR = 1
        const val INCOMING_SINGLE_BOOK_URI_INDICATOR = 2


        init {
            with(sBookProjectionMap) {
                put(BookProviderMetaData.BookTableMetaData._ID, BookProviderMetaData.BookTableMetaData._ID)
                put(BookProviderMetaData.BookTableMetaData.BOOK_NAME, BookProviderMetaData.BookTableMetaData.BOOK_NAME)
                put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, BookProviderMetaData.BookTableMetaData.BOOK_ISBN)
                put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR)
                put(BookProviderMetaData.BookTableMetaData.CREATED_DATE, BookProviderMetaData.BookTableMetaData.CREATED_DATE)
                put(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE, BookProviderMetaData.BookTableMetaData.MODIFIED_DATE)
            }
            with(sUriMatcher) {
                addURI(BookProviderMetaData.AUTHORITY, "books", INCOMING_BOOK_COLLECTION_RUI_INDICATOR)
                addURI(BookProviderMetaData.AUTHORITY, "books/#", INCOMING_SINGLE_BOOK_URI_INDICATOR)
            }
        }
    }
}
```

**Java 版本**

```java
package com.qty.bookprovider;

import android.content.ContentProvider;
import android.content.ContentUris;
import android.content.ContentValues;
import android.content.Context;
import android.content.UriMatcher;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.sqlite.SQLiteQueryBuilder;
import android.net.Uri;
import android.text.TextUtils;
import android.util.Log;

import java.util.HashMap;

public class BookProvider extends ContentProvider {

    //Logging helper tag. No significance to providers.
    private static final String TAG = "BookProvider";

    //Projection maps are similar to "as" construct
    //in an sql statement where by you can rename the
    //columns.
    private static final HashMap<String, String> sBooksProjectionMap;

    static {
        sBooksProjectionMap = new HashMap<>();
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData._ID,
                BookProviderMetaData.BookTableMetaData._ID);

        //name, isbn, author
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.BOOK_NAME,
                BookProviderMetaData.BookTableMetaData.BOOK_NAME);
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN,
                BookProviderMetaData.BookTableMetaData.BOOK_ISBN);
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR,
                BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR);

        //created date, modified date
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.CREATED_DATE,
                BookProviderMetaData.BookTableMetaData.CREATED_DATE);
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE,
                BookProviderMetaData.BookTableMetaData.MODIFIED_DATE);
    }

    //Provide a mechanism to identify
    //all the incoming uri patterns.
    private static final UriMatcher sUriMatcher;
    private static final int INCOMING_BOOK_COLLECTION_URI_INDICATOR = 1;
    private static final int INCOMING_SINGLE_BOOK_URI_INDICATOR = 2;

    static {
        sUriMatcher = new UriMatcher(UriMatcher.NO_MATCH);
        sUriMatcher.addURI(BookProviderMetaData.AUTHORITY, "books",
                INCOMING_BOOK_COLLECTION_URI_INDICATOR);
        sUriMatcher.addURI(BookProviderMetaData.AUTHORITY, "books/#",
                INCOMING_SINGLE_BOOK_URI_INDICATOR);

    }

    private DatabaseHelper mOpenHelper;

    @Override
    public boolean onCreate() {
        Log.d(TAG, "main onCreate called");
        mOpenHelper = new DatabaseHelper(getContext());
        return true;
    }

    @Override
    synchronized public int delete(Uri uri, String selection, String[] selectionArgs) {
        SQLiteDatabase db = mOpenHelper.getWritableDatabase();
        int count;
        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                count = db.delete(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                        selection, selectionArgs);
                break;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                String rowId = uri.getPathSegments().get(1);
                count = db.delete(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                        BookProviderMetaData.BookTableMetaData._ID + "=" + rowId
                                + (!TextUtils.isEmpty(selection) ? " AND (" + selection + ')' : ""),
                        selectionArgs);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }

        getContext().getContentResolver().notifyChange(uri, null);
        return count;
    }

    @Override
    public String getType(Uri uri) {
        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                return BookProviderMetaData.BookTableMetaData.CONTENT_TYPE;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                return BookProviderMetaData.BookTableMetaData.CONTENT_ITEM_TYPE;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }
    }

    @Override
    synchronized public Uri insert(Uri uri, ContentValues initialValues) {
        // Validate the requested uri
        if (sUriMatcher.match(uri)
                != INCOMING_BOOK_COLLECTION_URI_INDICATOR) {
            throw new IllegalArgumentException("Unknown URI " + uri);
        }

        ContentValues values;
        if (initialValues != null) {
            values = new ContentValues(initialValues);
        } else {
            values = new ContentValues();
        }

        Long now = System.currentTimeMillis();

        // Make sure that the fields are all set
        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.CREATED_DATE)) {
            values.put(BookProviderMetaData.BookTableMetaData.CREATED_DATE, now);
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE)) {
            values.put(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE, now);
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_NAME)) {
            throw new SQLException(
                    "Failed to insert row because Book Name is needed " + uri);
        }

        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_ISBN)) {
            values.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "Unknown ISBN");
        }
        if (!values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR)) {
            values.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "Unknown Author");
        }

        SQLiteDatabase db = mOpenHelper.getWritableDatabase();
        long rowId = db.insert(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                BookProviderMetaData.BookTableMetaData.BOOK_NAME, values);
        if (rowId > 0) {
            Uri insertedBookUri =
                    ContentUris.withAppendedId(
                            BookProviderMetaData.BookTableMetaData.CONTENT_URI, rowId);
            getContext()
                    .getContentResolver()
                    .notifyChange(insertedBookUri, null);

            return insertedBookUri;
        }

        throw new SQLException("Failed to insert row into " + uri);
    }

    @Override
    synchronized public Cursor query(Uri uri, String[] projection, String selection,
                        String[] selectionArgs, String sortOrder) {
        SQLiteQueryBuilder qb = new SQLiteQueryBuilder();

        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                qb.setTables(BookProviderMetaData.BookTableMetaData.TABLE_NAME);
                qb.setProjectionMap(sBooksProjectionMap);
                break;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                qb.setTables(BookProviderMetaData.BookTableMetaData.TABLE_NAME);
                qb.setProjectionMap(sBooksProjectionMap);
                qb.appendWhere(BookProviderMetaData.BookTableMetaData._ID + "="
                        + uri.getPathSegments().get(1));
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }

        // If no sort order is specified use the default
        String orderBy;
        if (TextUtils.isEmpty(sortOrder)) {
            orderBy = BookProviderMetaData.BookTableMetaData.DEFAULT_SORT_ORDER;
        } else {
            orderBy = sortOrder;
        }

        // Get the database and run the query
        SQLiteDatabase db = mOpenHelper.getReadableDatabase();
        Cursor c = qb.query(db, projection, selection,
                selectionArgs, null, null, orderBy);

        //example of getting a count
        int i = c.getCount();

        // Tell the cursor what uri to watch,
        // so it knows when its source data changes
        c.setNotificationUri(getContext().getContentResolver(), uri);
        return c;
    }

    @Override
    synchronized public int update(Uri uri, ContentValues values, String selection,
                      String[] selectionArgs) {
        SQLiteDatabase db = mOpenHelper.getWritableDatabase();
        int count;
        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                count = db.update(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                        values, selection, selectionArgs);
                break;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                String rowId = uri.getPathSegments().get(1);
                count = db.update(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                        values, BookProviderMetaData.BookTableMetaData._ID + "=" + rowId
                                + (!TextUtils.isEmpty(selection) ? " AND (" + selection + ')' : ""),
                        selectionArgs);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }

        getContext().getContentResolver().notifyChange(uri, null);
        return count;
    }

    /**
     * This class helps open, create, and upgrade the database file.
     */
    private static class DatabaseHelper extends SQLiteOpenHelper {

        DatabaseHelper(Context context) {
            super(context,
                    BookProviderMetaData.DATABASE_NAME,
                    null,
                    BookProviderMetaData.DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            Log.d(TAG, "inner oncreate called");
            db.execSQL("CREATE TABLE " + BookProviderMetaData.BookTableMetaData.TABLE_NAME + " ("
                    + BookProviderMetaData.BookTableMetaData._ID + " INTEGER PRIMARY KEY,"
                    + BookProviderMetaData.BookTableMetaData.BOOK_NAME + " TEXT,"
                    + BookProviderMetaData.BookTableMetaData.BOOK_ISBN + " TEXT,"
                    + BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR + " TEXT,"
                    + BookProviderMetaData.BookTableMetaData.CREATED_DATE + " INTEGER,"
                    + BookProviderMetaData.BookTableMetaData.MODIFIED_DATE + " INTEGER"
                    + ");");
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            Log.d(TAG, "inner onupgrade called");
            Log.w(TAG, "Upgrading database from version "
                    + oldVersion + " to "
                    + newVersion + ", which will destroy all old data");
            db.execSQL("DROP TABLE IF EXISTS " +
                    BookProviderMetaData.BookTableMetaData.TABLE_NAME);
            onCreate(db);
        }
    }
}
```

### 3. 注册 ContentProvider

需要在 `AndroidManifest.xml` 文件中注册 `ContentProvider`：

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.qty.bookprovider">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.BookProvider">

        <provider
            android:name=".BookProvider"
            android:authorities="com.qty.provider.BookProvider"
            android:enabled="true"
            android:exported="true" />

        </activity>
    </application>

</manifest>
```

### 4. 示例工程

示例工程地址： <https://gitee.com/AndroidSample/AndroidContentProvider>

