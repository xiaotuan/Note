`REPEAT(s, n)` 返回一个由重复的字符串 `s` 组成的字符串，字符串 `s` 的数目等于 `n`。若 n <= 0 ，则返回一个空字符串。若 `s` 或 `n` 为 `NULL`，则返回 `NULL`。

```sql
mysql> SELECT REPEAT('mysql', 3);
+--------------------+
| REPEAT('mysql', 3) |
+--------------------+
| mysqlmysqlmysql    |
+--------------------+
1 row in set (0.00 sec)
```

