

MySQL的版本更新很快，新版本中往往包含了很多新功能，并且解决了很多旧版本中的BUG，因此在很多情况下用户需要对数据库进行升级。

MySQL 的升级很简单，以下给出了几种不同的升级方法，每种升级方法都有一定的优缺点，用户可以按照实际需求选择合适的方法进行操作。

**方法一：最简单，适合于任何存储引擎（不一定速度最快）。**

（1）在目标服务器上安装新版本的MySQL。

（2）在新版本的MySQL上创建和老版本同名的数据库。命令如下：

shell> mysqladmin -h hostname -P port -u user -p passwd create db_name

（3）将老版本MySQL上的数据库通过管道导入到新版本数据库中。命令如下：

shell> mysqldump --opt db_name | mysql -h hostname -P port -u user -p passwd db_name

这里的--opt选项表明采用优化（Optimize）方式进行导出。

**注意：**如果网络较慢，可以在导出选项中加上--compress来减少网络传输。

对于不支持管道操作符（|）的操作系统，可以先用 mysqldump 工具将旧版本的数据导出为文本文件，然后再往新版本MySQL中导入此文件。其实就是把上面的操作分为两步执行，具体操作如下：

shell> mysqldump --opt db_name > filename（旧版本MySQL上执行）

shell> mysql –u user –p passwd db_name < filename（新版本MySQL上执行）

（4）将旧版本MySQL中的mysql数据库目录全部cp过来覆盖新版本MySQL中的mysql数据库。例如将/home/mysql_old/data/mysql 目录覆盖掉/home/mysql_new/data/mysql，可以使用如下命令：

shell>cp –R /home/mysql_old/data/mysql /home/mysql_new/data

这里，-R选项表示cp整个目录下的内容，包括嵌套的所有子目录。

（5）新版本服务器的shell里面执行mysql_fix_privilege_tables命令升级权限表。

shell>mysql_fix_privilege_tables

（6）重启新版本MySQL服务。至此，升级完毕。

**方法二：适合于任何存储引擎，速度较快。**

（1）参照方法一中的步骤（1）安装新版本MySQL。

（2）在旧版本MySQL中，创建用来保存输出文件的目录并用mysqldump备份数据库：

shell> mkdir DUMPDIR

shell>mysqldump --tab=DUMPDIR db_name

这里使用--tab选项不会生成SQL文本。而是在备份目录下对每个表分别生成了.sql和.txt文件，其中.sql保存了表的创建语句；.txt保存了用默认分隔符生成的纯数据文本。

（3）将DUMPDIR目录中的文件转移到目标服务器上相应的目录中并将文件装载到新版本的MySQL中，具体操作如下（以下命令都在新版本服务器中执行）：

shell> mysqladmin create db_name #创建数据库

shell> cat DUMPDIR/*.sql | mysql db_name #创建数据库表

shell> mysqlimport db_name DUMPDIR/*.txt #加载数据

（4）参照方法一中的步骤（4）、（5）、（6）升级权限表，并重启MySQL服务。

**方法三：适合于MyISAM存储引擎的表，速度最快。**

（1）参照方法一中的步骤（1）安装新数据库。

（2）将旧版本 MySQL 中的数据目录下的所有文件（.frm、.MYD 和.MYI）cp 到新版本MySQL下的相应目录下。

（3）参照方法一中的步骤（4）、（5）、（6）升级权限表，并重启MySQL服务。

从上面3种方法中可以看出，其实升级的步骤都大同小异，区别仅仅在于数据迁移方法的不同。这里需要提醒读者的有两点：

上面的升级方法都是假设升级期间旧版本MySQL不再进行数据更新，否则，迁移过去的数据将不能保证和原数据库一致；

迁移前后的数据库字符集最好能保持一致，否则可能会出现各种各样的乱码问题。



