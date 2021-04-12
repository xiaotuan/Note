### 2.1.3 配置MongoDB

除指定命令行参数外，可执行文件mongod还可接受一个配置文件，其中指定了控制MongoDB服务器行为的配置选项。使用配置文件可更轻松地管理MongoDB配置设置；另外，可创建多个配置文件，供各种数据库角色使用，如开发、测试和生产。

这些配置选项是使用下面的格式指定的，其中<setting>为配置设置，而<value>指定了设置的值：

```go
<setting> = <value>
```

例如，下面的是一个简单的基本配置文件示例：

```go
verbose = true
port = 27017
dbpath = /data/db
noauth = true
```

表2.2列出了在配置文件中指定的一些常见配置选项，让您对可指定哪些配置选项有大致了解。

<center class="my_markdown"><b class="my_markdown">表2.2 mongod配置文件设置</b></center>

| 设置 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| verbose | 增加内部报告的信息量，这些信息将显示到控制台屏幕上或写入到日志文件中。可能取值为true和false。另外，还可使用v、vv、vvv或vvvv来提高详细等级。例如： verbose = true vvv = true |
| logpath | 指定将包含MongoDB日志条目的日志文件的位置和文件名 |
| logappend | 如果为false，每次启动mongod实例时都将新建一个日志文件，并覆盖旧的日志文件；如果为true，将不会覆盖旧的日志文件，而在它末尾附加。默认为false |
| port | 指定一个TCP端口，mongod将在这个端口上侦听客户端连接。默认为27017 |
| bind_ip | 指定一个用逗号分隔的IP地址列表，mongod将在这些地址上侦听。默认为所有接口 |
| maxConns | 指定MongoDB服务器最多可同时接受多少个连接 |
| auth | 如果为true，将启用数据库身份验证，这意味着客户端必须提供身份验证凭证。默认为false |
| noauth | 如果为true，将禁用身份验证 |
| journal | 如果为true，将启用操作日记，以确保持久性和数据一致性。在64位系统上默认为true，在32位系统上默认为false |
| nohttpinterface | 如果为true，将禁用用于访问服务器状态和日志的HTTP接口。默认为false |
| rest | 如果为true，将启用MongoDB数据库服务器的简单REST接口，让您能够通过发送REST请求来访问数据库。默认为false |

