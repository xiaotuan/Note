

由于服务器生成的二进制日志文件以二进制格式保存，所以如果想要检查这些文件的文本格式，就会用到mysqlbinlog日志管理工具。

mysqlbinlog的具体用法如下：

shell> mysqlbinlog [options] log-files1 log-files2. .

option有很多选项，常用的选项如下。

-d, --database=name：指定数据库名称，只列出指定的数据库相关操作。

-o, --offset=#：忽略掉日志中的前 n行命令。

-r, --result-file=name：将输出的文本格式日志输出到指定文件。

-s, --short-form：显示简单格式，省略掉一些信息。

--set-charset=char-name：在输出为文本格式时，在文件第一行加上 set names char-name，这个选项在某些情况下装载数据时非常有用。

--start-datetime=name –stop-datetime=name：指定日期间隔内的所有日志。

--start-position=# --stop-position=#：指定位置间隔内的所有日志。

下面举一个例子说明这些选项的使用。

（1）创建新日志，对mysql和test数据库做不同的DML操作。

[root@localhost mysql]# mysql -uroot

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 2

Server version: 5.0.41-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> flush logs;

Query OK, 0 rows affected (0.10 sec)

mysql> use mysql

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A

Database changed

mysql> revoke process on *.* from z3@'%';

Query OK, 0 rows affected (0.00 sec)

mysql> use test

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A

Database changed

mysql> truncate table t2;

Query OK, 0 rows affected (0.00 sec)

mysql> insert into t2 values(1);

uery OK, 1 row affected (0.00 sec)

（2）不加任何参数，显示所有日志（粗体字显示上一步执行过的SQL）。

[root@localhost mysql]# mysqlbinlog localhost-bin.000033

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

# at 4

#070830 5:04:24 server id 1 end_log_pos 98 Start: binlog v 4, server v 5.0.41-community-log created 070830 5:04:24

# Warning: this binlog was not closed properly. Most probably mysqld crashed writing it.

# at 98

#070830 5:06:09 server id 1 end_log_pos 196 Query thread_id=2 exec_time=0 error_code=0

use mysql/*!*/;

SET TIMESTAMP=1188421569/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1,@@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28, @@session.collation_connection=28, @@session. collation_server=28/*!*/;

revoke process on *.* from z3@'%'/*!*/;

# at 196

#070830 5:06:28 server id 1 end_log_pos 276 Query thread_id=2 exec_time=0 error_code=0

use test/*!*/;

SET TIMESTAMP=1188421588/*!*/;

truncate table t2/*!*/;

# at 276

#070830 5:06:35 server id 1 end_log_pos 363 Query thread_id=2 exec_time=0 error_code=0

SET TIMESTAMP=1188421595/*!*/;

insert into t2 values(1)/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;

（3）加-d选项，将只显示对test数据库的操作日志。

[root@localhost mysql]# mysqlbinlog localhost-bin.000033 -d test

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

# at 4

#070830 5:04:24 server id 1 end_log_pos 98 Start: binlog v 4, server v 5.0.41-community-log created 070830 5:04:24

# Warning: this binlog was not closed properly. Most probably mysqld crashed writing it.

# at 98

# at 196

#070830 5:06:28 server id 1 end_log_pos 276 Query thread_id=2 exec_time=0 error_code=0

use test/*!*/;

SET TIMESTAMP=1188421588/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28,@@session.collation_ connection=28, @@session. collation_server=28/*!*/;

truncate table t2/*!*/;

# at 276

#070830 5:06:35 server id 1 end_log_pos 363 Query thread_id=2 exec_time=0 error_code=0

SET TIMESTAMP=1188421595/*!*/;

insert into t2 values(1)/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;

日志中的粗体字显示，输出中仅仅包含了对test数据库的操作部分。

（4）加-o选项，忽略掉前3个操作，只剩下对t2的insert操作。

[root@localhost mysql]# mysqlbinlog localhost-bin.000033 -o 3

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

# at 4

#070830 5:04:24 server id 1 end_log_pos 98 Start: binlog v 4, server v 5.0.41-community-log created 070830 5:04:24

# Warning: this binlog was not closed properly. Most probably mysqld crashed writing it.

# at 276

#070830 5:06:35 server id 1 end_log_pos 363 Query thread_id=2 exec_time=0 error_code=0

use test/*!*/;

SET TIMESTAMP=1188421595/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28,@@session.collation_connection=28, @@session. collation_server=28/*!*/;

insert into t2 values(1)/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;

（5）加-r选项，将上面的结果输出到文件resultfile中。

[root@localhost mysql]# mysqlbinlog localhost-bin.000033 -o 3 -r resultfile

[root@localhost mysql]# more resultfile

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

# at 4

#070830 5:04:24 server id 1 end_log_pos 98 Start: binlog v 4, server v 5.0.41-community-log created 070830 5:04:24

# Warning: this binlog was not closed properly. Most probably mysqld crashed writing it.

# at 276

#070830 5:06:35 server id 1 end_log_pos 363 Query thread_id=2 exec_time=0 error_code=0

use test/*!*/;

SET TIMESTAMP=1188421595/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28,@@session.collation_connection=28, @@session. collation_server=28/*!*/;

insert into t2 values(1)/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;

（6）结果显示的内容较多，显得比较乱，加-s选项将上面的内容进行简单显示。

[root@localhost mysql]# mysqlbinlog localhost-bin.000033 -o 3 -s

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

use test/*!*/;

SET TIMESTAMP=1188421595/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28,@@session.collation_connection=28, @@session. collation_server=28/*!*/;

insert into t2 values(1)/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;

可以发现，内容的确比上面的精简了一些，但粗体字显示的主要内容都没有少。

（7）加“--start-datetime --stop-datetime”选项显示 5:00:00～5:06:20之间的日志。

[root@localhost mysql]# mysqlbinlog localhost-bin.000033 --start-datetime= '2007/08/30 05:00:00' --stop-datetime='2007/08/30 05:06:20'

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

# at 4

#070830 5:04:24 server id 1 end_log_pos 98 Start: binlog v 4, server v 5.0.41-community-log created 070830 5:04:24

# Warning: this binlog was not closed properly. Most probably mysqld crashed writing it.

# at 98

#070830 5:06:09 server id 1 end_log_pos 196 Query thread_id=2 exec_time=0 error_code=0

use mysql/*!*/;

SET TIMESTAMP=1188421569/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28,@@session.collation_connection=28, @@session. collation_server=28/*!*/;

revoke process on *.* from z3@'%'/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;

开始日期和结束日期可以只写一个。如果只写开始日期，表示范围是开始日期到日志结束；如果只写结束日期，表示日志开始到指定的结束日期。

（8）--start-position=#和--stop-position=#，与日期范围类似，不过可以更精确地表示范围。例如，在上面的例子中，改成位置范围后如下：

[root@localhost mysql]# mysqlbinlog localhost-bin.000033 --start-position=4 --stop-position=196

/*!40019 SET @@session.max_insert_delayed_threads=0*/;

/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;

DELIMITER /*!*/;

# at 4

#070830 5:04:24 server id 1 end_log_pos 98 Start: binlog v 4, server v 5.0.41-community-log created 070830 5:04:24

# Warning: this binlog was not closed properly. Most probably mysqld crashed writing it.

# at 98

#070830 5:06:09 server id 1 end_log_pos 196 Query thread_id=2 exec_time=0 error_code=0

use mysql/*!*/;

SET TIMESTAMP=1188421569/*!*/;

SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1/*!*/;

SET @@session.sql_mode=0/*!*/;

/*!\C gbk *//*!*/;

SET @@session.character_set_client=28,@@session.collation_connection=28, @@session. collation_server=28/*!*/;

revoke process on *.* from z3@'%'/*!*/;

DELIMITER ;

# End of log file

ROLLBACK /* added by mysqlbinlog */;

/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;



