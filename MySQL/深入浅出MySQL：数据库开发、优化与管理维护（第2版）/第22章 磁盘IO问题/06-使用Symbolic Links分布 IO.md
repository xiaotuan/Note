

MySQL 的数据库名和表名是与文件系统的目录名和文件名对应的，默认情况下，创建的数据库和表都存放在参数datadir定义的目录下。这样如果不使用RAID或逻辑卷，所有的表都存放在一个磁盘设备上，无法发挥多磁盘并行读写的优势！在这种情况下，就可以利用操作系统的符号连接（Symbolic Links）将不同的数据库、表或索引指向不同的物理磁盘，从而达到分布磁盘I/O的目的。

（1）将一个数据库指向其他物理磁盘。

其方法是先在目标磁盘上创建目录，然后再创建从 MySQL 数据目录到目标目录的符号连接：

shell> mkdir /otherdisk/databases/test

shell> ln -s /otherdisk/databases/test /path/to/datadir

（2）将MyISAM（其他存储引擎的表不支持）表的数据文件或索引文件指向其他物理磁盘。

对于新建的表，可以通过在 CREATE TABLE 语句中增加 DATA DIRECTORY 和INDEX DIRECTORY选项来完成，例如：

Create table test(id int primary key,

Name varchar(20))

Type = myisam

DATA DIRECTORY = '/disk2/data'

INDEX DIRECTORY = '/disk3/index'

对于已有的表，可以先将其数据文件（.MYD）或索引文件（.MYI）转移到目标磁盘，然后再建立符号连接即可。需要说明的是表定义文件（.frm）必须位于 MySQL 数据文件目录下，不能用符号连接。

（3）在Windows下使用符号连接。

以上介绍的是Linux/UNIX下符号连接的使用方法，在Windows下，是通过在MySQL数据文件目录下创建包含目标路径并以“.sym”结尾的文本文件来实现的。例如，假设 MySQL的数据文件目录是C:\mysql\data，要把数据库foo存放到D:\data\foo，可以按以下步骤操做：

创建目录D:\data\foo；

创建文件C:\mysql\data\foo.sym，在其中输入D:\data\foo。

这样在数据库foo创建的表都会存储到D:\data\foo目录下。

**注意：**使用 Symbolic Links 存在一定的安全风险，如果不使用 Symbolic Links，应通过启动参数skip-symbolic-links禁用这一功能。



