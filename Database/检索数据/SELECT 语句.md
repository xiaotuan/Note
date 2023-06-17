[toc]

### 1. 检索单个列

简单检索单个列的语法如下：

```sql
SELECT 列名 FROM 表名;
```

例如：

```shell
mysql> SELECT prod_name FROM Products;
+---------------------+
| prod_name           |
+---------------------+
| Fish bean bag toy   |
| Bird bean bag toy   |
| Rabbit bean bag toy |
| 8 inch teddy bear   |
| 12 inch teddy bear  |
| 18 inch teddy bear  |
| Raggedy Ann         |
| King doll           |
| Queen doll          |
+---------------------+
9 rows in set (0.00 sec)
```

### 2. 检索多个列

要想从一个表中检索多个列，仍然使用相同的 `SELECT` 语句。唯一的不同是必须在 `SELECT` 关键字后给出多个列名，列名之间以逗号分隔。

> 提示：在选择多个列时，一定要在列名之间加上逗号，但最后一个列名后不加。如果在最后一个列名后加了逗号，将出现错误。

语法如下：

```sql
SELECT 列名1, 列名2, ..., 列名n FROM 表名;
```

例如：

```shell
mysql> SELECT prod_id, prod_name, prod_price FROM Products;
+---------+---------------------+------------+
| prod_id | prod_name           | prod_price |
+---------+---------------------+------------+
| BNBG01  | Fish bean bag toy   |       3.49 |
| BNBG02  | Bird bean bag toy   |       3.49 |
| BNBG03  | Rabbit bean bag toy |       3.49 |
| BR01    | 8 inch teddy bear   |       5.99 |
| BR02    | 12 inch teddy bear  |       8.99 |
| BR03    | 18 inch teddy bear  |      11.99 |
| RGAN01  | Raggedy Ann         |       4.99 |
| RYL01   | King doll           |       9.49 |
| RYL02   | Queen doll          |       9.49 |
+---------+---------------------+------------+
9 rows in set (0.00 sec)
```

### 3. 检查所有列

在实际列名的位置使用星号（`*`）通配符可以检索所有的列而不必逐个列出它们。语法如下：

```sql
SELECT * FROM 表名;
```

> 注意：一般而言，除非你确实需要表中的每一列，否则最好别使用 `*` 通配符。虽然使用通配符能让你自己省事，不用明确列出所需列，但检索不需要的列通常会降低检索速度和应用程序的性能。

> 提示：使用通配符有一个大优点，由于不明确指定列名，所以能检索出名字未知的列。

例如：

```sql
mysql> SELECT * FROM Products;
+---------+---------+---------------------+------------+-----------------------------------------------------------------------+
| prod_id | vend_id | prod_name           | prod_price | prod_desc                                                             |
+---------+---------+---------------------+------------+-----------------------------------------------------------------------+
| BNBG01  | DLL01   | Fish bean bag toy   |       3.49 | Fish bean bag toy, complete with bean bag worms with which to feed it |
| BNBG02  | DLL01   | Bird bean bag toy   |       3.49 | Bird bean bag toy, eggs are not included                              |
| BNBG03  | DLL01   | Rabbit bean bag toy |       3.49 | Rabbit bean bag toy, comes with bean bag carrots                      |
| BR01    | BRS01   | 8 inch teddy bear   |       5.99 | 8 inch teddy bear, comes with cap and jacket                          |
| BR02    | BRS01   | 12 inch teddy bear  |       8.99 | 12 inch teddy bear, comes with cap and jacket                         |
| BR03    | BRS01   | 18 inch teddy bear  |      11.99 | 18 inch teddy bear, comes with cap and jacket                         |
| RGAN01  | DLL01   | Raggedy Ann         |       4.99 | 18 inch Raggedy Ann doll                                              |
| RYL01   | FNG01   | King doll           |       9.49 | 12 inch king doll with royal garments and crown                       |
| RYL02   | FNG01   | Queen doll          |       9.49 | 12 inch queen doll with royal garments and crown                      |
+---------+---------+---------------------+------------+-----------------------------------------------------------------------+
9 rows in set (0.00 sec)
```

### 4. 检索不同的值

`SELECT` 语句返回所有匹配的行，例如：

```shell
mysql> SELECT vend_id, prod_price FROM Products;
+---------+------------+
| vend_id | prod_price |
+---------+------------+
| DLL01   |       3.49 |
| DLL01   |       3.49 |
| DLL01   |       3.49 |
| BRS01   |       5.99 |
| BRS01   |       8.99 |
| BRS01   |      11.99 |
| DLL01   |       4.99 |
| FNG01   |       9.49 |
| FNG01   |       9.49 |
+---------+------------+
9 rows in set (0.00 sec)
```

但是，如果你不希望每个值每次都出现，该怎么办呢？办法就是使用 `DISTINCT` 关键字，顾名思义，它指示数据库只返回不同的值，语法如下：

```sql
SELECT DISTINCT 列名 FROM 表名;
```

例如：

```shell
mysql> SELECT DISTINCT vend_id, prod_price FROM Products;
+---------+------------+
| vend_id | prod_price |
+---------+------------+
| DLL01   |       3.49 |
| BRS01   |       5.99 |
| BRS01   |       8.99 |
| BRS01   |      11.99 |
| DLL01   |       4.99 |
| FNG01   |       9.49 |
+---------+------------+
6 rows in set (0.00 sec)
```

> 注意：`DISTINCT` 关键字作用于所有的列，不仅仅是跟在其后的那一列。

### 5. 限制结果

`SELECT` 语句返回指定表中所有匹配的行，很可能是每一行。如果你只想返回第一行或者一定数量的行，该怎么办呢？

在 `SQL Server` 中使用 `SELECT` 时，可以用 `TOP` 关键字来显示最多返回多少行，语法如下：

```sql
SELECT TOP 限制的行数 列名 FROM Products;
```

> 注意：
>
> 1. `MySQL` 、`MariaDB`、`PostgreSQL` 或者 `SQLite` 限制查询结果数量语法
>
>    `MySQL` 使用 `LIMIT` 关键字限制查询结果，语法如下：
>
>    ```sql
>    SELECT 列名 FROM Products LIMIT 限制的行数;
>    ```
>
>    为了得到后面的 5 行数据，需要指定从哪儿开始以及检索的行数，例如：
>
>    ```sql
>    SELECT 列名 FROM 表名 LIMIT 限制数量 OFFSET 偏移数量;
>    ```
>
>    `LIMIT` 指定返回的行数，`LIMIT` 带的 `OFFSET` 指定从哪儿开始。
>
>    注意：第一个被检索的行是第 0 行，而不是第 1 行。
>
>    提示：在 `MySQL`、`MariaDB` 和 `SQLite` 可以使用另外一种语法：
>
>    ```sql
>    SELECT 列名 FROM 表名 LIMIT 偏移数量,限制数量;
>    ```
>
>    
>
> 2. `DB2` 限制查询结果语法
>
>    `DB2` 限制查询结果数量语法如下：
>
>    ```sql
>    SELECT 列名 FROM 表名 FETCH FIRST 限制数量 ROWS ONLY;
>    ```
>
> 3. `Oracle` 限制查询结果数量语法
>
>    `Oracle` 限制查询结果数量语法如下：
>
>    ```sql
>    SELECT 列名 FROM 表明 WHERE ROWNUM <= 限制数量;
>    ```
>
>    
>
> 

例如：

```shell
mysql> SELECT prod_name FROM Products LIMIT 5;
+---------------------+
| prod_name           |
+---------------------+
| Fish bean bag toy   |
| Bird bean bag toy   |
| Rabbit bean bag toy |
| 8 inch teddy bear   |
| 12 inch teddy bear  |
+---------------------+
5 rows in set (0.00 sec)
```

