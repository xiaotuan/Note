1. 执行下面命令：

```shell
$ cat build/core/version_defaults.mk | grep "PLATFORM_VERSION :="
PLATFORM_VERSION := 4.4.2
```

2. 在编译时，查看编译输出日志：

```shell
$ source build/envsetup.sh
$ lunch Hi3798MV200H
```

执行上面命令后会打印如下日志：

```shell
==========================================
PLATFORM_VERSION_CODENAME=REL
PLATFORM_VERSION=4.4.2
......
==========================================
```