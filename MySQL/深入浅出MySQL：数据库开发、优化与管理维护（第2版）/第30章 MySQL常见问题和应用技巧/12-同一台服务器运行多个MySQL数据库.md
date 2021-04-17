

在很多情况下，由于硬件资源的局限，用户通常需要在一台服务器上安装多个MySQL数据库，从而为多个应用提供服务。在这种情况下，通常可以使用以下方法进行安装。

将每个MySQL安装在不同的用户下面，例如mysql1和mysql2，在每个用户下面，分别执行如下操作：

export MYSQL_HOME=/home/mysql1/mysql

shell> groupadd mysql

shell> useradd -g mysql mysql1

shell> cd /home/mysql1

shell>tar -xzvf /home/mysql1/mysql-VERSION-OS.tar.gz

shell> ln -s mysql-VERSION-OS.tar.gz mysql

shell> cd mysql

cp support-files/my-large.cnf./my.cnf

通过vi命令修改my.cnf ，主要修改[client]和[mysqld]下面的port和socket，并指定字符集，例如：

[client]

port = 3307

socket = /home/mysql1/mysql/data/mysql.sock

# The MySQL server

[mysqld]

default-character-set = utf8

port = 3307

socket = /home/mysql1/mysql/data/mysql.sock

…

shell> scripts/mysql_install_db --user=mysql1

shell> chown -R root:mysql .

shell> chown -R mysql1:mysql data

shell> bin/mysqld_safe --user=mysql &

mysql2用户执行的操作和mysql1类似，区别在于指定不同的MYSQL_HOME，以及不同的port和socket即可



