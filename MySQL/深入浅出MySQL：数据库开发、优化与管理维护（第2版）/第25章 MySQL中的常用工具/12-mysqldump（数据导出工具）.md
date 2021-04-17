

mysqldump客户端工具用来备份数据库或在不同数据库之间进行数据迁移。备份内容包含创建表或装载表的SQL语句。mysqldump目前是MySQL中最常用的备份工具。

有3种方式来调用mysqldump：

shell> mysqldump [options] db_name [tables] #备份单个数据库或者库中部分数据表

shell> mysqldump [options] ---database DB1 [DB2 DB3. .] #备份指定的一个或者多个数据库

shell> mysqldump [options] --all—database #备份所有数据库

下面是mysqldump的一些常用选项，要查阅更详细的功能，可以使用“mysqldump –help”查看。



