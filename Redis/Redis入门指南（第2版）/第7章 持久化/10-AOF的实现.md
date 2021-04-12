### 7.2.2 AOF的实现

AOF文件以纯文本的形式记录了Redis执行的写命令，例如在开启AOF持久化的情况下执行了如下4个命令：

```shell
SET foo 1
SET foo 2
SET foo 3
GET foo

```

Redis会将前3条命令写入AOF文件中，此时AOF文件中的内容如下：

```shell
*2
$6
SELECT
$1
0
*3
$3
set
$3
foo
$1
1
*3
$3
set
$3
foo
$1
2
*3
$3
set
$3
foo
$1
3

```

可见AOF文件的内容正是Redis客户端向Redis发送的原始通信协议的内容（Redis的通信协议会在9.2节中介绍，为了便于阅读，这里将实际的命令部分以粗体显示），从中可见Redis确实只记录了前3条命令。然而这时有一个问题是前2条命令其实都是冗余的，因为这两条的执行结果会被第三条命令覆盖。随着执行的命令越来越多，AOF文件的大小也会越来越大，即使内存中实际的数据可能并没有多少。很自然地，我们希望Redis可以自动优化AOF文件，就上例而言，就是将前两条无用的记录删除，只保留第三条。实际上Redis也正是这样做的，每当达到一定条件时Redis就会自动重写AOF文件，这个条件可以在配置文件中设置：

```shell
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

```

`auto-aof-rewrite-percentage` 参数的意义是当目前的AOF文件大小超过上一次重写时的AOF文件大小的百分之多少时会再次进行重写，如果之前没有重写过，则以启动时的AOF文件大小为依据。 `auto-aof-rewrite-min-size` 参数限制了允许重写的最小AOF文件大小，通常在AOF文件很小的情况下即使其中有很多冗余的命令我们也并不太关心。除了让Redis自动执行重写外，我们还可以主动使用 `BGREWRITEAOF` 命令手动执行AOF重写。

上例中的AOF文件重写后的内容为：

```shell
*2
$6
SELECT
$1
0
*3
$3
SET
$3
foo
$1
3

```

可见冗余的命令已经被删除了。重写的过程只和内存中的数据有关，和之前的AOF文件无关，这与RDB很相似，只不过二者的文件格式完全不同。

在启动时Redis会逐个执行AOF文件中的命令来将硬盘中的数据载入到内存中，载入的速度相较RDB会慢一些。

