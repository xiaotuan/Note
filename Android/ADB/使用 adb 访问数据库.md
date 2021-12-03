[toc]

> 提示：在 `user` 版本软件中没有 `sqlite3` 命令。

### 1. 进入 adb shell 环境

```shell
$ adb shell
```

### 2. 打开指定数据库文件

```shell
$ sqlite3 /data/data/<your-package-path>/databases/<your-database>.db
```

### 3. 执行 SQL 命令

```shell
sqlite> select * frome students;
```

### 4. 常用的命令

+ `.help`：查看帮助文档
+ `.tables`：显示数据库中的数据表列表
+ `.output FILENAME`：允许你将查询结果输出到指定文件中，便于分析。
+ `.mode MODE`：允许你指定输出格式，例如，`CSV`、`HTML` 等等
+ `SELECT * FROME table_name`：标准的查询指定表的所有栏数据
+ `SELECT * FROM table_name WHERE col = 'value'`：标准的查询语句，查询指定表中所有栏中 col 的值为 value 的栏集合
+ `SELECT col1, col2 FROM table_name`：标准查询语句，查询指定表中 col1 和 col2 栏的数据。