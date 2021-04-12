### 2.3.3 理解MongoDB shell原生方法和构造函数

MongoDB shell提供了用于执行管理任务的原生方法，您可在MongoDB shell中直接调用它们，也可在MongoDB shell中执行的脚本中调用它们。

包括DB、Collection和Cursor在内的JavaScript对象也提供了管理方法，这将在本书后面讨论。

表2.4列出了最常见的原生方法，它们提供了建立连接、创建对象、加载脚本等功能。

<center class="my_markdown"><b class="my_markdown">表2.4 MongoDB shell原生方法和构造函数</b></center>

| 方法 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| Date() | 创建一个Date对象。默认情况下，创建一个包含当前日期的Date对象 |
| UUID(hex_string) | 将32字节的十六进制字符串转换为BSON子类型UUID |
| ObjectId.valueOf() | 将一个ObjectId的属性str显示为十六进制字符串 |
| Mongo.getDB(database) | 返回一个数据库对象，它表示指定的数据库 |
| Mongo(host:port) | 创建一个连接对象，它连接到指定的主机和端口 |
| connect(string) | 连接到指定MongoDB实例中的指定数据库。返回一个数据库对象。连接字符串的格式如下：host:port/database，如db = connect("localhost:28001/myDb") |
| cat(path) | 返回指定文件的内容 |
| version() | 返回当前MongoDB shell实例的版本 |
| cd(path) | 将工作目录切换到指定路径 |
| getMemInfo() | 返回一个文档，指出了MongoDB shell当前占用的内存量 |
| hostname() | 返回运行MongoDB shell的系统的主机名 |
| _isWindows() | 如果MongoDB shell运行在Windows系统上，就返回true；如果运行在UNIX或Linux系统上，就返回false |
| load(path) | 在MongoDB shell中加载并运行参数path指定的JavaScript文件 |
| _rand() | 返回一个0～1的随机数 |

