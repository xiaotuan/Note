

mysqladmin是一个执行管理操作的客户端程序。可以用它来检查服务器的配置和当前的状态、创建并删除数据库等。它的功能和mysql客户端非常类似，主要区别在于它更侧重于一些管理方面的功能，比如关闭数据库。

mysqladmin的用法如下：

shell> mysqladmin [options] command [command-options]

[command [command-options]] . .

使用方法和常用的选项和mysql非常类似，这里就不再赘述。这里将可以执行的命令行简单列举如下：

create databasename　Create a new database

debug　Instruct server to write debug information to log

drop databasename　Delete a database and all its tables

extended-status　Gives an extended status message from the server

flush-hosts　Flush all cached hosts

flush-logs　Flush all logs

flush-status　Clear status variables

flush-tables　Flush all tables

flush-threads　Flush the thread cache

flush-privileges　Reload grant tables (same as reload)

kill id,id,...　Kill mysql threads

password new-password Change old password to new-password, MySQL 4.1 hashing.

old-password new-password Change old password to new-password in old format.

ping　Check if mysqld is alive

processlist　Show list of active threads in server

reload　Reload grant tables

refresh　Flush all tables and close and open logfiles

shutdown　Take server down

status　Gives a short status message from the server

start-slave　Start slave

stop-slave　Stop slave

variables　Prints variables available

version　Get version info from server

这里简单举一个关闭数据库的例子：

[root@localhost test]# mysqladmin -uroot -p shutdown

Enter password:



