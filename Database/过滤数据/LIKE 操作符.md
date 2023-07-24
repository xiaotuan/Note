[toc]

为了搜索子句中使用通配符，必须使用 `LIKE` 操作符。`LIKE` 指示 `DBMS` ，后跟的搜索模式利用通配符匹配而不是简单的相等匹配进行比较。

通配符搜索只能用于文本字段，非文本数据类型字段不能使用通配符搜索。

### 1. 百分号（%）通配符

在搜索串中，`%` 表示任何字符出现任意次数。

```sql
mysql> SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE 'Fish%';
+---------+-------------------+
| prod_id | prod_name         |
+---------+-------------------+
| BNBG01  | Fish bean bag toy |
+---------+-------------------+
1 row in set (0.00 sec)
```

通配符可在任意位置使用，并且可以使用多个通配符。

```sql
mysql> SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '%bean bag%';
+---------+---------------------+
| prod_id | prod_name           |
+---------+---------------------+
| BNBG01  | Fish bean bag toy   |
| BNBG02  | Bird bean bag toy   |
| BNBG03  | Rabbit bean bag toy |
+---------+---------------------+
3 rows in set (0.00 sec)
```

> 注意：除了能匹配一个或多个字符外，`%` 还能匹配 0 个字符。

> 注意：有些 DBMS 用空格来填补字段的内容。例如，如果某列有 50 个字符，而存储的文本为 `Fish bean bag toy` （17 个字符），则为填满该列需要再文本后附加 33 个空格。子句 `WHERE prod_name LIKE 'F%y'` 只匹配以 `F` 开头、以 `y` 结尾的 `prod_name`。如果值后面跟空格则不是以 `y` 结尾，所以 `Fish bean bag toy` 就不会检索出来。简单的办法是给搜索模式再增加一个 `%` 号：`F%y%` 还匹配 `y` 之后的字符（或空格）。更好的解决办法是用函数去掉空格。

> 注意：通配符 `%` 看起来像是可以匹配任何东西，但有个例外，这就是 `NULL`。

### 2. 下划线（ _ ） 通配符

下划线通配符只匹配单个字符，而不是多个字符：

```sql
mysql> SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '__ inch teddy bear';
+---------+--------------------+
| prod_id | prod_name          |
+---------+--------------------+
| BR02    | 12 inch teddy bear |
| BR03    | 18 inch teddy bear |
+---------+--------------------+
2 rows in set (0.00 sec)
```

> 注意：DB2 不支持通配符 `_`。

### 3. 方括号（ [ ] ）通配符

方括号（ `[]` ） 通配符用来指定一个字符集，它必须匹配指定位置（通配符的位置）的一个字符。

```sql
mysql> SELECT cust_contact FROM Customers WHERE cust_cantact LIKE '[JM]%' ORDER BY cust_contact;
```

> 注意：并不是所有 `DBMS` 都支持用来创建集合的 `[]`。微软的 `SQL Server` 支持集合，但是 `MySQL`、`Oracle`、`DB2`、`SQLite` 都不支持。

> 提示：此通配符可以用前缀字符 `^` 来否定。
>
> ```sql
> mysql> SELECT cust_contact FROM Customers WHERE cust_cantact LIKE '[^JM]%' ORDER BY cust_contact;
> ```
>
> 当然，也可以使用 `NOT` 操作符：
>
> ```sql
> mysql> SELECT cust_contact FROM Customers WHERE NOT cust_cantact LIKE '[JM]%' ORDER BY cust_contact;
> ```



