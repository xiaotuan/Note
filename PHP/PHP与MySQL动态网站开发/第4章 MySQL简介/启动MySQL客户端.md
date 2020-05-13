可以通过如下命令启动 MySQL 客户端：

```console
$ mysql -u username -h hostname -p
```

`-p` 选项将导致客户提示你输入密码，也可以在这一行指定密码（直接在 `-p` 提示符后面输入它）但是它将是可见的。`-h hostname` 参数是可选的。

在 MySQL 客户端内，需要用分号来终止每一条语句（SQL命令）。

选择你想使用的数据库的命令如下：

```console
$ mysql> USE test;
```

`USE` 命令选择要用于每个后续命令的数据库。

退出 MySQL 客户端的命令如下：

```console
$ mysql> exit
或
$ mysql> quit
```
如果预先知道要使用哪个数据库，那么可以利用一下命令启动 MySQL：

```console
$ mysql -u username -p databasename
```

想要查看 MySQL 客户端的帮助文档，可以输入如下命令：

```console
$ mysql --help
```

在 MySQL 客户端，可以使用 \G 代替分号来结束 SQL 命令。

如果正在执行一条较长的语句并且犯了一个错误，可以输入 c 并按下 <kbd>Return</kbd> 或 <kbd>Enter</kbd> 键来取消当前的操作。