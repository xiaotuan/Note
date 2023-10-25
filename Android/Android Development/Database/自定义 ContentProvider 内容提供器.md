[toc]

自定义内容提供器步骤如下：

+ 定义数据模型（通常是 `SQLite` 数据库，其扩展自 `ContentProvider` 类）。
+ 定义其统一资源标识符（ `URI` ）。
+ 在 `AndroidManifest.xml` 中声明内容提供器。
+ 实现 `ContentProvider` 的抽象方法（ `query()`、`insert()`、`update()` 、`delete()`、`getType()` 和 `onCreate()` ）。

### 1. 定义数据库表信息

创建一个类用于保存数据库中一张表的列名、MIME 类型和内容提供器 `URI`。

1. 创建表的列名

   **Kotlin**

   ```kotlin
   object CitizenTable {
       public const val TABLE_NAME = "citizen_table"
   
       /**
        * Define the table
        */
       // ID column must look like this
       public const val ID = "_id"
       public const val NAME = "name"
       public const val STATE = "state"
       public const val INCOME = "income"
   }
   ```

   **Java**

   ```java
   public class CitizenTable {
       public static final String TABLE_NAME = "citizen_table";
   
       /**
        * Define the table
        */
       // ID column must look like this
       public static final String ID = "_id";
       public static final String NAME = "name";
       public static final String STATE = "state";
       public static final String INCOME = "income";
   }
   ```

2. 定义该表的授权 `URI`

   **Kotlin**

   ```kotlin
   public val CONTENT_URI = Uri.parse("content://${CitizenContentProvider.AUTHORITY}/citizen")
   ```

   **Java**

   ```java
   public static final String CONTENT_URI = Uri.parse("content://" + CitizenContentProvider.AUTHORITY + "/citizen");
   ```

   其中， `CitizenContentProvider.AUTHORIT` 变量定义在内容提供器中，其值为内容提供器的授权，同时也是在 `AndroidManifest.xml` 注册内容提供器时授权属性的值。

   表的授权 `URI` 格式为：

   ```
   "content://" + 内容提供器的授权字符串 + "/" + 表授权标识符
   ```

3. 定义表查询的 MIME 类型

   为数据指定 `MIME` 类型的规则如下：

   + `vnd.android.cursor.item/for a single record`： 查询单条记录的 `MIME` 类型
   + `vnd.android.cursor.dir/for multiple records`：查询多条记录的 `MIME` 类型

   例如:

   **Kotlin**

   ```kotlin
   // MIME type for group of citizens
   public val CONTENT_TYPE = "vnd.android.cursor.dir/vnd.qty.citizen"
   
   // MIME type for single citizen
   public val CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.qty.citizen"
   ```

   **Java**

   ```java
   // MIME type for group of citizens
   public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.qty.citizen";
   
   // MIME type for single citizen
   public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.qty.citizen";
   ```

4. 定义指定 ID 查询时，ID 值在 URI 中的位置

   **Kotlin**

   ```kotlin
   // Relative position of citizen ssid in uri
   public const val SSID_PATH_POSITION = 1
   ```

   **Java**

   ```java
   // Relative position of citizen ssid in uri
   public const val SSID_PATH_POSITION = 1
   ```

   `ID` 的位置通常是 1。具体位置可以通过如下方式获知：

   单条记录查询 `URI` 格式如下：

   ```
   content://内容提供器授权字符串/表标识字符串/ID值
   ```

   应用使用 `uri.pathSegments.get()` 方法获取指定的 ID 值，而 `uri.pathSegments` 返回的内容是除 `content://内容提供器授权字符串/` 部分的内容外的字符串通过 `/` 分割而成的数组，因此，上面的 `uri.pathSegments` 值为：

   ```
   [表标识字符串, ID值]
   ```

   从上面的可以看出 `ID值` 在数组中的 `1` 位置，因此 `SSID_PATH_POSITION` 的值为 1。

### 2. 创建内容提供器类

1. 定义内容提供器类

   内容提供器类需要继承自 `ContentProvider` 类，我们通常将自定义数据库类作为内容提供器类的内部类（这不是必需的）。

   **Kotlin**

   ```kotlin
   
   ```

   **Java**

   ```java
   
   ```

2. 定义内容提供器授权字符串

   内容提供器授权字符串的格式通常为：

   ```
   公司域名反写/内容提供器类名
   ```

   **Kotlin**

   ```kotlin
   public val AUTHORITY = "com.android.contentprovidertest.CitizenContentProvider"
   ```

   **Java**

   ```java
   public static final String AUTHORITY = "com.android.contentprovidertest.CitizenContentProvider";
   ```

3. 创建 `URI` 匹配器

   **Kotlin**

   ```kotlin
   // Uri match of a general citizens query
   private const val CITIZENS = 1;
   // Uri match of a specific citizen query
   private const val SSID = 2;
   
   private val sUriMatcher = UriMatcher(UriMatcher.NO_MATCH).apply {
           addURI(AUTHORITY, "citizen", CITIZENS)
           addURI(AUTHORITY, "citizen/#", SSID)
       }
   ```

   **Java**

   ```java
   ```

4. 创建表列名的哈希表

   `projectionMap` 的作用是允许你对列设置别名。在大多数内容提供器中，这种映射似乎没有什么意义，因为你只是告诉内容提供器将表的列映射到它们自己上。然而，在某些情况下，对于更复杂的模式（即具有联合表的模式），能够重命名的别名表的列可以使访问内容提供上的数据更加直观。

   **Kotlin**

   ```kotlin
   // Projection map used for row alls
   private val projectionMap = HashMap<String, String>().apply {
       put(CitizenTable.ID, CitizenTable.ID)
       put(CitizenTable.NAME, CitizenTable.NAME)
       put(CitizenTable.STATE, CitizenTable.STATE)
       put(CitizenTable.INCOME, CitizenTable.INCOME)
   }
   ```

   **Java**

   ```java
   ```

5. 实现内容提供器的 `query()` 方法

   由于内容提供器暴露给设备上的所有应用程序，因此可能会有多个应用程序同时访问我们的数据库，在这种情况下，我们的数据可能会发生更改。因此，在查询完成后，我们告诉返回的 `Cursor` 侦听对其底层数据所做的任何更改，这样当进行更改时，`Cursor` 将知道更新自己以及随后可能使用 `Cursor` 的任何 `UI` 组件。应用程序通过如下代码实时更新 `Cursor` 数据，以保持数据最新：

   ```kotlin
   
   ```

   **Kotlin**

   ```kotlin
   override fun query(
       uri: Uri,
       projection: Array<out String>?,
       selection: String?,
       selectionArgs: Array<out String>?,
       sortOrder: String?
   ): Cursor? {
       val qb = SQLiteQueryBuilder().apply { tables = CitizenTable.TABLE_NAME }
       when (sUriMatcher.match(uri)) {
           CITIZENS -> qb.projectionMap = projectionMap
           SSID -> {
               val ssid = uri.pathSegments.get(CitizenTable.SSID_PATH_POSITION)
               qb.projectionMap = projectionMap
               // For querying by specific ssid
               qb.appendWhere("${CitizenTable.ID}=$ssid")
           }
           else -> throw IllegalArgumentException("Unknown URI $uri")
       }
       val c = qb.query(dbHelper.readableDatabase, projection, selection, selectionArgs, null, null, sortOrder)
       // Registers notification listener with given cursor
       // Cursor knows when underlying data has changed
       context?.let {
           c.setNotificationUri(it.contentResolver, uri)
       }
       return c
   }
   ```

   **Java**

   ```java
   ```

6. 实现内容提供器的 `delete()` 和 `update()` 方法

   在执行 `delete()` 和 `update()` 方法成功后，需要再方法的最后调用如下代码：

   **Kotlin**

   ```kotlin
   context?.contentResolver?.notifyChange(uri, null)
   ```

   **Java**

   ```java
   getContext().getContentResolver().notifyChange(uri, null);
   ```

   通知绑定绑定该 `Uri` 的 `Cursor` 的 `UI` 控件，数据发生了变化，需要重新加载数据。

   **Kotlin**

   ```kotlin
   override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int {
       var count = 0
       when (sUriMatcher.match(uri)) {
           CITIZENS -> {
               // Perform regular delete
               count = dbHelper.writableDatabase.delete(CitizenTable.TABLE_NAME, selection, selectionArgs)
           }
           SSID -> {
               // From incoming uri get ssid
               val ssid = uri.pathSegments.get(CitizenTable.SSID_PATH_POSITION)
               // User wants to delete a specific citizen
               var finalWhere = "${CitizenTable.ID}=$ssid"
               // If user specifies where filter then append
               selection?.let {
                   finalWhere = "$finalWhere AND $it"
               }
               count = dbHelper.writableDatabase.delete(CitizenTable.TABLE_NAME, finalWhere, selectionArgs)
           }
           else -> throw IllegalArgumentException("Unknown URI $uri")
       }
       context?.contentResolver?.notifyChange(uri, null)
       return count
   }
   
   override fun update(
       uri: Uri,
       values: ContentValues?,
       selection: String?,
       selectionArgs: Array<out String>?
   ): Int {
       var count = 0
       when (sUriMatcher.match(uri)) {
           CITIZENS -> {
               // General update on all citizens
               count = dbHelper.writableDatabase.update(CitizenTable.TABLE_NAME, values, selection, selectionArgs)
           }
           SSID -> {
               // From incoming uri get ssid
               val ssid = uri.pathSegments.get(CitizenTable.SSID_PATH_POSITION)
               // The user wants to update a specific citizen
               var finalWhere = "${CitizenTable.ID}=$ssid"
               selection?.let {
                   finalWhere += " AND $it"
               }
               // Perform the update on the specific citizen
               count = dbHelper.writableDatabase.update(CitizenTable.TABLE_NAME, values, finalWhere, selectionArgs)
           }
           else -> throw IllegalArgumentException("Unknown URI $uri")
       }
       context?.contentResolver?.notifyChange(uri, null)
       return count
   }
   ```

   **Java**

   ```java
   ```

7. 实现内容提供器 `insert()` 和 `getType()` 方法

   首先，让我们处理 `getType()` 方法。此方法只是返回为给定 `URI` 请求的数据对象的多用途 `Internet` 邮件扩展（ MIME ）类型，这实际上意味着您为数据的每一行（或多行）提供了一个可区分的数据类型。这样，如果需要，开发人员就可以识别指向表的 `Cursor` 是否确实在检索有效的公民对象。为数据指定MIME类型的规则如下：

   + vnd.android.cursor.item/ for a single record
   + vnd.android.cursor.dir/ for multiple records  

   **Kotlin**

   ```kotlin
   override fun getType(uri: Uri): String? {
       return when (sUriMatcher.match(uri)) {
           CITIZENS -> CitizenTable.CONTENT_TYPE
           SSID -> CitizenTable.CONTENT_ITEM_TYPE
           else -> throw IllegalArgumentException("Unknown URI $uri")
       }
   }
   
   override fun insert(uri: Uri, values: ContentValues?): Uri? {
       // Only general citizens uri is allowed for inserts
       // Doesn't make sense to specify a single citizen
       if (sUriMatcher.match(uri) != CITIZENS) {
           throw IllegalArgumentException("Unknown URI $uri")
       }
       val finalValues = values?.let { ContentValues(values) } ?: ContentValues()
       val rowId = dbHelper.writableDatabase.insert(CitizenTable.TABLE_NAME, CitizenTable.NAME, values)
       if (rowId > 0) {
           val citizenUri = ContentUris.withAppendedId(CitizenTable.CONTENT_URI, rowId)
           // Notify context of the change
           context?.contentResolver?.notifyChange(citizenUri, null)
           return citizenUri
       } else {
           throw SQLiteException("Failed to insert row into $uri")
       }
   }
   ```
   
   **Java**
   
   ```java

### 3. 在 AndroidManifest.xml 中注册内容提供器

```xml
<provider
            android:authorities="com.android.contentprovidertest.CitizenContentProvider"
            android:name=".CitizenContentProvider" />
```

### 4. 使用内容提供器

**kotlin**

```kotlin
val contentValues = ContentValues().apply {
    put(CitizenTable.NAME, "Jason Wei")
    put(CitizenTable.STATE, "CA")
    put(CitizenTable.INCOME, 100000)
}
contentResolver.insert(CitizenTable.CONTENT_URI, contentValues)
val c = cr.query(CitizenTable.CONTENT_URI, null, null,
null, "${CitizenTable.INCOME} ASC")
```

**Java**

```java
```

### 5. 完整示例代码

#### 5.1 CitizenTable 类

##### 5.1.1 Kotlin 版本

```kotlin
package com.android.contentprovidertest

import android.net.Uri

object CitizenTable {
    public const val TABLE_NAME = "citizen_table"

    /**
     * Define the table
     */
    // ID column must look like this
    public const val ID = "_id"
    public const val NAME = "name"
    public const val STATE = "state"
    public const val INCOME = "income"

    /**
     * Define the content type and uri
     */
    // The content uri to our provider
    public val CONTENT_URI = Uri.parse("content://${CitizenContentProvider.AUTHORITY}/citizen")

    // MIME type for group of citizens
    public val CONTENT_TYPE = "vnd.android.cursor.dir/vnd.qty.citizen"

    // MIME type for single citizen
    public val CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.qty.citizen"

    // Relative position of citizen ssid in uri
    public const val SSID_PATH_POSITION = 1
}
```

##### 5.1.2 Java 版本

```java
package com.android.contentprovidertest;

import android.net.Uri;

public class CitizenTable {

    public static final String TABLE_NAME = "citizen_table";

    /**
     * Define the table
     */
    // ID column must look like this
    public static final String ID = "_id";
    public static final String NAME = "name";
    public static final String STATE = "state";
    public static final String INCOME = "income";

    /**
     * Define the content type and uri
     */
    // The content uri to our provider
    public static final Uri CONTENT_URI = Uri.parse("content://" + CitizenContentProvider.AUTHORITY + "/citizen");

    // MIME type for group of citizens
    public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.qty.citizen";

    // MIME type for single citizen
    public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.qty.citizen";

    // Relative position of citizen ssid in uri
    public static final int SSID_PATH_POSITION = 1;
}
```

#### 5.2 CitizenContentProvider 类

##### 5.2.1 Kotlin 版本

```kotlin
package com.android.contentprovidertest

import android.content.ContentProvider
import android.content.ContentUris
import android.content.ContentValues
import android.content.Context
import android.content.UriMatcher
import android.database.Cursor
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteException
import android.database.sqlite.SQLiteOpenHelper
import android.database.sqlite.SQLiteQueryBuilder
import android.net.Uri
import android.util.Log
import java.lang.IllegalArgumentException

private const val TAG = "CitizenContentProvider"
// Uri match of a general citizens query
private const val CITIZENS = 1;
// Uri match of a specific citizen query
private const val SSID = 2;

class CitizenContentProvider: ContentProvider() {

    private val sUriMatcher = UriMatcher(UriMatcher.NO_MATCH).apply {
        addURI(AUTHORITY, "citizen", CITIZENS)
        addURI(AUTHORITY, "citizen/#", SSID)
    }
    // Projection map used for row alls
    private val projectionMap = HashMap<String, String>().apply {
        put(CitizenTable.ID, CitizenTable.ID)
        put(CitizenTable.NAME, CitizenTable.NAME)
        put(CitizenTable.STATE, CitizenTable.STATE)
        put(CitizenTable.INCOME, CitizenTable.INCOME)
    }

    private lateinit var dbHelper: DataBaseHelper

    // Note the different methods that need to be implemented
    override fun onCreate(): Boolean {
        // Helper database is initialized
        dbHelper = DataBaseHelper(context!!)
        return true
    }

    override fun query(
        uri: Uri,
        projection: Array<out String>?,
        selection: String?,
        selectionArgs: Array<out String>?,
        sortOrder: String?
    ): Cursor? {
        val qb = SQLiteQueryBuilder().apply { tables = CitizenTable.TABLE_NAME }
        when (sUriMatcher.match(uri)) {
            CITIZENS -> qb.projectionMap = projectionMap
            SSID -> {
                val ssid = uri.pathSegments.get(CitizenTable.SSID_PATH_POSITION)
                qb.projectionMap = projectionMap
                // For querying by specific ssid
                qb.appendWhere("${CitizenTable.ID}=$ssid")
            }
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }
        val c = qb.query(dbHelper.readableDatabase, projection, selection, selectionArgs, null, null, sortOrder)
        // Registers notification listener with given cursor
        // Cursor knows when underlying data has changed
        context?.let {
            c.setNotificationUri(it.contentResolver, uri)
        }
        return c
    }

    override fun getType(uri: Uri): String? {
        return when (sUriMatcher.match(uri)) {
            CITIZENS -> CitizenTable.CONTENT_TYPE
            SSID -> CitizenTable.CONTENT_ITEM_TYPE
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }
    }

    override fun insert(uri: Uri, values: ContentValues?): Uri? {
        // Only general citizens uri is allowed for inserts
        // Doesn't make sense to specify a single citizen
        if (sUriMatcher.match(uri) != CITIZENS) {
            throw IllegalArgumentException("Unknown URI $uri")
        }
        val finalValues = values?.let { ContentValues(values) } ?: ContentValues()
        val rowId = dbHelper.writableDatabase.insert(CitizenTable.TABLE_NAME, CitizenTable.NAME, values)
        if (rowId > 0) {
            val citizenUri = ContentUris.withAppendedId(CitizenTable.CONTENT_URI, rowId)
            // Notify context of the change
            context?.contentResolver?.notifyChange(citizenUri, null)
            return citizenUri
        } else {
            throw SQLiteException("Failed to insert row into $uri")
        }
    }

    override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int {
        var count = 0
        when (sUriMatcher.match(uri)) {
            CITIZENS -> {
                // Perform regular delete
                count = dbHelper.writableDatabase.delete(CitizenTable.TABLE_NAME, selection, selectionArgs)
            }
            SSID -> {
                // From incoming uri get ssid
                val ssid = uri.pathSegments.get(CitizenTable.SSID_PATH_POSITION)
                // User wants to delete a specific citizen
                var finalWhere = "${CitizenTable.ID}=$ssid"
                // If user specifies where filter then append
                selection?.let {
                    finalWhere = "$finalWhere AND $it"
                }
                count = dbHelper.writableDatabase.delete(CitizenTable.TABLE_NAME, finalWhere, selectionArgs)
            }
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }
        context?.contentResolver?.notifyChange(uri, null)
        return count
    }

    override fun update(
        uri: Uri,
        values: ContentValues?,
        selection: String?,
        selectionArgs: Array<out String>?
    ): Int {
        var count = 0
        when (sUriMatcher.match(uri)) {
            CITIZENS -> {
                // General update on all citizens
                count = dbHelper.writableDatabase.update(CitizenTable.TABLE_NAME, values, selection, selectionArgs)
            }
            SSID -> {
                // From incoming uri get ssid
                val ssid = uri.pathSegments.get(CitizenTable.SSID_PATH_POSITION)
                // The user wants to update a specific citizen
                var finalWhere = "${CitizenTable.ID}=$ssid"
                selection?.let {
                    finalWhere += " AND $it"
                }
                // Perform the update on the specific citizen
                count = dbHelper.writableDatabase.update(CitizenTable.TABLE_NAME, values, finalWhere, selectionArgs)
            }
            else -> throw IllegalArgumentException("Unknown URI $uri")
        }
        context?.contentResolver?.notifyChange(uri, null)
        return count
    }

    // Override and implement our database schema
    companion object {
        private const val DATABASE_NAME = "citizens.db"
        private const val DATABASE_VERSION = 1

        public const val AUTHORITY = "com.android.contentprovidertest.CitizenContentProvider"

        private class DataBaseHelper(context: Context): SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {

            override fun onCreate(db: SQLiteDatabase?) {
                // Create income table
                db?.execSQL("CREATE TABLE ${CitizenTable.TABLE_NAME} ( ${CitizenTable.ID} INTEGER " +
                        "PRIMARY KEY AUTOINCREMENT, ${CitizenTable.NAME} TEXT, ${CitizenTable.STATE} TEXT, ${CitizenTable.INCOME} INTEGER);")
            }

            override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
                Log.w(TAG, "Upgrading database from version $oldVersion to $newVersion," +
                        " which will destroy all old data")
                // Kill previous tables if upgraded
                db?.execSQL("DROP TABLE IF EXISTS ${CitizenTable.TABLE_NAME}")
                // Create new instance of schema
                onCreate(db)
            }

        }
    }
}
```

##### 5.2.2 Java 版本

```java
package com.android.contentprovidertest;

import android.content.ContentProvider;
import android.content.ContentUris;
import android.content.ContentValues;
import android.content.Context;
import android.content.UriMatcher;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteException;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.sqlite.SQLiteQueryBuilder;
import android.net.Uri;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.HashMap;

public class CitizenContentProvider extends ContentProvider {

    private static final String TAG = "CitizenContentProvider";

    // Uri Match of a general citizens query
    private static final int CITIZENS = 1;
    // Uri match of a specific citizen query
    private static final int SSID = 2;
    public static final String AUTHORITY = "com.android.contentprovidertest.CitizenContentProvider";
    private static final UriMatcher sUriMatch;
    private static final HashMap<String, String> projectionMap;

    private DatabaseHelper dbHelper;

    // Instantiate and set static variables
    static {
        sUriMatch = new UriMatcher(UriMatcher.NO_MATCH);
        sUriMatch.addURI(AUTHORITY, "citizen", CITIZENS);
        sUriMatch.addURI(AUTHORITY, "citizen/#", SSID);
        // Projection map used for row allas
        projectionMap = new HashMap<>();
        projectionMap.put(CitizenTable.ID, CitizenTable.ID);
        projectionMap.put(CitizenTable.NAME, CitizenTable.NAME);
        projectionMap.put(CitizenTable.STATE, CitizenTable.STATE);
        projectionMap.put(CitizenTable.INCOME, CitizenTable.INCOME);
    }

    @Override
    public boolean onCreate() {
        dbHelper = new DatabaseHelper(getContext());
        return true;
    }

    @Nullable
    @Override
    public Cursor query(@NonNull Uri uri, @Nullable String[] projection, @Nullable String selection,
                        @Nullable String[] selectionArgs, @Nullable String sortOrder) {
        SQLiteDatabase db = dbHelper.getReadableDatabase();
        SQLiteQueryBuilder qb = new SQLiteQueryBuilder();
        qb.setTables(CitizenTable.TABLE_NAME);
        switch (sUriMatch.match(uri)) {
            case CITIZENS:
                qb.setProjectionMap(projectionMap);
                break;

            case SSID:
                String ssid = uri.getPathSegments().get(CitizenTable.SSID_PATH_POSITION);
                qb.setProjectionMap(projectionMap);
                // For querying by specific ssid
                qb.appendWhere(CitizenTable.ID + "=" + ssid);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }
        Cursor c = qb.query(db, projection, selection, selectionArgs, null, null, sortOrder);
        c.setNotificationUri(getContext().getContentResolver(), uri);
        return c;
    }

    @Nullable
    @Override
    public String getType(@NonNull Uri uri) {
        switch (sUriMatch.match(uri)) {
            case CITIZENS:
                return CitizenTable.CONTENT_TYPE;

            case SSID:
                return CitizenTable.CONTENT_ITEM_TYPE;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }
    }

    @Nullable
    @Override
    public Uri insert(@NonNull Uri uri, @Nullable ContentValues values) {
        // Only general citizens uri is allowed for inserts
        // Doesn't make sense to specify a single citizen
        if (sUriMatch.match(uri) != CITIZENS) {
            throw new IllegalArgumentException("Unknown URI " + uri);
        }
        if (values == null) {
            values = new ContentValues();
        }
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        long rowId = db.insert(CitizenTable.TABLE_NAME, CitizenTable.NAME, values);
        if (rowId > 0) {
            Uri citizenUri = ContentUris.withAppendedId(CitizenTable.CONTENT_URI, rowId);
            // NOtify context of the change
            getContext().getContentResolver().notifyChange(citizenUri, null);
            return citizenUri;
        } else {
            throw new SQLiteException("Failed to insert row into " + uri);
        }
    }

    @Override
    public int delete(@NonNull Uri uri, @Nullable String selection, @Nullable String[] selectionArgs) {
        int count = 0;
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        switch (sUriMatch.match(uri)) {
            case CITIZENS:
                // Perform regular delete
                count = db.delete(CitizenTable.TABLE_NAME, selection, selectionArgs);
                break;

            case SSID:
                // From incoming uri get ssid
                String ssid = uri.getPathSegments().get(CitizenTable.SSID_PATH_POSITION);
                // User wants to delete a specific citizen
                String finalWhere = CitizenTable.ID + "=" + ssid;
                // If user specifies where filter then append
                if (selection != null) {
                    finalWhere += " AND " + selection;
                }
                count = db.delete(CitizenTable.TABLE_NAME, finalWhere, selectionArgs);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }
        getContext().getContentResolver().notifyChange(uri, null);
        return count;
    }

    @Override
    public int update(@NonNull Uri uri, @Nullable ContentValues values, @Nullable String selection, @Nullable String[] selectionArgs) {
        int count = 0;
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        switch (sUriMatch.match(uri)) {
            case CITIZENS:
                // General update on all citizens
                count = db.update(CitizenTable.TABLE_NAME, values, selection, selectionArgs);
                break;

            case SSID:
                // From incoming uri get ssid
                String ssid = uri.getPathSegments().get(CitizenTable.SSID_PATH_POSITION);
                // The user wants to update a specific citizen
                String finalWhere = CitizenTable.ID + "=" + ssid;
                if (selection != null) {
                    finalWhere += " AND " + selection;
                }
                count = db.update(CitizenTable.TABLE_NAME, values, finalWhere, selectionArgs);
                break;

            default:
                throw new IllegalArgumentException("Unknown URI " + uri);
        }
        getContext().getContentResolver().notifyChange(uri, null);
        return count;
    }

    public static class DatabaseHelper extends SQLiteOpenHelper {

        private static final String DATABASE_NAME = "citizens.db";
        private static final int DATABASE_VERSION = 1;

        public DatabaseHelper(@Nullable Context context) {
            super(context, DATABASE_NAME, null, DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            // Create income table
            db.execSQL("CREATE TABLE " + CitizenTable.TABLE_NAME + " (" + CitizenTable.ID +
                    " INTEGER PRIMARY KEY AUTOINCREMENT, " + CitizenTable.NAME + " TEXT, " +
                    CitizenTable.STATE + " TEXT, " + CitizenTable.INCOME + " INTEGER);");
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            Log.w(TAG, "Upgrading database from version " + oldVersion + " to " + newVersion +
                    " which will destroy all old data");
            db.execSQL("DROP TABLE IF EXISTS " + CitizenTable.TABLE_NAME);
            onCreate(db);
        }
    }
}
```

#### 5.3 MainActivity 类

##### 5.3.1 Kotlin 版本

```kotlin
package com.android.contentprovidertest

import android.content.ContentValues
import android.database.Cursor
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.loader.app.LoaderManager
import androidx.loader.content.CursorLoader
import androidx.loader.content.Loader

private const val TAG = "MainActivity"

class MainActivity : AppCompatActivity(), LoaderManager.LoaderCallbacks<Cursor> {

    private lateinit var mLoaderManager: LoaderManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val contentValues = ContentValues().apply {
            put(CitizenTable.NAME, "Jason Wei")
            put(CitizenTable.STATE, "CA")
            put(CitizenTable.INCOME, 100000)
        }
        contentResolver.insert(CitizenTable.CONTENT_URI, contentValues)

        contentValues.clear()
        contentValues.apply {
            put(CitizenTable.NAME, "James Lee")
            put(CitizenTable.STATE, "NY")
            put(CitizenTable.INCOME, 120000)
        }
        contentResolver.insert(CitizenTable.CONTENT_URI, contentValues)

        contentValues.clear()
        contentValues.apply {
            put(CitizenTable.NAME, "Daniel Lee")
            put(CitizenTable.STATE, "NY")
            put(CitizenTable.INCOME, 80000)
        }
        contentResolver.insert(CitizenTable.CONTENT_URI, contentValues)

        mLoaderManager = LoaderManager.getInstance(this)
        // Query table for all columns and rows
        mLoaderManager.initLoader(0, null, this)
        mLoaderManager.initLoader(1, null, this)
    }

    override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
        Log.d(TAG, "onCreateLoader=>id: $id")
        if (id == 0) {
            return CursorLoader(
                this,
                CitizenTable.CONTENT_URI,
                null,
                null,
                null,
                "${CitizenTable.INCOME} ASC"
            )
        } else if (id == 1) {
            val uri = Uri.withAppendedPath(CitizenTable.CONTENT_URI, "2")
            uri.pathSegments
            Log.d(TAG, "onCreateLoader=>uri: $uri, pathSegments: ${uri.pathSegments}")
            return CursorLoader(
                this,
                uri,
                null,
                null,
                null,
                null
            )
        } else {
            return CursorLoader(
                this,
                CitizenTable.CONTENT_URI,
                null,
                null,
                null,
                null
            )
        }
    }

    override fun onLoaderReset(loader: Loader<Cursor>) {
        Log.d(TAG, "onLoaderReset=>id: ${loader.id}")
    }

    override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor?) {
        Log.d(TAG, "onLoadFinished=>id: ${loader.id}")
        data?.apply {
            val idCol = getColumnIndex(CitizenTable.ID)
            val nameCol = getColumnIndex(CitizenTable.NAME)
            val stateCol = getColumnIndex(CitizenTable.STATE)
            val incomeCol = getColumnIndex(CitizenTable.INCOME)
            while (moveToNext()) {
                val id = getInt(idCol)
                val name = getString(nameCol)
                val state = getString(stateCol)
                val income = getInt(incomeCol)
                Log.d(TAG, "Retrieved || $id || $name || $state || $income")
            }
            Log.d(TAG, "----------------------------------------------------")
        }
    }
}
```

##### 5.3.2 Java 版本

```java
package com.android.contentprovidertest;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.loader.app.LoaderManager;
import androidx.loader.content.CursorLoader;
import androidx.loader.content.Loader;

import android.content.ContentUris;
import android.content.ContentValues;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity implements LoaderManager.LoaderCallbacks<Cursor> {

    private static final String TAG = "MainActivity";

    private LoaderManager mLoaderManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ContentValues contentValues = new ContentValues();
        contentValues.put(CitizenTable.NAME, "Jason Wei");
        contentValues.put(CitizenTable.STATE, "CA");
        contentValues.put(CitizenTable.INCOME, 100000);
        getContentResolver().insert(CitizenTable.CONTENT_URI, contentValues);

        contentValues.clear();
        contentValues.put(CitizenTable.NAME, "James Lee");
        contentValues.put(CitizenTable.STATE, "NY");
        contentValues.put(CitizenTable.INCOME, 120000);
        getContentResolver().insert(CitizenTable.CONTENT_URI, contentValues);

        contentValues.clear();
        contentValues.put(CitizenTable.NAME, "Daniel Lee");
        contentValues.put(CitizenTable.STATE, "NY");
        contentValues.put(CitizenTable.INCOME, 80000);
        getContentResolver().insert(CitizenTable.CONTENT_URI, contentValues);

        mLoaderManager = LoaderManager.getInstance(this);
        // Query table for all columns and rows
        mLoaderManager.initLoader(0, null, this);
        mLoaderManager.initLoader(1, null, this);
    }

    @NonNull
    @Override
    public Loader<Cursor> onCreateLoader(int id, @Nullable Bundle args) {
        Log.d(TAG, "onCreateLoader=>id: " + id);
        if (id == 0) {
            return new CursorLoader(this, CitizenTable.CONTENT_URI, null,
                    null, null, CitizenTable.INCOME + " ASC");
        } else if (id == 1) {
            Uri uri = Uri.withAppendedPath(CitizenTable.CONTENT_URI, "2");
            return new CursorLoader(this, uri, null, null, null, null);
        }
        return null;
    }

    @Override
    public void onLoadFinished(@NonNull Loader<Cursor> loader, Cursor data) {
        Log.d(TAG, "onLoadFinished=>id: " + loader.getId());
        if (data != null) {
            int idCol = data.getColumnIndex(CitizenTable.ID);
            int nameCol = data.getColumnIndex(CitizenTable.NAME);
            int stateCol = data.getColumnIndex(CitizenTable.STATE);
            int incomingCol = data.getColumnIndex(CitizenTable.INCOME);
            while (data.moveToNext()) {
                int id = data.getInt(idCol);
                String name = data.getString(nameCol);
                String state = data.getString(stateCol);
                int incoming = data.getInt(incomingCol);
                Log.d(TAG, "Retrieved || " + id + " || " + name + " || " + state + " || " + incoming);
            }
        }
    }

    @Override
    public void onLoaderReset(@NonNull Loader<Cursor> loader) {
        Log.d(TAG, "onLoaderReset=>id: " + loader.getId());
    }
}
```

#### 5.4 AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.ContentProviderTest"
        tools:targetApi="31">
        <provider
            android:authorities="com.android.contentprovidertest.CitizenContentProvider"
            android:name=".CitizenContentProvider" />
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

