

在Linux下配置MySQL和在Windows下以noinstall方式配置非常类似，区别在于参数文件的位置和文件名不同。Linux 下也可以在多个位置部署配置文件，大多数情况下都放在/etc下，文件名称只能是my.cnf（在Windows下文件名称可以是my.ini）。

对于初学者来说，和Windows下类似，还是建议用MySQL自带的多个样例参数文件来代替实际的参数文件。在 Linux 下，如果安装方式是 RPM 包，则自带的参数文件会放到/usr/share/mysql下，如下所示：

[root@localhost mysql]# pwd

/usr/share/mysql

[root@localhost mysql]# ls *.cnf

my-huge.cnf my-innodb-heavy-4G.cnf my-large.cnf my-medium.cnf my-small.cnf

用户可以根据实际需求选择不同的配置文件复制到/etc下，改名为my.cnf，并根据实际需要做一些配置的改动。MySQL启动的时候会读取此文件中的配置选项。



