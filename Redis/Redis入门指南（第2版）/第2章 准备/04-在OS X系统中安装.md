### 2.1.2　在OS X系统中安装

OS X下的软件包管理工具Homebrew和MacPorts均提供了较新版本的Redis包，所以我们可以直接使用它们来安装Redis，省去了像其他POSIX系统那样需要手动编译的麻烦。下面以使用Homebrew安装Redis为例。

#### 1．安装Homebrew

在终端下输入 `ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"` 即可安装Homebrew。

如果之前安装过Homebrew，请执行 `brew update来` 更新Homebrew，以便安装较新版的Redis。

#### 2．通过Homebrew安装Redis

使用 `brew install软件包名` 可以安装相应的包，此处执行 `brew install redis` 来安装Redis：

```shell
$brew install redis
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/redis-3.0.0.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring redis-3.0.0.yosemite.bottle.tar.gz
==> Caveats
To have launchd start redis at login:
　　ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
Then to load redis now:
　　launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
Or, if you don't want/need launchctl, you can just run:
　　redis-server /usr/local/etc/redis.conf
==> Summary
　　/usr/local/Cellar/redis/3.0.0: 10 files, 1.4M
```

OS X系统从Tiger版本开始引入了launchd工具来管理后台程序，如果想让Redis随系统自动运行可以通过以下命令配置launchd：

```shell
ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
```

通过launchd运行的Redis会加载位于/usr/local/etc/redis.conf的配置文件，关于配置文件会在2.4节中介绍。

