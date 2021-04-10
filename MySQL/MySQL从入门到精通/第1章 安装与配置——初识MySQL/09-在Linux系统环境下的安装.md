#### 
  1.3.2 在Linux系统环境下的安装


本节选用的Navicat for MySQL版本为navicat111_mysql_cs.tar.gz，官方下载地址：http://www.navicat.com.cn/download/navicat-for-mysql。使用方法如下。

⑴打开终端。

选择应用程序→系统工具（或附件）→终端，切换到root账户：#su，密码：xx。

注意 
 输入root密码时，密码不会显示出来，也没有提示的特殊字符，输完密码后按Enter键就可以了。

⑵切换到存放 navicat_for_mysql_10.0.11_cn_linux.tar.gz 软件包的目录，例如/home/zdw/software 目录下。

# cd /home/zdw/software

⑶解压 navicat_for_mysql_10.0.11_cn_linux.tar.gz。

# tar -zxvf navicat_for_mysql_10.0.11_cn_linux.tar.gz

解压后会得到名为 navicat_for_mysql 的文件夹。

⑷将解压生成文件夹移动到/opt目录下。

# mv /home/zdw/software/navicat_for_mysql /opt

⑸运行 Navicat 的方法。

①进入安装目录：# cd /opt/navicat_for_mysql。

②执行命令：# ./start_navicat，这样即可启动Navicat。

为了方便，也可以创建Navicat的桌面启动器，方法如下：在桌面右键单击→单击“创建启动器”项→在“类型”栏选择“应用程序”；“名称”栏填入“Navicat”；“命令”栏单击右边的“浏览”选择到→“文件系统”→“opt”→“navicat_for_mysql”→“start_navicat”；

最后单击“确定”，就在桌面创建好Navicat的启动器。

