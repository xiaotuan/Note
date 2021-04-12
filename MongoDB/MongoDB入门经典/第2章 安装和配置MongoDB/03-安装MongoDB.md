### 2.1.1 安装MongoDB

实现MongoDB数据库的第一步是安装MongoDB服务器。有用于各种主要平台（Linux、Windows、Solaris和OS X）的MongoDB版本；还有用于Red Hat、SuSE、Ubuntu和Amazon Linux的企业版。MongoDB企业版是基于订阅的，提供了更强大的安全、管理和集成支持。

就本书以及学习MongoDB而言，MongoDB标准版就很好。有关如何下载并安装MongoDB，请参阅<a class="my_markdown" href="['http://docs.mongodb.org/manual/installation/']">http://docs.mongodb.org/manual/installation/</a>。

下面大致介绍了安装和配置过程，本节最后将引导您完成安装和配置。

1．下载MongoDB文件并解压缩。

2．在系统路径中添加<mongo_install_location>/bin。

3．创建一个数据文件目录：<mongo_data_location>/data/db。

4．在控制台提示符下使用下面的命令启动MongoDB。

```go
mongod –dbpath <mongo_data_location>/data/db
```

