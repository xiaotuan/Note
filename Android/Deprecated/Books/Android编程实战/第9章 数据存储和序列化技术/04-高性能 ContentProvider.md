### 9.4 高性能 ContentProvider

如果选择在 SQLite 数据库中存储数据，笔者总是建议你创建 ContentProvider，即使存储的数据仅供内部使用。原因是 Android 提供了一些工具类以及 UI 相关的类，它们工作在 ContentProvider 之上，能够简化开发者的工作。

#### 9.4.2 创建和升级数据库

下面的代码显示了没有查询方法（query()、insert()、update() 和 delete()）的 ContentProvider。该类用来打开 SQLiteDatabase 对象和管理数据库的升级。onCreate() 会在应用程序启动并且第一次访问 ContentProvider 时被调用——更具体地说，是第一次调用 getReadableDatabase() 或者 getWritableDatabase() 方法的时候。

```java
public class TaskProvider extends ContentProvider {
    public static final String AUTHORITY = "com.aptl.code.provider";
    public static final int ALL_TASKS = 10;
    public static final int SINGLE_TASK = 20;
    public static final String TASK_TABLE = "task";
    public static final String[] ALL_COLUMNS =
            new String[]{TaskColumns._ID, TaskColumns.NAME,
                    TaskColumns.CREATED, TaskColumns.PRIORITY,
                    TaskColumns.STATUS, TaskColumns.OWNER};
    public static final String DATABASE_NAME = "TaskProvider";
    public static final int DATABASE_VERSION = 2;
    public static final String TAG = "TaskProvider";
    public static final String CREATE_SQL = "CREATE TABLE "
            + TASK_TABLE + " ("
            + TaskColumns._ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
            + TaskColumns.NAME + " TEXT NOT NULL, "
            + TaskColumns.CREATED + " INTEGER DEFAULT NOW, "
            + TaskColumns.PRIORITY + " INTEGER DEFAULT 0, "
            + TaskColumns.STATUS + " INTEGER DEFAULT 0, "
            + TaskColumns.OWNER + " TEXT, "
            + TaskColumns.DATA + " TEXT);";
    public static final String CREATED_INDEX_SQL = "CREATE INDEX "
            + TaskColumns.CREATED + "_idx ON " + TASK_TABLE + " ("
            + TaskColumns.CREATED + " ASC);";
    public static final String OWNER_INDEX_SQL = "CREATE INDEX "
            + TaskColumns.OWNER + "_idx ON " + TASK_TABLE + " ("
            + TaskColumns.CREATED + " ASC);";
    private static final String FILE_PREFIX = "com.aptl_";
    private static final String FILE_SUFFIX = ".png";
    public static UriMatcher sUriMatcher
            = new UriMatcher(UriMatcher.NO_MATCH);
    public MyDatabaseHelper mOpenHelper;

    static {
        sUriMatcher.addURI(AUTHORITY, "task", ALL_TASKS);
        sUriMatcher.addURI(AUTHORITY, "task/#", SINGLE_TASK);
    }

    public static Bitmap readBitmapFromProvider(int taskId, ContentResolver resolver)
            throws FileNotFoundException {
        Uri uri = Uri.parse("content://" + TaskProvider.AUTHORITY
                + "/" + TaskProvider.TASK_TABLE + "/" + taskId);
        return BitmapFactory.decodeStream(resolver.openInputStream(uri));
    }

    public static String[] fixSelectionArgs(String[] selectionArgs,
                                            String taskId) {
        if (selectionArgs == null) {
            selectionArgs = new String[]{taskId};
        } else {
            String[] newSelectionArg =
                    new String[selectionArgs.length + 1];
            newSelectionArg[0] = taskId;
            System.arraycopy(selectionArgs, 0,
                    newSelectionArg, 1, selectionArgs.length);
        }
        return selectionArgs;
    }

    public static String fixSelectionString(String selection) {
        selection = selection == null ? TaskColumns._ID + " = ?" :
                TaskColumns._ID + " = ? AND (" + selection + ")";
        return selection;
    }

    @Override
    public boolean onCreate() {
        mOpenHelper = new MyDatabaseHelper(getContext());
        return true;
    }

    @Override
    public Cursor query(Uri uri, String[] projection,
                        String selection, String[] selectionArgs,
                        String sortOrder) {
        projection = projection == null ? ALL_COLUMNS : projection;
        sortOrder = sortOrder == null ? TaskColumns.PRIORITY : sortOrder;
        SQLiteDatabase database = mOpenHelper.getReadableDatabase();

        if (database != null) {
            switch (sUriMatcher.match(uri)) {
                case ALL_TASKS:
                    return database.query(TASK_TABLE, projection,
                            selection, selectionArgs,
                            null, null, sortOrder);
                case SINGLE_TASK:
                    String taskId = uri.getLastPathSegment();
                    selection = fixSelectionString(selection);
                    selectionArgs = fixSelectionArgs(selectionArgs, taskId);
                    return database.query(TASK_TABLE, projection,
                            selection, selectionArgs,
                            null, null, sortOrder);
                default:
                    throw new IllegalArgumentException("Invalid Uri: " + uri);
            }
        } else {
            throw new RuntimeException("Unable to open database!");
        }
    }

    @Override
    public String getType(Uri uri) {
        return null;
    }

    private Uri doInsert(Uri uri, ContentValues values,
                         SQLiteDatabase database) {
        Uri result = null;
        switch (sUriMatcher.match(uri)) {
            case ALL_TASKS:
                long id = database.insert(TASK_TABLE, "", values);
                if (id == -1) throw new SQLException("Error inserting data: "
                        + values.toString());
                result = Uri.withAppendedPath(uri, String.valueOf(id));

                // Update row with _data field pointing at a file...
                File dataFile = Environment.getExternalStoragePublicDirectory(
                        Environment.DIRECTORY_PICTURES);
                dataFile = new File(dataFile, FILE_PREFIX + id + FILE_SUFFIX);
                ContentValues valueForFile = new ContentValues();
                valueForFile.put("_data", dataFile.getAbsolutePath());
                update(result, values, null, null);
        }
        return result;
    }

    @Override
    public Uri insert(Uri uri, ContentValues values) {
        SQLiteDatabase database = mOpenHelper.getWritableDatabase();
        Uri result = doInsert(uri, values, database);
        return result;
    }

    @Override
    public int bulkInsert(Uri uri, ContentValues[] contentValueses) {
        SQLiteDatabase database = mOpenHelper.getWritableDatabase();
        int count = 0;
        try {
            database.beginTransaction();
            for (ContentValues values : contentValueses) {
                Uri resultUri = doInsert(uri, values, database);
                if (resultUri != null) {
                    count++;
                } else {
                    count = 0;
                    throw new RuntimeException("Error in bulk insert");
                }
            }
            database.setTransactionSuccessful();
        } finally {
            database.endTransaction();
        }
        return count;
    }

    @Override
    public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
        if(sUriMatcher.match(uri) == SINGLE_TASK)
            return openFileHelper(uri, mode);
        else
            return super.openFile(uri, mode);
    }

    @Override
    public ContentProviderResult[] applyBatch(ArrayList<ContentProviderOperation> operations)
            throws OperationApplicationException {
        SQLiteDatabase database = mOpenHelper.getWritableDatabase();
        ContentProviderResult[] result
                = new ContentProviderResult[operations.size()];
        try {
            database.beginTransaction();
            for (int i = 0; i < operations.size(); i++) {
                ContentProviderOperation operation = operations.get(i);
                result[i] = operation.apply(this, result, i);
            }
            database.setTransactionSuccessful();
        } finally {
            database.endTransaction();
        }
        return result;
    }

    @Override
    public int delete(Uri uri, String s, String[] strings) {
        // TODO
        return 0;
    }

    @Override
    public int update(Uri uri, ContentValues contentValues, String s, String[] strings) {
        // TODO
        return 0;
    }

    public interface TaskColumns extends BaseColumns {
        public static final String NAME = "name";
        public static final String CREATED = "created";
        public static final String PRIORITY = "priority";
        public static final String STATUS = "status";
        public static final String OWNER = "owner";
        public static final String DATA = "_data";
    }

    private class MyDatabaseHelper extends SQLiteOpenHelper {

        public MyDatabaseHelper(Context context) {
            super(context, DATABASE_NAME, null, DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase database) {
            Log.d(TAG, "Create SQL : " + CREATE_SQL);
            database.execSQL(CREATE_SQL);
            database.execSQL(CREATED_INDEX_SQL);
        }

        @Override
        public void onUpgrade(SQLiteDatabase db,
                              int oldVersion, int newVersion) {
            if (oldVersion < 2) {
                db.execSQL("ALTER TABLE " + TASK_TABLE
                        + " ADD COLUMN " + TaskColumns.OWNER + " TEXT");
                db.execSQL("ALTER TABLE " + TASK_TABLE + " ADD COLUMN " + TaskColumns.DATA + "TEXT");
                db.execSQL(OWNER_INDEX_SQL);
            }
        }
    }
}
```

#### 9.4.3 实现查询方法

下面的代码实现了 query() 方法，以及用于修改 selection 和 selectionArgs 参数的两个工具方法。

```java
public static String[] fixSelectionArgs(String[] selectionArgs,
                                            String taskId) {
    if (selectionArgs == null) {
        selectionArgs = new String[]{taskId};
    } else {
        String[] newSelectionArg =
            new String[selectionArgs.length + 1];
        newSelectionArg[0] = taskId;
        System.arraycopy(selectionArgs, 0,
                         newSelectionArg, 1, selectionArgs.length);
    }
    return selectionArgs;
}

public static String fixSelectionString(String selection) {
    selection = selection == null ? TaskColumns._ID + " = ?" :
    TaskColumns._ID + " = ? AND (" + selection + ")";
    return selection;
}

@Override
public Cursor query(Uri uri, String[] projection,
                    String selection, String[] selectionArgs,
                    String sortOrder) {
    projection = projection == null ? ALL_COLUMNS : projection;
    sortOrder = sortOrder == null ? TaskColumns.PRIORITY : sortOrder;
    SQLiteDatabase database = mOpenHelper.getReadableDatabase();

    if (database != null) {
        switch (sUriMatcher.match(uri)) {
            case ALL_TASKS:
                return database.query(TASK_TABLE, projection,
                                      selection, selectionArgs,
                                      null, null, sortOrder);
            case SINGLE_TASK:
                String taskId = uri.getLastPathSegment();
                selection = fixSelectionString(selection);
                selectionArgs = fixSelectionArgs(selectionArgs, taskId);
                return database.query(TASK_TABLE, projection,
                                      selection, selectionArgs,
                                      null, null, sortOrder);
            default:
                throw new IllegalArgumentException("Invalid Uri: " + uri);
        }
    } else {
        throw new RuntimeException("Unable to open database!");
    }
}
```

#### 9.4.4 数据库事务

ContentProvider 类提供了两个用于事务管理的方法：ContentProvider.bulkInsert() 和 ContentProvider.applyBatch()。下面的代码演示了如何实现 bulkInsert() 方法，它在一个事务中插入多条记录，相比每次有新数据都调用 ContentProvider.insert()，这种方法会明显快很多。

```java
private Uri doInsert(Uri uri, ContentValues values,
                         SQLiteDatabase database) {
    Uri result = null;
    switch (sUriMatcher.match(uri)) {
        case ALL_TASKS:
            long id = database.insert(TASK_TABLE, "", values);
            if (id == -1) throw new SQLException("Error inserting data: "
                                                 + values.toString());
            result = Uri.withAppendedPath(uri, String.valueOf(id));

            // Update row with _data field pointing at a file...
            File dataFile = Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_PICTURES);
            dataFile = new File(dataFile, FILE_PREFIX + id + FILE_SUFFIX);
            ContentValues valueForFile = new ContentValues();
            valueForFile.put("_data", dataFile.getAbsolutePath());
            update(result, values, null, null);
    }
    return result;
}

@Override
public Uri insert(Uri uri, ContentValues values) {
    SQLiteDatabase database = mOpenHelper.getWritableDatabase();
    Uri result = doInsert(uri, values, database);
    return result;
}

@Override
public int bulkInsert(Uri uri, ContentValues[] contentValueses) {
    SQLiteDatabase database = mOpenHelper.getWritableDatabase();
    int count = 0;
    try {
        database.beginTransaction();
        for (ContentValues values : contentValueses) {
            Uri resultUri = doInsert(uri, values, database);
            if (resultUri != null) {
                count++;
            } else {
                count = 0;
                throw new RuntimeException("Error in bulk insert");
            }
        }
        database.setTransactionSuccessful();
    } finally {
        database.endTransaction();
    }
    return count;
}
```

事务的语义很简单。首先调用 SQLiteDatabase.beginTransaction() 开始一个新的事务。当成功插入所有记录后调用 SQLiteDatabase.setTransactionSuccessful()，然后使用 SQLiteException.endTransaction() 结束本次事务。如果某条数据插入失败，会抛出 SQLiteException，而之前所有的插入都会回滚，因为在成功之前没有调用过 SQLiteDatabase.setTransactionSuccessful()。

强烈建议在继承 ContentProvider 时实现该方法，因为它会显著提高数据插入的性能。但是，由于此方法只适用于插入操作，开发者可能需要实现另一个方法来处理更复杂的操作。

如果要在一次事务中执行多次 update() 或者 delete() 语句，必须实现 ContentProvider.applyBatch() 方法。

```java
@Override
public ContentProviderResult[] applyBatch(ArrayList<ContentProviderOperation> operations)
    throws OperationApplicationException {
    SQLiteDatabase database = mOpenHelper.getWritableDatabase();
    ContentProviderResult[] result
        = new ContentProviderResult[operations.size()];
    try {
        database.beginTransaction();
        for (int i = 0; i < operations.size(); i++) {
            ContentProviderOperation operation = operations.get(i);
            result[i] = operation.apply(this, result, i);
        }
        database.setTransactionSuccessful();
    } finally {
        database.endTransaction();
    }
    return result;
}
```

#### 9.4.5 在 ContentProvider 中存储二进制数据

比如，要在数据库中为每个任务存储一张 JPG 图片，首先需要在表中新加一列，名为 _data，类型为 TEXT，如下所示：

```java
db.execSQL("ALTER TABLE " + TASK_TABLE + " ADD COLUMN _data TEXT");
```

ContentProvider.openFileHelper() 方法会在内部使用它。只需在每次插入时存储文件的路径。要做到这一点，修改前面所示的 doInsert() 方法。

```java
private Uri doInsert(Uri uri, ContentValues values,
                         SQLiteDatabase database) {
    Uri result = null;
    switch (sUriMatcher.match(uri)) {
        case ALL_TASKS:
            long id = database.insert(TASK_TABLE, "", values);
            if (id == -1) throw new SQLException("Error inserting data: "
                                                 + values.toString());
            result = Uri.withAppendedPath(uri, String.valueOf(id));

            // Update row with _data field pointing at a file...
            File dataFile = Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_PICTURES);
            dataFile = new File(dataFile, FILE_PREFIX + id + FILE_SUFFIX);
            ContentValues valueForFile = new ContentValues();
            valueForFile.put("_data", dataFile.getAbsolutePath());
            update(result, values, null, null);
    }
    return result;
}
```

本例要把 JPG 文件写到外部存储的 PICTURES 目录内。接下来，覆盖 ContentProvider.openFile() 方法返回 ParcelFileDescriptor 对象。然后就可以使用该对象直接读写文件了。

```java
@Override
public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
    if(sUriMatcher.match(uri) == SINGLE_TASK)
        return openFileHelper(uri, mode);
    else
        return super.openFile(uri, mode);
}
```

实际使用 openFileHelper() 来打开文件，并把结果传给调用客户端。当从 ContentProvider 中读取某条记录的 Bitmap 对象时，可以简单地使用该记录的 Uri，接下来的事情交给框架去处理，如下所示：

```java
public Bitmap readBitmapFromProvider(int taskId, ContentResolver resolver) throws FileNotFoundException {
    Uri uri = Uri.parse("content://" + TaskProvider.AUTHORITY + "/" + TaskProvider.TASK_TABLE + "/" + taskId);
    return BitmapFactory.decodeStream(resolver.openInputStream(uri));
}
```

