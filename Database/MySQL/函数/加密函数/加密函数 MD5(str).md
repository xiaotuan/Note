`MD5(str)` 为字符串算出一个 `MD5` 128 比特校验和。该值以 32 位十六进制数字的二进制字符串形式返回，若参数为 `NULL`，则会返回 `NULL`。

```sql
mysql> SELECT MD5('mypwd');
+----------------------------------+
| MD5('mypwd')                     |
+----------------------------------+
| 318bcb4be908d0da6448a0db76908d78 |
+----------------------------------+
1 row in set (0.03 sec)
```

