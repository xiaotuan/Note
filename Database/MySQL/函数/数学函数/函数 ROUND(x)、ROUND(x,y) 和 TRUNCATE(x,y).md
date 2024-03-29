`ROUND(x)` 返回最接近于参数 `x` 的整数，对 `x` 值进行四舍五入。

```sql
mysql> SELECT ROUND(-1.14), ROUND(-1.67), ROUND(1.14), ROUND(1.66);
+--------------+--------------+-------------+-------------+
| ROUND(-1.14) | ROUND(-1.67) | ROUND(1.14) | ROUND(1.66) |
+--------------+--------------+-------------+-------------+
|           -1 |           -2 |           1 |           2 |
+--------------+--------------+-------------+-------------+
1 row in set (0.00 sec)
```

`ROUND(x,y)` 返回最接近于参数 `x` 的数，其值保留到小数点后面 `y` 位，若 `y` 为负值，则将保留 `x` 值到小数点左边 `y` 位。

```sql
mysql> SELECT ROUND(1.38, 1), ROUND(1.38, 0), ROUND(232.38, -1), ROUND(232.38, -2);
+----------------+----------------+-------------------+-------------------+
| ROUND(1.38, 1) | ROUND(1.38, 0) | ROUND(232.38, -1) | ROUND(232.38, -2) |
+----------------+----------------+-------------------+-------------------+
|            1.4 |              1 |               230 |               200 |
+----------------+----------------+-------------------+-------------------+
1 row in set (0.00 sec)
```

> 提示：`y` 值为负数时，保留的小数点左边的相应位数直接保存为 0，不进行四舍五入。

`TRUNCATE(x,y)` 返回被舍去至小数点后 `y` 位的数字 `x`。若 `y` 的值为 0，则结果不带有小数点或不带有小数部分。若 `y` 设为负数，则截去（归零）`x` 小数点左起第 `y` 位开始后面所有低位的值。

```sql
mysql> SELECT TRUNCATE(1.31, 1), TRUNCATE(1.99, 1), TRUNCATE(1.99, 0), TRUNCATE(19.99, -1);
+-------------------+-------------------+-------------------+---------------------+
| TRUNCATE(1.31, 1) | TRUNCATE(1.99, 1) | TRUNCATE(1.99, 0) | TRUNCATE(19.99, -1) |
+-------------------+-------------------+-------------------+---------------------+
|               1.3 |               1.9 |                 1 |                  10 |
+-------------------+-------------------+-------------------+---------------------+
1 row in set (0.00 sec)
```

> 提示：`ROUND(x, y)` 函数在截取值的时候会四舍五入，而 `TRUNCATE(x, y)` 直接截取值，并不进行四舍五入。