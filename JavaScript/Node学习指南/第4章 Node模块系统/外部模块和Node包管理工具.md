以下是一些常用的查找 Node 模块的软件源：

+ npm registry (<http://search.npmjs.org/>)
+ Node module wiki (<https://github.com/joyent/node/wiki/modules>)
+ The node-toolbox (<http://toolboox.no.de/>)
+ Nipster! (<http://eirikb.github.com/nipster/>)

查看 npm 全部命令列表：

```console
$ npm help npm
```

安装模块命令：

```console
$ npm install modulename
```

如果想要全局安装，使用 `-g` 或者 `--global` 选项：

```console
$ npm -g install connect
```

安装本地文件系统中的模块，或者来自本地或 url 得到的压缩文件：

```console
$ npm install http://somecompany.com/somemodule.tgz
```

安装指定版本的模块：

```console
$ npm install modulename@0.1
```

卸载模块：

```console
$ npm uninstall modulename
```

更新所有模块：

```console
$ npm update
```

更新单个模块：

```console
$ npm update modulename
```

查看过期模块：

```console
$ npm outdated
```

显示安装的包和依赖命令为：list、ls 、la 或者 ll：

```console
$ npm ls
```

安装所有依赖：

```console
$ npm install -d
```

安装 GitHub 上未发布的模块：

```console
$ npm install https://github.com/visionmedia/express/tarball/master
```

查看全局安装的模块：

```console
$ npm ls -g
```

显示 npm 的配置设置：

```console
$ npm config list
```

更深入的了解配置的设置，使用：

```console
$ npm config ls -l
```

修改或者删除配置项：

```console
$ npm config delete keyname
$ npm config set keyname value
```

或者直接编辑配置文件：

```console
$ npm config edit
```

搜索模块时，可以挑选合适的关键字，从而返回最符合你需求的搜索结果：

```console
$ npm search html5 parser
```

