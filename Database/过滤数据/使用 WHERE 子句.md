在 `SELECT` 语句中，数据根据 `WHERE` 子句中指定的搜索条件进行过滤。`WHERE` 子句在表名（`FROM` 子句）之后给出，如下所示：

```sql
mysql> SELECT prod_name, prod_price FROM Products WHERE prod_price= 3.49;
+---------------------+------------+
| prod_name           | prod_price |
+---------------------+------------+
| Fish bean bag toy   |       3.49 |
| Bird bean bag toy   |       3.49 |
| Rabbit bean bag toy |       3.49 |
+---------------------+------------+
3 rows in set (0.00 sec)
```

