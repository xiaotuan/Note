`FIELD(s, s1, s2, ..., sn)` 返回字符串 `s` 在列表 `s1, s2, ..., sn` 中第一次出现的位置，在找不到 `s` 的情况下，返回值为 0。如果 `s` 为 `NULL`，则返回值为 0，原因是 `NULL` 不同任何值进行同等比较。

```sql
ysql> SELECT FIELD('Hi', 'hihi', 'Hey', 'Hi', 'bas') as col1, FIELD('Hi', 'Hey', 'Lo', 'Hilo', 'foo') as col2;
+------+------+
| col1 | col2 |
+------+------+
|    3 |    0 |
+------+------+
1 row in set (0.00 sec)
```

