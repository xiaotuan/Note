[toc]

### 1. 创建数据库

创建一个继承 `SQLiteOpenHelper` 的类，并复写 `onCreate()` 和 `onUpgrade()` 方法。

#### 1.1 Kotlin 版本

```kotlin
package net.zenconsult.android

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class ContactsDb(
    context: Context,
    name: String,
    factory: SQLiteDatabase.CursorFactory?,
    version: Int
): SQLiteOpenHelper(context, name, factory, version) {

    override fun onCreate(db: SQLiteDatabase?) {
        val createSQL = "CREATE TABLE " + TABLE_NAME +
                " ( FIRSTNAME TEXT, LASTNAME TEXT, EMAIL TEXT," +
                " PHONE TEXT, ADDRESS1 TEXT, ADDRESS2 TEXT);";
        db?.execSQL(createSQL)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        // KILL PREVIOUS TABLE IF UPGRADED
        db?.execSQL("DROP TABLE IF EXISTS $TABLE_NAME")

        // CREATE NEW INSTANCE OF TABLE
        onCreate(db)
    }

    companion object {
        const val TABLE_NAME = "Contacts"
    }
}
```

#### 1.2 Java 版本

```java
package net.zenconsult.android;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class ContactsDb extends SQLiteOpenHelper {

    public static final String TABLE_NAME = "Contacts";

    public ContactsDb(Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
        super(context, name, factory, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String createSQL = "CREATE TABLE " + TABLE_NAME
                + " ( FIRSTNAME TEXT, LASTNAME TEXT, EMAIL TEXT,"
                + " PHONE TEXT, ADDRESS1 TEXT, ADDRESS2 TEXT);";
        db.execSQL(createSQL);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // KILL PREVIOUS TABLE IF UPGRADED
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);

        // CREATE NEW INSTANCE OF TABLE
        onCreate(db);
    }
}
```

### 2. 使用数据库

#### 2.1 Kotlin 版本

```kotlin

val contact = Contact()
contact.firstName = "Sheran"
contact.lastName = "Gunasekera"
contact.email = "sheran@zenconsult.net"
contact.phone = "+12120031337"

val db = ContactsDb(this, "ContactsDb", null, 1)

// 写入数据
val values = ContentValues()
values.apply {
    put("FIRSTNAME", contact.firstName.toByteArray())
    put("LASTNAME", contact.lastName.toByteArray())
    put("EMAIL", contact.email.toByteArray())
    put("PHONE", contact.phone.toByteArray())
    put("ADDRESS1", contact.address1.toByteArray())
    put("ADDRESS2", contact.address2.toByteArray())
}
db.writableDatabase.insert(ContactsDb.TABLE_NAME, null, values)

// 读取数据
val cols = arrayOf( "FIRSTNAME", "LASTNAME", "EMAIL", "PHONE" )
val result = db.readableDatabase.query(ContactsDb.TABLE_NAME, cols, "", null, "", "", "")

val c = Contact()
result.moveToFirst()

c.firstName = result.getString(result.getColumnIndex("FIRSTNAME"))
c.lastName = result.getString(result.getColumnIndex("LASTNAME"))
c.email = result.getString(result.getColumnIndex("EMAIL"))
c.phone = result.getString(result.getColumnIndex("PHONE"))
```

#### 2.2 Java 版本

```java
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

Contact contact = new Contact();
contact.setFirstName("Sheran");
contact.setLastName("Gunasekera");
contact.setEmail("sheran@zenconsult.net");
contact.setPhone("+12120031337");

ContactsDb db = new ContactsDb(this, "ContactsDb", null, 1);

// 写入数据
ContentValues values = new ContentValues();
try {
    values.put("FIRSTNAME", contact.getFirstName());
    values.put("LASTNAME", contact.getLastName());
    values.put("EMAIL", contact.getEmail());
    values.put("PHONE", contact.getPhone());
    values.put("ADDRESS1", contact.getAddress1());
    values.put("ADDRESS2ADDRESS2", contact.getAddress2());
} catch (Exception e) {
    Log.e(TAG, "store=>error: ", e);
}

SQLiteDatabase wdb = db.getWritableDatabase();
wdb.insert(ContactsDb.TABLE_NAME, null, values);

// 读取数据
SQLiteDatabase rdb = db.getReadableDatabase();
        String[] cols = { "FIRSTNAME", "LASTNAME", "EMAIL", "PHONE" };
Cursor results = rdb.query(ContactsDb.TABLE_NAME, cols, "", null, "", "", "");

Contact c = new Contact();
results.moveToFirst();

try {
    c.setFirstName(results.getString(results.getColumnIndex("FIRSTNAME")));
    c.setLastName(results.getString(results.getColumnIndex("LASTNAME")));
    c.setEmail(results.getString(results.getColumnIndex("EMAIL")));
    c.setPhone(results.getString(results.getColumnIndex("PHONE")));
} catch (Exception e) {
    Log.e(TAG, "get=>error: ", e);
}
```

