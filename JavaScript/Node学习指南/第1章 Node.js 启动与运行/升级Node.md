偶数版本号代表了 `Node` 的稳定发行版本，而奇数版本号表示 `Node` 的开发版本。

在 `Node` 源代码目录中，可以运行如下 `make` 命令执行卸载：

```console
make uninstall
```

可以使用 `Node` 版本管理器 (Nvm, Node Version Manager) 在多个 `Node` 版本之间切换。

可以从 `GitHub` 上下载 `Nvm`，地址是：<https://github.com/creationix/nvm>。

使用 `Nvm` 安装指定版本的 `Node` ：

```console
nvm install v0.4.1
```

使用如下命令切换到指定 `Node` 版本：

```console
nvm run v0.4.1
```

查看可用的 `Node` 版本信息：

```console
nvm ls
```
