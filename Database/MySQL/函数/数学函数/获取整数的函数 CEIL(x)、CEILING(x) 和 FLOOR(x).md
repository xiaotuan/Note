`CEIL(x)` 和 `CEILING(x)` 的意义相同，返回不小于 `x` 的最小整数值，返回值转化为一个 `BIGINT`。

```sql
mysql> SELECT CEIL(-3.35), CEILING(3.35);
+-------------+---------------+
| CEIL(-3.35) | CEILING(3.35) |
+-------------+---------------+
|          -3 |             4 |
+-------------+---------------+
1 row in set (0.00 sec)
```

`FLOOR(x)` 返回不大于 `x` 的最大整数值，返回值转化为一个 `BIGINT`。

```sql
mysql> SELECT FLOOR(-3.35), FLOOR(3.35);
+--------------+-------------+
| FLOOR(-3.35) | FLOOR(3.35) |
+--------------+-------------+
|           -4 |           3 |
+--------------+-------------+
1 row in set (0.00 sec)
```

