使用 SQL 语句插入数据方法如下所示：

**kotlin**

```kotlin
val sqh = SQLiteHelper(this)
val sqdb = sqh.writableDatabase
val insertQuery = "INSERT INTO ${SQLiteHelper.TABLE_NAME} (${SQLiteHelper.NAME}) VALUES ('jwei')"
sqdb.execSQL(insertQuery)
```

**java**

```java
SQLiteHelper sqh = new SQLiteHelper(this);
SQLiteDatabase sqdb = sqh.getWritableDatabase();
String insertQuery = "INSERT INTO " + SQLiteHelper.TABLE_NAME + " (" + SQLiteHelper.NAME + ") VALUES ('jwei')";
sqdb.execSQL(insertQuery);
```

