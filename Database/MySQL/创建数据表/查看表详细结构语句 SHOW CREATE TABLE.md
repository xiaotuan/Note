 `SHOW CREATE TABLE` 语句可以用来显示创建表时的 `CREATE TABLE` 语句，语法格式如下：

```
SHOW CREATE TABLE <表名\G>;
```

> 提示：使用 `SHOW CREATE TABLE` 语句，不仅可以查看表创建时候的详细语句，还可以查看存储引擎和字符编码。

```sql
mysql> SHOW CREATE TABLE tb_emp3\G
*************************** 1. row ***************************
       Table: tb_emp3
Create Table: CREATE TABLE `tb_emp3` (
  `id` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `deptId` int(11) DEFAULT NULL,
  `salary` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)
```

如果不加 `\G` 参数，显示的结果可能非常混乱，加上参数 `\G` 之后，可以显示结果更加直观，易于查看。

例如：

```sql
mysql> SHOW CREATE TABLE tb_emp3;
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table   | Create Table                                                                                                                                                                                                     |
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tb_emp3 | CREATE TABLE `tb_emp3` (
  `id` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `deptId` int(11) DEFAULT NULL,
  `salary` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

