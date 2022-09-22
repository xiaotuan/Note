[toc]

### 1. 安装 MySQL

```shell
$ sudo apt install mysql-client-5.7
$ sudo apt install mysql-server-5.7
```

### 2. 连接到服务器

默认情况下，如果你再命令行上输入 `mysql`，且不加任何参数，它会视图用 `Linux` 登录用户名连接运行在同一 `Linux` 系统上的 MySQL 服务器。

可以使用 `-u` 参数指定登录用户名，`-p` 参数告诉 `mysql` 程序提示输入登录用户输入密码：

```shell
$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.33-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

### 3. mysql 命令

`mysql` 程序使用两种不同类型的命令：

+ 特殊的 `mysql` 命令
+ 标准 SQL 语句

`mysql` 程序使用它自有的一组命令，方便你控制环境和提取关于 MySQL 服务器的信息。这些命令要么是全名（例如 status），要么是简写形式（例如 `\s`）：

```shell
mysql> \s
--------------
mysql  Ver 14.14 Distrib 5.7.33, for Linux (x86_64) using  EditLine wrapper

Connection id:		4
Current database:	
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		5.7.33-0ubuntu0.16.04.1 (Ubuntu)
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	latin1
Db     characterset:	latin1
Client characterset:	utf8
Conn.  characterset:	utf8
UNIX socket:		/var/run/mysqld/mysqld.sock
Uptime:			7 min 13 sec

Threads: 1  Questions: 5  Slow queries: 0  Opens: 107  Flush tables: 1  Open tables: 26  Queries per second avg: 0.011
--------------
```

`mysql` 程序实现了 MySQL 服务器支持的所有标准 SQL 命令：

```shell
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> USE mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| engine_cost               |
| event                     |
| func                      |
| general_log               |
| gtid_executed             |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| ndb_binlog_index          |
| plugin                    |
| proc                      |
| procs_priv                |
| proxies_priv              |
| server_cost               |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
31 rows in set (0.00 sec)
```

你会注意到，在每个命令后面我们都加了一个分号。在 MySQL 程序中，分号表明命令的结束。如果不用分号，它会提示输入更多数据。

> 说明：MySQL 程序支持用大写或小写字母来指定 SQL 命令。

### 4. 创建数据库

创建一个新的数据库要用如下 SQL 语句：

```shell
CREATE DATABASE name;
```

例如：

```shell
mysql> CREATE DATABASE mytest;
Query OK, 1 row affected (0.01 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| mytest             |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

### 5. 创建用户账户

可以用 `GRANT` SQL语句来窗口用户账户：

```shell
mysql> GRANT SELECT,INSERT,DELETE,UPDATE ON test.* TO test IDENTIFIED by 'test';
Query OK, 0 rows affected, 1 warning (0.00 sec)

```

第一部分定义了用户账户对数据库有哪些权限。这条语句允许用户查询数据库（select 权限）、插入新的数据记录以及删除和更新已有数据记录。

`test.*` 项定义了权限作用的数据库和表。这通过下面的格式指定：

```shell
database.table
```

最后，你可以指定这些权限应用于哪些用户账户。`grant` 命令的便利之处在于，如果用户账户不存在，它会创建。`identified by` 部分允许你为新用户账户设定默认密码。

可以直接在 mysql 程序中测试新用户账户。

```shell
$ mysql -u test -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7
Server version: 5.7.33-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

### 6. 创建数据表

要在数据库中新建一张新表，需要用 SQL 命令 `CREATE TABLE`：

```shell
mysql> CREATE TABLE employees (
    -> empid int not null,
    -> lastname varchar(30),
    -> firstname varchar(30),
    -> salary float,
    -> primary key (empid));
Query OK, 0 rows affected (0.00 sec)
```

<center><b>MySQL 的数据类型</b></center>

| 数据类型  | 描述                             |
| --------- | -------------------------------- |
| char      | 定长字符串值                     |
| varchar   | 变长字符串值                     |
| int       | 整数值                           |
| float     | 浮点值                           |
| boolean   | 布尔类型 true/false 值           |
| date      | YYYY-MM-DD 格式的日期值          |
| time      | HH:mm:ss 格式的时间值            |
| timestamp | 日期和时间值的组合               |
| text      | 字符串值                         |
| BLOB      | 大的二进制值，比如图片或视频剪辑 |

`empid` 数据字段还指定了一个**数据约束**。数据约束会限制输入什么类型数据可以创建一个有效记录。`not null` 数据约束指明每条记录都必须有一个指定的 `empid` 值。

最后，`primary key` 定义了可以唯一标识每条记录的数据字段。这以为这每条记录中在表中都必须有一个唯一的 empid 值。

```shell
mysql> SHOW TABLES;
+------------------+
| Tables_in_mytest |
+------------------+
| employees        |
+------------------+
1 row in set (0.00 sec)
```

### 7. 插入和删除数据

可以使用 SQL 命令的 `INSERT` 语句向表中插入新的记录。SQL 命令 `INSERT` 的格式如下：

```shell
INSERT INTO table VALUES (...)
```

每个数据字段的值都用逗号分开：

```shell
mysql> INSERT INTO employees VALUES (1, 'Blum', 'Rich', 25000.00);
Query OK, 1 row affected (0.01 sec)
mysql> INSERT INTO employees VALUES (2, 'Blum', 'Barbara', 45000.00);
Query OK, 1 row affected (0.00 sec)
```

如果你需要从表中删除数据，可以用 SQL 命令 `DELETE`。`DELETE` 命令的基本格式如下：

```shell
DELETE FROM table;
```

其中 table 指定了要从中删除记录的表。这个命令有个小问题：它会删除该表中所有记录。

要想只删除其中一条或多条数据行，必须用 `WHERE` 字句。`WHERE` 字句允许创建一个过滤器来指定删除哪些记录。可以像下面这样使用 `WHERE` 字句：

```shell
mysql> DELETE FROM employees WHERE empid = 2;
Query OK, 1 row affected (0.01 sec)
```

### 8. 查询数据

所有查询都是用 SQL 命令 `SELECT` 来完成。`SELECT` 语句的基本格式如下：

```shell
SELECT datafields FROM table
```

datafields 参数时一个用逗号分开的数据字段名称列表，指明了希望查询返回的字段。如果你要提取所有的数据字段值，可以用星号作为通配符。

```shell
mysql> SELECT * FROM employees;
+-------+----------+------------+--------+
| empid | lastname | firstname  | salary |
+-------+----------+------------+--------+
|     1 | Blum     | Rich       |  25000 |
|     2 | Blum     | Barbara    |  45000 |
|     3 | Blum     | Katie Jane |  34500 |
|     4 | Blum     | Jessica    |  52340 |
+-------+----------+------------+--------+
4 rows in set (0.00 sec)
```

可以用一个或多个修饰符定义数据库服务器如何返回查询数据。下面列出了常用的修饰符：

+ `WHERE`：显示符合特定条件的数据行子集。
+ `ORDER BY`：以指定顺序显示数据行。
+ `LIMIT`：只显示数据行的一个子集。

下面是一个使用 `WHERE` 子句的例子：

```shell
mysql> SELECT * FROM employees WHERE salary > 40000;
+-------+----------+-----------+--------+
| empid | lastname | firstname | salary |
+-------+----------+-----------+--------+
|     2 | Blum     | Barbara   |  45000 |
|     4 | Blum     | Jessica   |  52340 |
+-------+----------+-----------+--------+
2 rows in set (0.00 sec)
```

