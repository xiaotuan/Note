### 9.3.1 redis-cli

> Instagram3团队开发了一个基于MONITOR命令的 Redis 查询分析程序redis-faina。redis-faina可以根据MONITOR命令的监控结果分析出最常用的命令、访问最频繁的键等信息，对了解Redis的使用情况帮助很大。
> redis-faina 的项目地址是<a class="my_markdown" href="['https://github.com/Instagram/redis-faina']">https://github.com/Instagram/redis-faina</a>，直接下载其中的redis-faina.py文件即可使用。
> redis-faina.py的输入值为一段时间的 `MONITOR` 命令执行结果。如：

相信大家对redis-cli已经很熟悉了，作为Redis自带的命令行客户端，你可以从任何安装有Redis的服务器中找到它，所以对于管理Redis而言redis-cli是最简单实用的工具。

redis-cli可以执行大部分的Redis命令，包括查看数据库信息的 `INFO` 命令，更改数据库设置的 `CONFIG` 命令和强制进行RDB快照的 `SAVE` 命令等。下面介绍几个管理Redis时非常有用的命令。

#### 1．耗时命令日志

```shell
redis-cli MONITOR | head -n <要分析的命令数> | ./redis-faina.py

```

当一条命令执行时间超过限制时，Redis会将该命令的执行时间等信息加入耗时命令日志（slow log）以供开发者查看。可以通过配置文件的 `slowlog-log-slower-than` 参数设置这一限制，要注意单位是微秒（1 000 000微秒相当于1秒），默认值是10 000。耗时命令日志存储在内存中，可以通过配置文件的 `slowlog-max-len` 参数来限制记录的条数。

使用 `SLOWLOG GET` 命令来获得当前的耗时命令日志，如：

```shell
redis> SLOWLOG GET
1) 1) (integer) 4
   2) (integer) 1356806413
   3) (integer) 58
   4) 1) "get"
　　  2) "foo"
2) 1) (integer) 3
   2) (integer) 1356806408
   3) (integer) 34
   4) 1) "set"
　　  2) "foo"
　　  3) "bar"

```

每条日志都由以下4个部分组成：

（1）该日志唯一ID；

（2）该命令执行的Unix时间；

（3）该命令的耗时时间，单位是微秒；

（4）命令及其参数。

提示

> 为了产生一些耗时命令日志作为演示，这里将 `slowlog-log-slower-than` 参数值设置为0，即记录所有命令。如果设置为负数则会关闭耗时命令日志。

#### 2．命令监控

Redis提供了 `MONITOR` 命令来监控Redis执行的所有命令，redis-cli同样支持这个命令，如在redis-cli中执行 `MONITOR` ：

```shell
redis> MONITOR
OK

```

这时 Redis 执行的任何命令都会在 redis-cli 中打印出来，如我们打开另一个redis-cli执行 `SET foo bar` 命令，在之前的redis-cli中会输出如下内容：

```shell
1356806981.885237 [0 127.0.0.1:57339] "SET" "foo" "bar

```

`MONITOR` 命令非常影响Redis的性能，一个客户端使用 `MONITOR` 命令会降低Redis将近一半的负载能力。所以 `MONITOR` 命令只适合用来调试和纠错。

补充知识

3 Instagram是Facebook旗下的图片分享社区。

