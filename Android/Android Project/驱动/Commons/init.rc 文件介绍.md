`init.rc` 文件位于 `system/core/rootdir/init.rc` 。它是在 init 启动后被执行的启动脚本，其语法主要包含如下内容：

+ **Commands：**命令
+ **Actions：**动作
+ **Triggers：**触发条件
+ **Services：**服务
+ **Options：**选项
+ **Properties：**属性

Commands 是一些基本的操作命令，例如：

```rc
mkdir /sdcard 0000 system system
mkdir /system
mount tmpfs tmpfs /sqlite_stmt_journals size=4m
```

Actions 是表示一系列动作的命令，通常在 Triggers 中被调用，动作和触发条件的形式如下所示：

```
on <trigger>
	<command>
	<command>
	<command>
```

例如：

```
on init
	export PATH /sbin:/system/sbin:/system/bin:/system/xbin
	mkdir /system
```

Services 通常表示启动一个可执行程序，用 Options 来表示服务的附加内容以配合服务使用。具体代码如下所示：

```
service vold /system/bin/vold
socket vold stream 0660 root mount
service bootsound /system/bin/playmp3
	user media
	group audio
	oneshot
```

socket、user、group 和 oneshot 是配合服务使用的选项，其中 oneshot 选项表示该服务只启动一次；如果没有 oneshot 选项，则这个可执行程序会一直存在；如果可执行程序被杀死，则会重新启动