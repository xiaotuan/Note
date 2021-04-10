### 2.1.4 停止MongoDB

> **在开发环境中安装并配置MongoDB**
> 在本节中，您将在开发环境中实现MongoDB。继续往下阅读前，务必完成本节介绍的步骤，确保在您的开发环境中正确地配置了MongoDB。
> 请按如下步骤在您的开发系统中安装并配置MongoDB。
> 1．前往<a class="my_markdown" href="['www.mongodb.org/downloads']">www.mongodb.org/downloads</a>，根据您的系统下载相应的MongoDB生产版本。
> 2．将文件解压缩到要运行MongoDB的位置（以下称之为<mongo_install_path>）。
> 3．在系统路径中添加<mongo_install_location>/bin。
> 4．创建一个数据文件目录：<mongo_install_location>/data/db。
> 5．创建配置文件<mongo_install_location>/bin/mongod_config.txt。
> 6．在该配置文件中添加如下配置设置并存盘：
> 7．启动MongoDB服务器。打开一个控制台窗口，并在其中使用下面的命令启动；您需要将<mongo_data_location>替换为您的安装目录。这将启动MongoDB数据库服务器。
> 8．启动MongoDB shell。再打开一个控制台窗口，并执行命令mongo来启动MongoDB shell。
> 9．执行下面的命令以停止MongoDB服务器：
> 10．执行命令exit退出MongoDB shell。
> 至此，您成功地安装、配置、启动和停止了MongoDB服务器。
> ▲

启动可执行文件mongod后，停止它的方法随平台而异。然而，停止它的最佳方法是在MongoDB shell中进行，这将干净地终止当前操作，并强制mongod退出。

要在MongoDB shell中停止MongoDB数据库服务器，可使用下面的命令，切换到admin数据库再关闭数据库引擎：

```go
use admin
db.shutdownServer()
```

▼　Try It Yourself

```go
verbose = true
port = 27017
dbpath=c:\mongodb\data\db\
noauth = true
maxConns = 10
rest = true
```

```go
mongod --config <mongo_install_location>/bin/mongod_config.txt
```

```go
use admin
db.shutdownServer()
```

