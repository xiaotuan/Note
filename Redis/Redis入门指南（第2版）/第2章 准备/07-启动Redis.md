### 2.2.1　启动Redis

启动Redis有直接启动和通过初始化脚本启动两种方式，分别适用于开发环境和生产环境。

#### 1．直接启动

直接运行redis-server即可启动Redis，十分简单：

```shell
$ redis-server
[5101] 14 Dec 20:58:59.944 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
[5101] 14 Dec 20:58:59.948 * Max number of open files set to 10032
...
[5101] 14 Dec 20:58:59.949 # Server started, Redis version 2.6.9
[5101] 14 Dec 20:58:59.949 * The server is now ready to accept connections on port 6379

```

Redis服务器默认会使用6379端口3，通过 `--port` 参数可以自定义端口号：

36379是手机键盘上MERZ对应的数字，MERZ是一名意大利歌女的名字。

```shell
$redis-server --port 6380

```

#### 2．通过初始化脚本启动Redis

在Linux系统中可以通过初始化脚本启动Redis，使得Redis能随系统自动运行，在生产环境中推荐使用此方法运行Redis，这里以Ubuntu和Debian发行版为例进行介绍。在Redis源代码目录的utils文件夹中有一个名为redis_init_script的初始化脚本文件，内容如下：

```shell
#!/bin/sh
#
# Simple Redis init.d script conceived to work on Linux systems
# as it does use of the /proc filesystem.
REDISPORT=6379
EXEC=/usr/local/bin/redis-server
CLIEXEC=/usr/local/bin/redis-cli
PIDFILE=/var/run/redis_${REDISPORT}.pid
CONF="/etc/redis/${REDISPORT}.conf"
case "$1" in
　　 start)
　　　　　if [ -f $PIDFILE ]
　　　　　then
　　　　　　　　　 echo "$PIDFILE exists, process is already running or crashed"
　　　　　else
　　　　　　　　　 echo "Starting Redis server..."
　　　　　　　　　 $EXEC $CONF
　　　　　fi
　　　　　;;
　　 stop)
　　　　　if [ ! -f $PIDFILE ]
　　　　　then
　　　　　　　　　 echo "$PIDFILE does not exist, process is not running"
　　　　　else
　　　　　　　　　 PID=$(cat $PIDFILE)
　　　　　　　　　 echo "Stopping ..."
　　　　　　　　　 $CLIEXEC -p $REDISPORT shutdown
　　　　　　　　　 while [ -x /proc/${PID} ]
　　　　　　　　　 do
　　　　　　　　　　　　echo "Waiting for Redis to shutdown ..."
　　　　　　　　　　　　sleep 1
　　　　　　　　　 done
　　　　　　　　　 echo "Redis stopped"
　　　　　fi
　　　　　;;
　　 *)
　　　　　echo "Please use start or stop as first argument"
　　　　　;;
esac
```

我们需要配置Redis的运行方式和持久化文件、日志文件的存储位置等，具体步骤如下。

（1）配置初始化脚本。首先将初始化脚本复制到/etc/init.d目录中，文件名为 `redis_` 端口号，其中端口号表示要让Redis监听的端口号，客户端通过该端口连接Redis。然后修改脚本第6行的 `REDISPORT` 变量的值为同样的端口号。

（2）建立需要的文件夹。建立表2-2中列出的目录。

<center class="my_markdown"><b class="my_markdown">表2-2　需要建立的目录及说明</b></center>

| 目　录　名 | 说　　明 |
| :-----  | :-----  | :-----  | :-----  |
| `/etc/redis` | 存放Redis的配置文件 |
| `/var/redis/端口号` | 存放Redis的持久化文件 |

（3）修改配置文件。首先将配置文件模板（见2.4节介绍）复制到/etc/redis目录中，以端口号命名（如“6379.conf”），然后按照表2-3对其中的部分参数进行编辑。

<center class="my_markdown"><b class="my_markdown">表2-3　需要修改的配置及说明</b></center>

| 参　　数 | 值 | 说　　明 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| `daemonize` | `yes` | 使Redis以守护进程模式运行 |
| `pidfile` | `/var/run/redis_端口号.pid` | 设置Redis的PID文件位置 |
| `port` | `端口号` | 设置Redis监听的端口号 |
| `dir` | `/var/redis/端口号` | 设置持久化文件存放位置 |

现在就可以使用 `/etc/init.d/redis_` 端口号 `start` 来启动Redis了，而后需要执行下面的命令使Redis随系统自动启动：

```shell
$sudo update-rc.d redis_端口号 defaults

```

