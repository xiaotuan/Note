#### 
  13.1.4 MySQL复制的几种模式


MySQL 5.1之后的版本中，在复制方面的改进就是引进了新的复制技术——基于行的复制。这种新技术就是关注表中发生变化的记录，而非以前的照抄binlog模式。从 MySQL 5.1.12 开始，可以用以下3种模式来实现。

⑴基于SQL语句的复制(Statement-Based Replication, SBR)。

⑵基于行的复制(Row-Based Replication, RBR)。

⑶混合模式复制(Mixed-Based Replication, MBR)。

相应地，binlog的格式也有3种：STATEMENT、ROW、MIXED。MBR 模式中，SBR 模式是默认的。在运行时可以动态地改变binlog的格式。设定主从复制模式的方法非常简单，只要在以前设定复制配置的基础上，再加一个参数，具体如下。

&#13;
    binlog_format="STATEMENT"&#13;
    #binlog_format="ROW"&#13;
    #binlog_format="MIXED"&#13;

当然了，也可以在运行时动态修改binlog的格式，如下。

&#13;
    mysql> SET SESSION binlog_format = 'STATEMENT';&#13;
    mysql> SET SESSION binlog_format = 'ROW';&#13;
    mysql> SET SESSION binlog_format = 'MIXED';&#13;
    mysql> SET GLOBAL binlog_format = 'STATEMENT';&#13;
    mysql> SET GLOBAL binlog_format = 'ROW';&#13;
    mysql> SET GLOBAL binlog_format = 'MIXED';&#13;

