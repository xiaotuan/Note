`LAST_INSERT_ID()` 函数返回最后生成的 `AUTO_INCREMENT` 值。

```sql
mysql> CREATE TABLE worker (Id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, Name VARCHAR(30));
Query OK, 0 rows affected (0.04 sec)

mysql> INSERT INTO worker VALUES(NULL, 'Jimy');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO worker VALUES(NULL, 'Tom');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM worker;
+----+------+
| Id | Name |
+----+------+
|  1 | Jimy |
|  2 | Tom  |
+----+------+
2 rows in set (0.00 sec)

mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                2 |
+------------------+
1 row in set (0.00 sec)
```

可以看到，一次插入一条记录时，返回值为最后一条插入记录的 `Id` 值。

```sql
mysql> INSERT INTO worker VALUES(NULL, 'Kevin'), (NULL, 'Michal'), (NULL, 'Nick');
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM worker;
+----+--------+
| Id | Name   |
+----+--------+
|  1 | Jimy   |
|  2 | Tom    |
|  3 | Kevin  |
|  4 | Michal |
|  5 | Nick   |
+----+--------+
5 rows in set (0.00 sec)

mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                3 |
+------------------+
1 row in set (0.00 sec)
```

一次同时插入多条记录，`LAST_INSERT_ID` 值不是 5 而是 3。这是因为当使用一条 `INSERT` 语句插入多行时，`LAST_INSERT_ID()` 只返回插入的第一行数据时产生的值，在这里为第 3 条记录。

> 提示：`LAST_INSERT_ID` 是与数据表无关的，如果向表 a 插入数据后再向表 b 插入数据，那么 `LAST_INSERT_ID` 只返回表 b 中的 `Id` 值。