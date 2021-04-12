### 24.2　从命令行实现GridFS

> **使用控制台在MongoDB GridFS存储区中存储和检索文件**
> 本节介绍如何使用控制台实现MongoDB GridFS存储。这个示例将引领您在控制台提示符下列出文件、添加文件、获取文件和删除文件。
> 请执行如下步骤，在控制台提示符下添加文件、列出文件、获取文件和删除文件。
> 1．确保启动了MongoDB服务器。
> 2．在文件夹code/hour24中新建一个文件，将其命名为console.txt，再在其中添加一些数据并存盘。
> 3．打开一个控制台窗口，并切换到目录code/hour24。
> 4．使用下面的命令将文件console.txt存储到MongoDB GridFS存储区中：
> 5．使用下面的命令列出MongoDB GridFS存储区中的文件。您将看到文件console.txt。
> 6．使用下面的命令从GridFS存储区获取文件console.txt，并将其作为文件retrieved.txt存储到本地文件系统中。打开文件retrieved.txt并检查其内容。
> 7．使用下面的命令从GridFS存储区中删除文件：
> 8．使用下面的命令列出GridFS存储区中的文件，并核实文件console.txt已删除：
> ▲

MongoDB自带了可从控制台执行的命令mongofiles，让您能够与MongoDB服务器中的GridFS存储区交互。命令mongofiles的语法如下：

```go
mongofiles <options> <commands>
```

<options>让您能够指定连接到MongoDB数据库的选项，类似于命令mongo的选项。表24.1描述了一些选项。

<center class="my_markdown"><b class="my_markdown">表24.1　　命令mongofiles支持的选项</b></center>

| 选项 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| --host <host>:<port> | 主机和端口 |
| --port <port> | 端口（如果在选项--host中没有指定） |
| --username <username> | 用户名，用于身份验证 |
| --password <password> | 密码，用于身份验证 |
| --dbpath <path> | MongoDB数据文件的路径。可使用这个选项来直接访问GridFS存储区，而无需启动mongod |
| --db <database> | 用于GridFS存储的数据库的名称 |
| --local <filename> | 使用get命令从GridFS存储区获取文件时，指定使用什么样的文件名将其存储在本地文件系统中 |
| --replace | 指定put请求用本地文件替换既有的GridFS对象，而不是添加同名对象。 |

<command>让您能够指定要执行的GridFS命令，这些命令列出GridFS存储区中的文件以及在其中添加、获取和删除文件。表24.2描述了其中的一些命令。

<center class="my_markdown"><b class="my_markdown">表24.2　　命令mongofiles支持的命令</b></center>

| 命令 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| list <prefix> | 列出GridFS存储区中的文件，参数prefix让您能够指定文件名的开头部分 |
| put <filename> | 将文件存储到GridFS存储区 |
| get <filename> | 从GridFS存储区获取文件 |
| delete <filename> | 从GridFS存储区删除文件 |
| search <string> | 列出GridFS存储区中的文件，参数string让您能够指定文件名包含的字符串 |

```go
mongofiles --db myFS put console.txt
```

例如，要将文件test.data存储到本地服务器的GridFS存储器，可使用类似于下面的命令：

```go
mongofiles --host localhost:27017 --db myFS put test.data
```

```go
mongofiles --db myFS list
```

▼　Try It Yourself

```go
mongofiles --db myFS --local retrieved.txt get console.txt
```

```go
mongofiles --db myFS delete console.txt
```

```go
mongofiles --db myFS list
```

