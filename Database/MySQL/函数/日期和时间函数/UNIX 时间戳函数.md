`UNIX_TIMESTAMP(date)` 若无参数调用，则返回一个 `UNIX` 时间戳（'1970-01-01 00:00:00' GMT 之后的秒数）作为无符号整数。其中， GMT（ Green wich mean time ）为格林尼治时间。若用 `date` 来调用 `UNIX_TIMESTAMP()`，它会将参数值以 '1970-01-01 00:00:00' GMT 后的秒数的形式返回。`date` 可以是一个 `DATE` 字符串、`DATETIME` 字符串、`TIMESTAMP` 或一个当地时间的 `YYMMDD` 或 `YYYYMMDD` 格式的数字。

```sql
mysql> SELECT UNIX_TIMESTAMP(), UNIX_TIMESTAMP(NOW()), NOW();
+------------------+-----------------------+---------------------+
| UNIX_TIMESTAMP() | UNIX_TIMESTAMP(NOW()) | NOW()               |
+------------------+-----------------------+---------------------+
|       1691371765 |            1691371765 | 2023-08-07 09:29:25 |
+------------------+-----------------------+---------------------+
1 row in set (0.00 sec)
```

`FORM_UNIXTIME(date)` 函数把 UNIX 时间戳转换为普通格式的时间，与 `UNIX_TIMESTAMP(date)` 函数互为反函数。

```sql
mysql> SELECT FROM_UNIXTIME('1691371765');
+-----------------------------+
| FROM_UNIXTIME('1691371765') |
+-----------------------------+
| 2023-08-07 09:29:25.000000  |
+-----------------------------+
1 row in set (0.00 sec)
```

