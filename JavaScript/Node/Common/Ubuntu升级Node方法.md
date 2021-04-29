可以执行下面的命令升级 Ubuntu 系统中的 Nodejs：

```shell
$ sudo npm install n -g
$ sudo n stable
```

执行结果如下：

```console
xiaotuan@xiaotuan:~/桌面$ sudo npm install n -g
/usr/local/bin/n -> /usr/local/lib/node_modules/n/bin/n
/usr/local/lib
└── n@7.2.2 

xiaotuan@xiaotuan:~/桌面$ sudo n stable
  installing : node-v14.16.1
       mkdir : /usr/local/n/versions/node/14.16.1
       fetch : https://nodejs.org/dist/v14.16.1/node-v14.16.1-linux-x64.tar.xz
   installed : v14.16.1 (with npm 6.14.12)

Note: the node command changed location and the old location may be remembered in your current shell.
         old : /usr/bin/node
         new : /usr/local/bin/node
To reset the command location hash either start a new shell, or execute PATH="$PATH"
```

> 提示：
>
> n是一个Node工具包，它提供了几个升级命令参数：
>
> + n 显示已安装的Node版本
> + n latest 安装最新版本Node
> + n stable 安装最新稳定版Node
> + n lts 安装最新长期维护版(lts)Node
> + n version 根据提供的版本号安装Node

