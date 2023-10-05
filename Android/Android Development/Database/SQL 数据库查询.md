[toc]

> 提示：文件使用到的数据库请参照 《[一个高级 SQLite 数据库的示例代码](./一个高级 SQLite 数据库的示例代码.md)》中的代码。

#### 1. 构建 SQLite 查询方法

查询 `SQLite` 数据库的最低级方法是通过 `SQLiteDatabase` 类的 `rawQuery()` 方法，定义如下：

```java
Cursor rawQuery(String sql, String[] selectionArgs)
```

该方法主要适用于哪些熟悉 `SQL` 背景的人，因为你可以将 `SQL` 查询语句作为第一个参数传递到该方法。如果查询语句中存在 `WHERE` 筛选器，那么可以通过第二个参数传入这些筛选器值。

第二个查询方法是 `SQLiteDatabase` 类提供查询包装器方法 `query()`，任何实际的 `SQL` 编程都是隐藏的，相反，查询的所有部分都作为参数传入：

```java
Cursor query(String table, String[] columns, String selection,
            String[] selectionArgs, String groupBy, String having,
            String orderBy)
```

第三个方法来自 `SQLiteQueryBuilder` 类的 `buildQuery()` 方法：

```java
String buildQuery(
            String[] projectionIn, String selection, String groupBy,
            String having, String sortOrder, String limit)
```

上面的方法是构造 `SELECT` 语句的一种快捷方法，它可以用于一组 `SELECT` 语句，这些语句将通过 `buildUnionQuery()` 方法中的 `UNION` 运算符连接，如下所示：

```java
String buildUnionQuery(String[] subQueries, String sortOrder, String limit)
```

`buildUnionQuery()` 方法允许你传入一组 `SELECT` 语句，并构造一个将返回这些字查询的 `UNION` 的查询语句。

`buildQueryString()` 方法类似于 `SQLiteDatabase` 类的 `query()` 方法，但只是将查询作为字符串返回：

```java
public static String buildQueryString(
            boolean distinct, String tables, String[] columns, String where,
            String groupBy, String having, String orderBy, String limit)
```

`setDistinct()` 方法允许你将当前查询设置为是否只返回不同的行。`setTables()` 方法允许你设置要查询的表的列表，如果传递了多个表，则允许你对这些表执行 `JOIN`。

#### 2. SELECT 语法

`SELECT` 语法格式如下：

```sql
SELECT 列名1, 列名2, ..., 列名n FROM 表名
```

如果需要查询表中所有列，可以使用下面语法格式：

```sql
SELECT * FROM 表名
```

##### 2.1 Kotlin 示例代码

```kotlin
/*
 * SELECT Query
 */
val sqdb = sh.readableDatabase

Log.d(TAG, "METHOD 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT * from ${StudentTable.TABLE_NAME}", null)
colid = c.getColumnIndex(StudentTable.NAME)
if (colid != -1) {
    while (c.moveToNext()) {
        val name = c.getString(colid)
        Log.d(TAG, "Got student $name")
    }
}

Log.d(TAG, "Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, null, null, null,
    null, null, null)
colid = c.getColumnIndex(StudentTable.NAME)
if (colid != -1) {
    while (c.moveToNext()) {
        val name = c.getString(colid)
        Log.d(TAG, "Got student $name")
    }
}

Log.d(TAG, "Method 3")
// Method #3 - SQLiteQueryBuilder
var query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    null, null, null, null, null, null)
Log.d(TAG, "query: $query")
c = sqdb.rawQuery(query, null)
colid = c.getColumnIndex(StudentTable.NAME)
if (colid != -1) {
    while (c.moveToNext()) {
        val name = c.getString(colid)
        Log.d(TAG, "Got student $name")
    }
}

 /*
 * SELECT COLUMNS Query
 */
Log.d(TAG, "SELECT COLUMNS Query Method 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT ${StudentTable.NAME}, ${StudentTable.STATE} from ${StudentTable.TABLE_NAME}",
    null)
var nameIndex = c.getColumnIndex(StudentTable.NAME)
var stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "SELECT COLUMNS Query Method 2")
// Method #2 - SQLiteDatabase query()
val cols = arrayOf( StudentTable.NAME, StudentTable.STATE )
c = sqdb.query(StudentTable.TABLE_NAME, cols, null, null, null,
    null, null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "SELECT COLUMNS Query Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME, cols,
    null, null, null, null, null)
Log.d(TAG, "SELECT COLUMNS query: $query")
c = sqdb.rawQuery(query, null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}
```

##### 2.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * SELECT Query
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
Cursor c = sqdb.rawQuery("SELECT * from " + StudentTable.TABLE_NAME, null);
int colid = c.getColumnIndex(StudentTable.NAME);
while (c.moveToNext()) {
    String name = c.getString(colid);
    Log.d(TAG, "Got Student " + name);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
c = sqdb.query(StudentTable.TABLE_NAME, null, null, null,
        null, null, null);
colid = c.getColumnIndex(StudentTable.NAME);
while (c.moveToNext()) {
    String name = c.getString(colid);
    Log.d(TAG, "Got Student " + name);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
        null, null, null, null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
colid = c.getColumnIndex(StudentTable.NAME);
while (c.moveToNext()) {
    String name = c.getString(colid);
    Log.d(TAG, "Got Student " + name);
}
```

指定查询列的示例代码：

```javaa
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * SELECT COLUMNS Query
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
Cursor c = sqdb.rawQuery("SELECT " + StudentTable.NAME + ", " + StudentTable.STATE + " from "
        + StudentTable.TABLE_NAME, null);
int nameIndex = c.getColumnIndex(StudentTable.NAME);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
String[] cols = new String[] { StudentTable.NAME, StudentTable.STATE };
c = sqdb.query(StudentTable.TABLE_NAME, cols, null, null,
        null, null, null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
        cols, null, null, null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}
```

#### 3. WHERE 过滤器和 SQL 运算符

`WHERE` 过滤器的语法格式如下：

```sql
SELECT 列名1, 列名2, ..., 列名n FROM 表名 WHERE 列名 = 过滤值
```

可以通过 `SQL` 运算符 `AND` 或 `OR` 将多个过滤器组合在一起，语法格式如下：

```sql
SELECT 列名1, 列名2, ..., 列名n FROM 表名 WHERE 列名1 = 过滤值1 AND WHERE 列名2 = 过滤值2 AND WHERE 列名n = 过滤n
SELECT 列名1, 列名2, ..., 列名n FROM 表名 WHERE 列名1 = 过滤值1 OR WHERE 列名2 = 过滤值2 OR WHERE 列名n = 过滤n
SELECT 列名1, 列名2, ..., 列名n FROM 表名 WHERE 列名1 = 过滤值1 OR WHERE 列名2 = 过滤值2 AND WHERE 列名n = 过滤n
```

> 注意：`WHERE` 子句可以包含任意数目的 `AND` 和 `OR` 操作符。允许两者结合以进行复杂、高级的过滤。在处理求值顺序时，优先处理 `AND` 操作符。

##### 3.1 Kotlin 示例代码

```kotlin
/*
 * WHERE filter - Filter by State
 */
Log.d(TAG, "WHERE Filter Method 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT * from ${StudentTable.TABLE_NAME} WHERE ${StudentTable.STATE} = ?", arrayOf( "IL" ))
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "WHERE Filter Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, null, "${StudentTable.STATE} = ?",
    arrayOf( "IL" ), null, null, null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "WHERE Filter Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    null, "${StudentTable.STATE}='IL'", null, null,
    null , null)
Log.d(TAG, "WHERE Filter query: $query")
c = sqdb.rawQuery(query, null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

/*
 * AND/OR Clauses
 */
Log.d(TAG, "AND/OR Clauses method 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT * from ${StudentTable.TABLE_NAME} WHERE ${StudentTable.STATE} = ? OR ${StudentTable.STATE} = ?",
    arrayOf( "IL", "AR" ))
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "AND/OR Clauses method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, null, "${StudentTable.STATE} = ? OR ${StudentTable.STATE} = ?",
    arrayOf( "IL", "AR" ), null, null, null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "AND/OR Clauses method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    null, "${StudentTable.STATE}='IL' OR ${StudentTable.STATE}='AR'",
    null, null, null, null)
Log.d(TAG, "AND/OR Clauses query: $query")
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}
```

##### 3.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
    SQLiteDatabase sqdb = sh.getReadableDatabase();

    /*
     * WHERE Filter - Filter by State
     */
    Log.d(TAG, "Method 1");
    // Method #1 - SQLiteDatabase rawQuery
    Cursor c = sqdb.rawQuery("SELECT * FROM " + StudentTable.TABLE_NAME + " WHERE "
            + StudentTable.STATE + "= ? ", new String[] { "IL" });
    int nameIndex = c.getColumnIndex(StudentTable.NAME);
    int stateIndex = c.getColumnIndex(StudentTable.STATE);
    while (c.moveToNext()) {
        String name = c.getString(nameIndex);
        String state = c.getString(stateIndex);
        Log.d(TAG, "Got Student " + name + " in " + state);
    }

    Log.d(TAG, "Method 2");
    // Method #2 - SQLiteDatabase query
    String[] cols = new String[] { StudentTable.NAME, StudentTable.STATE };
    c = sqdb.query(StudentTable.TABLE_NAME, cols, StudentTable.STATE + " = ?",
            new String[] { "IL" }, null, null, null);
    nameIndex = c.getColumnIndex(StudentTable.NAME);
    stateIndex = c.getColumnIndex(StudentTable.STATE);
    while (c.moveToNext()) {
        String name = c.getString(nameIndex);
        String state = c.getString(stateIndex);
        Log.d(TAG, "Got Student " + name + " in " + state);
    }

    Log.d(TAG, "Method 3");
    // Method #3 - SQLiteQueryBuilder
    String query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
            cols, StudentTable.STATE + " = 'IL'", null, null, null, null);
    Log.d(TAG, "Query: " + query);
    c = sqdb.rawQuery(query, null);
    nameIndex = c.getColumnIndex(StudentTable.NAME);
    stateIndex = c.getColumnIndex(StudentTable.STATE);
    while (c.moveToNext()) {
        String name = c.getString(nameIndex);
        String state = c.getString(stateIndex);
        Log.d(TAG, "Got Student " + name + " in " + state);
    }
}
```

`WHERE` 语句添加 `AND` 或 `OR` 条件的示例代码：

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * AND/OR Clauses
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
Cursor c = sqdb.rawQuery("SELECT * FROM " + StudentTable.TABLE_NAME + " WHERE "
        + StudentTable.STATE + "= ? OR " + StudentTable.STATE + " = ?", new String[] { "IL", "AR" });
int nameIndex = c.getColumnIndex(StudentTable.NAME);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
String[] cols = new String[] { StudentTable.NAME, StudentTable.STATE };
c = sqdb.query(StudentTable.TABLE_NAME, cols, StudentTable.STATE + " = ? OR "
        + StudentTable.STATE + " = ?", new String[] { "IL", "AR" }, null, null, null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
        cols, StudentTable.STATE + " = 'IL' OR " + StudentTable.STATE + " = 'AR'",
        null, null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}
```

#### 4. DISTINCT 和 LIMIT 子句

要想检索的结果没有重复值，可以使用 `DISTINCT` 语句，其语法格式如下：

```sql
SELECT DISTINCT 列名1, 列名2, ..., 列名n FROM 表名
```

> 注意：`DISTINCT` 关键字作用于所有的列，不仅仅时跟在其后的那一列。

要想限制查询的结果数量，可以使用 `LIMIT` 语句，其语法格式如下：

```sql
SELECT 列名1, 列名2, ..., 列名n FROM 表名 LIMIT n
SELECT 列名1, 列名2, ..., 列名n FROM 表名 LIMIT n, m
```

`n` ：表示从第 `n` 行开始返回数据。

`n, m`：表示从第 `n` 行开始返回 `m` 行数据。

##### 4.1 Kotlin 示例代码

```kotlin
/*
 * DISTINCT Clause
 */
Log.d(TAG, "DISTINCT Clause Method 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT DISTINCT ${StudentTable.STATE} from ${StudentTable.TABLE_NAME}",
    null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student state $state")
    }
}

Log.d(TAG, "DISTINCT Clause Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(true, StudentTable.TABLE_NAME, arrayOf( StudentTable.STATE ),
    null, null, null, null, null, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student state $state")
    }
}

Log.d(TAG, "DISTINCT Clause Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
    arrayOf( StudentTable.STATE ), null, null, null, null, null)
Log.d(TAG, "DISTINCT Clauses query: $query")
c = sqdb.rawQuery(query, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student state $state")
    }
}

/*
 * LIMIT Clause
 */
Log.d(TAG, "LIMIT Clause Method 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT * FROM ${StudentTable.TABLE_NAME} LIMIT 0, 3", null)
colid = c.getColumnIndex(StudentTable.NAME)
if (colid != -1) {
    while (c.moveToNext()) {
        val name = c.getString(colid)
        Log.d(TAG, "Got student $name")
    }
}

Log.d(TAG, "LIMIT Clause Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(false, StudentTable.TABLE_NAME, null, null,
    null, null, null, null, "3")
colid = c.getColumnIndex(StudentTable.NAME)
if (colid != -1) {
    while (c.moveToNext()) {
        val name = c.getString(colid)
        Log.d(TAG, "Got student $name")
    }
}

Log.d(TAG, "LIMIT Clause Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    null, null, null, null, null, "3")
Log.d(TAG, "LIMIT Clauses query: $query")
colid = c.getColumnIndex(StudentTable.NAME)
if (colid != -1) {
    while (c.moveToNext()) {
        val name = c.getString(colid)
        Log.d(TAG, "Got student $name")
    }
}
```

##### 4.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * DISTINCT Clause
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
Cursor c = sqdb.rawQuery("SELECT DISTINCT " + StudentTable.STATE + " FROM "
        + StudentTable.TABLE_NAME, null);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got State " + state);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
String[] cols = new String[] { StudentTable.STATE };
c = sqdb.query(true, StudentTable.TABLE_NAME, cols, null, null,
        null, null, null, null);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got State " + state);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        cols, null,null, null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got State " + state);
}
```

`LIMIT` 子句的示例代码：

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * LIMIT Clause
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
Cursor c = sqdb.rawQuery("SELECT * FROM " + StudentTable.TABLE_NAME + " LIMIT 0, 2", null);
int nameIndex = c.getColumnIndex(StudentTable.NAME);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
c = sqdb.query(true, StudentTable.TABLE_NAME, null, null, null,
        null, null, null, "2");
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        null, null,null, null, null, "2");
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}
```

#### 5. ORDER BY 和 GROUP BY 子句

`ORDER BY` 语法格式如下：

```sql
SELECT 列名1, 列名2, ..., 列名n FROM 表名 ORDER BY 列名 ASC|DESC
```

`ASC`： 升序排序（默认值）。

`DESC`：降序排序。

`GROUP BY` 语法格式如下：

```sql
SELECT 列名1, 列名2, ..., 列名n, aggregate_function(列名) FROM 表名 GROUP BY 列名
```

##### 5.1 Kotlin 示例代码

```kotlin
/*
 * ORDER BY Clause
 */
Log.d(TAG, "ORDER BY Clause Method 1")
// Method #1 - SQLiteDatabase rawQuery()
c = sqdb.rawQuery("SELECT * FROM ${StudentTable.TABLE_NAME} ORDER BY ${StudentTable.STATE} ASC", null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "ORDER BY Clause Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, null, null, null,
    null, null, "${StudentTable.STATE} ASC", null)
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

Log.d(TAG, "LIMIT Clause Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    null, null, null, null, "${StudentTable.STATE} ASC", null)
Log.d(TAG, "LIMIT Clauses query: $query")
nameIndex = c.getColumnIndex(StudentTable.NAME)
stateIndex = c.getColumnIndex(StudentTable.STATE)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val name = c.getString(nameIndex)
        val state = c.getString(stateIndex)
        Log.d(TAG, "Got student $name in $state")
    }
}

/*
 * GROUP BY Clause
 */
Log.d(TAG, "GROUP BY Clause Method 1")
// Method #1 - SQLiteDatabase rawQuery()
val colName = "COUNT(${StudentTable.STATE})"
c = sqdb.rawQuery("SELECT ${StudentTable.STATE}, $colName FROM ${StudentTable.TABLE_NAME} GROUP BY ${StudentTable.STATE}", null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
var colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

Log.d(TAG, "GROUP BY Clause Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, arrayOf( StudentTable.STATE, colName ), null,
    null, StudentTable.STATE, null, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

Log.d(TAG, "GROUP BY Clause Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    arrayOf( StudentTable.STATE, colName ), null, StudentTable.STATE, null,
    null, null)
Log.d(TAG, "GROUP BY Clauses query: $query")
c = sqdb.rawQuery(query, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}
```

##### 5.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * ORDER BY Clause
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
Cursor c = sqdb.rawQuery("SELECT * FROM " + StudentTable.TABLE_NAME + " ORDER BY " + StudentTable.STATE + " DESC", null);
int nameIndex = c.getColumnIndex(StudentTable.NAME);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
c = sqdb.query(true, StudentTable.TABLE_NAME, null, null, null,
        null, null, StudentTable.STATE + " DESC", null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        null, null,null, null, StudentTable.STATE + " DESC", null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
nameIndex = c.getColumnIndex(StudentTable.NAME);
stateIndex = c.getColumnIndex(StudentTable.STATE);
while (c.moveToNext()) {
    String name = c.getString(nameIndex);
    String state = c.getString(stateIndex);
    Log.d(TAG, "Got Student " + name + " in " + state);
}
```

`GROUP BY` 子句的示例代码：

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * GROUP BY Clause
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
String colName = "COUNT(" + StudentTable.STATE + ")";
Cursor c = sqdb.rawQuery("SELECT " + StudentTable.STATE + ", " + colName + " FROM "
        + StudentTable.TABLE_NAME + " GROUP BY " + StudentTable.STATE, null);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
int stateCountIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    String count = c.getString(stateCountIndex);
    Log.d(TAG, "Got state " + state + ", count " + count);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
c = sqdb.query(true, StudentTable.TABLE_NAME, new String[] { StudentTable.STATE, colName },
        null, null, StudentTable.STATE, null, null, null);
stateIndex = c.getColumnIndex(StudentTable.STATE);
stateCountIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    String count = c.getString(stateCountIndex);
    Log.d(TAG, "Got state " + state + ", count " + count);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        new String[] { StudentTable.STATE, colName }, null,StudentTable.STATE,
        null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
stateIndex = c.getColumnIndex(StudentTable.STATE);
stateCountIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    String count = c.getString(stateCountIndex);
    Log.d(TAG, "Got state " + state + ", count " + count);
}
```

#### 6. HAVING 过滤器和聚合函数

`HAVING` 过滤器只能与 `GROUPBY` 子句一起使用。使用 `HAVING` 过滤器，使其值返回哪些总计数大于或小于某个值的状态。

##### 6.1 Kotlin 示例代码

```kotlin
/*
 * GROUP BY Clause
 */
Log.d(TAG, "GROUP BY Clause Method 1")
// Method #1 - SQLiteDatabase rawQuery()
var colName = "COUNT(${StudentTable.STATE})"
c = sqdb.rawQuery("SELECT ${StudentTable.STATE}, $colName FROM ${StudentTable.TABLE_NAME} GROUP BY ${StudentTable.STATE}", null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
var colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

Log.d(TAG, "GROUP BY Clause Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, arrayOf( StudentTable.STATE, colName ), null,
    null, StudentTable.STATE, null, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

Log.d(TAG, "GROUP BY Clause Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    arrayOf( StudentTable.STATE, colName ), null, StudentTable.STATE, null,
    null, null)
Log.d(TAG, "GROUP BY Clauses query: $query")
c = sqdb.rawQuery(query, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

/*
 * HAVING Filter
 */
Log.d(TAG, "HAVING Filter Method 1")
// Method #1 - SQLiteDatabase rawQuery()
colName = "COUNT(${StudentTable.STATE})"
c = sqdb.rawQuery("SELECT ${StudentTable.STATE}, $colName FROM ${StudentTable.TABLE_NAME} GROUP BY ${StudentTable.STATE} HAVING $colName > 1", null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

Log.d(TAG, "HAVING Filter Method 2")
// Method #2 - SQLiteDatabase query()
c = sqdb.query(StudentTable.TABLE_NAME, arrayOf( StudentTable.STATE, colName ), null, 
    null, StudentTable.STATE, "$colName > 1", null);
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}

Log.d(TAG, "HAVING Filter Method 3")
// Method #3 - SQLiteQueryBuilder
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME,
    arrayOf( StudentTable.STATE, colName ), null, StudentTable.STATE, "$colName > 1",
    null, null)
Log.d(TAG, "HAVING Filter query: $query")
c = sqdb.rawQuery(query, null)
stateIndex = c.getColumnIndex(StudentTable.STATE)
colNameIndex = c.getColumnIndex(colName)
if (nameIndex != -1 && stateIndex != -1) {
    while (c.moveToNext()) {
        val state = c.getString(stateIndex)
        val count = c.getInt(colNameIndex)
        Log.d(TAG, "Got student $state count $count")
    }
}
```

##### 6.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * HAVING Filter
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
String colName = "COUNT(" + StudentTable.STATE + ")";
Cursor c = sqdb.rawQuery("SELECT " + StudentTable.STATE + ", " + colName + " FROM "
        + StudentTable.TABLE_NAME + " GROUP BY " + StudentTable.STATE + " HAVING "
        + colName + " > 1", null);
int stateIndex = c.getColumnIndex(StudentTable.STATE);
int stateCountIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    String count = c.getString(stateCountIndex);
    Log.d(TAG, "Got state " + state + ", count " + count);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
c = sqdb.query(true, StudentTable.TABLE_NAME, new String[] { StudentTable.STATE, colName },
        null, null, StudentTable.STATE, colName + " > 1",
        null, null);
stateIndex = c.getColumnIndex(StudentTable.STATE);
stateCountIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    String count = c.getString(stateCountIndex);
    Log.d(TAG, "Got state " + state + ", count " + count);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        new String[] { StudentTable.STATE, colName }, null, StudentTable.STATE,
        colName + " > 1", null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
stateIndex = c.getColumnIndex(StudentTable.STATE);
stateCountIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String state = c.getString(stateIndex);
    String count = c.getString(stateCountIndex);
    Log.d(TAG, "Got state " + state + ", count " + count);
}
```

#### 7. SQL 聚合函数

完整的 `SQL` 聚合函数列表请参阅：<https://www.sqlite.org/lang_aggfunc.html>。

##### 7.1 MIN/MAX/AVG 函数

###### 7.1.1 Kotlin 示例代码

```kotlin
/*
 * SQL Functions - MIN/MAX/AVG
 */
Log.d(TAG, "SQL Functions Method 1")
// Method #1 - SQLiteDatabase rawQuery()
colName = "MIN(${StudentTable.GRADE})"
c = sqdb.rawQuery("SELECT $colName FROM ${StudentTable.TABLE_NAME}", null)
colid = c.getColumnIndex(colName)
if (colid != -1) {
    while (c.moveToNext()) {
        val minGrade = c.getInt(colid)
        Log.d(TAG, "MIN GRADE $minGrade")
    }
}

Log.d(TAG, "SQL Functions Method 2")
// Method #2 - SQLiteDatabase query()
colName = "MAX(${StudentTable.GRADE})"
c = sqdb.query(StudentTable.TABLE_NAME, arrayOf( colName ), null, null,
    null, null, null)

Log.d(TAG, "SQL Functions Method 3")
// Method #3 - SQLiteQueryBuilder
colName = "AVG(${StudentTable.GRADE})"
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME, arrayOf( colName ), null, null, null, null, null)
Log.d(TAG, "SQL Fuctions query: $query")
c = sqdb.rawQuery(query, null)
colid = c.getColumnIndex(colName)
if (colid != -1) {
    while (c.moveToNext()) {
        val avgGrade = c.getInt(colid)
        Log.d(TAG, "AVG GRADE $avgGrade")
    }
}
}
```

###### 7.1.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * SQL Functions - MIN/MAX/AVG
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
String colName = "MIN(" + StudentTable.GRADE + ")";
Cursor c = sqdb.rawQuery("SELECT " + colName + " FROM " + StudentTable.TABLE_NAME, null);
int colNameIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String minGrade = c.getString(colNameIndex);
    Log.d(TAG, "Min Grade " + minGrade);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
colName = "MAX(" + StudentTable.GRADE + ")";
c = sqdb.query(true, StudentTable.TABLE_NAME, new String[] {  colName },
        null, null, null, null, null, null);
colNameIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String maxGrade = c.getString(colNameIndex);
    Log.d(TAG, "Max Grade " + maxGrade);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
colName = "AVG(" + StudentTable.GRADE + ")";
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        new String[] { colName }, null, null, null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
colNameIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String avgGrade = c.getString(colNameIndex);
    Log.d(TAG, "Avg Grade " + avgGrade);
}
```

##### 7.2 UPPER/LOWER/SUBSTR 函数

###### 7.2.1 Kotlin 示例代码

```kotlin
/*
 * SQL Functions - UPPER/LOWER/SUBSTR
 */
Log.d(TAG, "UPPER/LOWER/SUBSTR Method 1")
// Method #1 - SQLiteDatabase rawQuery()
colName = "UPPER(${StudentTable.NAME})"
c = sqdb.rawQuery("SELECT $colName FROM ${StudentTable.TABLE_NAME}", null)
colid = c.getColumnIndex(colName)
if (colid != -1) {
    while (c.moveToNext()) {
        val upperName = c.getInt(colid)
        Log.d(TAG, "Got Student $upperName")
    }
}

Log.d(TAG, "UPPER/LOWER/SUBSTR Method 2")
// Method #2 - SQLiteDatabase query()
colName = "LOWER(${StudentTable.NAME})"
c = sqdb.query(StudentTable.TABLE_NAME, arrayOf( colName ), null, null, 
    null, null, null)

Log.d(TAG, "UPPER/LOWER/SUBSTR Method 3")
// Method #3 - SQLiteQueryBuilder
colName = "SUBSTR(${StudentTable.NAME}, 1, 4)"
query = SQLiteQueryBuilder.buildQueryString(false, StudentTable.TABLE_NAME, arrayOf( colName ), 
    null, null, null, null, null)
Log.d(TAG, "SUBSTR query: $query")
c = sqdb.rawQuery(query, null)
```

###### 7.2.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * SQL Functions - UPPER/LOWER/SUBSTR
 */
Log.d(TAG, "Method 1");
// Method #1 - SQLiteDatabase rawQuery
String colName = "UPPER(" + StudentTable.NAME + ")";
Cursor c = sqdb.rawQuery("SELECT " + colName + " FROM " + StudentTable.TABLE_NAME, null);
int colNameIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String name = c.getString(colNameIndex);
    Log.d(TAG, "Student name " + name);
}

Log.d(TAG, "Method 2");
// Method #2 - SQLiteDatabase query
colName = "LOWER(" + StudentTable.NAME + ")";
c = sqdb.query(true, StudentTable.TABLE_NAME, new String[] {  colName },
        null, null, null, null, null, null);
colNameIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String name = c.getString(colNameIndex);
    Log.d(TAG, "Student name " + name);
}

Log.d(TAG, "Method 3");
// Method #3 - SQLiteQueryBuilder
colName = "SUBSTR(" + StudentTable.NAME + ", 1, 4)";
String query = SQLiteQueryBuilder.buildQueryString(true, StudentTable.TABLE_NAME,
        new String[] { colName }, null, null, null, null, null);
Log.d(TAG, "Query: " + query);
c = sqdb.rawQuery(query, null);
colNameIndex = c.getColumnIndex(colName);
while (c.moveToNext()) {
    String name = c.getString(colNameIndex);
    Log.d(TAG, "Student name " + name);
}
```

##### 7.3 JOINS 子句

`JOINS` 子句是联结表的意思，它根据指定的条件将多个表的数据联结成一个表。因此当我们返回特定列时，需要指出该列来自哪个表，可以使用下面的语法格式指定该列来自哪个表：

```sql
table_name.column_name
```

然后在 `SQLiteQueryBuilder` 类中，我们使用 `setTables()` 方法来格式化 `JOIN` 语句。

###### 7.3.1 Kotlin 示例代码

```kotlin
/*
 * SQL JOINS
 */
val sqdb = sh.readableDatabase
val sqb = SQLiteQueryBuilder()
// Notice the syntax for columns in join queries
val courseIdCol = "${CourseTable.TABLE_NAME}.${CourseTable.ID}"
val classCourseIdCol = "${ClassTable.TABLE_NAME}.${ClassTable.COURSE_ID}"
val classIdCol = "${ClassTable.TABLE_NAME}.${ClassTable.ID}"
sqb.tables = "${ClassTable.TABLE_NAME} INNER JOIN ${CourseTable.TABLE_NAME} ON ($classCourseIdCol = $courseIdCol)"
val cols = arrayOf( classIdCol, ClassTable.COURSE_ID, CourseTable.NAME )
val query = sqb.buildQuery(cols, null, null, null, null,  null)
Log.d(TAG, "SQL JOINS query: $query")
val c = sqdb.rawQuery(query, null)
val colid = c.getColumnIndex(cols[0])
val colid2 = c.getColumnIndex(cols[1])
val colid3 = c.getColumnIndex(cols[2])
while (c.moveToNext()) {
    val rowId = c.getInt(colid)
    val courseId = c.getInt(colid2)
    val courseName = c.getString(colid3)
    Log.d(TAG, "$rowId || COURSE ID $courseId || $courseName")
}
```

###### 7.3.2 Java 示例代码

```java
SchemaHelper sh = new SchemaHelper(this);
SQLiteDatabase sqdb = sh.getReadableDatabase();

/*
 * SQL JOINS
 */
SQLiteQueryBuilder sqb = new SQLiteQueryBuilder();
// Notice the syntax for columns in JOIN Queries
String courseIdCol = CourseTable.TABLE_NAME + "." + CourseTable.ID;
String classCourseIdCol = ClassTable.TABLE_NAME + "." + ClassTable.COURSE_ID;
String classIdCol = ClassTable.TABLE_NAME + "." + ClassTable.ID;
sqb.setTables(ClassTable.TABLE_NAME + " INNER JOIN " + CourseTable.TABLE_NAME
        + " ON (" + classCourseIdCol + " = " + courseIdCol + ")");
String[] cols = new String[] {
        classIdCol, ClassTable.COURSE_ID, CourseTable.NAME
};
String query = sqb.buildQuery(cols, null, null, null, null, null);
Log.d(TAG, "Query: " + query);
Cursor c = sqdb.rawQuery(query, null);
int colid = c.getColumnIndex(cols[0]);
int colid2 = c.getColumnIndex(cols[1]);
int colid3 = c.getColumnIndex(cols[2]);
while (c.moveToNext()) {
    int rowId = c.getInt(colid);
    int courseId = c.getInt(colid2);
    String courseName = c.getString(colid3);
    Log.d(TAG, rowId + " || COURSE ID " + courseId + " || " + courseName);
}
```

