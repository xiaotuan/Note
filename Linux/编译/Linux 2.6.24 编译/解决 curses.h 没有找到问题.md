[toc]

### 1. 报错信息

```shell
$ make menuconfig
HOSTCC  scripts/kconfig/lxdialog/checklist.o
In file included from scripts/kconfig/lxdialog/checklist.c:24:0:
scripts/kconfig/lxdialog/dialog.h:31:20: fatal error: curses.h: 没有那个文件或目录
```

### 2. 报错原因

`libncurses5-dev` 软件未安装。

### 3. 解决方法

```shell
sudo apt-get install libncurses5-dev
```

