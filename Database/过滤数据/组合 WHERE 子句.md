`SQL` 允许给出多个 `WHERE` 子句。这些子句有两种使用方式，即以 `AND` 子句或 `OR` 子句的方式使用。

### 1. AND 操作符

要通过不止一个列进行过滤，可以使用 `AND` 操作符给 `WHERE` 子句附加条件。

```sql
mysql> SELECT prod_id, prod_price, prod_name FROM Products WHERE vend_id = 'DLL01' AND prod_price <= 4;
+---------+------------+---------------------+
| prod_id | prod_price | prod_name           |
+---------+------------+---------------------+
| BNBG01  |       3.49 | Fish bean bag toy   |
| BNBG02  |       3.49 | Bird bean bag toy   |
| BNBG03  |       3.49 | Rabbit bean bag toy |
+---------+------------+---------------------+
3 rows in set (0.00 sec)
```

可以增加多个过滤添加，每个条件间都要使用 `AND` 关键字。

如果需要使用 `ORDER BY` 子句进行排序，它应该放在 `WHERE` 子句之后。

### 2. OR 操作符

`OR` 操作符与 AND 操作符正好相反，它指示 `DBMS` 检索匹配任一条件的行。事实上，许多 `DBMS` 在 `OR WHERE` 子句的第一个条件得到满足的情况下，就不再计算第二个条件了。

```sql
mysql> SELECT prod_id, prod_price, prod_name FROM Products WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';
+---------+------------+---------------------+
| prod_id | prod_price | prod_name           |
+---------+------------+---------------------+
| BNBG01  |       3.49 | Fish bean bag toy   |
| BNBG02  |       3.49 | Bird bean bag toy   |
| BNBG03  |       3.49 | Rabbit bean bag toy |
| BR01    |       5.99 | 8 inch teddy bear   |
| BR02    |       8.99 | 12 inch teddy bear  |
| BR03    |      11.99 | 18 inch teddy bear  |
| RGAN01  |       4.99 | Raggedy Ann         |
+---------+------------+---------------------+
7 rows in set (0.00 sec)
```

