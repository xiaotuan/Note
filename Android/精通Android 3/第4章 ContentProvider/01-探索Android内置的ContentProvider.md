`Android` 中存在大量的内置 `ContentProvider`，它们记录在 SDK 的 `android.provider` Java 包中。可以在以下网址查看这些 `ContentProvider` 的列表：

<https://developer.android.google.cn/reference/android/provider/package-summary.html>

下面给出了该文档页上列出的部分 `ContentProvider`：

```
Browser
CallLog
Contacts
	People
	Phones
	Photos
	Groups
MediaStore
	Audio
		Albums
		Artists
		Genres
		Playlists
	Images
		Thumbnails
	video
Settings
```

在 `Android` 的 `shell` 提示符下键入以下命令，可以看到 `shell` 中可用的命令集：

```shell
$ ls /system/bin
```

可以使用如下命令列出设备中所有 `*.db` 文件：

```shell
$ find . -iname *.db 2>/dev/null
```

如果设备中没有 `find` 命令，可以使用如下命令替代：

```shell
$ ls -R /data/data/*/databases
```

通过在 `adb shell ` 内部键入以下命令，可以在这些数据库上调用 `sqlite3`：

```shell
$ sqlite3 /data/data/com.android.providers.contacts/databases/contacts2.db
```

可以键入以下命令退出 `sqlite3`：

```shell
sqlite> .exit
```

访问 <http://www.sqlite.org/sqlite.html> ，可以看到各种 `sqlite3` 命令。

键入以下命令可以查看到一组表：

```shell
sqlite> .tables
```

以下命令行将输出 contacts2.db 中的 calls 表的 create 语句：

```shell
sqlite> .schema people
```

下面的示例 SQL 语句可以帮助你快速了解 SQLite 数据库：

```shell
// Set the column headers to show in the tool
sqlite> .headers on

// select all rows from a table
select * from table1;

// count the number of rows in a table
select count(*) from table1;

// select a specific set of columns
select col1, col2 from table1;

// Selectdistinct values in a column
select distinct col1 from table1;

// counting the distinct values
select count(col1) from (select distinct col1 from table1);

// group by 
select count(*), col1 from table1 group by col1;

// regular inner join
select * from table1 t1, table2 t2 where t1.col1 = t2.col1;

// left outer join
// Give me everything in t1 even though there are no rows in t2
select * from table t1 left outer join table2 t2 on t1.col1 = t2.col1 where ...
```



