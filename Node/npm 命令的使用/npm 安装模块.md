[toc]

### 1. 安装模块

可以通过如下命令安装模块：

```shell
$ npm install modulename
```

例如：

```shell
$ npm install request
```

### 2. 安装全局模块

如果要将模块安装到全局环境中，需要用 `-g` 或者 `--global` 参数：

```shell
$ npm install request -g
```

在 `Linux` 环境下，不要忘了在命令前面加上 `sudo`：

```shell
$ sudo npm install request -g
```

### 3. 从文件夹或 URL 中安装模块

```shell
$ npm install http://somecompany.com/somemodule.tgz
```

### 4. 安装指定版本的模块

```shell
$ npm install modulename@0.1
```

### 5. 安装所有依赖

```shell
$ npm install -d
```

### 6. 从 Git 仓库安装模块

```shell
$ npm install https://github.com/visionmedia/express/tarball/master
```

> 注意：如果你安装了一个尚未发布的模块版本，然后执行一次npm update，那么已发布的版本就会覆盖你本地已经安装的版本。

