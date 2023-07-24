`MySQL` 服务器端实用工具程序如下：

（1）`mysqld`：`SQL` 后台程序（`MySQL` 服务器进程）。必须在该程序运行之后，客户端才能通过连接服务器来访问数据库。

（2）`mysqld_safe`：服务器启动脚本。在 `UNIX` 和 `NetWare` 中推荐使用 `mysqld_safe` 来启动 `mysqld` 服务器。`mysqld_safe` 增加了一些安全特性，例如当出现错误时重启服务器并向错误日志文件写入运行时间信息。

（3）`mysql.server`：服务器启动脚本。该脚本用于使用包含为特定级别的、运行启动服务的脚步的、运行目录的系统。它调用 `mysqld_safe` 来启动 `MySQL` 服务器。

（4）`mysql_multi`：服务器启动脚本，可以启动或停止系统上安装的多个服务器。

（5）`myisamchk`：用来描述、检查、优化和维护 `MyISAM` 表的使用工具。

（6）`mysqlbug`：`MySQL` 缺陷报告脚本。它可以用来向 `MySQL` 邮件系统发送缺陷报告。

（7）`mysql_install_db`：该脚本用默认权限创建 `MySQL` 授权表。通常只是在系统上首次安装 `MySQL` 时执行一次。

