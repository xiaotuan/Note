

DDL是数据定义语言的缩写，简单来说，就是对数据库内部的对象进行创建、删除、修改等操作的语言。它和DML语句的最大区别是DML只是对表内部数据操作，而不涉及表的定义、结构的修改，更不会涉及其他对象。DDL 语句更多地由数据库管理员（DBA）使用，开发人员一般很少使用。

下面通过一些例子来介绍MySQL中常用DDL语句的使用方法。

**1．创建数据库**

启动MySQL服务之后，输入以下命令连接到MySQL服务器：

[mysql@db3～]$ mysql -uroot -p

Enter password:

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 7344941 to server version: 5.1.9-beta-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>

在以上命令行中，mysql 代表客户端命令，“-u”后面跟连接的数据库用户，“-p”表示需要输入密码。

如果数据库设置正常，并输入了正确的密码，将看到上面一段欢迎界面和一个“mysql>”提示符。在欢迎界面中说明了以下几部分内容。

命令的结束符，用“;”或者“\g”结束。

客户端的连接ID，这个数字记录了MySQL服务到目前为止的连接次数；每个新连接都会自动加1，本例中是7344941。

MySQL 服务器的版本，本例中是“5.1.9-beta-log”，说明是 5.1.9 的测试版；如果是标准版，则会用standard代替beta。

通过“help;”或者“\h”命令来显示帮助内容，通过“\c”命令来清除命令行buffer。

在mysql>提示符后面输入所要执行的SQL语句，每个SQL语句以分号（；）或者“\g”结束，按回车键执行。

因为所有的数据都存储在数据库中，因此需要学习的第一个命令是创建数据库，语法如下所示：

CREATE DATABASE dbname

例如，创建数据库test1，命令执行如下：

mysql> create database test1;

Query OK, 1 row affected (0.00 sec)

可以发现，执行完创建命令后，下面有一行提示“Query OK, 1 row affected (0.00 sec)”，这段提示可以分为 3部分。“Query OK”表示上面的命令执行成功。读者可能奇怪，又不是执行查询操作，为什么显示查询成功？其实这是MySQL的一个特点，所有的DDL和DML（不包括 SELECT）操作执行成功后都显示“Query OK”，这里理解为执行成功就可以了。“1 row affected”表示操作只影响了数据库中一行的记录，“0.00 sec”则记录了操作执行的时间。

如果已经存在这个数据库，系统会提示：

mysql> create database test1;

ERROR 1007 (HY000): Can't create database 'test1'; database exists

这个时候，如果需要知道系统中都存在哪些数据库，可以用以下命令来查看：

mysql> show databases;

+--------------------+

| Database|

+--------------------+

| information_schema |

| cluster |

| mysql |

| test|

| test1|

+--------------------+

5 rows in set (0.00 sec)

可以发现，在上面的列表中除了刚刚创建的 test1 外，还有另外 4 个数据库，它们都是安装MySQL时系统自动创建的，其各自功能如下。

information_schema：主要存储了系统中的一些数据库对象信息，比如用户表信息、列信息、权限信息、字符集信息、分区信息等。

cluster：存储了系统的集群信息。

mysql：存储了系统的用户权限信息。

test：系统自动创建的测试数据库，任何用户都可以使用。

在查看了系统中已有的数据库后，可以用如下命令选择要操作的数据库：

USE dbname

例如，选择数据库test1：

mysql> use test1

Database changed

然后再用以下命令来查看test1数据库中创建的所有数据表：

mysql> show tables;

Empty set (0.00 sec)

由于 test1是刚创建的数据库，还没有表，所以显示为空。命令行下面的“Empty set”表示操作的结果集为空。如果查看一下mysql数据库里面的表，则可以得到以下信息：

mysql> use mysql Database changed

mysql> show tables;

+---------------------------+

| Tables_in_mysql|

+---------------------------+

| columns_priv|

| db|

| event|

| func|

| general_log|

| help_category|

| help_keyword|

| help_relation |

| help_topic |

| host|

| plugin|

| proc|

| procs_priv|

| slow_log|

| tables_priv |

| time_zone |

| time_zone_leap_second|

| time_zone_name|

| time_zone_transition|

| time_zone_transition_type |

| user|

+---------------------------+

21 rows in set (0.00 sec)

**2．删除数据库**

删除数据库的语法很简单，如下所示：

drop database dbname;

例如，要删除test1数据库可以使用以下语句：

mysql> drop database test1;

Query OK, 0 rows affected (0.00 sec)

可以发现，提示操作成功后，后面却显示了“0 rows affected”，这个提示可以不用管它，在MySQL里面，drop语句操作的结果都是显示“0 rows affected”。

**注意：**数据库删除后，下面的所有表数据都会全部删除，所以删除前一定要仔细检查并做好相应备份。

**3．创建表**

在数据库中创建一张表的基本语法如下：

CREATE TABLE tablename (

column_name_1 column_type_1 constraints,

column_name_2 column_type_2 constraints,

…

column_name_n column_type_n constraints）

因为MySQL的表名是以目录的形式存在于磁盘上的，所以表名的字符可以用任何目录名允许的字符。column_name是列的名字；column_type是列的数据类型；constraints是这个列的约束条件，在后面的章节中会详细介绍。

例如，创建一个名称为 emp 的表。表中包括 ename（姓名）、hiredate（雇用日期）和 sal （薪水）3个字段，字段类型分别为varchar(10)、date、int(2)（关于字段类型将会在下一章中介绍）：

mysql> create table emp(ename varchar(10),hiredate date,sal decimal(10,2),deptno int(2));

Query OK, 0 rows affected (0.02 sec)

表创建完毕后，如果需要查看一下表的定义，可以使用如下命令：

DESC tablename

例如，查看emp表，将输出以下信息：

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename | varchar(10) | YES | | | |

| hiredate | date | YES | | | |

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

+----------+---------------+------+-----+---------+-------+

4 rows in set (0.00 sec)

虽然desc命令可以查看表定义，但是其输出的信息还是不够全面。为了得到更全面的表定义信息，有时就需要查看创建表的SQL语句，可以使用如下命令查看：

mysql> show create table emp \G;

*************************** 1. row ***************************

Table: emp

Create Table: CREATE TABLE 'emp' (

'ename' varchar(20) DEFAULT NULL,

'hiredate' date DEFAULT NULL,

'sal' decimal(10,2) DEFAULT NULL,

'deptno' int(2) DEFAULT NULL,

KEY 'idx_emp_ename' ('ename')

) ENGINE=InnoDB DEFAULT CHARSET=gbk

1 row in set (0.02 sec)

ERROR:

No query specified

mysql>

从上面创建表的SQL语句中，除了可以看到表定义以外，还可以看到表的engine（存储引擎）和 charset（字符集）等信息。“\G”选项的含义是使得记录能够按照字段竖向排列，以便更好地显示内容较长的记录。

**4．删除表**

表的删除命令如下：

DROP TABLE tablename

例如，要删除数据库emp可以使用以下命令：

mysql> drop table emp;

Query OK, 0 rows affected (0.00 sec)

**5．修改表**

对于已经创建好的表，尤其是已经有大量数据的表，如果需要做一些结构上的改变，可以先将表删除（drop），然后再按照新的表定义重建表。这样做没有问题，但是必然要做一些额外的工作，比如数据的重新加载。而且，如果有服务在访问表，也会对服务产生影响。

因此，在大多数情况下，表结构的更改都使用 alter table语句，以下是一些常用的命令。

（1）修改表类型，语法如下：

ALTER TABLE tablename MODIFY [COLUMN] column_definition [FIRST | AFTER col_name]

例如，修改表emp的ename字段定义，将varchar(10)改为varchar(20)：

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field| Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename | varchar(10) | YES | | | |

| hiredate | date | YES ||||

| sal| decimal(10,2) | YES ||||

| deptno | int(2)| YES ||||

+----------+---------------+------+-----+---------+-------+

4 rows in set (0.00 sec)

mysql> alter table emp modify ename varchar(20);

Query OK, 0 rows affected (0.03 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field| Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename | varchar(20) | YES | | | |

| hiredate | date | YES | | | |

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

+----------+---------------+------+-----+---------+-------+

4 rows in set (0.00 sec)

（2）增加表字段，语法如下：

ALTER TABLE tablename ADD [COLUMN] column_definition [FIRST | AFTER col_name]

例如，在表emp中新增加字段age，类型为int(3)：

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field| Type| Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename | varchar(20) | YES | | | |

| hiredate | date | YES | | | |

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

+----------+---------------+------+-----+---------+-------+

4 rows in set (0.00 sec)

mysql> alter table emp add column age int(3);

Query OK, 0 rows affected (0.03 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename| varchar(20) | YES ||||

| hiredate | date | YES | | | |

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

| age | int(3) | YES | | | |

+----------+---------------+------+-----+---------+-------+

5 rows in set (0.00 sec)

（3）删除表字段，语法如下：

ALTER TABLE tablename DROP [COLUMN] col_name

例如，将字段age删除掉：

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename | varchar(20) | YES | | | |

| hiredate | date | YES | | | |

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

| age | int(3) | YES | | | |

+----------+---------------+------+-----+---------+-------+

5 rows in set (0.00 sec)

mysql> alter table emp drop column age;

Query OK, 0 rows affected (0.04 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field| Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename| varchar(20) | YES ||||

| hiredate | date| YES ||||

| sal| decimal(10,2) | YES ||||

| deptno | int(2)| YES ||||

+----------+---------------+------+-----+---------+-------+

4 rows in set (0.00 sec)

（4）字段改名，语法如下：

ALTER TABLE tablename CHANGE [COLUMN] old_col_name column_definition

[FIRST|AFTER col_name]

例如，将age改名为age1，同时修改字段类型为int(4)：

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename| varchar(20) | YES ||||

| hiredate | date | YES ||||

| sal| decimal(10,2) | YES ||||

| deptno | int(2)| YES ||||

| age | int(3) | YES | | | |

+----------+---------------+------+-----+---------+-------+

mysql> alter table emp change age age1 int(4) ;

Query OK, 0 rows affected (0.02 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> desc emp

-> ;

+----------+---------------+------+-----+---------+-------+

| Field| Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename| varchar(20) | YES ||||

| hiredate | date | YES ||||

| sal| decimal(10,2) | YES ||||

| deptno | int(2) | YES | | | |

| age1 | int(4) | YES | | | |

+----------+---------------+------+-----+---------+-------+

5 rows in set (0.00 sec)

**注意：**change和modify都可以修改表的定义，不同的是change后面需要写两次列名，不方便。但是change的优点是可以修改列名称，modify则不能。

（5）修改字段排列顺序。

前面介绍的**字段增加和修改语法**（ADD/CHANGE/MODIFY）中，都有一个可选项first|after column_name，这个选项可以用来修改字段在表中的位置，ADD增加的新字段默认是加在表的最后位置，而CHANGE/MODIFY默认都不会改变字段的位置。

例如，将新增的字段 birth date加在 ename之后：

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field| Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename| varchar(20) | YES ||||

| hiredate | date | YES ||||

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

| age| int(3)| YES ||||

+----------+---------------+------+-----+---------+-------+

5 rows in set (0.00 sec)

mysql> alter table emp add birth date after ename;

Query OK, 0 rows affected (0.03 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| ename | varchar(20) | YES | | | |

| birth| date| YES ||||

| hiredate | date | YES | | | |

| sal| decimal(10,2) | YES ||||

| deptno | int(2) | YES | | | |

| age | int(3) | YES | | | |

+----------+---------------+------+-----+---------+-------+

6 rows in set (0.00 sec)

修改字段age，将它放在最前面：

mysql> alter table emp modify age int(3) first;

Query OK, 0 rows affected (0.03 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> desc emp;

+----------+---------------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| age | int(3) | YES | | | |

| ename | varchar(20) | YES | | | |

| birth | date | YES | | | |

| hiredate | date | YES | | | |

| sal | decimal(10,2) | YES | | | |

| deptno | int(2) | YES | | | |

+----------+---------------+------+-----+---------+-------+

6 rows in set (0.00 sec)

**注意：**CHANGE/FIRST|AFTER COLUMN这些关键字都属于MySQL在标准 SQL上的扩展，在其他数据库上不一定适用。

（6）更改表名，语法如下：

ALTER TABLE tablename RENAME [TO] new_tablename

例如，将表emp改名为emp1，命令如下：

mysql> alter table emp rename emp1;

Query OK, 0 rows affected (0.00 sec)

mysql> desc emp;

ERROR 1146 (42S02): Table 'sakila.emp' doesn't exist

mysql> desc emp1;

+----------+---------------+------+-----+---------+-------+

| Field| Type| Null | Key | Default | Extra |

+----------+---------------+------+-----+---------+-------+

| age| int(3)| YES ||||

| ename| varchar(20) | YES ||||

| birth| date | YES ||||

| hiredate | date | YES ||||

| sal| decimal(10,2) | YES ||||

| deptno | int(2)| YES ||||

+----------+---------------+------+-----+---------+-------+

6 rows in set (0.00 sec)



