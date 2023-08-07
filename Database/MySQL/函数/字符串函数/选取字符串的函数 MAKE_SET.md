`MAKE_SET(x, s1, s2, ..., sn)` 函数按 `x` 的二进制数从 `s1, s2, ..., sn` 中选取字符串。

```sql
mysql> SELECT MAKE_SET(1, 'a', 'b', 'c') as col1, MAKE_SET(1 | 4, 'hello', 'nice', 'world') as col2, MAKE_SET(1 | 4, 'hello', 'nice', NULL, 'world') as col3, MAKE_SET(0, 'a', 'b', 'c') as col4;
+------+-------------+-------+------+
| col1 | col2        | col3  | col4 |
+------+-------------+-------+------+
| a    | hello,world | hello |      |
+------+-------------+-------+------+
1 row in set (0.00 sec)
```

1 的二进制值为 0001，4 的二进制值为 0100，1 与 4 进行或操作之后的二进制值为 0101，从右到左第 1 位和第 3 位为 1。`MAKE_SET(1, 'a', 'b', 'c')` 返回第 1 个字符串；`MAKE_SET(1 | 4, 'hello', 'nice', 'world')` 返回从左端开始第 1 个和第 3 个字符串组成的字符串；`NULL` 不会添加到结果中，因此 `MAKE_SET(1 | 4, 'hello', 'nice', NULL, 'world')` 只返回第 1 个字符串 `hello`。