### 
  15.3 MySQL分布式应用实例


<img class="my_markdown" class="h-pic" src="../images/Figure-0388-273.jpg" style="width:87px;  height: 85px; "/> 本节视频教学录像：3分钟

MySQL是当前世界互联网行业应用最为广泛的开源数据库，在实际应用中，全球访问量最大的10个网站中有9个都在使用MySQL数据库，包括Facebook、Google、YouTube及Yahoo。在LAMP架构(Linux，Apache，MySQL，PHP/Perl/Python)中代表M的MySQL经历了大交易处理应用、T级数据仓库和高流量网站的严苛测试，证明了其在开源数据库中的领先地位。全球超过1200万个MySQL安装，每天在MySQL网站有50000个下载，没有其他开源数据库像MySQL这样流行。《华尔街日报》研究发现，在所有开源软件中，MySQL数据库的下载次数仅次于Mozilla Firefox浏览器。

利用MySQL的复制功能，可以十分便利地将一个MySQL数据库(主库)中的数据复制到多台MySQL服务器(从库)上，组成一个MySQL集群，然后通过这个MySQL集群来对外提供服务。这样，每台MySQL主机所需要承担的负载就会大大降低，整个MySQL集群的处理能力也很容易得到提升。MySQL 能够实现简便的水平扩展，以获得更高性能，通过MySQL自带的扩展方式，可以组成由数十台服务器构成的MySQL集群/群组，支持数百万用户的访问压力。通过更高级的扩展方案，MySQL 可以组成由数百台甚至数千台服务器组成的数据库群组，以承载千万、上亿用户的访问压力。这些方案在国内外互联网、电信行业已经普遍应用。

下面将以MySQL Cluster为例为大家介绍如何构建MySQL分布式应用。

1.下载MySQL Cluster

MySQL Cluster支持多种操作系统。笔者将以Windows系统下的MySQL Cluster 7.2.5为例说明MySQL Cluster的配置和启动。MySQL Cluster的下载地址是http://dev.mysql.com/downloads/cluster，提供有Windows 32位和64位的下载。

2.配置MySQL Cluster

准备两台服务器，管理节点部署在其中一台服务器（IP为10.212.103.113）上，另一台（IP为10.212.103.95）部署一个数据节点和一个SQL节点。最好不要将管理节点和数据节点部署到同一台服务器上，因为如果数据节点死机会导致管理节点也不可用，整个MySQL集群就不可用了。

以下为具体的实现过程：在IP为10.212.103.113的主机的C盘中新建文件夹MySQL，然后在此文件夹下新建子目录bin和mysql-cluster，再将安装包解压后的mysql\bin中的ndb_mgm.exe和ndb_mgmd.exe拷贝到C:\mysql\bin下。在目录C:\mysql\bin下新建cluster-logs目录、config.ini文件和my.ini文件。

config.ini文件的内容如下。

&#13;
    [ndbd default]&#13;
    # Options affecting ndbd processes on all data nodes:&#13;
    NoOfReplicas=2 #Number of replicas&#13;
    DataDir=c:/mysqlcluster/datanode/mysql/bin/cluster-data&#13;
    #Directory for each data node's data files&#13;
    DataMemory=80M  #Memory allocated to data storage&#13;
    IndexMemory=18M #Memory allocated to indexstorage&#13;
    # For DataMemory and IndexMemory, we have used the default values.&#13;
    [ndb_mgmd]&#13;
  # Management process options:&#13;
    HostName=10.212.103.113#IP address or Hostname of management node&#13;
    DataDir=C:/mysql/bin/cluster-logs# Directory for management node log files&#13;
    [ndbd]&#13;
    #Options for data node "A":&#13;
  # (one [ndbd] section per data node)&#13;
  HostName=10.212.103.113      #IP address or Hostname&#13;
   [ndbd]&#13;
  # Options for data node "B":&#13;
    HostName=10.212.103.95     #IP address or Hostname&#13;
    [mysqld]&#13;
   # SQL node options:&#13;
    HostName=10.212.103.113     #IP address or Hostname&#13;
    [mysqld]&#13;
    # SQL node options:&#13;
    HostName=10.212.103.95     #IP address or Hostname&#13;
   my.ini中的内容为：&#13;
   [mysql_cluster]&#13;
    # Options for management node process&#13;
   config-file=C:/mysql/bin/config.ini&#13;

3.配置数据节点

在IP为10.212.103.113的主机中新建文件夹C:\mysqlcluster\datanode\mysql，然后在此文件夹中继续新建子目录bin和cluster-data，bin下再建一个子目录也叫cluster-data。

将安装包解压文件夹中mysql\bin中的ndbd.exe复制到C:\mysqlcluster\datanode\mysql\bin下，并在C:\mysqlcluster\datanode\mysql中新建my.ini文件，文件内容如下。

&#13;
    [mysql_cluster]&#13;
  # Options for data node process:&#13;
    ndb-connectstring=10.212.103.113   #location of management server&#13;

因为两台主机的数据节点的配置是一样的，所以可以直接将10.212.103.113主机中的文件夹C:\mysqlcluster拷贝到10.212.103.95主机的C盘下。

4.配置SQL节点

在10.212.103.113主机的C:\mysqlcluster下新建子目录sqlnode，将安装包解压文件夹mysql整个拷贝到这个子目录下，然后在C:\mysqlcluster\sqlnode\mysql下新建my.ini文件，文件内容如下。

&#13;
    [mysqld]&#13;
    # Options for mysqld process:&#13;
    ndbcluster            #run NDB storage engine&#13;
    ndb-connectstring=10.212.103.113 #location of management server&#13;

之后也把C:\mysqlcluster\sqlnode文件夹整个拷贝到10.212.103.95主机的相同目录下。

5.MySQL Cluster的启动

3种节点服务启动时，一定要按照先启动管理节点，后启动数据节点，再启动SQL节点的顺序进行。

6.启动管理节点

在10.212.103.113主机中打开命令行窗口，切到C:\mysql\bin目录，输入：“ndb_mgmd -f config.ini --configdir=C:\mysql\mysql-cluster”按Enter键，管理节点服务就启动了，命令行上可能没有任何提示信息，可以打开C:\mysql\bin\cluster-logs\ndb_1_cluster.log日志文件查看启动信息。注意，此命令行窗口不能关闭，除非想停止服务。也可以将其做成服务，在命令行中输入：“ndb_mgmd--install=ndb_mgmd -f config.ini--configdir=C:\mysql\mysql-cluster”。

7.启动数据节点

在10.212.103.113主机中打开一个新的命令行窗口，切到目录C:\mysqlcluster\datanode\mysql\bin，输入：“ndbd”按Enter键，数据节点就启动了。也可以将其做成服务，在命令行中输入：“ndbd--install=ndbd”以相同的方法在10.212.103.95中启动数据节点服务。可以在10.212.103.113主机中再新开一个命令行窗口，切到目录C:\mysql\bin，输入：“ ndb_mgm”按Enter键，然后再输入：“ALL STATUS”按Enter键，就可以看到数据节点的连接信息了。

8.启动SQL节点

在10.212.103.113主机中继续打开一个新的命令行窗口，切到目录C:\mysqlcluster\sqlnode\mysql\bin，输入“mysqld --console”，按Enter键，SQL节点启动。也可以将其做成服务，输入“mysqld -install mysql”，以相同的方法在10.212.103.95中启动SQL节点。想要查看SQL节点的启动情况可以在10.212.103.113主机中同样打开新命令行，输入：“ndb_mgm”按Enter键，再输入SHOW，按Enter键，就可以看到SQL节点的连接情况了。

9.测试MySQL Cluster

在任一SQL节点对数据节点进行操作后，测试各数据节点是否能够实现数据同步。例如，在10.212.103.113主机上新创建一个数据库xscj，然后再建一个表student（新建表使用如下命令：create table student (id int(2)) engine=ndbcluster），插入若干数据，接着到10.212.103.95主机上查看是否能看到新的数据库xscj和新的表student以及插入数据。

当关闭任一数据节点后，在所有SQL节点中进行操作是否不受其影响。例如，关闭10.212.103.113主机上的数据节点服务，在两台主机上应该能够继续对数据库进行各种操作。

关闭某数据节点进行了数据库操作，然后重新启动，查看所有SQL节点的操作是否正常。这里要说明的是，通过SQL节点创建新的数据库时，必须在CREATE语句中使用“engine=ndbcluster”选择ndbcluster数据库引擎，否则创建的数据库不会加到MySQL群集系统中，只能作为普通的数据库独立使用。

