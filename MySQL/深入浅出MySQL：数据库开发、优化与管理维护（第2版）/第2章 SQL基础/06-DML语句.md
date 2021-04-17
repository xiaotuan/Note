+--------+------------+---------+--------+



DML 操作是指对数据库中表记录的操作，主要包括表记录的插入（ insert ）、更新（update）、删除（delete）和查询（select），是开发人员日常使用最频繁的操作。下面将依次对它们进行介绍。

**1．插入记录**

表创建好后，就可以往里插入记录了，插入记录的基本语法如下：

INSERT INTO tablename (field1,field2,…,fieldn) VALUES(value1,value2,…,valuen);

例如，向表emp中插入以下记录：ename为zzx1，hiredate为2000-01-01，sal为2000，deptno为1，命令执行如下：

mysql> insert into emp (ename,hiredate,sal,deptno) values('zzx1','2000-01- 01','2000',1);

Query OK, 1 row affected (0.00 sec)

也可以不用指定字段名称，但是values后面的顺序应该和字段的排列顺序一致：

mysql> insert into emp values('lisa','2003-02-01','3000',2);

Query OK, 1 row affected (0.00 sec)

含可空字段、非空但是含有默认值的字段、自增字段，可以不用在insert后的字段列表里面出现，values后面只写对应字段名称的value。这些没写的字段可以自动设置为NULL、默认值、自增的下一个数字，这样在某些情况下可以大大缩短SQL语句的复杂性。

例如，只对表中的ename和sal字段显式插入值：

mysql> insert into emp (ename,sal) values('dony',1000);

Query OK, 1 row affected (0.00 sec)

来查看一下实际插入值：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 100.00 |1|

| lisa | 2003-02-01 | 400.00 |2|

| bjguan | 2004-04-02 | 100.00 | 1 |

| dony | NULL | 1000.00 | NULL |

+--------+------------+---------+--------+

果然，设置为可空的两个字段都显示为NULL。在MySQL中，insert语句还有一个很好的特性，可以一次性插入多条记录，语法如下：

INSERT INTO tablename (field1, field2, …, fieldn)

VALUES

(record1_value1, record1_value2, …, record1_valuesn),

(record2_value1, record2_value2, …, record2_valuesn),

…

(recordn_value1, recordn_value2, …, recordn_valuesn)

;

可以看出，每条记录之间都用逗号进行了分隔。下面的例子中，对表dept一次插入两条记录：

mysql> insert into dept values(5,'dept5'),(6,'dept6');

Query OK, 2 rows affected (0.04 sec)

Records: 2 Duplicates: 0 Warnings: 0

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1 | tech|

| 2 | sale|

| 5 | fin |

| 5 | dept5 |

| 6 | dept6 |

+--------+----------+

5 rows in set (0.00 sec)

这个特性可以使得MySQL在插入大量记录时，节省很多的网络开销，大大提高插入效率。

**2．更新记录**

表里的记录值可以通过update命令进行更改，语法如下：

UPDATE tablename SET field1=value1,field2.=value2,…,fieldn=valuen [WHERE CONDITION]

例如，将表emp中ename为“lisa”的薪水（sal）从3000更改为4000：

mysql> update emp set sal=4000 where ename='lisa';

Query OK, 1 row affected (0.00 sec)

Rows matched: 1 Changed: 1 Warnings: 0

在MySQL中，update命令可以同时更新多个表中数据，语法如下：

UPDATE t1,t2,…,tn set t1.field1=expr1,tn.fieldn=exprn [WHERE CONDITION]

在下例中，同时更新表emp中的字段sal和表dept中的字段deptname：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal| deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 100.00 | 1|

| lisa | 2003-02-01 | 200.00 | 2|

| bjguan | 2004-04-02 | 100.00 | 1|

| dony | 2005-02-05 | 2000.00 | 4|

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1| tech|

| 2| sale|

| 5| fin|

+--------+----------+

3 rows in set (0.00 sec)

mysql> update emp a,dept b set a.sal=a.sal*b.deptno,b.deptname=a.ename where a.deptno=b.deptno;

Query OK, 3 rows affected (0.04 sec)

Rows matched: 5 Changed: 3 Warnings: 0

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal| deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 100.00 | 1|

| lisa | 2003-02-01 | 400.00 | 2|

| bjguan | 2004-04-02 | 100.00 | 1|

| dony | 2005-02-05 | 2000.00 | 4|

+--------+------------+---------+--------+

4 rows in set (0.01 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1 | zzx |

| 2 | lisa |

| 5 | fin |

+--------+----------+

3 rows in set (0.00 sec)

至此，两个表的数据同时进行了更新。

**注意：**多表更新的语法更多地用在了根据一个表的字段来动态地更新另外一个表的字段。

**3．删除记录**

如果记录不再需要，可以用delete命令进行删除，语法如下：

DELETE FROM tablename [WHERE CONDITION]

例如，在emp中将ename为“dony”的记录全部删除，命令如下：

mysql> delete from emp where ename='dony';

Query OK, 1 row affected (0.00 sec)

在MySQL中可以一次删除多个表的数据，语法如下：

DELETE t1,t2,…,tn FROM t1,t2,…,tn [WHERE CONDITION]

如果from后面的表名用别名，则delete后面也要用相应的别名，否则会提示语法错误。

在下例中，同时删除表emp和dept中deptno为3的记录：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 100.00 | 1 |

| lisa | 2003-02-01 | 200.00 | 2 |

| bjguan | 2004-04-02 | 100.00 | 1 |

| bzshen | 2005-04-01 | 300.00 | 3 |

| dony | 2005-02-05 | 2000.00 | 4 |

+--------+------------+---------+--------+

5 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1 | tech |

| 2 | sale |

| 3 | hr |

| 5 | fin |

+--------+----------+

4 rows in set (0.00 sec)

mysql> delete a,b from emp a,dept b where a.deptno=b.deptno and a.deptno=3;

Query OK, 2 rows affected (0.04 sec)

mysql>

mysql>

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 100.00 | 1|

| lisa | 2003-02-01 | 200.00 | 2|

| bjguan | 2004-04-02 | 100.00 | 1|

| dony | 2005-02-05 | 2000.00 | 4|

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1| tech|

| 2| sale|

| 5| fin|

+--------+----------+

3 rows in set (0.00 sec)

**注意：**不管是单表还是多表，不加where条件将会把表的所有记录删除，所以操作时一定要小心。

**4．查询记录**

数据插入到数据库中后，就可以用SELECT命令进行各种各样的查询，使得输出的结果符合用户的要求。SELECT的语法很复杂，这里只介绍最基本的语法：

SELECT * FROM tablename [WHERE CONDITION]

查询最简单的方式是将记录全部选出。在下面的例子中，将表emp中的记录全部查询出来：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 2000.00 | 1|

| lisa | 2003-02-01 | 4000.00 | 2|

| bjguan | 2004-04-02 | 5000.00 | 3|

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

其中“*”表示要将所有的记录都选出来，也可以用逗号分割的所有字段来代替，例如，以下两个查询是等价的：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 2000.00 | 1|

| lisa | 2003-02-01 | 4000.00 | 2|

| bjguan | 2004-04-02 | 5000.00 | 3|

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

mysql> select ename,hiredate,sal,deptno from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 3 |

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

“*”的好处是当需要查询所有字段信息时，查询语句很简单，但是只查询部分字段的时候，必须要将字段一个一个列出来。

上例中已经介绍了查询全部记录的语法，但是在实际应用中，用户还会遇到各种各样的查询要求，下面将分别介绍。

（1）查询不重复的记录。

有时需要将表中的记录去掉重复后显示出来，可以用distinct关键字来实现：

mysql> select ename,hiredate,sal,deptno from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 1 |

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

mysql> select distinct deptno from emp;

+--------+

| deptno |

+--------+

| 1 |

| 2 |

+--------+

2 rows in set (0.00 sec)

（2）条件查询。

在很多情况下，用户并不需要查询所有的记录，而只是需要根据限定条件来查询一部分数据，用where关键字可以来实现这样的操作。

例如，需要查询所有deptno为1的记录：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 1 |

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

mysql> select * from emp where deptno=1;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 2000.00 | 1|

| bjguan | 2004-04-02 | 5000.00 | 1|

+--------+------------+---------+--------+

2 rows in set (0.00 sec)

结果集中将符合条件的记录列出来。上面的例子中，where后面的条件是一个字段的=比较，除了=外，还可以使用>、<、>=、<=、!=等比较运算符；多个条件之间还可以使用 or、and 等逻辑运算符进行多条件联合查询，运算符会在以后的章节中详细讲解。

以下是一个使用多字段条件查询的例子：

mysql> select * from emp where deptno=1 and sal<3000;

+-------+------------+---------+--------+

| ename | hiredate | sal| deptno |

+-------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1|

+-------+------------+---------+--------+

1 row in set (0.00 sec)

（3）排序和限制。

我们经常会有这样的需求，取出按照某个字段进行排序后的记录结果集，这就用到了数据库的排序操作，用关键字ORDER BY来实现，语法如下：

SELECT * FROM tablename [WHERE CONDITION] [ORDER BY field1 [DESC|ASC]，field2 [DESC|ASC],…,fieldn [DESC|ASC]]

其中，DESC和ASC是排序顺序关键字，DESC表示按照字段进行降序排列，ASC则表示升序排列，如果不写此关键字默认是升序排列。ORDER BY后面可以跟多个不同的排序字段，并且每个排序字段可以有不同的排序顺序。

例如，把emp表中的记录按照工资高低进行显示：

mysql> select * from emp order by sal;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 2000.00 | 1|

| bzshen | 2005-04-01 | 3000.00 | 3|

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 1 |

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

如果排序字段的值一样，则值相同的字段按照第二个排序字段进行排序，依次类推。如果只有一个排序字段，则这些字段相同的记录将会无序排列。

例如，把emp表中的记录按照部门编号deptno字段排序：

mysql> select * from emp order by deptno;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| bjguan | 2004-04-02 | 5000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bzshen | 2005-04-01 | 4000.00 | 3 |

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

对于deptno相同的前两条记录，如果要按照工资由高到低排序，可以使用以下命令：

mysql> select * from emp order by deptno,sal desc;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| bjguan | 2004-04-02 | 5000.00 | 1 |

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bzshen | 2005-04-01 | 4000.00 | 3 |

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

对于排序后的记录，如果希望只显示一部分，而不是全部，这时，就可以使用LIMIT关键字来实现，LIMIT的语法如下：

SELECT …[LIMIT offset_start,row_count]

其中offset_start表示记录的起始偏移量，row_count表示显示的行数。

在默认情况下，起始偏移量为 0，只需要写记录行数就可以，这时，实际显示的就是前 n条记录。例如，显示emp表中按照sal排序后的前3条记录：

mysql> select * from emp order by sal limit 3;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bzshen | 2005-04-01 | 4000.00 | 3 |

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

如果要显示emp表中按照sal排序后从第二条记录开始的3条记录，可以使用以下命令：

mysql> select * from emp order by sal limit 1,3;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| lisa | 2003-02-01 | 4000.00 | 2 |

| bzshen | 2005-04-01 | 4000.00 | 3 |

| bjguan | 2004-04-02 | 5000.00 | 1|

+--------+------------+---------+--------+

3 rows in set (0.00 sec)

limit经常和 order by一起配合使用来进行记录的分页显示。

**注意：**limit属于MySQL扩展SQL92后的语法，在其他数据库上并不能通用。

（4）聚合。

很多情况下，用户都需要进行一些汇总操作，比如统计整个公司的人数或者统计每个部门的人数，这时就要用到SQL的聚合操作。

聚合操作的语法如下：

SELECT [field1,field2,…,fieldn] fun_name

FROM tablename

[WHERE where_contition]

[GROUP BY field1,field2,…,fieldn

[WITH ROLLUP]]

[HAVING where_contition]

对其参数进行以下说明。

fun_name 表示要做的聚合操作，也就是聚合函数，常用的有 sum（求和）、count(*) （记录数）、max（最大值）、min（最小值）。

GROUP BY关键字表示要进行分类聚合的字段，比如要按照部门分类统计员工数量，部门就应该写在 group by后面。

WITH ROLLUP是可选语法，表明是否对分类聚合后的结果进行再汇总。

HAVING关键字表示对分类后的结果再进行条件的过滤。

**注意：**having和where的区别在于，having是对聚合后的结果进行条件的过滤，而where是在聚合前就对记录进行过滤，如果逻辑允许，我们尽可能用where先过滤记录，这样因为结果集减小，将对聚合的效率大大提高，最后再根据逻辑看是否用having进行再过滤。

例如，要在emp表中统计公司的总人数：

mysql> select count(1) from emp;

+----------+

| count(1) |

+----------+

|4|

+----------+

1 row in set (0.00 sec)

在此基础上，要统计各个部门的人数：

mysql> select deptno,count(1) from emp group by deptno;

+--------+----------+

| deptno | count(1) |

+--------+----------+

| 1 | 2 |

| 2 | 1 |

| 4 | 1 |

+--------+----------+

3 rows in set (0.00 sec)

更细一些，既要统计各部门人数，又要统计总人数：

mysql> select deptno,count(1) from emp group by deptno with rollup;

+--------+----------+

| deptno | count(1) |

+--------+----------+

|1|2|

|2|1|

|4|1|

| NULL |4|

+--------+----------+

4 rows in set (0.00 sec)

统计人数大于1人的部门：

mysql> select deptno,count(1) from emp group by deptno having count(1)>1;

+--------+----------+

| deptno | count(1) |

+--------+----------+

| 1 | 2 |

+--------+----------+

1 row in set (0.00 sec)

最后统计公司所有员工的薪水总额、最高和最低薪水：

mysql> select * from emp;

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 100.00 | 1 |

| lisa | 2003-02-01 | 400.00 | 2 |

| bjguan | 2004-04-02 | 100.00 | 1 |

| dony | 2005-02-05 | 2000.00 | 4 |

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

mysql> select sum(sal),max(sal),min(sal) from emp;

+----------+----------+----------+

| sum(sal) | max(sal) | min(sal) |

+----------+----------+----------+

| 2600.00 | 2000.00 | 100.00 |

+----------+----------+----------+

1 row in set (0.00 sec)

（5）表连接。

当需要同时显示多个表中的字段时，就可以用表连接来实现这样的功能。从大类上分，表连接分为**内连接**和**外连接**，它们之间的最主要区别是，内连接仅选出两张表中互相匹配的记录，而外连接会选出其他不匹配的记录。我们最常用的是内连接。

例如，查询出所有雇员的名字和所在部门名称，因为雇员名称和部门分别存放在表 emp和dept中，因此，需要使用表连接来进行查询：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 2000.00 | 1|

| lisa | 2003-02-01 | 4000.00 | 2|

| bjguan | 2004-04-02 | 5000.00 | 1|

| bzshen | 2005-04-01 | 4000.00 | 3|

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1 | tech|

| 2 | sale|

| 3 | hr|

+--------+----------+

3 rows in set (0.00 sec)

mysql> select ename,deptname from emp,dept where emp.deptno=dept.deptno;

+--------+----------+

| ename | deptname |

+--------+----------+

| zzx | tech|

| lisa | sale |

| bjguan | tech |

| bzshen | hr|

+--------+----------+

4 rows in set (0.00 sec)

外连接又分为**左连接**和**右连接**，具体定义如下。

左连接：包含所有的左边表中的记录甚至是右边表中没有和它匹配的记录。

右连接：包含所有的右边表中的记录甚至是左边表中没有和它匹配的记录。

例如，查询emp中所有用户名和所在部门名称：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx| 2000-01-01 | 2000.00 | 1|

| lisa | 2003-02-01 | 4000.00 | 2|

| bjguan | 2004-04-02 | 5000.00 | 1|

| bzshen | 2005-04-01 | 4000.00 | 3|

| dony | 2005-02-05 | 2000.00 | 4|

+--------+------------+---------+--------+

5 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1 | tech|

| 2 | sale |

| 3 | hr |

+--------+----------+

3 rows in set (0.00 sec)

mysql> select ename,deptname from emp left join dept on emp.deptno=dept. deptno;

+--------+----------+

| ename | deptname |

+--------+----------+

| zzx| tech|

| lisa | sale|

| bjguan | tech|

| bzshen | hr|

| dony ||

+--------+----------+

5 rows in set (0.00 sec)

比较这个查询和上例中的查询，都是查询用户名和部门名，两者的区别在于本例中列出了所有的用户名，即使有的用户名（dony）并不存在合法的部门名称（部门号为4，在dept中没有这个部门）；而上例中仅仅列出了存在合法部门的用户名和部门名称。

右连接和左连接类似，两者之间可以互相转化，例如，上面的例子可以改写为如下的右连接：

mysql> select ename,deptname from dept right join emp on dept.deptno=emp.deptno;

+--------+----------+

| ename | deptname |

+--------+----------+

| zzx| tech|

| lisa | sale |

| bjguan | tech |

| bzshen | hr|

| dony | |

+--------+----------+

5 rows in set (0.00 sec)

（6）子查询。

某些情况下，当进行查询的时候，需要的条件是另外一个select语句的结果，这个时候，就要用到子查询。用于子查询的关键字主要包括 in、not in、=、!=、exists、not exists等。

例如，从emp表中查询出所有部门在dept表中的所有记录：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 1 |

| bzshen | 2005-04-01 | 4000.00 | 3|

| dony | 2005-02-05 | 2000.00 | 4|

+--------+------------+---------+--------+

5 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1| tech|

| 2| sale|

| 3| hr|

| 5| fin|

+--------+----------+

4 rows in set (0.00 sec)

mysql> select * from emp where deptno in(select deptno from dept);

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1|

| lisa | 2003-02-01 | 4000.00 | 2|

| bjguan | 2004-04-02 | 5000.00 | 1|

| bzshen | 2005-04-01 | 4000.00 | 3|

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

如果子查询记录数唯一，还可以用=代替in：

mysql> select * from emp where deptno = (select deptno from dept);

ERROR 1242 (21000): Subquery returns more than 1 row

mysql> select * from emp where deptno = (select deptno from dept limit 1);

+--------+------------+---------+--------+

| ename | hiredate | sal| deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1|

| bjguan | 2004-04-02 | 5000.00 | 1|

+--------+------------+---------+--------+

2 rows in set (0.00 sec)

某些情况下，子查询可以转化为表连接，例如：

mysql> select * from emp where deptno in(select deptno from dept);

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 1|

| bzshen | 2005-04-01 | 4000.00 | 3|

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

转换为表连接后：

mysql> select emp.* from emp ,dept where emp.deptno=dept.deptno;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 2000.00 | 1 |

| lisa | 2003-02-01 | 4000.00 | 2 |

| bjguan | 2004-04-02 | 5000.00 | 1 |

| bzshen | 2005-04-01 | 4000.00 | 3 |

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

**注意：**子查询和表连接之间的转换主要应用在两个方面。

MySQL 4.1以前的版本不支持子查询，需要用表连接来实现子查询的功能。

表连接在很多情况下用于优化子查询。

（7）记录联合。

我们经常会碰到这样的应用，将两个表的数据按照一定的查询条件查询出来后，将结果合并到一起显示出来，这个时候，就需要用 union和 union all关键字来实现这样的功能，具体语法如下：

SELECT * FROM t1

UNION|UNION ALL

SELECT * FROM t2

…

UNION|UNION ALL

SELECT * FROM tn;

UNION和UNION ALL的主要区别是UNION ALL是把结果集直接合并在一起，而UNION是将UNION ALL后的结果进行一次DISTINCT，去除重复记录后的结果。

来看下面的例子，将emp和dept表中的部门编号的集合显示出来：

mysql> select * from emp;

+--------+------------+---------+--------+

| ename | hiredate | sal | deptno |

+--------+------------+---------+--------+

| zzx | 2000-01-01 | 100.00 | 1 |

| lisa | 2003-02-01 | 400.00 | 2 |

| bjguan | 2004-04-02 | 100.00 | 1 |

| dony | 2005-02-05 | 2000.00 | 4 |

+--------+------------+---------+--------+

4 rows in set (0.00 sec)

mysql> select * from dept;

+--------+----------+

| deptno | deptname |

+--------+----------+

| 1 | tech |

| 2 | sale |

| 5 | fin |

+--------+----------+

3 rows in set (0.00 sec)

mysql> select deptno from emp

-> union all

-> select deptno from dept;

+--------+

| deptno |

+--------+

| 1|

| 2|

| 1|

| 4|

| 1|

| 2|

| 5|

+--------+

7 rows in set (0.00 sec)

将结果去掉重复记录后显示如下：

mysql> select deptno from emp

-> union

-> select deptno from dept;

+--------+

| deptno |

+--------+

| 1|

| 2|

| 4 |

| 5 |

+--------+

4 rows in set (0.00 sec)



