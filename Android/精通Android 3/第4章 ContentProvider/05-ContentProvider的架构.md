设备上的每个 `ContentProvider` 都会使用字符串注册自身，这个字符串类似于域名，但称为授权。这个可唯一标识的字符串是此 `ContentProvider` 可提供的一组 URI 的基础。

授权的注册在 `AndroidManifest.xml` 中进行。下面给出了在 `AndroidManifest.xml` 中注册 `ContentProvider` 的两个示例：

```xml
<provider android:name="SomeProvider"
          android:authorities="com.your-company.SomeProvider" />

<provider android:name="NotePadProvider"
          android:authoritie="com.google.provider.NotePad" />
```

**1. Android内容 URI 的结构**

授权就像是 `ContentProvider` 的域名。在进行了前面的授权注册之后，这些 `ContentProvider` 就拥有了以授权前缀开头的 URL：

```
content://com.your-company.SomeProvider/
content://com.google.provider.NotePad/
```

`ContentProvider` 还提供了一种类似 REST 的 URL 来获取或操作数据。对于前面的注册，标识 NotePadProvider 数据库中的笔记目录或集合的 URI 为：

```
content://com.google.provider.NotePad/Notes
```

标识具体笔记的 URI 为：

```
content://com.google.provider.NotePad/Notes/#
```

其中 # 是特定笔记的 id。

**2. Android MIME 类型的结构**

`Android` 遵循类似的约定来定义 MIME 类型。`Android` MIME 类型中的 vnd 表示这些类型和子类型具有非标准的、供应商特定的形式。为了实现唯一性，`Android` 使用了多个类似域规范的部分来进一步区分类型和子类。而且，每个内容类型的 `Android MIME` 类型都具有两种形式：一个用于某条具体的记录，另一个用于多条记录。

对于单条记录，MIME 类型类似于：

```
vnd.android.cursor.item/vnd.yourcompanyname.contenttype
```

对于记录或行的集合，MIME 类型类似于：

```
vnd.android.cursor.dir/vnd.yourcompanyname.cotenttype
```

重申一下，通过 `Android` cursor 返回的项集合的主要 MIME 类型应该始终为 `vnd.android.cursor.dir`，通过 `Android` cursor 获取的单一项的主要 MIME 类型应该为 `vn.android.cursor.item`。

**3. 使用 URI 读取数据**

考虑 `Android SDK` 中帮助器类定义的以下 3 个 URI：

```
MediaStore.Images.Media.INTERNAL_CONTENT_URI
MediaStore.Images.Media.EXTERNAL_CONTENT_URI
Contacts.People.CONTENT_URI
```

给定这些 URI，从联系人提供程序获取单行联系人信息的代码类似于：

```java
Uri peopleBaseUri = Contacts.People.CONTENT_URI;
Uri myPersonUri = Uri.withAppendedPath(Content.People.CONTENT_URI, "23");

// Query for this record.
// managedQuery is a method on Activity class
Cursor cur = managedQuery(myPersonUri, null, null, null);
```

**代码清单4-1** 从 ContentProvider 获取一个游标

```java
// An array specifying which columns to return.
String[] projection = new String[] {
    People._ID,
    People.NAME,
    People.NUMBER,
};

// Get the base URI for People table in Contacts Content Provider.
// ie. content://contacts/people
Uri mContactsUri = Contacts.People.CONTENT_URI;

// Bast way to retrieve a query; returns a managed query,
Cursor managedCursor = managedQuery(mContactsUri,
                                   projection, // which columns to return.
                                   null, // WHERE clause
                                   Contacts.People.NAME + " ASC");	// Order-by clause.
```

**4. 使用游标**

在使用 `Android` 游标之前，应该了解有关游标的一些知识：

+ 游标是一个行集合；
+ 读取数据之前，需要使用 `moveToFirst()` ，因为游标放在第一行之前；
+ 需要知道列名称；
+ 需要知道列类型；
+ 所有字段访问方法都基于列编号，所以必须首先将列名称转换为列编号；
+ 游标可以随意移动（可以向前和向后移动，也可以跳过一段距离）；
+ 由于游标可以随意移动，所以可以向它获取行计数。

**代码清单4-2** 使用 while 循环导航游标

```java
if (cur.moveToFirst() == false) {
    // no rows empty cursor
    return;
}

// The cursor is already pointing to the first row
// let's access a few columns
int nameColumnIndex = cur.getColumnIndex(People.NAME);
String name = cur.getString(nameColumnIndex);

// let's now see how we can loop through a cursor
while (cur.moveToNext()) {
    // cursor moved successfully
    // acccess fields
}
```

为了将游标放在第一行上，我们在游标对象上使用 `moveToFirst()` 方法。如果游标为空，此方法返回 false。然后使用 `moveToNext()` 方法反复导航该游标。

为了帮助理解游标的位置， `Android`提供了一下方法：

```java
isBeforeFirst()
isAfterLast()
isClosed()
```

**代码清单4-3** 使用 for 循环导航游标

```java
// Get your indexes first outside the for loop
int nameColumn = cur.getColumnIndex(People.NAME);
int phoneColumn = cur.getColumnIndex(People.NUMBER);

// Walk the cursor now based on column indexes 
for (cur.moveToFirst(); !cur.isAfterLast(); cur.moveToNext()) {
    String name = cur.getString(nameColumn);
    String phoneNumber = cur.getString(phoneColumn);
}
```

l列的索引顺序似乎有些随意。因此，建议首先从游标显式获取索引，以避免意外。为了找到游标中的行数，`Android` 为游标对象提供了一个 `getCount()` 方法。

**5. 使用 where 子句**

**代码清单4-4** 通过 URI 传递 SQL WHERE 子句

```java
Activity someActivity;

// ..initialize someActivity
String noteUri = "content://com.google.provider.NotePad/notes/23";
Cursor managedCursor = someActivity.managedQuery(noteUri,
                                                projection, // which columns to return.
                                                null, // WHERE clause
                                                null); // Order-by clause.
```

当你留意笔记提供程序如何实现响应的查询方法时，就会很明显地发现这一点。下面查询方法中的一段代码：

```java
// Retrieve a note id from the incoming uri that looks like
// content://.../notes/23
int noteId = uri.getPathSegments().get(1);

// ask a query builder to build a query
// specify a table name
queryBuilder.setTables(NOTES_TABLE_NAME);

// use the notid to put a where clause
queryBuilder.appendWhere(Notes._ID + "=" + noteId);
```

可以使用两种方法之一来查询 ID 为 23 的笔记：

```java
// URI method
mangedQuery("content://com.google.provider.NotePad/notes/23",
           null,
           null,
           null,
           null);
```

或

```java
// explicit where clause
managedQuery("content://com.google.provider.NotePad/notes",
            null,
            "_id=?",
            new String[] { "23" },
            null);
```

**6. 插入记录**

下面这个例子展示了在 `ContentValues` 中填充单行笔记，为插入做准备：

```java
ContentValues values = new ContentValues();
values.put("title", "New note");
values.put("note", "This is a new note");

// values object is now ready to be inserted
```

可以请求 `Activity` 类来获取对 `ContentResolver` 的引用：

```java
ContentResolver contentResolver = activity.getContentResolver();
```

可以使用此 URI 和我们所拥有的 ContentValues，然后进行调用来插入该行：

```java
Uri uri = contentResolver.insert(NotePad.Notes.CONTENT_URI, values);
```

**7. 将文件添加到 ContentProvider 中**

有时，可能需要将文件存储到数据库中，常见的方法时将文件保存到磁盘，然后更新数据库中指向响应文件名的记录。

`Android` 借鉴了此协议，并通过定义一个具体过程来保存和检索文件，自动化了这一过程。`Android` 使用了一种约定，那就是使用保留的列名 `_data` 将对文件名的引用保存在记录中。

当将记录插入该表时，`Android` 向调用方返回 URI。使用此机制保存记录之后，还需要将文件保存在该位置。为此，`Android` 允许 `ContentResolver` 获取数据库记录的 Uri，然后返回可写的输出流。在后台，`Android` 会分配一个内部文件，并将对该文件名的引用存储在 `_data` 字段中。

如果要扩展 `NotePad` 示例来存储给定笔记的图像，可以创建另一个名为 `_data` 的列，并首先运行一次插入来取回 URI。以下代码颜色协议的这一部分：

```java
ContentValues values = new ContentValues();
values.put("title", "New note");
vlaues.put("note", "This is a new note");

// Use a content resolver to insert the record
ContentResolver contentResolver = activity.getContentResolver();
Uri newUri = contentResolver.insert(NotePad.Notes.CONTENT_URI, values);
```

拥有了记录的 URI 之后，以下代码告诉 ContentResolver 获取对文件输出流的引用：

```java
......
// Use the content resolver to get an output stream directly
// ContentResolver hides the access to the _data field where
// it stores the real file reference.
OutputStream outStream = activity.getContentResolver().openOutputStream(newUri);
someSourceBitmap.compress(Bitmap.CompressFormat.JPEG, 50, outStream);
outStream.close();
```

**8. 更新和删除**

执行更新类似于执行插入，在更新时，通过 ContentValues 对象传递更改的列值。下面是 ContentResolver 对象上一个更新方法的签名：

```java
int numberOfRowsUpdated = activity.getContentResolver().update(Uri uri,
                                                              ContentValues values,
                                                              String whereClause,
                                                              String[] selectionArgs)
```

whereCause 参数将强制对有关的行进行更新。类似地，删除方法的签名为：

```java
int numberOfRowsDeleted = activity.getContentResolver().delete(Uri uri,
                                                              String whereClause,
                                                              String[] selectionArgs)
```

