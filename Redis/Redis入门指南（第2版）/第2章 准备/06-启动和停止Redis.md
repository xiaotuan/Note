### 2.2　启动和停止Redis

安装完Redis后的下一步就是启动它，本节将分别介绍在开发环境和生产环境中运行Redis的方法以及正确停止Redis的步骤。

在这之前首先需要了解Redis包含的可执行文件都有哪些，表2-1中列出了这些程序的名称以及对应的说明。如果在编译后执行了make install命令，这些程序会被复制到/usr/local/bin目录内，所以在命令行中直接输入程序名称即可执行。

<center class="my_markdown"><b class="my_markdown">表2-1　Redis可执行文件说明</b></center>

| 文　件　名 | 说　　明 |
| :-----  | :-----  | :-----  | :-----  |
| redis-server | Redis服务器 |
| redis-cli | Redis命令行客户端 |
| redis-benchmark | Redis性能测试工具 |
| redis-check-aof | AOF文件修复工具 |
| redis-check-dump | RDB文件检查工具 |
| redis-sentinel | Sentinel服务器（仅在2.8版以后） |

我们最常使用的两个程序是redis-server和redis-cli，其中redis-server是Redis的服务器，启动Redis即运行redis-server；而redis-cli是Redis自带的Redis命令行客户端，是学习Redis的重要工具，2.3节会详细介绍它。

