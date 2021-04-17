

对于noinstall安装的MySQL，可以在DOS窗口下通过命令行方式启动和关闭MySQL服务。

（1）启动服务：

cd C:\mysql-5.0.45-win32\bin

C:\mysql-5.0.45-win32\bin>mysqld --console

070703 17:19:10 InnoDB: Started; log sequence number 0 43655

070703 17:19:10 [Note] mysqld: ready for connections.

Version: '5.0.45-community-nt' socket: '' port: 3306 MySQL Community Edition

(GPL)

（2）关闭服务：

C:\mysql-5.0.45-win32\bin>mysqladmin -uroot shutdown

此时，控制台输出：

070703 17:21:13 [Note] mysqld: Normal shutdown

070703 17:21:13 InnoDB: Starting shutdown...

070703 17:21:16 InnoDB: Shutdown completed; log sequence number 0 43655 070703 17:21:16 [Note] mysqld: Shutdown complete

Error in my_thread_global_end(): 1 threads didn't exit

对于采用图形化方式安装的MySQL，可以直接通过Windows的“开始”菜单（单击“开始”Æ“控制面板”Æ“管理工具”Æ“服务”菜单）启动和关闭MySQL，如图1-25所示。



![figure_0040_0029.jpg](../images/figure_0040_0029.jpg)
图1-25 服务列表中启动和关闭MySQL5

用户也可以在命令行中手工启动和关闭MySQL服务，如下所示。

（1）启动服务：

C:\Program Files\MySQL\MySQL Server 5.0\bin>net start mysql5

MySQL5 服务正在启动.

MySQL5 服务已经启动成功.

（2）关闭服务：

C:\Program Files\MySQL\MySQL Server 5.0\bin>net stop mysql5

MySQL5 服务正在停止.

MySQL5 服务已成功停止.



