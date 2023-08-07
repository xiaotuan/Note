`LEFT(s, n)` 返回字符串 `s` 开始的最左边 `n` 个字符。

```sql
mysql> SELECT LEFT('football', 5);
+---------------------+
| LEFT('football', 5) |
+---------------------+
| footb               |
+---------------------+
1 row in set (0.00 sec)
```

`RIGHT(s, n)` 返回字符串 `str` 最右边的 `n` 个字符。

```sql
mysql> SELECT RIGHT('football', 4);
+----------------------+
| RIGHT('football', 4) |
+----------------------+
| ball                 |
+----------------------+
1 row in set (0.00 sec)
```

