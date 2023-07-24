`WHERE` 子句中的 `NOT` 操作符有且只有一个功能，那就是否定其后所跟的任何条件。因为 `NOT` 从不单独使用，所以它的语法与其他操作符有所不同。`NOT` 关键字可以用在要过滤的列前，而不仅是在其后。

```sql
mysql> SELECT prod_name FROM Products WHERE NOT vend_id = 'DLL01' ORDER BY prod_name;
+--------------------+
| prod_name          |
+--------------------+
| 12 inch teddy bear |
| 18 inch teddy bear |
| 8 inch teddy bear  |
| King doll          |
| Queen doll         |
+--------------------+
5 rows in set (0.00 sec)
```

上面的例子也可以使用 `<>` 操作符来完成：

```sql
mysql> SELECT prod_name FROM Products WHERE vend_id <> 'DLL01' ORDER BY prod_name;
+--------------------+
| prod_name          |
+--------------------+
| 12 inch teddy bear |
| 18 inch teddy bear |
| 8 inch teddy bear  |
| King doll          |
| Queen doll         |
+--------------------+
5 rows in set (0.00 sec)
```

> 注意：`MariaDB` 支持使用 `NOT` 否定 `IN`、`BETWEEN` 和 `EXISTS` 子句。大多数 `DBMS` 允许使用 `NOT` 否定任何条件。