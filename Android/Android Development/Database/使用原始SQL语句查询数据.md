使用原始 SQL 语句查询数据方法如下所示：

**Kotlin**

```kotlin
val sqh = SQLiteHelper(this)
val sqdb = sqh.writableDatabase
val query = "SELECT ${SQLiteHelper.UID}, ${SQLiteHelper.NAME} FROM ${SQLiteHelper.TABLE_NAME}"
val c2 = sqdb.rawQuery(query, null)

while (c2.moveToNext()) {
    val id = c2.getInt(c2.getColumnIndex(SQLiteHelper.UID))
    val name = c2.getString(c2.getColumnIndex(SQLiteHelper.NAME))
    Log.i("LOG_TAG", "ROW $id HAS NAME $name")
}

c2.close()
```

**Java**

```java
SQLiteHelper sqh = new SQLiteHelper(this);
SQLiteDatabase sqdb = sqh.getWritableDatabase();
String query = "SELECT " + SQLiteHelper.UID + "," + SQLiteHelper.NAME + " FROM " + SQLiteHelper.TABLE_NAME;
Cursor c2 = sqdb.rawQuery(query, null);

while (c2.moveToNext()) {
    int id = c2.getInt(c2.getColumnIndex(SQLiteHelper.UID));
    String name = c2.getString(c2.getColumnIndex(SQLiteHelper.NAME));
    Log.i("LOG_TAG", "ROW " + id + " HAS NAME " + name);
}

c2.close();
```

