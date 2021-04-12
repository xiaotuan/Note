### 2.1.2 启动MongoDB

安装MongoDB，需要知道如何启动和停止数据库引擎。要启动数据库引擎，可执行<mondo_install_location>/bin中的可执行文件mongod（Windows中为mongod.exe）。这个可执行文件启动MongoDB服务器，并开始在指定端口上侦听数据库请求。

可执行文件mongod接受多个参数，这些参数提供了控制其行为的途径。例如，您可以配置MongoDB在哪个IP地址和端口上侦听，还可配置日志和身份验证。表2.1列出了最常用的参数。

下面的示例在启动MongoDB时指定了参数port和dbpath：

```go
mongod –port 28008 –dbpath <mongo_data_location>/data/db
```

<center class="my_markdown"><b class="my_markdown">表2.1 mongod命令行参数</b></center>

| 参数 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| --help，-h | 返回基本的帮助和用法信息 |
| --version | 返回MongoDB的版本 |
| --config <filename>，-f <filename> | 指定包含运行阶段配置的配置文件 |
| --verbose、-v | 增加内部报告的信息量；这些信息被发送到控制台，并被写入到--logpath指定的日志文件 |
| --quiet | 减少发送到控制台和日志文件的内部报告的信息量 |
| --port <port> | 指定一个TCP端口，mongod将在这个端口上侦听客户端连接。默认为27017 |
| --bind_ip <ip address> | 指定mongod将绑定到哪个IP地址以侦听连接。默认为所有接口 |
| --maxConns <number> | 指定mongod最多同时接受多少个连接，最多为20000个 |
| --logpath <path> | 指定日志文件的路径。重启后将覆盖日志文件，除非指定了--logappend |
| --auth | 启用数据库身份验证，对从远程主机连接到数据库的用户进行身份验证 |
| --dbpath <path> | 指定一个目录，mongod实例将在其中存储数据 |
| --nohttpinterface | 禁用HTTP接口 |
| --nojournal | 禁用支持持久性的日记功能（journaling） |
| --noprealloc | 禁用数据文件预分配。这将缩短启动时间，但可能严重影响正常操作的性能 |
| --repair | 对所有数据库运行修复例程 |

