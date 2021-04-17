

MyISAM存储引擎有自己的索引缓存机制，但数据文件的读写完全依赖于操作系统，操作系统磁盘I/O缓存对MyISAM表的存取很重要。但InnoDB存储引擎与MyISAM不同，它采用类似Oracle的数据缓存机制来Cache索引和数据，操作系统的磁盘I/O缓存对其性能不仅没有帮助，甚至还有反作用。因此，在 InnoDB缓存充足的情况下，可以考虑使用Raw Device来存放InnoDB共享表空间，具体操作方法如下。

（1）修改 MySQL 配置文件，在 innodb_data_file_path 参数中增加裸设备文件名并指定newraw属性：

…

[mysqld]

innodb_data_home_dir=

innodb_data_file_path=/dev/hdd1:3Gnewraw;/dev/hdd2:2Gnewraw

…

（2）启动MySQL，使其完成分区初始化工作，然后关闭MySQL。此时还不能创建或修改InnoDB表。

（3）将innodb_data_file_path中的newraw改成raw：

…

class=programlisting[mysqld]

innodb_data_home_dir=

innodb_data_file_path=/dev/hdd1:3Graw;/dev/hdd2:2Graw

…

（4）重新启动即可开始使用。



