

mysqlcheck 客户端工具可以检查和修复 MyISAM 表，还可以优化和分析表。实际上，它集成了mysql工具中check、repair、analyze、optimize的功能。

有3种方式可以来调用mysqlcheck：

shell> mysqlcheck[options] db_name [tables]

shell> mysqlcheck[options] ---database DB1 [DB2 DB3. .]

shell> mysqlcheck[options] --all—database

option中有以下常用选项：

-c, --check（检查表）；

-r, --repair（修复表）；

-a, --analyze（分析表）；

-o, --optimize（优化表）。

其中，默认选项是-c（检查表）。

下面对这些选项依次进行举例说明。

（1）检查表（check）：

[root@localhost mysql]# mysqlcheck -uroot -c test

test.dept OK

test.emp OK

test.emp1 OK

test.t2 OK

（2）修复表（repair）：

[root@localhost mysql]# mysqlcheck -uroot -r test

test.dept OK

test.emp

note : The storage engine for the table doesn't support repair

test.emp1

note : The storage engine for the table doesn't support repair

test.t2 OK

emp和emp1表的存储引擎为InnoDB，不支持repair。

（3）分析表（analyze）：

[root@localhost mysql]# mysqlcheck -uroot -a test

test.dept OK

test.emp OK

test.emp1 OK

test.t2 OK

（4）优化表（optimize）：

[root@localhost mysql]# mysqlcheck -uroot -o test

test.dept OK

test.emp OK

test.emp1 OK

test.t2 OK



