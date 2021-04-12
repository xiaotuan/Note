### 2.1.1　在POSIX系统中安装

Redis兼容大部分POSIX系统，包括Linux、OS X和BSD等，在这些系统中推荐直接下载Redis源代码编译安装以获得最新的稳定版本。Redis最新稳定版本的源代码可以从地址<a class="my_markdown" href="['http://download.redis.io/redis-stable.tar.gz']">http://download.redis.io/redis-stable.tar.gz</a>下载。

下载安装包后解压即可使用 `make命令` 完成编译，完整的命令如下：

```shell
wget http://download.redis.io/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd redis-stable
make
```

Redis没有其他外部依赖，安装过程很简单。编译后在Redis源代码目录的 `src` 文件夹中可以找到若干个可执行程序，最好在编译后直接执行 `make install` 命令来将这些可执行程序复制到/usr/local/bin目录中以便以后执行程序时可以不用输入完整的路径。

在实际运行Redis前推荐使用 `make test` 命令测试Redis是否编译正确，尤其是在编译一个不稳定版本的Redis时。

提示

> 除了手工编译外，还可以使用操作系统中的软件包管理器来安装Redis，但目前大多数软件包管理器中的Redis的版本都较古老。考虑到 Redis 的每次升级都提供了对以往版本的问题修复和性能提升，使用最新版本的 Redis 往往可以提供更加稳定的体验。如果希望享受包管理器带来的便利，在安装前请确认您使用的软件包管理器中Redis的版本并了解该版本与最新版之间的差异。<a class="my_markdown" href="['http://redis.io/topics/problems']">http://redis.io/topics/problems</a>中列举了一些在以往版本中存在的已知问题。

