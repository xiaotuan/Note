`INSERT(s1, x, len, s2)` 返回字符串 `s1`，其子字符串起始于 `x` 位置和被字符串 `s2` 取代的 `len` 字符。如果 `x` 超过字符串长度，则返回值为原始字符串。假如 `len` 的长度大于其他字符串的长度，则从位置 `x` 开始替换。若任何一个参数为 `NULL`，则返回值为 `NULL`。

```sql
mysql> SELECT INSERT('Quest', 2, 4, 'What') As col1, INSERT('Quest', -1, 4, 'What') AS col2, INSERT('Quest', 3, 100, 'Wh') AS col3;
+-------+-------+------+
| col1  | col2  | col3 |
+-------+-------+------+
| QWhat | Quest | QuWh |
+-------+-------+------+
1 row in set (0.00 sec)
```

