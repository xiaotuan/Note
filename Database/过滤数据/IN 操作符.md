`IN` 操作符用来指定条件范围，范围中的每个条件都可以进行匹配。`IN` 取一组由逗号分隔、括在圆括号中的合法值。

```sql
mysql> SELECT prod_name, prod_price FROM Products WHERE vend_id IN ('DLL01', 'BRS01') ORDER BY prod_name;
+---------------------+------------+
| prod_name           | prod_price |
+---------------------+------------+
| 12 inch teddy bear  |       8.99 |
| 18 inch teddy bear  |      11.99 |
| 8 inch teddy bear   |       5.99 |
| Bird bean bag toy   |       3.49 |
| Fish bean bag toy   |       3.49 |
| Rabbit bean bag toy |       3.49 |
| Raggedy Ann         |       4.99 |
+---------------------+------------+
7 rows in set (0.01 sec)
```

> 注意：`IN` 操作符后跟由逗号分隔的合法值，这些值必须括在圆括号中。

`IN` 操作符与 `OR` 操作符功能相同：

```sql
mysql> SELECT prod_name, prod_price FROM Products WHERE vend_id = 'DLL01' OR vend_id = 'BRS01' ORDER BY prod_name;
+---------------------+------------+
| prod_name           | prod_price |
+---------------------+------------+
| 12 inch teddy bear  |       8.99 |
| 18 inch teddy bear  |      11.99 |
| 8 inch teddy bear   |       5.99 |
| Bird bean bag toy   |       3.49 |
| Fish bean bag toy   |       3.49 |
| Rabbit bean bag toy |       3.49 |
| Raggedy Ann         |       4.99 |
+---------------------+------------+
7 rows in set (0.00 sec)
```

