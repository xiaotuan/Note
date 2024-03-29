`DESCRIBE / DESC` 语句可以查看表的字段信息，其中包括字段名、字段数据类型、是否为主键、是否有默认值等。语法规则如下：

```
DESCRIBE 表名;
```

或者简写为：

```
DESC 表名;
```

例如：

```sql
mysql> DESC tb_emp8;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| name   | varchar(25) | NO   |     | NULL    |                |
| deptId | int(11)     | YES  |     | NULL    |                |
| salary | float       | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

其中，各个字段的含义分别解释如下：

+ `NULL`：表示该列是否可以存储 `NULL` 值。
+ `Key`：表示该列是否已编制索引。`PRI` 表示该列是表主键的一部分；`UNI` 表示该列是 `UNIQUE` 索引的一部分；`MUL` 表示在列中某个给定值允许出现多次。
+ `Default` ：表示该列是否有默认值，有的话指定值是多少。
+ `Extra`：表示可以获取的与给定列有关的附加信息，例如 `AUTO_INCREMENT` 等。

