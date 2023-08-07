`SUBSTRING(s, n, len)` 带有 `len` 参数的格式，从字符串 `s` 返回一个长度与 `len` 字符相同的子字符串，起始于位置 `n`。也可能对 `n` 使用一个负值。假若这样，则子字符串的位置起始于字符串结尾的 `n` 字符，即倒数第 `n` 个字符。

```sql
mysql> SELECT SUBSTRING('breakfast', 5) As col1, SUBSTRING('breakfast', 5, 3) AS col2, SUBSTRING('lunch', -3) AS col3, SUBSTRING('lunch', -5, 3) AS col4;
+-------+------+------+------+
| col1  | col2 | col3 | col4 |
+-------+------+------+------+
| kfast | kfa  | nch  | lun  |
+-------+------+------+------+
1 row in set (0.00 sec)
```

`MID(s, n, len)` 与 `SUBSTRING(s, n, len)` 的作用相同。

```sql
mysql> SELECT MID('breakfast', 5) As col1, MID('breakfast', 5, 3) AS col2, MID('lunch', -3) AS col3, MID('lunch', -5, 3) AS col4;+-------+------+------+------+
| col1  | col2 | col3 | col4 |
+-------+------+------+------+
| kfast | kfa  | nch  | lun  |
+-------+------+------+------+
1 row in set (0.01 sec)
```

> 提示：如果对 `len` 使用的是一个小于 1 的值，则结果始终为空字符串。