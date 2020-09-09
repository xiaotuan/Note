在实现它们之前需要进行大量设置。我们将介绍 ContentProvider 实现的所有细节，介绍需要采取的各种步骤。

（1）计划数据库、URI、列名称等，创建元数据类来定义所有这些元数据元素的常量。

（2）扩展抽象类 ContentProvider。

（3）实现方法：query、insert、update、delete 和 getType。

（4）在描述文件中注册提供程序。

**1. 计划数据库**

**代码清单4-5** 定义数据库的元数据：BookProviderMetaData 类

```java
public class BookProviderMetaData {

    public static final String AUTHORITY = "com.androidbook.provider.BookProvider";

    public static final String DATABASE_NAME = "book.db";
    public static final int DATABASE_VERSION = 1;
    public static final String BOOKS_TABLE_NAME = "books";

    private BookProviderMetaData() {}

    // inner class describing columns and their types
    public static final class BookTableMetaData implements BaseColumns {

        public static final String TABLE_NAME = "books";

        // uri and mime type definitions
        public static final Uri CONTENT_URI = Uri.parse("content://" + AUTHORITY + "/books");
        public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.androidbook.book";
        public static final String CONTENT_TIEM_TYPE = "vnd.android.cursor.item/vnd.androidbook.book";

        public static final String DEFAULT_SORT_ORDER = "modified DESC";

        // Additional Columns start here.
        // String type
        public static final String BOOK_NAME = "name";
        // string type
        public static final String BOOK_ISBN = "isbn";
        // string type
        public static final String BOOK_AUTHOR = "author";
        // Integer from System.currentTimeMillis()
        public static final String CREATED_DATE = "created";
        // Integer from System.currentTimeMillis()
        public static final String MODIFIED_DATE = "modified";

        private BookTableMetaData() {}

    }
}
```

元数据类 BookTableMetaData 也继承自 BaseColumns 类，后者提供了标准的 `_id` 字段，该字段表示行 ID。

**2. 扩展 ContentProvider**

**代码清单4-6** 实现 BookProvider 内容提供程序

```java
public class BookProvider extends ContentProvider {

    // Logging helper tag. No significance to providers.
    private static final String TAG = "BookProvider";

    // Projection maps are similar to "as" construct
    // in an sql statement where by you can rename the
    // columns.
    private static HashMap<String, String> sBooksProjectionMap;

    static {
        sBooksProjectionMap = new HashMap<>();
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData._ID, BookProviderMetaData.BookTableMetaData._ID);

        // name, isbn, author
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.BOOK_NAME, BookProviderMetaData.BookTableMetaData.BOOK_NAME);
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, BookProviderMetaData.BookTableMetaData.BOOK_ISBN);
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR);

        // created date, modified date
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.CREATED_DATE, BookProviderMetaData.BookTableMetaData.CREATED_DATE);
        sBooksProjectionMap.put(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE, BookProviderMetaData.BookTableMetaData.MODIFIED_DATE);
    }

    // Provide a mechanism to identify
    // all the incoming uri patterns.
    private static final UriMatcher sUriMatcher;
    private static final int INCOMING_BOOK_COLLECTION_URI_INDICATOR = 1;
    private static final int INCOMING_SINGLE_BOOK_URI_INDICATOR = 2;

    static {
        sUriMatcher = new UriMatcher(UriMatcher.NO_MATCH);
        sUriMatcher.addURI(BookProviderMetaData.AUTHORITY, "books", INCOMING_BOOK_COLLECTION_URI_INDICATOR);
        sUriMatcher.addURI(BookProviderMetaData.AUTHORITY, "books/#", INCOMING_SINGLE_BOOK_URI_INDICATOR);
    }

    /**
     * This class helps open, create, and upgrade the database file.
     */
    private static class DatabaseHelper extends SQLiteOpenHelper {

        DatabaseHelper(Context context) {
            super(context, BookProviderMetaData.DATABASE_NAME, null, BookProviderMetaData.DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase sqLiteDatabase) {
            Log.d(TAG, "inner oncreate called");
            sqLiteDatabase.execSQL("CREATE TABLE " + BookProviderMetaData.BookTableMetaData.TABLE_NAME + " ("
                                    + BookProviderMetaData.BookTableMetaData._ID + " INTEGER PRIMARY KEY,"
                                    + BookProviderMetaData.BookTableMetaData.BOOK_NAME + " TEXT,"
                                    + BookProviderMetaData.BookTableMetaData.BOOK_ISBN + " TEXT,"
                                    + BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR + " TEXT,"
                                    + BookProviderMetaData.BookTableMetaData.CREATED_DATE + " INTEGER,"
                                    + BookProviderMetaData.BookTableMetaData.MODIFIED_DATE + " INTEGER"
                                    + ");");
        }

        @Override
        public void onUpgrade(SQLiteDatabase sqLiteDatabase, int oldVersion, int newVersion) {
            Log.d(TAG, "inner onupgrade called");
            Log.w(TAG, "Upgrading database from version "
                    + oldVersion + " to "
                    + newVersion + ", which will destroy all old data");
            sqLiteDatabase.execSQL("DROP TABLE IF EXISTS " + BookProviderMetaData.BookTableMetaData.TABLE_NAME);
            onCreate(sqLiteDatabase);
        }

    }

    private DatabaseHelper mOpenHelper;

    @Override
    public boolean onCreate() {
        Log.d(TAG, "main onCreate called");
        mOpenHelper = new DatabaseHelper(getContext());
        return true;
    }

    @Nullable
    @Override
    public Cursor query(@NonNull Uri uri, @Nullable String[] projection, @Nullable String selection,
                        @Nullable String[] selectionArgs, @Nullable String sortOrder) {
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
        Cursor c = qb.query(db, projection, selection, selectionArgs, null, null, orderBy);

        // example of getting a count
        int i = c.getCount();

        // Tell the cursor what uri to watch,
        // so it knows when its source data changes
        c.setNotificationUri(getContext().getContentResolver(), uri);
        return c;
    }

    @Nullable
    @Override
    public String getType(@NonNull Uri uri) {
        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                return BookProviderMetaData.BookTableMetaData.CONTENT_TYPE;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                return BookProviderMetaData.BookTableMetaData.CONTENT_TIEM_TYPE;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }
    }

    @Nullable
    @Override
    public Uri insert(@NonNull Uri uri, @Nullable ContentValues contentValues) {
        // Validate the requested uri
        if (sUriMatcher.match(uri) != INCOMING_BOOK_COLLECTION_URI_INDICATOR) {
            throw new IllegalArgumentException("Unknown URI " + uri);
        }

        ContentValues values;
        if (contentValues != null) {
            values = new ContentValues(contentValues);
        } else {
            values = new ContentValues();
        }

        Long now = Long.valueOf(System.currentTimeMillis());

        // Make sure that the fields are all set
        if (values.containsKey(BookProviderMetaData.BookTableMetaData.CREATED_DATE) == false) {
            values.put(BookProviderMetaData.BookTableMetaData.CREATED_DATE, now);
        }

        if (values.containsKey(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE) == false) {
            values.put(BookProviderMetaData.BookTableMetaData.MODIFIED_DATE, now);
        }

        if (values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_NAME) == false) {
            throw new SQLException("Failed to insert row because Book Name is needed " + uri);
        }

        if (values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_ISBN) == false) {
            values.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "Unknown ISBN");
        }

        if (values.containsKey(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR) == false) {
            values.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "Unknown Author");
        }

        SQLiteDatabase db = mOpenHelper.getWritableDatabase();
        long rowId = db.insert(BookProviderMetaData.BookTableMetaData.TABLE_NAME, BookProviderMetaData.BookTableMetaData.BOOK_NAME, values);
        if (rowId > 0) {
            Uri insertedBookUri = ContentUris.withAppendedId(BookProviderMetaData.BookTableMetaData.CONTENT_URI, rowId);
            getContext().getContentResolver().notifyChange(insertedBookUri, null);
            return insertedBookUri;
        }
        throw new SQLException("Failed to inset row into " + uri);
    }

    @Override
    public int delete(@NonNull Uri uri, @Nullable String where, @Nullable String[] whereArgs) {
        SQLiteDatabase db = mOpenHelper.getWritableDatabase();
        int count;
        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                count = db.delete(BookProviderMetaData.BookTableMetaData.TABLE_NAME, where, whereArgs);
                break;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                String rowId = uri.getPathSegments().get(1);
                count = db.delete(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                        BookProviderMetaData.BookTableMetaData._ID + "=" + rowId
                                    + (!TextUtils.isEmpty(where) ? " AND (" + where + ')' : ""),
                                    whereArgs);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }

        getContext().getContentResolver().notifyChange(uri, null);
        return count;
    }

    @Override
    public int update(@NonNull Uri uri, @Nullable ContentValues contentValues, @Nullable String where, @Nullable String[] whereArgs) {
        SQLiteDatabase db = mOpenHelper.getWritableDatabase();
        int count;
        switch (sUriMatcher.match(uri)) {
            case INCOMING_BOOK_COLLECTION_URI_INDICATOR:
                count = db.update(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                                    contentValues, where, whereArgs);
                break;

            case INCOMING_SINGLE_BOOK_URI_INDICATOR:
                String rowId = uri.getPathSegments().get(1);
                count = db.update(BookProviderMetaData.BookTableMetaData.TABLE_NAME,
                                    contentValues, BookProviderMetaData.BookTableMetaData._ID + "=" + rowId
                                    + (!TextUtils.isEmpty(where) ? " AND (" + where + ')' : ""),
                                    whereArgs);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }

        getContext().getContentResolver().notifyChange(uri, null);
        return count;
    }

}
```

**3. 注册提供程序**

**代码清单4-8** 注册 ContentProvider

```xml
<provider
          android:authorities="com.androidbook.provider.BookProvider"
          android:name=".BookProvider" />
```

