

在MySQL 4.1版本之前，PASSWORD函数生成的密码是 16位。4.1以后，MySQL改进了密码算法，生成的函数值变成了41位，如下所示。

MySQL 3.23中执行的结果如下：

mysql> SELECT PASSWORD('mypass');

+--------------------+

| PASSWORD('mypass') |

+--------------------+

| 6f8c114b58f2ce9e |

+--------------------+

MySQL 5.1中执行的结果如下：

mysql> SELECT PASSWORD('mypass');

+-------------------------------------------+

| PASSWORD('mypass')|

+-------------------------------------------+

| *6C8989366EAF75BB670AD8EA7A7FC1176A95CEF4 |

+-------------------------------------------+

这样就会出现一个问题，当4.1以后的客户端连接4.1以前的客户端时，没有问题，因为新客户端可以理解新旧两种加密算法。但是反过来，当4.1以前的客户端需要连接4.1以后的服务器时，由于无法理解新的密码算法，发到服务器端的密码还是旧的算法加密后的结果，于是导致在新的服务器上出现下面无法认证的情况：

shell> mysql -h localhost -u root

Client does not support authentication protocol requested

by server; consider upgrading MySQL client

对于这个问题，可以采用以下办法解决。

（1）在服务器端用 OLD_PASSWORD 函数更改密码为旧密码格式，客户端可以进行正常连接：

mysql> SET PASSWORD FOR 'some_user'@'some_host' = OLD_PASSWORD('mypass');

（2）在my.cnf的[mysqld]中增加old-passwords参数并重启服务器，这样新的数据库连接成功之后做的 set password、grant、password()操作后生成的新密码全部变成旧的密码格式。

**注意：**这个参数只是为了支持 4.1 版本前的客户端才进行设置，但是这将使得新建或者修改的用户密码全部变成旧的格式，降低了系统的安全性。



